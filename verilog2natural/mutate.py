import sys
import re
import random
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from VerilogLexer import VerilogLexer
from VerilogParser import VerilogParser
from VerilogParserVisitor import VerilogParserVisitor
from antlr4.tree.Tree import ParseTreeListener, ParseTree, TerminalNodeImpl, ErrorNodeImpl, TerminalNode, \
    INVALID_INTERVAL


class IndexCollector(VerilogParserVisitor):
    def __init__(self):
        self.index_info = {'Module_identifier': [], 
                        'Port_identifier':[],'Input_declaration': [],'Output_declaration': [], 
                        'Always_construct': [],'Initial_construct': [],'Procedural_continuous_assign': [],
                        'Conditional_statement': [], 'True_block': [],
                        'Case_statement': [], 'Case_item': [],
                        'Blocking_assignment': [], 'Nonblocking_assignmen': [],
                        'Expression': [], 'Module_item': []}

    def visitSource_text(self, ctx):
        self.index_info['Source_text'] = ctx.getSourceInterval()
        return self.visitChildren(ctx)
    
    def visitModule_identifier(self, ctx:VerilogParser.Module_identifierContext):
        self.index_info['Module_identifier'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitInput_declaration(self, ctx: VerilogParser.Input_declarationContext):
        self.index_info['Input_declaration'].append(ctx.getSourceInterval())
        #     print(ctx.getChild(i).getText())
        return self.visitChildren(ctx)
    
    def visitPort_identifier(self, ctx:VerilogParser.Port_identifierContext):
        self.index_info['Port_identifier'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitOutput_declaration(self, ctx: VerilogParser.Output_declarationContext):
        self.index_info['Output_declaration'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitList_of_port_declarations(self, ctx): 
        self.index_info['List_of_port_declarations'] = ctx.getSourceInterval() 
        return self.visitChildren(ctx)
    
    def visitModule_item(self, ctx):
        self.index_info['Module_item'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)

    def visitRange_(self, ctx:VerilogParser.Range_Context):
        self.index_info['Range_'] = ctx.getSourceInterval()
        return self.visitChildren(ctx)

    def visitInitial_construct(self, ctx):
        self.index_info['Initial_construct'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)

    def visitAlways_construct(self, ctx):
        self.index_info['Always_construct'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitProcedural_continuous_assign(self, ctx):
        self.index_info['Procedural_continuous_assign'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitConditional_statement(self, ctx):
        self.index_info['Conditional_statement'].append(ctx.expression().getSourceInterval())
        self.index_info['True_block'].append(ctx.statement_or_null(0).getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitCase_statement(self, ctx):
        self.index_info['Case_statement'].append(ctx.expression().getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitCase_item(self, ctx:VerilogParser.Case_itemContext):
        self.index_info['Case_item'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)
    
    def visitBlocking_assignment(self, ctx:VerilogParser.Blocking_assignmentContext):
        self.index_info['Blocking_assignment'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)

    def visitNonblocking_assignment(self, ctx:VerilogParser.Nonblocking_assignmentContext):
        self.index_info['Nonblocking_assignmen'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)

    def visitExpression(self, ctx:VerilogParser.ExpressionContext):
        self.index_info['Expression'].append(ctx.getSourceInterval())
        return self.visitChildren(ctx)


class AstTraveller:
    def __init__(self, input_file):
        self.input_file = input_file

    def travel_ast(self):
        input_stream = FileStream(self.input_file, encoding='utf-8')
        lexer = VerilogLexer(input_stream)
        stream = CommonTokenStream(lexer)
        # stream.fill()
        parser = VerilogParser(stream)
        tree = parser.source_text()
        indexes = IndexCollector()
        indexes.visitSource_text(tree)
        
        return indexes



class VerilogCodeModifier:
    def __init__(self, input_file,index):
        self.input_file = input_file
        self.index = index
        self.replace_info = []
        self.direct_info = []
        self.count = 1
        self.mi = 1

    def modify_code(self):
        input_stream = FileStream(self.input_file, encoding='utf-8')
        lexer = VerilogLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        parser = VerilogParser(stream)
        rewriter = TokenStreamRewriter(tokens=stream)
        # rewriter.insertBeforeIndex(index1, 'start')
        # rewriter.insertAfter(index2, 'end')
        self.modify_rules(rewriter)
        return rewriter.getDefaultText(), self.replace_info, self.direct_info
    
    def modify_rules(self, rewriter):
        pass


class ModifyRules(VerilogCodeModifier):

    def modify_rules(self, rewriter):
        # functions_to_execute = [
        #     self.conflict_assign,
        #     self.no_driving_line,
        #     self.comb_logic_introduce,
        #     ]

        # selected_functions =  [self.modify_input_width]
        # if random.random() < 0.5:
        #     selected_functions += [self.modify_port_list]
        # selected_functions += random.sample(functions_to_execute, 2)

        # for func in selected_functions:
        #     func(rewriter)

        try:
            self.modify_input_width(rewriter)
        except Exception as e:
            pass
        try:
            self.modify_port_list(rewriter)
        except Exception as e:
            pass
        try:
            self.no_driving_line(rewriter)
        except Exception as e:
            pass
        try:
            self.conflict_assign(rewriter)
        except Exception as e:
            pass
        try:
            self.comb_logic_introduce(rewriter)
        except Exception as e:
            pass


    def get_text(self, rewriter, key_value):
        text = []
        for start_index, stop_index in self.index.get(key_value):
            text.append(rewriter.getText('default', start = start_index, stop = stop_index))
        return text
    
    def modify_port_list(self, rewriter):
        rewriter.insertAfter(self.index['List_of_port_declarations'][0], 'out_n, ')
        dinfo = "The module declares an 'out_n' output port without a corresponding "\
                "driver line in the logic. Delete this port declaration."
        self.direct_info.append(dinfo)

    def modify_input_width(self, rewriter):
        width = str(random.randint(0,20))
        start_index = self.index['Range_'][0] + 1
        stop_index = self.index['Range_'][0] + 1
        range_info = rewriter.getText('default', start = start_index, stop = stop_index)
        start_index = self.index['Range_'][0] + 6
        stop_index = self.index['Range_'][0] + 6
        port_info = rewriter.getText('default', start = start_index, stop = stop_index)
        rewriter.replaceIndex(self.index['Range_'][0] + 1, width)
        # print(width, range_info)
        dinfo = f"The bit width of {port_info} should be {int(range_info)+1} instead of {int(width)+1}, correct it."
        self.direct_info.append(dinfo)
    
    def conflict_assign(self, rewriter):
        port = self.get_text(rewriter, 'Port_identifier')
        input_decl = self.get_text(rewriter, 'Input_declaration')
        output_decl = self.get_text(rewriter, 'Output_declaration')
        # TODO: Ensure that the in/out labels of ports are correct before performing assignments
        if(len(port)<3): return
        sp = random.sample(port, 3)
        # TODO: Consider more possible operators. '|', '&', '*' etc...
        # TODO: Determine the insertion position more precisely: module item ---> (Please refer to the grammar tree).
        distractor = 'assign {} = {} {} {}\n'.format(sp[2], sp[1], '|', sp[0])
        for start_index, _ in self.index.get('Module_item'):
            if random.random() < 0.3:
                rewriter.insertBeforeIndex(start_index, distractor)
                dinfo = f"The assignment statement {distractor} repeatedly assigns a "\
                            f"value to the left signal {sp[2]}, delete this statement"
                self.direct_info.append(dinfo)

    def no_driving_line(self, rewriter):
        distractor = '\n\toutput out_n;\n'
        for _, end_index in self.index.get('Output_declaration'):
            if random.random() < 0.3:
                rewriter.insertAfter(end_index+1, distractor)
                dinfo = "The module declares an 'out_n' output port without a corresponding "\
                        "driver line in the logic. Delete this declaration statement."
                self.direct_info.append(dinfo)

    
    def comb_logic_introduce(self, rewriter):
        port = self.get_text(rewriter, 'Port_identifier')
        if(len(port)<3): return
        sp = random.sample(port, 3)
        distractor = '\twire our_d, our_e;\n\tassign our_d = {} && {};\n\tassign our_e = {} || our_d;\n\tassign {} = our_e;\n'\
                    .format(sp[0], sp[1], sp[2], sp[1])
        for _, end_index in self.index.get('Module_item'):
            if random.random() < 0.23:
                rewriter.insertAfter(end_index+1, distractor)
                dinfo = f"Combination logic here {distractor} is useless, delete them ."
                self.direct_info.append(dinfo)


class MaskRules(VerilogCodeModifier):

    def modify_rules(self, rewriter):
        functions_to_execute = [
            self.mask_module_name,
            self.mask_port_name,
            self.mask_port_type,
            self.mask_construct_type,
            self.mask_cond_exp,
            self.mask_cond_br1,
            self.mask_assign_stat,
            self.mask_exp
            ]

        selected_functions = random.sample(functions_to_execute, 2)

        for func in selected_functions:
            func(rewriter)

    def get_text(self, rewriter, key_value):
        text = ""
        for start_index, stop_index in self.index.get(key_value):
            text += rewriter.getText('default', start = start_index, stop = stop_index)
        return text
    
    def get_prob_text(self, rewriter, start_index, end_index):
        text = rewriter.getText('default', start = start_index, stop = end_index)
        return text

    def probably_mask(self, rewriter, key_value, p):
        masked = []
        for start_index, end_index in self.index.get(key_value):
            if (p == 1) or random.random() < p:
                masked.append(self.get_prob_text(rewriter, start_index, end_index))
                rewriter.replaceIndex(start_index, f'[MASK{self.mi}]')
                self.mi += 1
        return masked

    def probably_mask_fwd(self, rewriter, key_value, p1, p2):
        masked = []
        for start_index, end_index in self.index.get(key_value):
            if random.random() < 0.6:
                masked.append(self.get_prob_text(rewriter, start_index, end_index))
                rewriter.replaceIndex(start_index, f'[MASK{self.mi}]')
                self.mi += 1
                if random.random() < 0.5:
                    for i in range(start_index+1, end_index+1):
                        rewriter.deleteIndex(i)
        return masked

    def mask_module_name(self, rewriter):
        text = self.probably_mask(rewriter, 'Module_identifier', 0.85)
        info = f"[MASK{self.count}]: Here, a module name is masked. Considering the"\
                    f" module's functionality, we can assign it a meaningful name,"\
                    f" like '{text[0]}' or something similar."
        dinfo = f"[MASK{self.count}]: {text[0]}"
        self.count += 1
        self.replace_info.append(info)
        self.direct_info.append(dinfo)


    def mask_port_name(self, rewriter):
        text = self.probably_mask(rewriter, 'Port_identifier', 0.5)
        info = f"[MASK{self.count}-{self.count+len(text)-1}]: In this case, the mask is the port name of the module. "\
                "Based on the correspondence between the port list and port declarations, "\
                "as well as the subsequent use of port names in the module, "\
                "we can determine that the information where the mask is located is"\
                f" {text}."
        dinfo = f"[MASK{self.count}-{self.count+len(text)-1}]: {text}."
        if len(text) > 0:
            self.count += len(text)
            self.replace_info.append(info)
            self.direct_info.append(dinfo)
        
    def mask_port_type(self, rewriter):
        text1 = self.probably_mask(rewriter, 'Input_declaration', 0.8)
        info1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: By analyzing the left and right-hand sides of the assignment statements within the module,"\
        f" we can infer that the port type of the masked element should be: {text1[0]}"
        dinfo1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: {text1[0]}."
        if len(text1) > 0:
            self.count += len(text1)
            self.replace_info.append(info1)
            self.direct_info.append(dinfo1)

        text2 = self.probably_mask(rewriter, 'Output_declaration', 0.8)
        info2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: After analyzing the assignment statements within the module,"\
        f" it can be deduced that the port type of the masked element should be: {text2[0]}"
        dinfo2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: {text2[0]}."
        if len(text2) > 0:
            self.count += len(text2)
            self.replace_info.append(info2)
            self.direct_info.append(dinfo2)

    def mask_construct_type(self, rewriter):
        text1 = self.probably_mask(rewriter, 'Always_construct', 1)
        info1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: Based on the context and syntactical analysis,"\
            " we infer that the masked block is most likely an always block."
        dinfo1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: always."
        if len(text1) > 0:
            self.count += len(text1)
            self.replace_info.append(info1)
            self.direct_info.append(dinfo1)

        text2 = self.probably_mask(rewriter, 'Initial_construct', 1)
        info2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: Based on the context and syntactical analysis,"\
            " we infer that the masked block is most likely an initial block."
        dinfo2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: initial."
        if len(text2) > 0:
            self.count += len(text2)
            self.replace_info.append(info2)
            self.direct_info.append(dinfo2)

        # text3 = self.probably_mask(rewriter, 'Procedural_continuous_assign', 1)

    def mask_cond_exp(self, rewriter):
        text1 = self.probably_mask(rewriter, 'Conditional_statement', 1)
        info1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: "\
            "This mask type pertains to conditional branch statements, "\
            "which decide the jump direction. Based on context and function,"\
            f" the expected sequence of these statements is as follows::{text1}"
        dinfo1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: {text1}."
        if len(text1) > 0:
            self.count += len(text1)
            self.replace_info.append(info1)
            self.direct_info.append(dinfo1)

        text2 = self.probably_mask(rewriter, 'Case_statement', 1)
        info2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: "\
            "This mask applies to case block condition statements, which dictate the "\
            "case selections. Considering the contextual cues and functional context,"\
            f" the expected ordering of these statements is as follows: {text2}"
        dinfo2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: {text2}."
        if len(text2) > 0:
            self.count += len(text2)
            self.replace_info.append(info2)
            self.direct_info.append(dinfo2)
        
    def mask_cond_br1(self, rewriter):
        text1 = self.probably_mask_fwd(rewriter, 'True_block', 0.5, 0.3)
        info1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: "\
        "The masked section corresponds to the true branch of conditional statements, "\
        "which is executed when the condition is met. The expected sequence of statements "\
        f"is determined by the surrounding context and is as follows: {text1}"
        dinfo1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: {text1}."
        if len(text1) > 0:
            self.count += len(text1)
            self.replace_info.append(info1)
            self.direct_info.append(dinfo1)

        text2 = self.probably_mask(rewriter, 'Case_item', 0.35)
        info2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: "\
        "This mask pertains to case items within a case statement."\
        " These case items are used to match different conditions and execute corresponding"\
        " code blocks. The expected sequence of case items is influenced by the "\
        f"surrounding context and functional understanding and is as follows: {text2}"
        dinfo2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: {text2}."
        if len(text2) > 0:
            self.count += len(text2)
            self.replace_info.append(info2)
            self.direct_info.append(dinfo2)

    def mask_assign_stat(self, rewriter):
        text1 = self.probably_mask_fwd(rewriter, 'Blocking_assignment', 0.6, 0.5)
        info1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: Given the overall context and functional analysis,"\
        " as well as its role within particular functional constructs, "\
        f"the expression here should be the following blocking assignment statement accordingly:{text1}"
        dinfo1 = f"[MASK{self.count}-{self.count+len(text1)-1}]: {text1}."
        if len(text1) > 0:
            self.count += len(text1)
            self.replace_info.append(info1)
            self.direct_info.append(dinfo1)

        text2 = self.probably_mask_fwd(rewriter, 'Nonblocking_assignmen', 0.6, 0.5)
        info2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: Given the overall context and functional analysis,"\
        " as well as its role within particular functional constructs, "\
        f"the expression here should be the following non-blocking assignment statement accordingly:{text2}"
        dinfo2 = f"[MASK{self.count}-{self.count+len(text2)-1}]: {text2}."
        if len(text2) > 0:
            self.count += len(text2)
            self.replace_info.append(info2)
            self.direct_info.append(dinfo2)
    
    def mask_exp(self, rewriter):
        text = self.probably_mask(rewriter, 'Expression', 0.15)
        info = f"[MASK{self.count}-{self.count+len(text)-1}]:Based on the context, the masked expression should be"\
                f" {text}."
        dinfo = f"[MASK{self.count}-{self.count+len(text)-1}]: {text}."
        if len(text) > 0:
            self.count += len(text)
            self.replace_info.append(info)
            self.direct_info.append(dinfo)


def main(argv):

    traveller = AstTraveller(argv[1])
    index_info = traveller.travel_ast().index_info

    # modifier = VerilogCodeModifier(argv[1], index_info)
    modified_code, _, doutput = ModifyRules(argv[1], index_info).modify_code()
    print(modified_code)
    print(doutput)
    # masked_code, output, doutput = MaskRules(argv[1], index_info).modify_code()
    

if __name__ == '__main__':
    main(sys.argv)