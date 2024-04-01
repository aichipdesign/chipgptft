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
                        'Always_construct': [],'Initial_construct': [],'Continuous_assign': [],
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
    
    def visitContinuous_assign(self, ctx):
        self.index_info['Continuous_assign'].append(ctx.getSourceInterval())
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
        input_stream = FileStream(self.input_file)
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

    def modify_code(self):
        input_stream = FileStream(self.input_file)
        lexer = VerilogLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        parser = VerilogParser(stream)
        rewriter = TokenStreamRewriter(tokens=stream)
        # rewriter.insertBeforeIndex(index1, 'start')
        # rewriter.insertAfter(index2, 'end')
        self.modify_rules(rewriter)
        return rewriter.getDefaultText()
    
    def modify_rules(self, rewriter):
        pass


class ModifyRules(VerilogCodeModifier):

    def modify_rules(self, rewriter):
        # self.modify_port_list(rewriter)
        # self.modify_input_width(rewriter)
        self.conflict_assign(rewriter)
        self.comb_logic_introduce(rewriter)
        self.no_driving_line(rewriter)
    def get_text(self, rewriter, key_value):
        text = []
        for start_index, stop_index in self.index.get(key_value):
            text.append(rewriter.getText('default', start = start_index, stop = stop_index))
        return text
    
    def modify_port_list(self, rewriter):
        rewriter.insertAfter(self.index['List_of_port_declarations'][0], 'out_n, ')

    def modify_input_width(self, rewriter):
        rewriter.replaceIndex(self.index['Range_'][0] + 1, '20')
    
    def conflict_assign(self, rewriter):
        port = self.get_text(rewriter, 'Port_identifier')
        input_decl = self.get_text(rewriter, 'Input_declaration')
        output_decl = self.get_text(rewriter, 'Output_declaration')
        # TODO: Ensure that the in/out labels of ports are correct before performing assignments
        if(len(port)<3): return
        sp = random.sample(port, 3)
        # TODO: Consider more possible operators. '|', '&', '*' etc...
        # TODO: Determine the insertion position more precisely: module item ---> (Please refer to the grammar tree).
        distractor = 'assign {} = {} {} {};\n'.format(sp[2], sp[1], '|', sp[0])
        for start_index, _ in self.index.get('Module_item'):
            now__index = start_index
        if random.random() > 0.5:
            #print("this is ",now__index)
            rewriter.insertBeforeIndex(now__index, distractor)

    def no_driving_line(self, rewriter):
        
        #distractor = '\n\t,output out_n\n'
        #for _, end_index in self.index.get('Output_declaration'):
            if random.random() < 0.5:
               # print("hschjjj")
               # print(self.index['List_of_port_declarations'][1])
               
               # rewriter.insertAfter(nowc_end_index, distractor)
                rewriter.insertAfter(self.index['List_of_port_declarations'][1]-1, ',output out_n')
              #  rewriter.insertAfter(end_index-1, distractor)
               # for _, end_index in self.index.get('Module_item'):
               #       nowc_end_index=end_index
                
    
    def comb_logic_introduce(self, rewriter):
        port = self.get_text(rewriter, 'Port_identifier')
        if(len(port)<3): return
        sp = random.sample(port, 3)

        distractor = '\twire our_d, our_e;\n\tassign our_d = {} && {};\n\tassign our_e = {} || our_d;\n\tassign {} = our_e;\n'\
                    .format(sp[0], sp[1], sp[2], sp[1])
        for _, end_index in self.index.get('Module_item'):
            nowc_end_index=end_index
        if random.random() < 0.5:
            rewriter.insertAfter(nowc_end_index+1, distractor)


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

    def probably_mask(self, rewriter, key_value, p):
        for start_index, _ in self.index.get(key_value):
            if (p == 1) or random.random() < p:
                rewriter.replaceIndex(start_index, '[MASK]')

    def probably_mask_fwd(self, rewriter, key_value, p1, p2):
        for start_index, end_index in self.index.get(key_value):
            if random.random() < 0.6:
                rewriter.replaceIndex(start_index, '[MASK]')
                if random.random() < 0.5:
                    for i in range(start_index+1, end_index+1):
                        rewriter.deleteIndex(i)

    def mask_module_name(self, rewriter):
        self.probably_mask(rewriter, 'Module_identifier', 1)

    def mask_port_name(self, rewriter):
        self.probably_mask(rewriter, 'Port_identifier', 0.5)
        
    def mask_port_type(self, rewriter):
        self.probably_mask(rewriter, 'Input_declaration', 1)
        self.probably_mask(rewriter, 'Output_declaration', 1)

    def mask_construct_type(self, rewriter):
        self.probably_mask(rewriter, 'Always_construct', 1)
        self.probably_mask(rewriter, 'Initial_construct', 1)
        self.probably_mask(rewriter, 'Continuous_assign', 1)

    def mask_cond_exp(self, rewriter):
        self.probably_mask(rewriter, 'Conditional_statement', 1)
        self.probably_mask(rewriter, 'Case_statement', 1)
        
    def mask_cond_br1(self, rewriter):
        self.probably_mask(rewriter, 'True_block', 1)
        for start_index, end_index in self.index.get('True_block'):
            if random.random() < 0.3:
                for i in range(start_index+1, end_index):
                    rewriter.deleteIndex(i)
        self.probably_mask(rewriter, 'Case_item', 0.5)

    def mask_assign_stat(self, rewriter):
        self.probably_mask_fwd(rewriter, 'Blocking_assignment', 0.6, 0.5)
        self.probably_mask_fwd(rewriter, 'Nonblocking_assignmen', 0.6, 0.5)
    
    def mask_exp(self, rewriter):
        self.probably_mask(rewriter, 'Expression', 0.3)


def main(argv):

    traveller = AstTraveller(argv[1])
    index_info = traveller.travel_ast().index_info

    # modifier = VerilogCodeModifier(argv[1], index_info)
    modified_code = ModifyRules(argv[1], index_info).modify_code()
    print(modified_code)
    # masked_code = MaskRules(argv[1], index_info).modify_code()
    # print(masked_code)
    

if __name__ == '__main__':
    main(sys.argv)