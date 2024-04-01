# Generated from VerilogParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .VerilogParser import VerilogParser
else:
    from VerilogParser import VerilogParser

# This class defines a complete generic visitor for a parse tree produced by VerilogParser.

class VerilogParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerilogParser#library_text.
    def visitLibrary_text(self, ctx:VerilogParser.Library_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_description.
    def visitLibrary_description(self, ctx:VerilogParser.Library_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_declaration.
    def visitLibrary_declaration(self, ctx:VerilogParser.Library_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_incdir.
    def visitLibrary_incdir(self, ctx:VerilogParser.Library_incdirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#include_statement.
    def visitInclude_statement(self, ctx:VerilogParser.Include_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_path_spec.
    def visitFile_path_spec(self, ctx:VerilogParser.File_path_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#source_text.
    def visitSource_text(self, ctx:VerilogParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#description.
    def visitDescription(self, ctx:VerilogParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_declaration.
    def visitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_keyword.
    def visitModule_keyword(self, ctx:VerilogParser.Module_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_parameter_port_list.
    def visitModule_parameter_port_list(self, ctx:VerilogParser.Module_parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx:VerilogParser.List_of_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port.
    def visitPort(self, ctx:VerilogParser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_implicit.
    def visitPort_implicit(self, ctx:VerilogParser.Port_implicitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_explicit.
    def visitPort_explicit(self, ctx:VerilogParser.Port_explicitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_expression.
    def visitPort_expression(self, ctx:VerilogParser.Port_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_reference.
    def visitPort_reference(self, ctx:VerilogParser.Port_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_declaration.
    def visitPort_declaration(self, ctx:VerilogParser.Port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_item.
    def visitModule_item(self, ctx:VerilogParser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_or_generate_item.
    def visitModule_or_generate_item(self, ctx:VerilogParser.Module_or_generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_or_generate_item_declaration.
    def visitModule_or_generate_item_declaration(self, ctx:VerilogParser.Module_or_generate_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_override.
    def visitParameter_override(self, ctx:VerilogParser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_declaration.
    def visitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#design_statement.
    def visitDesign_statement(self, ctx:VerilogParser.Design_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#design_statement_item.
    def visitDesign_statement_item(self, ctx:VerilogParser.Design_statement_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_rule_statement.
    def visitConfig_rule_statement(self, ctx:VerilogParser.Config_rule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#default_clause.
    def visitDefault_clause(self, ctx:VerilogParser.Default_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inst_clause.
    def visitInst_clause(self, ctx:VerilogParser.Inst_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inst_name.
    def visitInst_name(self, ctx:VerilogParser.Inst_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cell_clause.
    def visitCell_clause(self, ctx:VerilogParser.Cell_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#liblist_clause.
    def visitLiblist_clause(self, ctx:VerilogParser.Liblist_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#use_clause.
    def visitUse_clause(self, ctx:VerilogParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx:VerilogParser.Local_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:VerilogParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_declaration.
    def visitSpecparam_declaration(self, ctx:VerilogParser.Specparam_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_type.
    def visitParameter_type(self, ctx:VerilogParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inout_declaration.
    def visitInout_declaration(self, ctx:VerilogParser.Inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_declaration.
    def visitInput_declaration(self, ctx:VerilogParser.Input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_declaration.
    def visitOutput_declaration(self, ctx:VerilogParser.Output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_declaration.
    def visitEvent_declaration(self, ctx:VerilogParser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#integer_declaration.
    def visitInteger_declaration(self, ctx:VerilogParser.Integer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_declaration.
    def visitNet_declaration(self, ctx:VerilogParser.Net_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_declaration.
    def visitReal_declaration(self, ctx:VerilogParser.Real_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#realtime_declaration.
    def visitRealtime_declaration(self, ctx:VerilogParser.Realtime_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#reg_declaration.
    def visitReg_declaration(self, ctx:VerilogParser.Reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#time_declaration.
    def visitTime_declaration(self, ctx:VerilogParser.Time_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_type.
    def visitNet_type(self, ctx:VerilogParser.Net_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_variable_type.
    def visitOutput_variable_type(self, ctx:VerilogParser.Output_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_type.
    def visitReal_type(self, ctx:VerilogParser.Real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_type.
    def visitVariable_type(self, ctx:VerilogParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#drive_strength.
    def visitDrive_strength(self, ctx:VerilogParser.Drive_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strength0.
    def visitStrength0(self, ctx:VerilogParser.Strength0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strength1.
    def visitStrength1(self, ctx:VerilogParser.Strength1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#charge_strength.
    def visitCharge_strength(self, ctx:VerilogParser.Charge_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay3.
    def visitDelay3(self, ctx:VerilogParser.Delay3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay2.
    def visitDelay2(self, ctx:VerilogParser.Delay2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_value.
    def visitDelay_value(self, ctx:VerilogParser.Delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_defparam_assignments.
    def visitList_of_defparam_assignments(self, ctx:VerilogParser.List_of_defparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_event_identifiers.
    def visitList_of_event_identifiers(self, ctx:VerilogParser.List_of_event_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_id.
    def visitEvent_id(self, ctx:VerilogParser.Event_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_decl_assignments.
    def visitList_of_net_decl_assignments(self, ctx:VerilogParser.List_of_net_decl_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_identifiers.
    def visitList_of_net_identifiers(self, ctx:VerilogParser.List_of_net_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_id.
    def visitNet_id(self, ctx:VerilogParser.Net_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_param_assignments.
    def visitList_of_param_assignments(self, ctx:VerilogParser.List_of_param_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx:VerilogParser.List_of_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_real_identifiers.
    def visitList_of_real_identifiers(self, ctx:VerilogParser.List_of_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_specparam_assignments.
    def visitList_of_specparam_assignments(self, ctx:VerilogParser.List_of_specparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_variable_identifiers.
    def visitList_of_variable_identifiers(self, ctx:VerilogParser.List_of_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_variable_port_identifiers.
    def visitList_of_variable_port_identifiers(self, ctx:VerilogParser.List_of_variable_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#var_port_id.
    def visitVar_port_id(self, ctx:VerilogParser.Var_port_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#defparam_assignment.
    def visitDefparam_assignment(self, ctx:VerilogParser.Defparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_decl_assignment.
    def visitNet_decl_assignment(self, ctx:VerilogParser.Net_decl_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#param_assignment.
    def visitParam_assignment(self, ctx:VerilogParser.Param_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_assignment.
    def visitSpecparam_assignment(self, ctx:VerilogParser.Specparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulse_control_specparam.
    def visitPulse_control_specparam(self, ctx:VerilogParser.Pulse_control_specparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#error_limit_value.
    def visitError_limit_value(self, ctx:VerilogParser.Error_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#reject_limit_value.
    def visitReject_limit_value(self, ctx:VerilogParser.Reject_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#limit_value.
    def visitLimit_value(self, ctx:VerilogParser.Limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dimension.
    def visitDimension(self, ctx:VerilogParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#range_.
    def visitRange_(self, ctx:VerilogParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_declaration.
    def visitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx:VerilogParser.Function_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_port_list.
    def visitFunction_port_list(self, ctx:VerilogParser.Function_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#func_port_item.
    def visitFunc_port_item(self, ctx:VerilogParser.Func_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_range_or_type.
    def visitFunction_range_or_type(self, ctx:VerilogParser.Function_range_or_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_declaration.
    def visitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_item_declaration.
    def visitTask_item_declaration(self, ctx:VerilogParser.Task_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_list.
    def visitTask_port_list(self, ctx:VerilogParser.Task_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_item.
    def visitTask_port_item(self, ctx:VerilogParser.Task_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_input_declaration.
    def visitTf_input_declaration(self, ctx:VerilogParser.Tf_input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_output_declaration.
    def visitTf_output_declaration(self, ctx:VerilogParser.Tf_output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_inout_declaration.
    def visitTf_inout_declaration(self, ctx:VerilogParser.Tf_inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_type.
    def visitTask_port_type(self, ctx:VerilogParser.Task_port_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx:VerilogParser.Block_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_block_variable_identifiers.
    def visitList_of_block_variable_identifiers(self, ctx:VerilogParser.List_of_block_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_block_real_identifiers.
    def visitList_of_block_real_identifiers(self, ctx:VerilogParser.List_of_block_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_variable_type.
    def visitBlock_variable_type(self, ctx:VerilogParser.Block_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_real_type.
    def visitBlock_real_type(self, ctx:VerilogParser.Block_real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#gate_instantiation.
    def visitGate_instantiation(self, ctx:VerilogParser.Gate_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx:VerilogParser.Cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx:VerilogParser.Enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx:VerilogParser.Mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx:VerilogParser.N_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx:VerilogParser.N_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx:VerilogParser.Pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx:VerilogParser.Pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx:VerilogParser.Pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#name_of_gate_instance.
    def visitName_of_gate_instance(self, ctx:VerilogParser.Name_of_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulldown_strength.
    def visitPulldown_strength(self, ctx:VerilogParser.Pulldown_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pullup_strength.
    def visitPullup_strength(self, ctx:VerilogParser.Pullup_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_terminal.
    def visitEnable_terminal(self, ctx:VerilogParser.Enable_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inout_terminal.
    def visitInout_terminal(self, ctx:VerilogParser.Inout_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_terminal.
    def visitInput_terminal(self, ctx:VerilogParser.Input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx:VerilogParser.Ncontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_terminal.
    def visitOutput_terminal(self, ctx:VerilogParser.Output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx:VerilogParser.Pcontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx:VerilogParser.Cmos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_gatetype.
    def visitEnable_gatetype(self, ctx:VerilogParser.Enable_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mos_switchtype.
    def visitMos_switchtype(self, ctx:VerilogParser.Mos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx:VerilogParser.N_input_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx:VerilogParser.N_output_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_en_switchtype.
    def visitPass_en_switchtype(self, ctx:VerilogParser.Pass_en_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_switchtype.
    def visitPass_switchtype(self, ctx:VerilogParser.Pass_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instantiation.
    def visitModule_instantiation(self, ctx:VerilogParser.Module_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_value_assignment.
    def visitParameter_value_assignment(self, ctx:VerilogParser.Parameter_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_parameter_assignments.
    def visitList_of_parameter_assignments(self, ctx:VerilogParser.List_of_parameter_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ordered_parameter_assignment.
    def visitOrdered_parameter_assignment(self, ctx:VerilogParser.Ordered_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#named_parameter_assignment.
    def visitNamed_parameter_assignment(self, ctx:VerilogParser.Named_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instance.
    def visitModule_instance(self, ctx:VerilogParser.Module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#name_of_module_instance.
    def visitName_of_module_instance(self, ctx:VerilogParser.Name_of_module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_connections.
    def visitList_of_port_connections(self, ctx:VerilogParser.List_of_port_connectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ordered_port_connection.
    def visitOrdered_port_connection(self, ctx:VerilogParser.Ordered_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#named_port_connection.
    def visitNamed_port_connection(self, ctx:VerilogParser.Named_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_region.
    def visitGenerate_region(self, ctx:VerilogParser.Generate_regionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_declaration.
    def visitGenvar_declaration(self, ctx:VerilogParser.Genvar_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_genvar_identifiers.
    def visitList_of_genvar_identifiers(self, ctx:VerilogParser.List_of_genvar_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#loop_generate_construct.
    def visitLoop_generate_construct(self, ctx:VerilogParser.Loop_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_initialization.
    def visitGenvar_initialization(self, ctx:VerilogParser.Genvar_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_expression.
    def visitGenvar_expression(self, ctx:VerilogParser.Genvar_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_iteration.
    def visitGenvar_iteration(self, ctx:VerilogParser.Genvar_iterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conditional_generate_construct.
    def visitConditional_generate_construct(self, ctx:VerilogParser.Conditional_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#if_generate_construct.
    def visitIf_generate_construct(self, ctx:VerilogParser.If_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_generate_construct.
    def visitCase_generate_construct(self, ctx:VerilogParser.Case_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_generate_item.
    def visitCase_generate_item(self, ctx:VerilogParser.Case_generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block.
    def visitGenerate_block(self, ctx:VerilogParser.Generate_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block_name.
    def visitGenerate_block_name(self, ctx:VerilogParser.Generate_block_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block_or_null.
    def visitGenerate_block_or_null(self, ctx:VerilogParser.Generate_block_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_declaration.
    def visitUdp_declaration(self, ctx:VerilogParser.Udp_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_port_list.
    def visitUdp_port_list(self, ctx:VerilogParser.Udp_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_declaration_port_list.
    def visitUdp_declaration_port_list(self, ctx:VerilogParser.Udp_declaration_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_port_declaration.
    def visitUdp_port_declaration(self, ctx:VerilogParser.Udp_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_output_declaration.
    def visitUdp_output_declaration(self, ctx:VerilogParser.Udp_output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_input_declaration.
    def visitUdp_input_declaration(self, ctx:VerilogParser.Udp_input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_reg_declaration.
    def visitUdp_reg_declaration(self, ctx:VerilogParser.Udp_reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_body.
    def visitUdp_body(self, ctx:VerilogParser.Udp_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#combinational_body.
    def visitCombinational_body(self, ctx:VerilogParser.Combinational_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#combinational_entry.
    def visitCombinational_entry(self, ctx:VerilogParser.Combinational_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#sequential_body.
    def visitSequential_body(self, ctx:VerilogParser.Sequential_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_initial_statement.
    def visitUdp_initial_statement(self, ctx:VerilogParser.Udp_initial_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#init_val.
    def visitInit_val(self, ctx:VerilogParser.Init_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#sequential_entry.
    def visitSequential_entry(self, ctx:VerilogParser.Sequential_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#seq_input_list.
    def visitSeq_input_list(self, ctx:VerilogParser.Seq_input_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#level_input_list.
    def visitLevel_input_list(self, ctx:VerilogParser.Level_input_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_input_list.
    def visitEdge_input_list(self, ctx:VerilogParser.Edge_input_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_indicator.
    def visitEdge_indicator(self, ctx:VerilogParser.Edge_indicatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#current_state.
    def visitCurrent_state(self, ctx:VerilogParser.Current_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#next_state.
    def visitNext_state(self, ctx:VerilogParser.Next_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_symbol.
    def visitOutput_symbol(self, ctx:VerilogParser.Output_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#level_symbol.
    def visitLevel_symbol(self, ctx:VerilogParser.Level_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_symbol.
    def visitEdge_symbol(self, ctx:VerilogParser.Edge_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_instantiation.
    def visitUdp_instantiation(self, ctx:VerilogParser.Udp_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_instance.
    def visitUdp_instance(self, ctx:VerilogParser.Udp_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#name_of_udp_instance.
    def visitName_of_udp_instance(self, ctx:VerilogParser.Name_of_udp_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#continuous_assign.
    def visitContinuous_assign(self, ctx:VerilogParser.Continuous_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_assignments.
    def visitList_of_net_assignments(self, ctx:VerilogParser.List_of_net_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_assignment.
    def visitNet_assignment(self, ctx:VerilogParser.Net_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#initial_construct.
    def visitInitial_construct(self, ctx:VerilogParser.Initial_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#always_construct.
    def visitAlways_construct(self, ctx:VerilogParser.Always_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#blocking_assignment.
    def visitBlocking_assignment(self, ctx:VerilogParser.Blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx:VerilogParser.Nonblocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx:VerilogParser.Procedural_continuous_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_assignment.
    def visitVariable_assignment(self, ctx:VerilogParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#par_block.
    def visitPar_block(self, ctx:VerilogParser.Par_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_name.
    def visitBlock_name(self, ctx:VerilogParser.Block_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#seq_block.
    def visitSeq_block(self, ctx:VerilogParser.Seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#statement.
    def visitStatement(self, ctx:VerilogParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#statement_or_null.
    def visitStatement_or_null(self, ctx:VerilogParser.Statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_statement.
    def visitFunction_statement(self, ctx:VerilogParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_control.
    def visitDelay_control(self, ctx:VerilogParser.Delay_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx:VerilogParser.Delay_or_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#disable_statement.
    def visitDisable_statement(self, ctx:VerilogParser.Disable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_control.
    def visitEvent_control(self, ctx:VerilogParser.Event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_trigger.
    def visitEvent_trigger(self, ctx:VerilogParser.Event_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_expression.
    def visitEvent_expression(self, ctx:VerilogParser.Event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_timing_control.
    def visitProcedural_timing_control(self, ctx:VerilogParser.Procedural_timing_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx:VerilogParser.Procedural_timing_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#wait_statement.
    def visitWait_statement(self, ctx:VerilogParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conditional_statement.
    def visitConditional_statement(self, ctx:VerilogParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_statement.
    def visitCase_statement(self, ctx:VerilogParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_item.
    def visitCase_item(self, ctx:VerilogParser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#loop_statement.
    def visitLoop_statement(self, ctx:VerilogParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_task_enable.
    def visitSystem_task_enable(self, ctx:VerilogParser.System_task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#sys_task_en_port_list.
    def visitSys_task_en_port_list(self, ctx:VerilogParser.Sys_task_en_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#sys_task_en_port_item.
    def visitSys_task_en_port_item(self, ctx:VerilogParser.Sys_task_en_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_enable.
    def visitTask_enable(self, ctx:VerilogParser.Task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_en_port_list.
    def visitTask_en_port_list(self, ctx:VerilogParser.Task_en_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_block.
    def visitSpecify_block(self, ctx:VerilogParser.Specify_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_item.
    def visitSpecify_item(self, ctx:VerilogParser.Specify_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulsestyle_declaration.
    def visitPulsestyle_declaration(self, ctx:VerilogParser.Pulsestyle_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#showcancelled_declaration.
    def visitShowcancelled_declaration(self, ctx:VerilogParser.Showcancelled_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_declaration.
    def visitPath_declaration(self, ctx:VerilogParser.Path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#simple_path_declaration.
    def visitSimple_path_declaration(self, ctx:VerilogParser.Simple_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parallel_path_description.
    def visitParallel_path_description(self, ctx:VerilogParser.Parallel_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#full_path_description.
    def visitFull_path_description(self, ctx:VerilogParser.Full_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_inputs.
    def visitList_of_path_inputs(self, ctx:VerilogParser.List_of_path_inputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_outputs.
    def visitList_of_path_outputs(self, ctx:VerilogParser.List_of_path_outputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_input_terminal_descriptor.
    def visitSpecify_input_terminal_descriptor(self, ctx:VerilogParser.Specify_input_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_output_terminal_descriptor.
    def visitSpecify_output_terminal_descriptor(self, ctx:VerilogParser.Specify_output_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_identifier.
    def visitInput_identifier(self, ctx:VerilogParser.Input_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_identifier.
    def visitOutput_identifier(self, ctx:VerilogParser.Output_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_delay_value.
    def visitPath_delay_value(self, ctx:VerilogParser.Path_delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_delay_expressions.
    def visitList_of_path_delay_expressions(self, ctx:VerilogParser.List_of_path_delay_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t_path_delay_expression.
    def visitT_path_delay_expression(self, ctx:VerilogParser.T_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#trise_path_delay_expression.
    def visitTrise_path_delay_expression(self, ctx:VerilogParser.Trise_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tfall_path_delay_expression.
    def visitTfall_path_delay_expression(self, ctx:VerilogParser.Tfall_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz_path_delay_expression.
    def visitTz_path_delay_expression(self, ctx:VerilogParser.Tz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t01_path_delay_expression.
    def visitT01_path_delay_expression(self, ctx:VerilogParser.T01_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t10_path_delay_expression.
    def visitT10_path_delay_expression(self, ctx:VerilogParser.T10_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t0z_path_delay_expression.
    def visitT0z_path_delay_expression(self, ctx:VerilogParser.T0z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz1_path_delay_expression.
    def visitTz1_path_delay_expression(self, ctx:VerilogParser.Tz1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t1z_path_delay_expression.
    def visitT1z_path_delay_expression(self, ctx:VerilogParser.T1z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz0_path_delay_expression.
    def visitTz0_path_delay_expression(self, ctx:VerilogParser.Tz0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t0x_path_delay_expression.
    def visitT0x_path_delay_expression(self, ctx:VerilogParser.T0x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tx1_path_delay_expression.
    def visitTx1_path_delay_expression(self, ctx:VerilogParser.Tx1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t1x_path_delay_expression.
    def visitT1x_path_delay_expression(self, ctx:VerilogParser.T1x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tx0_path_delay_expression.
    def visitTx0_path_delay_expression(self, ctx:VerilogParser.Tx0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#txz_path_delay_expression.
    def visitTxz_path_delay_expression(self, ctx:VerilogParser.Txz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tzx_path_delay_expression.
    def visitTzx_path_delay_expression(self, ctx:VerilogParser.Tzx_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_delay_expression.
    def visitPath_delay_expression(self, ctx:VerilogParser.Path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_sensitive_path_declaration.
    def visitEdge_sensitive_path_declaration(self, ctx:VerilogParser.Edge_sensitive_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parallel_edge_sensitive_path_description.
    def visitParallel_edge_sensitive_path_description(self, ctx:VerilogParser.Parallel_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#full_edge_sensitive_path_description.
    def visitFull_edge_sensitive_path_description(self, ctx:VerilogParser.Full_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#data_source_expression.
    def visitData_source_expression(self, ctx:VerilogParser.Data_source_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_identifier.
    def visitEdge_identifier(self, ctx:VerilogParser.Edge_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#state_dependent_path_declaration.
    def visitState_dependent_path_declaration(self, ctx:VerilogParser.State_dependent_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#polarity_operator.
    def visitPolarity_operator(self, ctx:VerilogParser.Polarity_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_timing_check.
    def visitSystem_timing_check(self, ctx:VerilogParser.System_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#setup_timing_check.
    def visitSetup_timing_check(self, ctx:VerilogParser.Setup_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#notifier_opt.
    def visitNotifier_opt(self, ctx:VerilogParser.Notifier_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hold_timing_check.
    def visitHold_timing_check(self, ctx:VerilogParser.Hold_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#setuphold_timing_check.
    def visitSetuphold_timing_check(self, ctx:VerilogParser.Setuphold_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timing_check_opt.
    def visitTiming_check_opt(self, ctx:VerilogParser.Timing_check_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#stamptime_cond_opt.
    def visitStamptime_cond_opt(self, ctx:VerilogParser.Stamptime_cond_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#checktime_cond_opt.
    def visitChecktime_cond_opt(self, ctx:VerilogParser.Checktime_cond_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delayed_ref_opt.
    def visitDelayed_ref_opt(self, ctx:VerilogParser.Delayed_ref_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delayed_data_opt.
    def visitDelayed_data_opt(self, ctx:VerilogParser.Delayed_data_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#recovery_timing_check.
    def visitRecovery_timing_check(self, ctx:VerilogParser.Recovery_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#removal_timing_check.
    def visitRemoval_timing_check(self, ctx:VerilogParser.Removal_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#recrem_timing_check.
    def visitRecrem_timing_check(self, ctx:VerilogParser.Recrem_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#skew_timing_check.
    def visitSkew_timing_check(self, ctx:VerilogParser.Skew_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timeskew_timing_check.
    def visitTimeskew_timing_check(self, ctx:VerilogParser.Timeskew_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#skew_timing_check_opt.
    def visitSkew_timing_check_opt(self, ctx:VerilogParser.Skew_timing_check_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_based_flag_opt.
    def visitEvent_based_flag_opt(self, ctx:VerilogParser.Event_based_flag_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#remain_active_flag_opt.
    def visitRemain_active_flag_opt(self, ctx:VerilogParser.Remain_active_flag_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#fullskew_timing_check.
    def visitFullskew_timing_check(self, ctx:VerilogParser.Fullskew_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#period_timing_check.
    def visitPeriod_timing_check(self, ctx:VerilogParser.Period_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#width_timing_check.
    def visitWidth_timing_check(self, ctx:VerilogParser.Width_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#threshold_opt.
    def visitThreshold_opt(self, ctx:VerilogParser.Threshold_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#nochange_timing_check.
    def visitNochange_timing_check(self, ctx:VerilogParser.Nochange_timing_checkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#checktime_condition.
    def visitChecktime_condition(self, ctx:VerilogParser.Checktime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#controlled_reference_event.
    def visitControlled_reference_event(self, ctx:VerilogParser.Controlled_reference_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#data_event.
    def visitData_event(self, ctx:VerilogParser.Data_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delayed_data.
    def visitDelayed_data(self, ctx:VerilogParser.Delayed_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delayed_reference.
    def visitDelayed_reference(self, ctx:VerilogParser.Delayed_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#end_edge_offset.
    def visitEnd_edge_offset(self, ctx:VerilogParser.End_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_based_flag.
    def visitEvent_based_flag(self, ctx:VerilogParser.Event_based_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#notifier.
    def visitNotifier(self, ctx:VerilogParser.NotifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#reference_event.
    def visitReference_event(self, ctx:VerilogParser.Reference_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#remain_active_flag.
    def visitRemain_active_flag(self, ctx:VerilogParser.Remain_active_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#stamptime_condition.
    def visitStamptime_condition(self, ctx:VerilogParser.Stamptime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#start_edge_offset.
    def visitStart_edge_offset(self, ctx:VerilogParser.Start_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#threshold.
    def visitThreshold(self, ctx:VerilogParser.ThresholdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timing_check_limit.
    def visitTiming_check_limit(self, ctx:VerilogParser.Timing_check_limitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timing_check_event.
    def visitTiming_check_event(self, ctx:VerilogParser.Timing_check_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#controlled_timing_check_event.
    def visitControlled_timing_check_event(self, ctx:VerilogParser.Controlled_timing_check_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timing_check_event_control.
    def visitTiming_check_event_control(self, ctx:VerilogParser.Timing_check_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_terminal_descriptor.
    def visitSpecify_terminal_descriptor(self, ctx:VerilogParser.Specify_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_control_specifier.
    def visitEdge_control_specifier(self, ctx:VerilogParser.Edge_control_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_descriptor.
    def visitEdge_descriptor(self, ctx:VerilogParser.Edge_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#timing_check_condition.
    def visitTiming_check_condition(self, ctx:VerilogParser.Timing_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#scalar_timing_check_condition.
    def visitScalar_timing_check_condition(self, ctx:VerilogParser.Scalar_timing_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#scalar_constant.
    def visitScalar_constant(self, ctx:VerilogParser.Scalar_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#concatenation.
    def visitConcatenation(self, ctx:VerilogParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_concatenation.
    def visitConstant_concatenation(self, ctx:VerilogParser.Constant_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_multiple_concatenation.
    def visitConstant_multiple_concatenation(self, ctx:VerilogParser.Constant_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_concatenation.
    def visitModule_path_concatenation(self, ctx:VerilogParser.Module_path_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_multiple_concatenation.
    def visitModule_path_multiple_concatenation(self, ctx:VerilogParser.Module_path_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx:VerilogParser.Multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_function_call.
    def visitConstant_function_call(self, ctx:VerilogParser.Constant_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_system_function_call.
    def visitConstant_system_function_call(self, ctx:VerilogParser.Constant_system_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_call.
    def visitFunction_call(self, ctx:VerilogParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_function_call.
    def visitSystem_function_call(self, ctx:VerilogParser.System_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#sys_func_call_port_list.
    def visitSys_func_call_port_list(self, ctx:VerilogParser.Sys_func_call_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#base_expression.
    def visitBase_expression(self, ctx:VerilogParser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_base_expression.
    def visitConstant_base_expression(self, ctx:VerilogParser.Constant_base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_expression.
    def visitConstant_expression(self, ctx:VerilogParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_mintypmax_expression.
    def visitConstant_mintypmax_expression(self, ctx:VerilogParser.Constant_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_range_expression.
    def visitConstant_range_expression(self, ctx:VerilogParser.Constant_range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dimension_constant_expression.
    def visitDimension_constant_expression(self, ctx:VerilogParser.Dimension_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#expression.
    def visitExpression(self, ctx:VerilogParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#lsb_constant_expression.
    def visitLsb_constant_expression(self, ctx:VerilogParser.Lsb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx:VerilogParser.Mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_expression.
    def visitModule_path_expression(self, ctx:VerilogParser.Module_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_mintypmax_expression.
    def visitModule_path_mintypmax_expression(self, ctx:VerilogParser.Module_path_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#msb_constant_expression.
    def visitMsb_constant_expression(self, ctx:VerilogParser.Msb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#range_expression.
    def visitRange_expression(self, ctx:VerilogParser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#width_constant_expression.
    def visitWidth_constant_expression(self, ctx:VerilogParser.Width_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_primary.
    def visitConstant_primary(self, ctx:VerilogParser.Constant_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_primary.
    def visitModule_path_primary(self, ctx:VerilogParser.Module_path_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#primary.
    def visitPrimary(self, ctx:VerilogParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#select_.
    def visitSelect_(self, ctx:VerilogParser.Select_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#bit_select.
    def visitBit_select(self, ctx:VerilogParser.Bit_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_lvalue.
    def visitNet_lvalue(self, ctx:VerilogParser.Net_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#const_select.
    def visitConst_select(self, ctx:VerilogParser.Const_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#const_bit_select.
    def visitConst_bit_select(self, ctx:VerilogParser.Const_bit_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_lvalue.
    def visitVariable_lvalue(self, ctx:VerilogParser.Variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#unary_operator.
    def visitUnary_operator(self, ctx:VerilogParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#unary_module_path_operator.
    def visitUnary_module_path_operator(self, ctx:VerilogParser.Unary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#number.
    def visitNumber(self, ctx:VerilogParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_number.
    def visitReal_number(self, ctx:VerilogParser.Real_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#decimal_number.
    def visitDecimal_number(self, ctx:VerilogParser.Decimal_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#binary_number.
    def visitBinary_number(self, ctx:VerilogParser.Binary_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#octal_number.
    def visitOctal_number(self, ctx:VerilogParser.Octal_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hex_number.
    def visitHex_number(self, ctx:VerilogParser.Hex_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#size.
    def visitSize(self, ctx:VerilogParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#fixed_point_number.
    def visitFixed_point_number(self, ctx:VerilogParser.Fixed_point_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#exponential_number.
    def visitExponential_number(self, ctx:VerilogParser.Exponential_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#unsigned_number.
    def visitUnsigned_number(self, ctx:VerilogParser.Unsigned_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#decimal_value.
    def visitDecimal_value(self, ctx:VerilogParser.Decimal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#binary_value.
    def visitBinary_value(self, ctx:VerilogParser.Binary_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#octal_value.
    def visitOctal_value(self, ctx:VerilogParser.Octal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hex_value.
    def visitHex_value(self, ctx:VerilogParser.Hex_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#decimal_base.
    def visitDecimal_base(self, ctx:VerilogParser.Decimal_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#binary_base.
    def visitBinary_base(self, ctx:VerilogParser.Binary_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#octal_base.
    def visitOctal_base(self, ctx:VerilogParser.Octal_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hex_base.
    def visitHex_base(self, ctx:VerilogParser.Hex_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#string_.
    def visitString_(self, ctx:VerilogParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attribute_instance.
    def visitAttribute_instance(self, ctx:VerilogParser.Attribute_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attr_spec.
    def visitAttr_spec(self, ctx:VerilogParser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attr_name.
    def visitAttr_name(self, ctx:VerilogParser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_identifier.
    def visitBlock_identifier(self, ctx:VerilogParser.Block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cell_identifier.
    def visitCell_identifier(self, ctx:VerilogParser.Cell_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_identifier.
    def visitConfig_identifier(self, ctx:VerilogParser.Config_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#escaped_identifier.
    def visitEscaped_identifier(self, ctx:VerilogParser.Escaped_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_identifier.
    def visitEvent_identifier(self, ctx:VerilogParser.Event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_identifier.
    def visitFunction_identifier(self, ctx:VerilogParser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx:VerilogParser.Gate_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx:VerilogParser.Generate_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_identifier.
    def visitGenvar_identifier(self, ctx:VerilogParser.Genvar_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:VerilogParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hier_ref.
    def visitHier_ref(self, ctx:VerilogParser.Hier_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#identifier.
    def visitIdentifier(self, ctx:VerilogParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_port_identifier.
    def visitInput_port_identifier(self, ctx:VerilogParser.Input_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#instance_identifier.
    def visitInstance_identifier(self, ctx:VerilogParser.Instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_identifier.
    def visitLibrary_identifier(self, ctx:VerilogParser.Library_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_identifier.
    def visitModule_identifier(self, ctx:VerilogParser.Module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx:VerilogParser.Module_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_identifier.
    def visitNet_identifier(self, ctx:VerilogParser.Net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_port_identifier.
    def visitOutput_port_identifier(self, ctx:VerilogParser.Output_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_identifier.
    def visitParameter_identifier(self, ctx:VerilogParser.Parameter_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_identifier.
    def visitPort_identifier(self, ctx:VerilogParser.Port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_identifier.
    def visitReal_identifier(self, ctx:VerilogParser.Real_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#simple_identifier.
    def visitSimple_identifier(self, ctx:VerilogParser.Simple_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_identifier.
    def visitSpecparam_identifier(self, ctx:VerilogParser.Specparam_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx:VerilogParser.System_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx:VerilogParser.System_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_identifier.
    def visitTask_identifier(self, ctx:VerilogParser.Task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#terminal_identifier.
    def visitTerminal_identifier(self, ctx:VerilogParser.Terminal_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#topmodule_identifier.
    def visitTopmodule_identifier(self, ctx:VerilogParser.Topmodule_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_identifier.
    def visitUdp_identifier(self, ctx:VerilogParser.Udp_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_instance_identifier.
    def visitUdp_instance_identifier(self, ctx:VerilogParser.Udp_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_identifier.
    def visitVariable_identifier(self, ctx:VerilogParser.Variable_identifierContext):
        return self.visitChildren(ctx)



del VerilogParser