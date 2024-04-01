# Generated from VerilogPreParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .VerilogPreParser import VerilogPreParser
else:
    from VerilogPreParser import VerilogPreParser

# This class defines a complete generic visitor for a parse tree produced by VerilogPreParser.

class VerilogPreParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerilogPreParser#source_text.
    def visitSource_text(self, ctx:VerilogPreParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#compiler_directive.
    def visitCompiler_directive(self, ctx:VerilogPreParser.Compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#begin_keywords_directive.
    def visitBegin_keywords_directive(self, ctx:VerilogPreParser.Begin_keywords_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#celldefine_directive.
    def visitCelldefine_directive(self, ctx:VerilogPreParser.Celldefine_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#default_nettype_directive.
    def visitDefault_nettype_directive(self, ctx:VerilogPreParser.Default_nettype_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#default_nettype_value.
    def visitDefault_nettype_value(self, ctx:VerilogPreParser.Default_nettype_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#else_directive.
    def visitElse_directive(self, ctx:VerilogPreParser.Else_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#elsif_directive.
    def visitElsif_directive(self, ctx:VerilogPreParser.Elsif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#end_keywords_directive.
    def visitEnd_keywords_directive(self, ctx:VerilogPreParser.End_keywords_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#endcelldefine_directive.
    def visitEndcelldefine_directive(self, ctx:VerilogPreParser.Endcelldefine_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#endif_directive.
    def visitEndif_directive(self, ctx:VerilogPreParser.Endif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#filename.
    def visitFilename(self, ctx:VerilogPreParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#group_of_lines.
    def visitGroup_of_lines(self, ctx:VerilogPreParser.Group_of_linesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#identifier.
    def visitIdentifier(self, ctx:VerilogPreParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#ifdef_directive.
    def visitIfdef_directive(self, ctx:VerilogPreParser.Ifdef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#ifndef_directive.
    def visitIfndef_directive(self, ctx:VerilogPreParser.Ifndef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#include_directive.
    def visitInclude_directive(self, ctx:VerilogPreParser.Include_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#level.
    def visitLevel(self, ctx:VerilogPreParser.LevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#line_directive.
    def visitLine_directive(self, ctx:VerilogPreParser.Line_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_delimiter.
    def visitMacro_delimiter(self, ctx:VerilogPreParser.Macro_delimiterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_esc_newline.
    def visitMacro_esc_newline(self, ctx:VerilogPreParser.Macro_esc_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_esc_quote.
    def visitMacro_esc_quote(self, ctx:VerilogPreParser.Macro_esc_quoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_identifier.
    def visitMacro_identifier(self, ctx:VerilogPreParser.Macro_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_name.
    def visitMacro_name(self, ctx:VerilogPreParser.Macro_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_quote.
    def visitMacro_quote(self, ctx:VerilogPreParser.Macro_quoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_text.
    def visitMacro_text(self, ctx:VerilogPreParser.Macro_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_text_.
    def visitMacro_text_(self, ctx:VerilogPreParser.Macro_text_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#macro_usage.
    def visitMacro_usage(self, ctx:VerilogPreParser.Macro_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#nounconnected_drive_directive.
    def visitNounconnected_drive_directive(self, ctx:VerilogPreParser.Nounconnected_drive_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#number.
    def visitNumber(self, ctx:VerilogPreParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#pragma_directive.
    def visitPragma_directive(self, ctx:VerilogPreParser.Pragma_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#pragma_expression.
    def visitPragma_expression(self, ctx:VerilogPreParser.Pragma_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#pragma_keyword.
    def visitPragma_keyword(self, ctx:VerilogPreParser.Pragma_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#pragma_name.
    def visitPragma_name(self, ctx:VerilogPreParser.Pragma_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#pragma_value.
    def visitPragma_value(self, ctx:VerilogPreParser.Pragma_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#resetall_directive.
    def visitResetall_directive(self, ctx:VerilogPreParser.Resetall_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#source_text_.
    def visitSource_text_(self, ctx:VerilogPreParser.Source_text_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#string_.
    def visitString_(self, ctx:VerilogPreParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#text_macro_definition.
    def visitText_macro_definition(self, ctx:VerilogPreParser.Text_macro_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#text_macro_usage.
    def visitText_macro_usage(self, ctx:VerilogPreParser.Text_macro_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#time_precision.
    def visitTime_precision(self, ctx:VerilogPreParser.Time_precisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#time_unit.
    def visitTime_unit(self, ctx:VerilogPreParser.Time_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#timescale_directive.
    def visitTimescale_directive(self, ctx:VerilogPreParser.Timescale_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#unconnected_drive_directive.
    def visitUnconnected_drive_directive(self, ctx:VerilogPreParser.Unconnected_drive_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#unconnected_drive_value.
    def visitUnconnected_drive_value(self, ctx:VerilogPreParser.Unconnected_drive_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#undef_directive.
    def visitUndef_directive(self, ctx:VerilogPreParser.Undef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreParser#version_specifier.
    def visitVersion_specifier(self, ctx:VerilogPreParser.Version_specifierContext):
        return self.visitChildren(ctx)



del VerilogPreParser