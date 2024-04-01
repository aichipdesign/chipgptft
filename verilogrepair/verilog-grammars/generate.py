import sys
import re
from antlr4 import *
from VerilogLexer import VerilogLexer
from VerilogParser import VerilogParser
from VerilogParserVisitor import VerilogParserVisitor
 
# DONE: always block trigger signal
# DONE: bonding  trigger signal to condition block
# DONE: conditional block construct
# DONE: case block construct
# DONE: cond: nest? repetitive information?
# TODO: detail analysis of assignment statement

class VerilogVisitor(VerilogParserVisitor):
    def __init__(self):
        self.input_ports = []
        self.output_ports = []
        self.always_block_count = 0
        self.trigger_signal = []
        self.conditional_stat_count = [0] * 10
        self.conditional_stat = [' '] * 10
        self.case_stat_count = [0] * 10
        self.case_stat = [' '] * 10
        self.macro_dict = {}

    # =============
    # tools
    # =============

    def print_attribute_asterisk(self, ctx, attribute_name):
        attributes = getattr(ctx, attribute_name)
        if attributes:
            for attribute in attributes():
                print(f"{attribute_name}:   ", attribute.getText())
        else:
            print(f"No {attribute_name} found.\n")
            pass
    
    def return_attribute_asterisk(self, ctx, attribute_name):
        attributes = getattr(ctx, attribute_name)
        info = []
        if attributes:
            for attribute in attributes():
                print(f"{attribute_name}:   ", attribute.getText())
                info.append(attribute.getText())
            return info
        else:
            print(f"No {attribute_name} found.\n")
            pass

    
    def print_attribute_qmask(self, ctx, attribute_name):
        attribute = getattr(ctx, attribute_name)
        if attribute() is not None:
            print(f"{attribute_name}:   ", attribute().getText())
        else:
            print(f"No {attribute_name} found.")
            pass

    def return_attribute_qmask(self, ctx, attribute_name):
        attribute = getattr(ctx, attribute_name)
        if attribute() is not None:
            # print(f"{attribute_name}:   ", attribute().getText())
            return attribute().getText()
        else:
            # print(f"No {attribute_name} found.")
            return None
            pass
    
    def extract_macros(self, macro_str):
        macro_str = macro_str[2:-1]
        macros = macro_str.split(',')
        for macro in macros:
            key_value = macro.split('=')
            if len(key_value) == 2:
                key = key_value[0].strip()
                key = key.replace("parameter", "")
                value = key_value[1].strip()
                self.macro_dict[key] = value

    # DONE:?!? 
    def convert_port_width(self, port_width):
        try:
            numeric_part = int(port_width)
            return numeric_part
        except ValueError:
            if "'" in port_width:
                width_part, _ = port_width.split("'")
                return int(width_part)
            elif '-' in port_width:
                macro_name = port_width.split('-')[0]
                if macro_name in self.macro_dict:
                    macro_value = self.macro_dict[macro_name]
                    return int(macro_value) - 1
                else:
                    return None  
            elif port_width in self.macro_dict:
                return self.macro_dict[port_width]
            else:
                return None

    # ===============
    # rule analysis
    # ===============

    def visitSource_text(self,ctx):
        return self.visitChildren(ctx)
    
    def visitDescription(self,ctx):
        return self.visitChildren(ctx)

    def visitModule_declaration(self, ctx):
        self.visitChildren(ctx)
        # print("module_declaration:      ", ctx.getText())
        # self.print_attribute_asterisk(ctx, "attribute_instance")
        # print("module_identifier:       ", ctx.module_identifier().getText())
        # self.print_attribute_qmask(ctx, "module_parameter_port_list")
        # self.print_attribute_qmask(ctx, "list_of_port_declarations")
        # self.print_attribute_asterisk(ctx, "module_item")

        # template1 = "Line 1: module {} has {} ports, their names are {}, {}."
        template1 = "module {} has {} ports, their names are {}, {}."
        in_port_info = ", ".join(f"{port}" for  port, _ in self.input_ports )
        out_port_info = ", ".join(f"{port}" for  port, _ in self.output_ports)
        output = template1.format(ctx.module_identifier().getText(), \
                            len(self.input_ports)+len(self.output_ports), \
                            in_port_info, out_port_info)
        print(output)

        # template2 = "Line {}: In the {} {} ports, {}."
        template2 = "In the {} {} ports, {}."
        input_ports_info = ", ".join(f"{port} has {width}-bit width" if width else port for port, width in self.input_ports)
        output_ports_info = ", ".join(f"{port} has {width}-bit width" if width else port for port, width in self.output_ports)
        # output1 = template2.format(2,len(self.input_ports),'input' ,input_ports_info)
        # output2 = template2.format(3,len(self.output_ports), 'output',output_ports_info)
        output1 = template2.format(len(self.input_ports),'input' ,input_ports_info)
        output2 = template2.format(len(self.output_ports), 'output',output_ports_info)
        print(output1)
        print(output2)

        # template4 = "Line 4: This module has {} always block."
        template4 = "This module has {} always block."
        print(template4.format(self.always_block_count))

        ordinal_names = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        if self.always_block_count > 0:
            for i in range(self.always_block_count):
                ordinal_number = ordinal_names[i]
                # template5 = "Line 5: The sensitive signal for {} block is{}."
                template5 = "The sensitive signal for {} block is{}."
                output5 = template5.format(ordinal_number, self.trigger_signal[i])
                print(output5)

                # template6 = "Line 6: In the {} always block, {} conditional statements exist. {}"
                template6 = "In the {} always block, {} conditional statements exist. {}"
                output6 = template6.format(ordinal_number, self.conditional_stat_count[i], self.conditional_stat[i])
                print(output6)

                # template7 = "Line 7: In the {} always block, {} case statements exist. {}"
                template7 = "In the {} always block, {} case statements exist. {}"
                output7 = template7.format(ordinal_number, self.case_stat_count[i], self.case_stat[i])
                print(output7)
                

        return None
    
    def visitList_of_port_declarations(self, ctx):
        # print("List_of_port_declarations     ",ctx.getText())
        # self.print_attribute_asterisk(ctx, "port_declaration")
        # TODO: inout port declarations
        return self.visitChildren(ctx)
    
    def visitInput_declaration(self, ctx:VerilogParser.Input_declarationContext):
        width = 1
        if ctx.range_():
            width_info = ctx.range_().msb_constant_expression().constant_expression().getText()
            width = self.convert_port_width(width_info) + 1

        for port_identifier in ctx.list_of_port_identifiers().getText().split(','):
            self.input_ports.append((port_identifier, width))

        return self.visitChildren(ctx)
    
    def visitOutput_declaration(self, ctx:VerilogParser.Output_declarationContext):
        width = 1
        if ctx.range_():
            width_info = ctx.range_().msb_constant_expression().constant_expression().getText()
            width = self.convert_port_width(width_info) + 1

        # DONE:'output' net_type? 'signed'? range_? list_of_port_identifiersort_identifiers").split(' '):
        output_ports = ctx.list_of_variable_port_identifiers().getText().split(',') \
                        if ctx.list_of_variable_port_identifiers() is not None \
                        else ctx.list_of_port_identifiers().getText().split(',')
        for port_identifier in output_ports:
            self.output_ports.append((port_identifier, width))
        return self.visitChildren(ctx)

    def visitModule_item(self, ctx):
        # print("module item:",ctx.getText())
        # print("module_or_generate_item:",ctx.module_or_generate_item().getText())
        return self.visitChildren(ctx)

    def visitModule_parameter_port_list(self, ctx):
        # print("module parameter port list:",ctx.getText())
        # DONE: macro params of ports width
        macro_str = ctx.getText()
        self.extract_macros(macro_str)
        return self.visitChildren(ctx)

    def visitModule_or_generate_item(self, ctx):
        # print("module or generate item:",ctx.getText())
        return self.visitChildren(ctx)

    def visitModule_or_generate_item_declaration(self, ctx):
        # print("module or generate item declaration:",ctx.getText())
        return self.visitChildren(ctx)

    def visitModule_instantiation(self, ctx):
        # print("module_instantiation:",ctx.getText())
        return self.visitChildren(ctx)

    def visitInitial_construct(self, ctx):
        # print("initial_construct:",ctx.getText())
        return self.visitChildren(ctx)

    def visitAlways_construct(self, ctx):
        self.visitChildren(ctx)
        trigger_block = ctx.statement().getText()
        self.always_block_count += 1
        return None
        
    def visitCase_statement(self, ctx: VerilogParser.Case_statementContext):
        self.case_stat_count[self.always_block_count] += 1

        case_expr = ctx.expression().getText()
        case_output = "In this case block: "
        for case_item_ctx in ctx.case_item():
            if case_item_ctx.DEFAULT():
                case_output += "Otherwise, the default setting is {}".format(case_item_ctx.statement_or_null().getText())
            else:
                case_output += "if {} equals to {}, then {}".format(case_expr,\
                                    case_item_ctx.expression(0).getText(),\
                                    case_item_ctx.statement_or_null().getText())
        self.case_stat[self.always_block_count] += case_output

        return self.visitChildren(ctx)

    def has_nested_conditional_stat(self, ctx):
        flag = [0, 0]

        # conditional_statement -> statement_or_null -> statement -> conditional_statement
        # true_block
        if isinstance(ctx.getChild(4).getChild(0).getChild(0), \
                        VerilogParser.Conditional_statementContext):
            flag[0] = 1
        # false_block
        if ctx.getChildCount() == 7:
            if isinstance(ctx.getChild(6).getChild(0).getChild(0), \
                        VerilogParser.Conditional_statementContext):
                flag[1] = 1

        # begin ... end
        # conditional_statement -> statement_or_null -> statement -> seq_block -> statement -> conditional_statement
        # true_block
        if isinstance(ctx.getChild(4).getChild(0).getChild(0), \
                        VerilogParser.Seq_blockContext):
            for i in range(ctx.getChild(4).getChild(0).getChild(0).getChildCount()):
                for j in range(ctx.getChild(4).getChild(0).getChild(0).getChild(i).getChildCount()):
                    if isinstance(ctx.getChild(4).getChild(0).getChild(0).getChild(i).getChild(j), \
                        VerilogParser.Conditional_statementContext):
                        flag[0] = 2
        # false_block
        if ctx.getChildCount() == 7:
            if isinstance(ctx.getChild(6).getChild(0).getChild(0), \
                        VerilogParser.Seq_blockContext):
                for i in range(ctx.getChild(6).getChild(0).getChild(0).getChildCount()):
                    for j in range(ctx.getChild(6).getChild(0).getChild(0).getChild(i).getChildCount()):
                        if isinstance(ctx.getChild(6).getChild(0).getChild(0).getChild(i).getChild(j), \
                            VerilogParser.Conditional_statementContext):
                            flag[1] = 2
        return flag
    
    def is_nested_conditional_stat(self, ctx):
        flag = 0
        if isinstance(ctx.parentCtx.parentCtx.parentCtx, \
                        VerilogParser.Conditional_statementContext):
            flag = 1
        if isinstance(ctx.parentCtx.parentCtx, \
                        VerilogParser.Seq_blockContext):
            if isinstance(ctx.parentCtx.parentCtx.parentCtx.parentCtx.parentCtx, \
                VerilogParser.Conditional_statementContext):
                flag = 1

        return flag

    def visitConditional_statement(self, ctx: VerilogParser.Conditional_statementContext):
        condition = ctx.expression().getText()
        true_block = ctx.statement_or_null(0).getText()
        false_block = ctx.statement_or_null(1).getText() \
                            if ctx.statement_or_null(1) is not None \
                            else "switch to other statements or blocks"

        template = "If {} is true, then {}. Otherwise, {}."
        mode_info_1 = " under this circumstance, we enter another conditional block. "\
                            "Inside the nested conditional block, " 
        mode_info_2 = " We enter a sequential block that contains multiple statements."\
                           " Within these statements, there is a conditional statement."\
                            "Inside the nested conditional block, "
        intro =  " Now, let's delve deeper into the inner conditional block, where we find that "

        nested_flag = self.has_nested_conditional_stat(ctx)
        self.conditional_stat_count[self.always_block_count] += 1
        child_flag = self.is_nested_conditional_stat(ctx)

        nested_info = [" ", mode_info_1, mode_info_2]
        branch0 = nested_info[nested_flag[0]]
        branch1 = nested_info[nested_flag[1]]
        info = template.format(condition, branch0 + true_block, branch1 + false_block)
        if child_flag != 0:
            self.conditional_stat[self.always_block_count] += intro
        self.conditional_stat[self.always_block_count] += info

        return self.visitChildren(ctx)


    # def visitLoop_statement(self, ctx):
    #     loop_type = ctx.start.text
    #     loop_body = ctx.loop_body().getText()
    #     print("Loop statement:", loop_type, loop_body)
    #     return self.visitChildren(ctx)

    # def visitBlocking_assignment(self, ctx: VerilogParser.Blocking_assignmentContext):
    #     lhs = ctx.variable_lvalue().getText()
    #     rhs = ctx.expression().getText()

    #     print("blocking assignment:")
    #     print("left-hand side:", lhs)
    #     print("right-hand side:", rhs)
    #     print("blocking assignment:", lhs, "=", rhs)

    #     return self.visitChildren(ctx)

    # def visitNonblocking_assignment(self, ctx: VerilogParser.Nonblocking_assignmentContext):
    #     lhs = ctx.variable_lvalue().getText()
    #     rhs = ctx.expression().getText()
    #     print("nonblocking assignment:",ctx.getText())
    #     print("nonblocking assignment:")
    #     print("left-hand side:", lhs)
    #     print("right-hand side:", rhs)
    #     print("nonblocking assignment:", lhs, "<=", rhs)
    #     return self.visitChildren(ctx)

    def visitEvent_control(self, ctx:VerilogParser.Event_controlContext):
        # print("event_control", ctx.getText() )
        exp = self.return_attribute_qmask(ctx, "event_expression")
        
        template = " on the {} edge of {} "
        if ("*" in ctx.getText()) and (exp is None):
            edge = "any edge"
            sig = "any input signal or level"
            info = template.format(edge, sig)
        elif exp is not None:
            sig = self.return_attribute_qmask(ctx.event_expression(), "expression")
            edge = "negative" if "neg" in exp else "positive"
            info = template.format(edge, sig)
            if (sig == None) and (ctx.event_expression().getChildCount() == 3):
                left_sig = ctx.event_expression().getChild(0).expression().getText()
                left_edge = "positive" if "pos"  in ctx.event_expression().getChild(0).getText()\
                                 else "negative"
                right_sig = ctx.event_expression().getChild(2).expression().getText()
                right_edge = "negative" if "pos"  not in ctx.event_expression().getChild(2).getText()\
                                 else "positive"
                template = " on the {} edge of {} and the {} edge of {}"
                info = template.format(left_edge, left_sig, right_edge, right_sig)
                
        self.trigger_signal.append(info)
        return self.visitChildren(ctx)

    def visitEvent_expression(self, ctx:VerilogParser.Event_expressionContext):
        # print("event_expression ", ctx.getText())
        return self.visitChildren(ctx)

    def visitProcedural_timing_control_statement(self, ctx:VerilogParser.Procedural_timing_control_statementContext):
        # print("Procedural_timing_control_statementContext ",ctx.getText())
        # self.print_attribute_qmask(ctx, "statement_or_null")
        return self.visitChildren(ctx)

    def visitSeq_block(self, ctx:VerilogParser.Seq_blockContext):
        # print("seq block:",ctx.getText())
        return self.visitChildren(ctx)

    # def visitNet_declaration(self, ctx):
    #     print("net declaration:",ctx.getText())
    #     return self.visitChildren(ctx)
    
    # def visitReg_declaration(self, ctx):
    #     print("reg declaration:", ctx.getText())
    #     return self.visitChildren(ctx)

    # def visitInteger_declaration(self, ctx):
    #     print("integer declaration:", ctx.getText())
    #     return self.visitChildren(ctx)

def main(argv):
    input_stream = FileStream(argv[1])  # load input stream
    # print(input_stream)
    lexer = VerilogLexer(input_stream)  # input stream -> tokens            [@-1,9:11='dhf',<198>,1:9]
    # tokens = lexer.getAllTokens()
    # for token in tokens:
    #     print(token)
    stream = CommonTokenStream(lexer)   # token organized to token stream   [@2,9:11='dhf',<198>,1:9][@18,40:39='<EOF>',<-1>,4:7]
    # stream.fill()
    # for token in stream.tokens:
    #     print(token)
    parser = VerilogParser(stream)      # token stream -> ast node
    # rewriter = TokenStreamRewriter(tokens=stream)   # rewrite token stream
    # rewriter.insertBeforeIndex(4, 'start')
    # rewriter.insertAfter(15, 'end')
    # rewriter.replaceIndex(46, 'negative!')
    # print(rewriter.getDefaultText())

    tree = parser.source_text()                     # ast node -> ast tree
    # print(tree.toStringTree(recog=parser))
    calculator = VerilogVisitor()             # instantiate
    calculator.visitSource_text(tree)               # invoke func and travel tree

if __name__ == '__main__':
    main(sys.argv)