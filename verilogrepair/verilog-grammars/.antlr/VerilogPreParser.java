// Generated from /home/yangnan/antlr4ds/verilog-grammars/VerilogPreParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VerilogPreParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ALWAYS=1, AND=2, ASSIGN=3, AUTOMATIC=4, BEGIN=5, BUF=6, BUFIFONE=7, BUFIFZERO=8, 
		CASE=9, CASEX=10, CASEZ=11, CELL=12, CMOS=13, CONFIG=14, DEASSIGN=15, 
		DEFAULT=16, DEFPARAM=17, DESIGN=18, DISABLE=19, DLFULLSKEW=20, DLHOLD=21, 
		DLNOCHANGE=22, DLPERIOD=23, DLRECOVERY=24, DLRECREM=25, DLREMOVAL=26, 
		DLSETUP=27, DLSETUPHOLD=28, DLSKEW=29, DLTIMESKEW=30, DLWIDTH=31, EDGE=32, 
		ELSE=33, END=34, ENDCASE=35, ENDCONFIG=36, ENDFUNCTION=37, ENDGENERATE=38, 
		ENDMODULE=39, ENDPRIMITIVE=40, ENDSPECIFY=41, ENDTABLE=42, ENDTASK=43, 
		EVENT=44, FOR=45, FORCE=46, FOREVER=47, FORK=48, FUNCTION=49, GENERATE=50, 
		GENVAR=51, HIGHZONE=52, HIGHZZERO=53, IF=54, IFNONE=55, INCLUDE=56, INITIAL=57, 
		INOUT=58, INPUT=59, INSTANCE=60, INTEGER=61, JOIN=62, LARGE=63, LIBLIST=64, 
		LIBRARY=65, LOCALPARAM=66, MACROMODULE=67, MEDIUM=68, MIINCDIR=69, MODULE=70, 
		NAND=71, NEGEDGE=72, NMOS=73, NOR=74, NOSHOWCANCELLED=75, NOT=76, NOTIFONE=77, 
		NOTIFZERO=78, OR=79, OUTPUT=80, PARAMETER=81, PATHPULSEDL=82, PMOS=83, 
		POSEDGE=84, PRIMITIVE=85, PULLDOWN=86, PULLONE=87, PULLUP=88, PULLZERO=89, 
		PULSESTYLE_ONDETECT=90, PULSESTYLE_ONEVENT=91, RCMOS=92, REAL=93, REALTIME=94, 
		REG=95, RELEASE=96, REPEAT=97, RNMOS=98, RPMOS=99, RTRAN=100, RTRANIFONE=101, 
		RTRANIFZERO=102, SCALARED=103, SHOWCANCELLED=104, SIGNED=105, SMALL=106, 
		SPECIFY=107, SPECPARAM=108, STRONGONE=109, STRONGZERO=110, SUPPLYONE=111, 
		SUPPLYZERO=112, TABLE=113, TASK=114, TIME=115, TRAN=116, TRANIFONE=117, 
		TRANIFZERO=118, TRI=119, TRIAND=120, TRIONE=121, TRIOR=122, TRIREG=123, 
		TRIZERO=124, USE=125, UWIRE=126, VECTORED=127, WAIT=128, WAND=129, WEAKONE=130, 
		WEAKZERO=131, WHILE=132, WIRE=133, WOR=134, XNOR=135, XOR=136, AM=137, 
		AMAM=138, AMAMAM=139, AS=140, ASAS=141, ASGT=142, AT=143, CA=144, CATI=145, 
		CL=146, CO=147, DL=148, DQ=149, DT=150, EM=151, EMEQ=152, EMEQEQ=153, 
		EQ=154, EQEQ=155, EQEQEQ=156, EQGT=157, GA=158, GT=159, GTEQ=160, GTGT=161, 
		GTGTGT=162, HA=163, LB=164, LC=165, LP=166, LT=167, LTEQ=168, LTLT=169, 
		LTLTLT=170, MI=171, MICL=172, MIGT=173, MO=174, PL=175, PLCL=176, QM=177, 
		RB=178, RC=179, RP=180, SC=181, SL=182, TI=183, TIAM=184, TICA=185, TIVL=186, 
		VL=187, VLVL=188, BINARY_BASE=189, BLOCK_COMMENT=190, DECIMAL_BASE=191, 
		ESCAPED_IDENTIFIER=192, EXPONENTIAL_NUMBER=193, FIXED_POINT_NUMBER=194, 
		HEX_BASE=195, LINE_COMMENT=196, OCTAL_BASE=197, SIMPLE_IDENTIFIER=198, 
		STRING=199, SYSTEM_TF_IDENTIFIER=200, UNSIGNED_NUMBER=201, WHITE_SPACE=202, 
		BINARY_VALUE=203, X_OR_Z_UNDERSCORE=204, EDGE_DESCRIPTOR=205, HEX_VALUE=206, 
		FILE_PATH_SPEC=207, OCTAL_VALUE=208, EDGE_SYMBOL=209, LEVEL_ONLY_SYMBOL=210, 
		OUTPUT_OR_LEVEL_SYMBOL=211, BEGIN_KEYWORDS_DIRECTIVE=212, CELLDEFINE_DIRECTIVE=213, 
		DEFAULT_NETTYPE_DIRECTIVE=214, DEFINE_DIRECTIVE=215, ELSE_DIRECTIVE=216, 
		ELSIF_DIRECTIVE=217, END_KEYWORDS_DIRECTIVE=218, ENDCELLDEFINE_DIRECTIVE=219, 
		ENDIF_DIRECTIVE=220, IFDEF_DIRECTIVE=221, IFNDEF_DIRECTIVE=222, INCLUDE_DIRECTIVE=223, 
		LINE_DIRECTIVE=224, NOUNCONNECTED_DRIVE_DIRECTIVE=225, PRAGMA_DIRECTIVE=226, 
		RESETALL_DIRECTIVE=227, TIMESCALE_DIRECTIVE=228, UNCONNECTED_DRIVE_DIRECTIVE=229, 
		UNDEF_DIRECTIVE=230, MACRO_USAGE=231, VERSION_SPECIFIER=232, DEFAULT_NETTYPE_VALUE=233, 
		MACRO_NAME=234, FILENAME=235, MACRO_DELIMITER=236, MACRO_ESC_NEWLINE=237, 
		MACRO_ESC_QUOTE=238, MACRO_QUOTE=239, MACRO_TEXT=240, SOURCE_TEXT=241, 
		TIME_UNIT=242, TIME_VALUE=243, UNCONNECTED_DRIVE_VALUE=244, MACRO_IDENTIFIER=245;
	public static final int
		RULE_source_text = 0, RULE_compiler_directive = 1, RULE_begin_keywords_directive = 2, 
		RULE_celldefine_directive = 3, RULE_default_nettype_directive = 4, RULE_default_nettype_value = 5, 
		RULE_else_directive = 6, RULE_elsif_directive = 7, RULE_end_keywords_directive = 8, 
		RULE_endcelldefine_directive = 9, RULE_endif_directive = 10, RULE_filename = 11, 
		RULE_group_of_lines = 12, RULE_identifier = 13, RULE_ifdef_directive = 14, 
		RULE_ifndef_directive = 15, RULE_include_directive = 16, RULE_level = 17, 
		RULE_line_directive = 18, RULE_macro_delimiter = 19, RULE_macro_esc_newline = 20, 
		RULE_macro_esc_quote = 21, RULE_macro_identifier = 22, RULE_macro_name = 23, 
		RULE_macro_quote = 24, RULE_macro_text = 25, RULE_macro_text_ = 26, RULE_macro_usage = 27, 
		RULE_nounconnected_drive_directive = 28, RULE_number = 29, RULE_pragma_directive = 30, 
		RULE_pragma_expression = 31, RULE_pragma_keyword = 32, RULE_pragma_name = 33, 
		RULE_pragma_value = 34, RULE_resetall_directive = 35, RULE_source_text_ = 36, 
		RULE_string_ = 37, RULE_text_macro_definition = 38, RULE_text_macro_usage = 39, 
		RULE_time_precision = 40, RULE_time_unit = 41, RULE_timescale_directive = 42, 
		RULE_unconnected_drive_directive = 43, RULE_unconnected_drive_value = 44, 
		RULE_undef_directive = 45, RULE_version_specifier = 46;
	private static String[] makeRuleNames() {
		return new String[] {
			"source_text", "compiler_directive", "begin_keywords_directive", "celldefine_directive", 
			"default_nettype_directive", "default_nettype_value", "else_directive", 
			"elsif_directive", "end_keywords_directive", "endcelldefine_directive", 
			"endif_directive", "filename", "group_of_lines", "identifier", "ifdef_directive", 
			"ifndef_directive", "include_directive", "level", "line_directive", "macro_delimiter", 
			"macro_esc_newline", "macro_esc_quote", "macro_identifier", "macro_name", 
			"macro_quote", "macro_text", "macro_text_", "macro_usage", "nounconnected_drive_directive", 
			"number", "pragma_directive", "pragma_expression", "pragma_keyword", 
			"pragma_name", "pragma_value", "resetall_directive", "source_text_", 
			"string_", "text_macro_definition", "text_macro_usage", "time_precision", 
			"time_unit", "timescale_directive", "unconnected_drive_directive", "unconnected_drive_value", 
			"undef_directive", "version_specifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'always'", "'and'", "'assign'", "'automatic'", "'begin'", "'buf'", 
			"'bufif1'", "'bufif0'", "'case'", "'casex'", "'casez'", "'cell'", "'cmos'", 
			"'config'", "'deassign'", "'default'", "'defparam'", "'design'", "'disable'", 
			"'$fullskew'", "'$hold'", "'$nochange'", "'$period'", "'$recovery'", 
			"'$recrem'", "'$removal'", "'$setup'", "'$setuphold'", "'$skew'", "'$timeskew'", 
			"'$width'", "'edge'", "'else'", "'end'", "'endcase'", "'endconfig'", 
			"'endfunction'", "'endgenerate'", "'endmodule'", "'endprimitive'", "'endspecify'", 
			"'endtable'", "'endtask'", "'event'", "'for'", "'force'", "'forever'", 
			"'fork'", "'function'", "'generate'", "'genvar'", "'highz1'", "'highz0'", 
			"'if'", "'ifnone'", "'include'", "'initial'", "'inout'", "'input'", "'instance'", 
			"'integer'", "'join'", "'large'", "'liblist'", "'library'", "'localparam'", 
			"'macromodule'", "'medium'", "'-incdir'", "'module'", "'nand'", "'negedge'", 
			"'nmos'", "'nor'", "'noshowcancelled'", "'not'", "'notif1'", "'notif0'", 
			"'or'", "'output'", "'parameter'", "'PATHPULSE$'", "'pmos'", "'posedge'", 
			"'primitive'", "'pulldown'", "'pull1'", "'pullup'", "'pull0'", "'pulsestyle_ondetect'", 
			"'pulsestyle_onevent'", "'rcmos'", "'real'", "'realtime'", "'reg'", "'release'", 
			"'repeat'", "'rnmos'", "'rpmos'", "'rtran'", "'rtranif1'", "'rtranif0'", 
			"'scalared'", "'showcancelled'", "'signed'", "'small'", "'specify'", 
			"'specparam'", "'strong1'", "'strong0'", "'supply1'", "'supply0'", "'table'", 
			"'task'", "'time'", "'tran'", "'tranif1'", "'tranif0'", "'tri'", "'triand'", 
			"'tri1'", "'trior'", "'trireg'", "'tri0'", "'use'", "'uwire'", "'vectored'", 
			"'wait'", "'wand'", "'weak1'", "'weak0'", "'while'", "'wire'", "'wor'", 
			"'xnor'", "'xor'", "'&'", "'&&'", "'&&&'", "'*'", "'**'", "'*>'", "'@'", 
			"'^'", "'^~'", "':'", "','", "'$'", "'\"'", "'.'", "'!'", "'!='", "'!=='", 
			"'='", "'=='", "'==='", "'=>'", null, "'>'", "'>='", "'>>'", "'>>>'", 
			"'#'", "'['", "'{'", "'('", "'<'", "'<='", "'<<'", "'<<<'", "'-'", "'-:'", 
			"'->'", "'%'", "'+'", "'+:'", "'?'", "']'", "'}'", "')'", "';'", "'/'", 
			"'~'", "'~&'", "'~^'", "'~|'", "'|'", "'||'", null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "'celldefine'", null, 
			null, null, null, "'end_keywords'", "'endcelldefine'", null, null, null, 
			null, null, "'nounconnected_drive'", null, "'resetall'", null, null, 
			null, null, null, null, null, null, "'``'", null, "'`\\`\"'", "'`\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ALWAYS", "AND", "ASSIGN", "AUTOMATIC", "BEGIN", "BUF", "BUFIFONE", 
			"BUFIFZERO", "CASE", "CASEX", "CASEZ", "CELL", "CMOS", "CONFIG", "DEASSIGN", 
			"DEFAULT", "DEFPARAM", "DESIGN", "DISABLE", "DLFULLSKEW", "DLHOLD", "DLNOCHANGE", 
			"DLPERIOD", "DLRECOVERY", "DLRECREM", "DLREMOVAL", "DLSETUP", "DLSETUPHOLD", 
			"DLSKEW", "DLTIMESKEW", "DLWIDTH", "EDGE", "ELSE", "END", "ENDCASE", 
			"ENDCONFIG", "ENDFUNCTION", "ENDGENERATE", "ENDMODULE", "ENDPRIMITIVE", 
			"ENDSPECIFY", "ENDTABLE", "ENDTASK", "EVENT", "FOR", "FORCE", "FOREVER", 
			"FORK", "FUNCTION", "GENERATE", "GENVAR", "HIGHZONE", "HIGHZZERO", "IF", 
			"IFNONE", "INCLUDE", "INITIAL", "INOUT", "INPUT", "INSTANCE", "INTEGER", 
			"JOIN", "LARGE", "LIBLIST", "LIBRARY", "LOCALPARAM", "MACROMODULE", "MEDIUM", 
			"MIINCDIR", "MODULE", "NAND", "NEGEDGE", "NMOS", "NOR", "NOSHOWCANCELLED", 
			"NOT", "NOTIFONE", "NOTIFZERO", "OR", "OUTPUT", "PARAMETER", "PATHPULSEDL", 
			"PMOS", "POSEDGE", "PRIMITIVE", "PULLDOWN", "PULLONE", "PULLUP", "PULLZERO", 
			"PULSESTYLE_ONDETECT", "PULSESTYLE_ONEVENT", "RCMOS", "REAL", "REALTIME", 
			"REG", "RELEASE", "REPEAT", "RNMOS", "RPMOS", "RTRAN", "RTRANIFONE", 
			"RTRANIFZERO", "SCALARED", "SHOWCANCELLED", "SIGNED", "SMALL", "SPECIFY", 
			"SPECPARAM", "STRONGONE", "STRONGZERO", "SUPPLYONE", "SUPPLYZERO", "TABLE", 
			"TASK", "TIME", "TRAN", "TRANIFONE", "TRANIFZERO", "TRI", "TRIAND", "TRIONE", 
			"TRIOR", "TRIREG", "TRIZERO", "USE", "UWIRE", "VECTORED", "WAIT", "WAND", 
			"WEAKONE", "WEAKZERO", "WHILE", "WIRE", "WOR", "XNOR", "XOR", "AM", "AMAM", 
			"AMAMAM", "AS", "ASAS", "ASGT", "AT", "CA", "CATI", "CL", "CO", "DL", 
			"DQ", "DT", "EM", "EMEQ", "EMEQEQ", "EQ", "EQEQ", "EQEQEQ", "EQGT", "GA", 
			"GT", "GTEQ", "GTGT", "GTGTGT", "HA", "LB", "LC", "LP", "LT", "LTEQ", 
			"LTLT", "LTLTLT", "MI", "MICL", "MIGT", "MO", "PL", "PLCL", "QM", "RB", 
			"RC", "RP", "SC", "SL", "TI", "TIAM", "TICA", "TIVL", "VL", "VLVL", "BINARY_BASE", 
			"BLOCK_COMMENT", "DECIMAL_BASE", "ESCAPED_IDENTIFIER", "EXPONENTIAL_NUMBER", 
			"FIXED_POINT_NUMBER", "HEX_BASE", "LINE_COMMENT", "OCTAL_BASE", "SIMPLE_IDENTIFIER", 
			"STRING", "SYSTEM_TF_IDENTIFIER", "UNSIGNED_NUMBER", "WHITE_SPACE", "BINARY_VALUE", 
			"X_OR_Z_UNDERSCORE", "EDGE_DESCRIPTOR", "HEX_VALUE", "FILE_PATH_SPEC", 
			"OCTAL_VALUE", "EDGE_SYMBOL", "LEVEL_ONLY_SYMBOL", "OUTPUT_OR_LEVEL_SYMBOL", 
			"BEGIN_KEYWORDS_DIRECTIVE", "CELLDEFINE_DIRECTIVE", "DEFAULT_NETTYPE_DIRECTIVE", 
			"DEFINE_DIRECTIVE", "ELSE_DIRECTIVE", "ELSIF_DIRECTIVE", "END_KEYWORDS_DIRECTIVE", 
			"ENDCELLDEFINE_DIRECTIVE", "ENDIF_DIRECTIVE", "IFDEF_DIRECTIVE", "IFNDEF_DIRECTIVE", 
			"INCLUDE_DIRECTIVE", "LINE_DIRECTIVE", "NOUNCONNECTED_DRIVE_DIRECTIVE", 
			"PRAGMA_DIRECTIVE", "RESETALL_DIRECTIVE", "TIMESCALE_DIRECTIVE", "UNCONNECTED_DRIVE_DIRECTIVE", 
			"UNDEF_DIRECTIVE", "MACRO_USAGE", "VERSION_SPECIFIER", "DEFAULT_NETTYPE_VALUE", 
			"MACRO_NAME", "FILENAME", "MACRO_DELIMITER", "MACRO_ESC_NEWLINE", "MACRO_ESC_QUOTE", 
			"MACRO_QUOTE", "MACRO_TEXT", "SOURCE_TEXT", "TIME_UNIT", "TIME_VALUE", 
			"UNCONNECTED_DRIVE_VALUE", "MACRO_IDENTIFIER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "VerilogPreParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VerilogPreParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Source_textContext extends ParserRuleContext {
		public List<Compiler_directiveContext> compiler_directive() {
			return getRuleContexts(Compiler_directiveContext.class);
		}
		public Compiler_directiveContext compiler_directive(int i) {
			return getRuleContext(Compiler_directiveContext.class,i);
		}
		public Source_textContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_source_text; }
	}

	public final Source_textContext source_text() throws RecognitionException {
		Source_textContext _localctx = new Source_textContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_source_text);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==GA) {
				{
				{
				setState(94);
				compiler_directive();
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Compiler_directiveContext extends ParserRuleContext {
		public Begin_keywords_directiveContext begin_keywords_directive() {
			return getRuleContext(Begin_keywords_directiveContext.class,0);
		}
		public Celldefine_directiveContext celldefine_directive() {
			return getRuleContext(Celldefine_directiveContext.class,0);
		}
		public Default_nettype_directiveContext default_nettype_directive() {
			return getRuleContext(Default_nettype_directiveContext.class,0);
		}
		public End_keywords_directiveContext end_keywords_directive() {
			return getRuleContext(End_keywords_directiveContext.class,0);
		}
		public Endcelldefine_directiveContext endcelldefine_directive() {
			return getRuleContext(Endcelldefine_directiveContext.class,0);
		}
		public Ifdef_directiveContext ifdef_directive() {
			return getRuleContext(Ifdef_directiveContext.class,0);
		}
		public Ifndef_directiveContext ifndef_directive() {
			return getRuleContext(Ifndef_directiveContext.class,0);
		}
		public Include_directiveContext include_directive() {
			return getRuleContext(Include_directiveContext.class,0);
		}
		public Line_directiveContext line_directive() {
			return getRuleContext(Line_directiveContext.class,0);
		}
		public Nounconnected_drive_directiveContext nounconnected_drive_directive() {
			return getRuleContext(Nounconnected_drive_directiveContext.class,0);
		}
		public Pragma_directiveContext pragma_directive() {
			return getRuleContext(Pragma_directiveContext.class,0);
		}
		public Resetall_directiveContext resetall_directive() {
			return getRuleContext(Resetall_directiveContext.class,0);
		}
		public Text_macro_definitionContext text_macro_definition() {
			return getRuleContext(Text_macro_definitionContext.class,0);
		}
		public Text_macro_usageContext text_macro_usage() {
			return getRuleContext(Text_macro_usageContext.class,0);
		}
		public Timescale_directiveContext timescale_directive() {
			return getRuleContext(Timescale_directiveContext.class,0);
		}
		public Unconnected_drive_directiveContext unconnected_drive_directive() {
			return getRuleContext(Unconnected_drive_directiveContext.class,0);
		}
		public Undef_directiveContext undef_directive() {
			return getRuleContext(Undef_directiveContext.class,0);
		}
		public Compiler_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compiler_directive; }
	}

	public final Compiler_directiveContext compiler_directive() throws RecognitionException {
		Compiler_directiveContext _localctx = new Compiler_directiveContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_compiler_directive);
		try {
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				begin_keywords_directive();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				celldefine_directive();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(102);
				default_nettype_directive();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(103);
				end_keywords_directive();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(104);
				endcelldefine_directive();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(105);
				ifdef_directive();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(106);
				ifndef_directive();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(107);
				include_directive();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(108);
				line_directive();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(109);
				nounconnected_drive_directive();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(110);
				pragma_directive();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(111);
				resetall_directive();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(112);
				text_macro_definition();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(113);
				text_macro_usage();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(114);
				timescale_directive();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(115);
				unconnected_drive_directive();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(116);
				undef_directive();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Begin_keywords_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode BEGIN_KEYWORDS_DIRECTIVE() { return getToken(VerilogPreParser.BEGIN_KEYWORDS_DIRECTIVE, 0); }
		public List<TerminalNode> DQ() { return getTokens(VerilogPreParser.DQ); }
		public TerminalNode DQ(int i) {
			return getToken(VerilogPreParser.DQ, i);
		}
		public Version_specifierContext version_specifier() {
			return getRuleContext(Version_specifierContext.class,0);
		}
		public Begin_keywords_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_begin_keywords_directive; }
	}

	public final Begin_keywords_directiveContext begin_keywords_directive() throws RecognitionException {
		Begin_keywords_directiveContext _localctx = new Begin_keywords_directiveContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_begin_keywords_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(GA);
			setState(120);
			match(BEGIN_KEYWORDS_DIRECTIVE);
			setState(121);
			match(DQ);
			setState(122);
			version_specifier();
			setState(123);
			match(DQ);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Celldefine_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode CELLDEFINE_DIRECTIVE() { return getToken(VerilogPreParser.CELLDEFINE_DIRECTIVE, 0); }
		public Celldefine_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_celldefine_directive; }
	}

	public final Celldefine_directiveContext celldefine_directive() throws RecognitionException {
		Celldefine_directiveContext _localctx = new Celldefine_directiveContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_celldefine_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(GA);
			setState(126);
			match(CELLDEFINE_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Default_nettype_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode DEFAULT_NETTYPE_DIRECTIVE() { return getToken(VerilogPreParser.DEFAULT_NETTYPE_DIRECTIVE, 0); }
		public Default_nettype_valueContext default_nettype_value() {
			return getRuleContext(Default_nettype_valueContext.class,0);
		}
		public Default_nettype_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default_nettype_directive; }
	}

	public final Default_nettype_directiveContext default_nettype_directive() throws RecognitionException {
		Default_nettype_directiveContext _localctx = new Default_nettype_directiveContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_default_nettype_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(GA);
			setState(129);
			match(DEFAULT_NETTYPE_DIRECTIVE);
			setState(130);
			default_nettype_value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Default_nettype_valueContext extends ParserRuleContext {
		public TerminalNode DEFAULT_NETTYPE_VALUE() { return getToken(VerilogPreParser.DEFAULT_NETTYPE_VALUE, 0); }
		public Default_nettype_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default_nettype_value; }
	}

	public final Default_nettype_valueContext default_nettype_value() throws RecognitionException {
		Default_nettype_valueContext _localctx = new Default_nettype_valueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_default_nettype_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(DEFAULT_NETTYPE_VALUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode ELSE_DIRECTIVE() { return getToken(VerilogPreParser.ELSE_DIRECTIVE, 0); }
		public Group_of_linesContext group_of_lines() {
			return getRuleContext(Group_of_linesContext.class,0);
		}
		public Else_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_directive; }
	}

	public final Else_directiveContext else_directive() throws RecognitionException {
		Else_directiveContext _localctx = new Else_directiveContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_else_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(GA);
			setState(135);
			match(ELSE_DIRECTIVE);
			setState(136);
			group_of_lines();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Elsif_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode ELSIF_DIRECTIVE() { return getToken(VerilogPreParser.ELSIF_DIRECTIVE, 0); }
		public Macro_identifierContext macro_identifier() {
			return getRuleContext(Macro_identifierContext.class,0);
		}
		public Group_of_linesContext group_of_lines() {
			return getRuleContext(Group_of_linesContext.class,0);
		}
		public Elsif_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elsif_directive; }
	}

	public final Elsif_directiveContext elsif_directive() throws RecognitionException {
		Elsif_directiveContext _localctx = new Elsif_directiveContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_elsif_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(GA);
			setState(139);
			match(ELSIF_DIRECTIVE);
			setState(140);
			macro_identifier();
			setState(141);
			group_of_lines();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class End_keywords_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode END_KEYWORDS_DIRECTIVE() { return getToken(VerilogPreParser.END_KEYWORDS_DIRECTIVE, 0); }
		public End_keywords_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_keywords_directive; }
	}

	public final End_keywords_directiveContext end_keywords_directive() throws RecognitionException {
		End_keywords_directiveContext _localctx = new End_keywords_directiveContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_end_keywords_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(GA);
			setState(144);
			match(END_KEYWORDS_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Endcelldefine_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode ENDCELLDEFINE_DIRECTIVE() { return getToken(VerilogPreParser.ENDCELLDEFINE_DIRECTIVE, 0); }
		public Endcelldefine_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endcelldefine_directive; }
	}

	public final Endcelldefine_directiveContext endcelldefine_directive() throws RecognitionException {
		Endcelldefine_directiveContext _localctx = new Endcelldefine_directiveContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_endcelldefine_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(GA);
			setState(147);
			match(ENDCELLDEFINE_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Endif_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode ENDIF_DIRECTIVE() { return getToken(VerilogPreParser.ENDIF_DIRECTIVE, 0); }
		public Endif_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endif_directive; }
	}

	public final Endif_directiveContext endif_directive() throws RecognitionException {
		Endif_directiveContext _localctx = new Endif_directiveContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_endif_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(GA);
			setState(150);
			match(ENDIF_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilenameContext extends ParserRuleContext {
		public TerminalNode FILENAME() { return getToken(VerilogPreParser.FILENAME, 0); }
		public FilenameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filename; }
	}

	public final FilenameContext filename() throws RecognitionException {
		FilenameContext _localctx = new FilenameContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_filename);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(FILENAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group_of_linesContext extends ParserRuleContext {
		public List<Source_text_Context> source_text_() {
			return getRuleContexts(Source_text_Context.class);
		}
		public Source_text_Context source_text_(int i) {
			return getRuleContext(Source_text_Context.class,i);
		}
		public List<Compiler_directiveContext> compiler_directive() {
			return getRuleContexts(Compiler_directiveContext.class);
		}
		public Compiler_directiveContext compiler_directive(int i) {
			return getRuleContext(Compiler_directiveContext.class,i);
		}
		public Group_of_linesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_of_lines; }
	}

	public final Group_of_linesContext group_of_lines() throws RecognitionException {
		Group_of_linesContext _localctx = new Group_of_linesContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_group_of_lines);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(156);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SOURCE_TEXT:
						{
						setState(154);
						source_text_();
						}
						break;
					case GA:
						{
						setState(155);
						compiler_directive();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(160);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode SIMPLE_IDENTIFIER() { return getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(SIMPLE_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ifdef_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode IFDEF_DIRECTIVE() { return getToken(VerilogPreParser.IFDEF_DIRECTIVE, 0); }
		public Macro_identifierContext macro_identifier() {
			return getRuleContext(Macro_identifierContext.class,0);
		}
		public Group_of_linesContext group_of_lines() {
			return getRuleContext(Group_of_linesContext.class,0);
		}
		public Endif_directiveContext endif_directive() {
			return getRuleContext(Endif_directiveContext.class,0);
		}
		public List<Elsif_directiveContext> elsif_directive() {
			return getRuleContexts(Elsif_directiveContext.class);
		}
		public Elsif_directiveContext elsif_directive(int i) {
			return getRuleContext(Elsif_directiveContext.class,i);
		}
		public Else_directiveContext else_directive() {
			return getRuleContext(Else_directiveContext.class,0);
		}
		public Ifdef_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifdef_directive; }
	}

	public final Ifdef_directiveContext ifdef_directive() throws RecognitionException {
		Ifdef_directiveContext _localctx = new Ifdef_directiveContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_ifdef_directive);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(GA);
			setState(164);
			match(IFDEF_DIRECTIVE);
			setState(165);
			macro_identifier();
			setState(166);
			group_of_lines();
			setState(170);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(167);
					elsif_directive();
					}
					} 
				}
				setState(172);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(173);
				else_directive();
				}
				break;
			}
			setState(176);
			endif_directive();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ifndef_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode IFNDEF_DIRECTIVE() { return getToken(VerilogPreParser.IFNDEF_DIRECTIVE, 0); }
		public Macro_identifierContext macro_identifier() {
			return getRuleContext(Macro_identifierContext.class,0);
		}
		public Group_of_linesContext group_of_lines() {
			return getRuleContext(Group_of_linesContext.class,0);
		}
		public Endif_directiveContext endif_directive() {
			return getRuleContext(Endif_directiveContext.class,0);
		}
		public List<Elsif_directiveContext> elsif_directive() {
			return getRuleContexts(Elsif_directiveContext.class);
		}
		public Elsif_directiveContext elsif_directive(int i) {
			return getRuleContext(Elsif_directiveContext.class,i);
		}
		public Else_directiveContext else_directive() {
			return getRuleContext(Else_directiveContext.class,0);
		}
		public Ifndef_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifndef_directive; }
	}

	public final Ifndef_directiveContext ifndef_directive() throws RecognitionException {
		Ifndef_directiveContext _localctx = new Ifndef_directiveContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ifndef_directive);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(GA);
			setState(179);
			match(IFNDEF_DIRECTIVE);
			setState(180);
			macro_identifier();
			setState(181);
			group_of_lines();
			setState(185);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(182);
					elsif_directive();
					}
					} 
				}
				setState(187);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(188);
				else_directive();
				}
				break;
			}
			setState(191);
			endif_directive();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode INCLUDE_DIRECTIVE() { return getToken(VerilogPreParser.INCLUDE_DIRECTIVE, 0); }
		public List<TerminalNode> DQ() { return getTokens(VerilogPreParser.DQ); }
		public TerminalNode DQ(int i) {
			return getToken(VerilogPreParser.DQ, i);
		}
		public FilenameContext filename() {
			return getRuleContext(FilenameContext.class,0);
		}
		public Include_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_directive; }
	}

	public final Include_directiveContext include_directive() throws RecognitionException {
		Include_directiveContext _localctx = new Include_directiveContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_include_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(GA);
			setState(194);
			match(INCLUDE_DIRECTIVE);
			setState(195);
			match(DQ);
			setState(196);
			filename();
			setState(197);
			match(DQ);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LevelContext extends ParserRuleContext {
		public TerminalNode UNSIGNED_NUMBER() { return getToken(VerilogPreParser.UNSIGNED_NUMBER, 0); }
		public LevelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_level; }
	}

	public final LevelContext level() throws RecognitionException {
		LevelContext _localctx = new LevelContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_level);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(UNSIGNED_NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Line_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode LINE_DIRECTIVE() { return getToken(VerilogPreParser.LINE_DIRECTIVE, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public List<TerminalNode> DQ() { return getTokens(VerilogPreParser.DQ); }
		public TerminalNode DQ(int i) {
			return getToken(VerilogPreParser.DQ, i);
		}
		public FilenameContext filename() {
			return getRuleContext(FilenameContext.class,0);
		}
		public LevelContext level() {
			return getRuleContext(LevelContext.class,0);
		}
		public Line_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line_directive; }
	}

	public final Line_directiveContext line_directive() throws RecognitionException {
		Line_directiveContext _localctx = new Line_directiveContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_line_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(GA);
			setState(202);
			match(LINE_DIRECTIVE);
			setState(203);
			number();
			setState(204);
			match(DQ);
			setState(205);
			filename();
			setState(206);
			match(DQ);
			setState(207);
			level();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_delimiterContext extends ParserRuleContext {
		public TerminalNode MACRO_DELIMITER() { return getToken(VerilogPreParser.MACRO_DELIMITER, 0); }
		public Macro_delimiterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_delimiter; }
	}

	public final Macro_delimiterContext macro_delimiter() throws RecognitionException {
		Macro_delimiterContext _localctx = new Macro_delimiterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_macro_delimiter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(MACRO_DELIMITER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_esc_newlineContext extends ParserRuleContext {
		public TerminalNode MACRO_ESC_NEWLINE() { return getToken(VerilogPreParser.MACRO_ESC_NEWLINE, 0); }
		public Macro_esc_newlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_esc_newline; }
	}

	public final Macro_esc_newlineContext macro_esc_newline() throws RecognitionException {
		Macro_esc_newlineContext _localctx = new Macro_esc_newlineContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_macro_esc_newline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(MACRO_ESC_NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_esc_quoteContext extends ParserRuleContext {
		public TerminalNode MACRO_ESC_QUOTE() { return getToken(VerilogPreParser.MACRO_ESC_QUOTE, 0); }
		public Macro_esc_quoteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_esc_quote; }
	}

	public final Macro_esc_quoteContext macro_esc_quote() throws RecognitionException {
		Macro_esc_quoteContext _localctx = new Macro_esc_quoteContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_macro_esc_quote);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(MACRO_ESC_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_identifierContext extends ParserRuleContext {
		public TerminalNode MACRO_IDENTIFIER() { return getToken(VerilogPreParser.MACRO_IDENTIFIER, 0); }
		public Macro_identifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_identifier; }
	}

	public final Macro_identifierContext macro_identifier() throws RecognitionException {
		Macro_identifierContext _localctx = new Macro_identifierContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_macro_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(MACRO_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_nameContext extends ParserRuleContext {
		public TerminalNode MACRO_NAME() { return getToken(VerilogPreParser.MACRO_NAME, 0); }
		public Macro_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_name; }
	}

	public final Macro_nameContext macro_name() throws RecognitionException {
		Macro_nameContext _localctx = new Macro_nameContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_macro_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(MACRO_NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_quoteContext extends ParserRuleContext {
		public TerminalNode MACRO_QUOTE() { return getToken(VerilogPreParser.MACRO_QUOTE, 0); }
		public Macro_quoteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_quote; }
	}

	public final Macro_quoteContext macro_quote() throws RecognitionException {
		Macro_quoteContext _localctx = new Macro_quoteContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_macro_quote);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(MACRO_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_textContext extends ParserRuleContext {
		public List<Macro_text_Context> macro_text_() {
			return getRuleContexts(Macro_text_Context.class);
		}
		public Macro_text_Context macro_text_(int i) {
			return getRuleContext(Macro_text_Context.class,i);
		}
		public List<Macro_delimiterContext> macro_delimiter() {
			return getRuleContexts(Macro_delimiterContext.class);
		}
		public Macro_delimiterContext macro_delimiter(int i) {
			return getRuleContext(Macro_delimiterContext.class,i);
		}
		public List<Macro_esc_newlineContext> macro_esc_newline() {
			return getRuleContexts(Macro_esc_newlineContext.class);
		}
		public Macro_esc_newlineContext macro_esc_newline(int i) {
			return getRuleContext(Macro_esc_newlineContext.class,i);
		}
		public List<Macro_esc_quoteContext> macro_esc_quote() {
			return getRuleContexts(Macro_esc_quoteContext.class);
		}
		public Macro_esc_quoteContext macro_esc_quote(int i) {
			return getRuleContext(Macro_esc_quoteContext.class,i);
		}
		public List<Macro_quoteContext> macro_quote() {
			return getRuleContexts(Macro_quoteContext.class);
		}
		public Macro_quoteContext macro_quote(int i) {
			return getRuleContext(Macro_quoteContext.class,i);
		}
		public List<String_Context> string_() {
			return getRuleContexts(String_Context.class);
		}
		public String_Context string_(int i) {
			return getRuleContext(String_Context.class,i);
		}
		public Macro_textContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_text; }
	}

	public final Macro_textContext macro_text() throws RecognitionException {
		Macro_textContext _localctx = new Macro_textContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_macro_text);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 199)) & ~0x3f) == 0 && ((1L << (_la - 199)) & ((1L << (STRING - 199)) | (1L << (MACRO_DELIMITER - 199)) | (1L << (MACRO_ESC_NEWLINE - 199)) | (1L << (MACRO_ESC_QUOTE - 199)) | (1L << (MACRO_QUOTE - 199)) | (1L << (MACRO_TEXT - 199)))) != 0)) {
				{
				setState(227);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MACRO_TEXT:
					{
					setState(221);
					macro_text_();
					}
					break;
				case MACRO_DELIMITER:
					{
					setState(222);
					macro_delimiter();
					}
					break;
				case MACRO_ESC_NEWLINE:
					{
					setState(223);
					macro_esc_newline();
					}
					break;
				case MACRO_ESC_QUOTE:
					{
					setState(224);
					macro_esc_quote();
					}
					break;
				case MACRO_QUOTE:
					{
					setState(225);
					macro_quote();
					}
					break;
				case STRING:
					{
					setState(226);
					string_();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_text_Context extends ParserRuleContext {
		public TerminalNode MACRO_TEXT() { return getToken(VerilogPreParser.MACRO_TEXT, 0); }
		public Macro_text_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_text_; }
	}

	public final Macro_text_Context macro_text_() throws RecognitionException {
		Macro_text_Context _localctx = new Macro_text_Context(_ctx, getState());
		enterRule(_localctx, 52, RULE_macro_text_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(MACRO_TEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Macro_usageContext extends ParserRuleContext {
		public TerminalNode MACRO_USAGE() { return getToken(VerilogPreParser.MACRO_USAGE, 0); }
		public Macro_usageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_usage; }
	}

	public final Macro_usageContext macro_usage() throws RecognitionException {
		Macro_usageContext _localctx = new Macro_usageContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_macro_usage);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(MACRO_USAGE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Nounconnected_drive_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode NOUNCONNECTED_DRIVE_DIRECTIVE() { return getToken(VerilogPreParser.NOUNCONNECTED_DRIVE_DIRECTIVE, 0); }
		public Nounconnected_drive_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nounconnected_drive_directive; }
	}

	public final Nounconnected_drive_directiveContext nounconnected_drive_directive() throws RecognitionException {
		Nounconnected_drive_directiveContext _localctx = new Nounconnected_drive_directiveContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_nounconnected_drive_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			match(GA);
			setState(237);
			match(NOUNCONNECTED_DRIVE_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode UNSIGNED_NUMBER() { return getToken(VerilogPreParser.UNSIGNED_NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(UNSIGNED_NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pragma_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode PRAGMA_DIRECTIVE() { return getToken(VerilogPreParser.PRAGMA_DIRECTIVE, 0); }
		public Pragma_nameContext pragma_name() {
			return getRuleContext(Pragma_nameContext.class,0);
		}
		public List<Pragma_expressionContext> pragma_expression() {
			return getRuleContexts(Pragma_expressionContext.class);
		}
		public Pragma_expressionContext pragma_expression(int i) {
			return getRuleContext(Pragma_expressionContext.class,i);
		}
		public List<TerminalNode> CO() { return getTokens(VerilogPreParser.CO); }
		public TerminalNode CO(int i) {
			return getToken(VerilogPreParser.CO, i);
		}
		public Pragma_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pragma_directive; }
	}

	public final Pragma_directiveContext pragma_directive() throws RecognitionException {
		Pragma_directiveContext _localctx = new Pragma_directiveContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_pragma_directive);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(GA);
			setState(242);
			match(PRAGMA_DIRECTIVE);
			setState(243);
			pragma_name();
			setState(252);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 166)) & ~0x3f) == 0 && ((1L << (_la - 166)) & ((1L << (LP - 166)) | (1L << (SIMPLE_IDENTIFIER - 166)) | (1L << (STRING - 166)) | (1L << (UNSIGNED_NUMBER - 166)))) != 0)) {
				{
				setState(244);
				pragma_expression();
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CO) {
					{
					{
					setState(245);
					match(CO);
					setState(246);
					pragma_expression();
					}
					}
					setState(251);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pragma_expressionContext extends ParserRuleContext {
		public Pragma_valueContext pragma_value() {
			return getRuleContext(Pragma_valueContext.class,0);
		}
		public Pragma_keywordContext pragma_keyword() {
			return getRuleContext(Pragma_keywordContext.class,0);
		}
		public TerminalNode EQ() { return getToken(VerilogPreParser.EQ, 0); }
		public Pragma_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pragma_expression; }
	}

	public final Pragma_expressionContext pragma_expression() throws RecognitionException {
		Pragma_expressionContext _localctx = new Pragma_expressionContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_pragma_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(254);
				pragma_keyword();
				setState(255);
				match(EQ);
				}
				break;
			}
			setState(259);
			pragma_value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pragma_keywordContext extends ParserRuleContext {
		public TerminalNode SIMPLE_IDENTIFIER() { return getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0); }
		public Pragma_keywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pragma_keyword; }
	}

	public final Pragma_keywordContext pragma_keyword() throws RecognitionException {
		Pragma_keywordContext _localctx = new Pragma_keywordContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_pragma_keyword);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			match(SIMPLE_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pragma_nameContext extends ParserRuleContext {
		public TerminalNode SIMPLE_IDENTIFIER() { return getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0); }
		public Pragma_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pragma_name; }
	}

	public final Pragma_nameContext pragma_name() throws RecognitionException {
		Pragma_nameContext _localctx = new Pragma_nameContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_pragma_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(SIMPLE_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pragma_valueContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(VerilogPreParser.LP, 0); }
		public List<Pragma_expressionContext> pragma_expression() {
			return getRuleContexts(Pragma_expressionContext.class);
		}
		public Pragma_expressionContext pragma_expression(int i) {
			return getRuleContext(Pragma_expressionContext.class,i);
		}
		public TerminalNode RP() { return getToken(VerilogPreParser.RP, 0); }
		public List<TerminalNode> CO() { return getTokens(VerilogPreParser.CO); }
		public TerminalNode CO(int i) {
			return getToken(VerilogPreParser.CO, i);
		}
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public String_Context string_() {
			return getRuleContext(String_Context.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Pragma_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pragma_value; }
	}

	public final Pragma_valueContext pragma_value() throws RecognitionException {
		Pragma_valueContext _localctx = new Pragma_valueContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_pragma_value);
		int _la;
		try {
			setState(279);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(265);
				match(LP);
				setState(266);
				pragma_expression();
				setState(271);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CO) {
					{
					{
					setState(267);
					match(CO);
					setState(268);
					pragma_expression();
					}
					}
					setState(273);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(274);
				match(RP);
				}
				break;
			case UNSIGNED_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(276);
				number();
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(277);
				string_();
				}
				break;
			case SIMPLE_IDENTIFIER:
				enterOuterAlt(_localctx, 4);
				{
				setState(278);
				identifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Resetall_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode RESETALL_DIRECTIVE() { return getToken(VerilogPreParser.RESETALL_DIRECTIVE, 0); }
		public Resetall_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_resetall_directive; }
	}

	public final Resetall_directiveContext resetall_directive() throws RecognitionException {
		Resetall_directiveContext _localctx = new Resetall_directiveContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_resetall_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			match(GA);
			setState(282);
			match(RESETALL_DIRECTIVE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Source_text_Context extends ParserRuleContext {
		public TerminalNode SOURCE_TEXT() { return getToken(VerilogPreParser.SOURCE_TEXT, 0); }
		public Source_text_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_source_text_; }
	}

	public final Source_text_Context source_text_() throws RecognitionException {
		Source_text_Context _localctx = new Source_text_Context(_ctx, getState());
		enterRule(_localctx, 72, RULE_source_text_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(SOURCE_TEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class String_Context extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(VerilogPreParser.STRING, 0); }
		public String_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_; }
	}

	public final String_Context string_() throws RecognitionException {
		String_Context _localctx = new String_Context(_ctx, getState());
		enterRule(_localctx, 74, RULE_string_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Text_macro_definitionContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode DEFINE_DIRECTIVE() { return getToken(VerilogPreParser.DEFINE_DIRECTIVE, 0); }
		public Macro_nameContext macro_name() {
			return getRuleContext(Macro_nameContext.class,0);
		}
		public Macro_textContext macro_text() {
			return getRuleContext(Macro_textContext.class,0);
		}
		public Text_macro_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text_macro_definition; }
	}

	public final Text_macro_definitionContext text_macro_definition() throws RecognitionException {
		Text_macro_definitionContext _localctx = new Text_macro_definitionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_text_macro_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(GA);
			setState(289);
			match(DEFINE_DIRECTIVE);
			setState(290);
			macro_name();
			setState(291);
			macro_text();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Text_macro_usageContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public Macro_usageContext macro_usage() {
			return getRuleContext(Macro_usageContext.class,0);
		}
		public Text_macro_usageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text_macro_usage; }
	}

	public final Text_macro_usageContext text_macro_usage() throws RecognitionException {
		Text_macro_usageContext _localctx = new Text_macro_usageContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_text_macro_usage);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			match(GA);
			setState(294);
			macro_usage();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Time_precisionContext extends ParserRuleContext {
		public TerminalNode TIME_VALUE() { return getToken(VerilogPreParser.TIME_VALUE, 0); }
		public TerminalNode TIME_UNIT() { return getToken(VerilogPreParser.TIME_UNIT, 0); }
		public Time_precisionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_time_precision; }
	}

	public final Time_precisionContext time_precision() throws RecognitionException {
		Time_precisionContext _localctx = new Time_precisionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_time_precision);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			match(TIME_VALUE);
			setState(297);
			match(TIME_UNIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Time_unitContext extends ParserRuleContext {
		public TerminalNode TIME_VALUE() { return getToken(VerilogPreParser.TIME_VALUE, 0); }
		public TerminalNode TIME_UNIT() { return getToken(VerilogPreParser.TIME_UNIT, 0); }
		public Time_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_time_unit; }
	}

	public final Time_unitContext time_unit() throws RecognitionException {
		Time_unitContext _localctx = new Time_unitContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_time_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			match(TIME_VALUE);
			setState(300);
			match(TIME_UNIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Timescale_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode TIMESCALE_DIRECTIVE() { return getToken(VerilogPreParser.TIMESCALE_DIRECTIVE, 0); }
		public Time_unitContext time_unit() {
			return getRuleContext(Time_unitContext.class,0);
		}
		public TerminalNode SL() { return getToken(VerilogPreParser.SL, 0); }
		public Time_precisionContext time_precision() {
			return getRuleContext(Time_precisionContext.class,0);
		}
		public Timescale_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_timescale_directive; }
	}

	public final Timescale_directiveContext timescale_directive() throws RecognitionException {
		Timescale_directiveContext _localctx = new Timescale_directiveContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_timescale_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			match(GA);
			setState(303);
			match(TIMESCALE_DIRECTIVE);
			setState(304);
			time_unit();
			setState(305);
			match(SL);
			setState(306);
			time_precision();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unconnected_drive_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode UNCONNECTED_DRIVE_DIRECTIVE() { return getToken(VerilogPreParser.UNCONNECTED_DRIVE_DIRECTIVE, 0); }
		public Unconnected_drive_valueContext unconnected_drive_value() {
			return getRuleContext(Unconnected_drive_valueContext.class,0);
		}
		public Unconnected_drive_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unconnected_drive_directive; }
	}

	public final Unconnected_drive_directiveContext unconnected_drive_directive() throws RecognitionException {
		Unconnected_drive_directiveContext _localctx = new Unconnected_drive_directiveContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_unconnected_drive_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(GA);
			setState(309);
			match(UNCONNECTED_DRIVE_DIRECTIVE);
			setState(310);
			unconnected_drive_value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unconnected_drive_valueContext extends ParserRuleContext {
		public TerminalNode UNCONNECTED_DRIVE_VALUE() { return getToken(VerilogPreParser.UNCONNECTED_DRIVE_VALUE, 0); }
		public Unconnected_drive_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unconnected_drive_value; }
	}

	public final Unconnected_drive_valueContext unconnected_drive_value() throws RecognitionException {
		Unconnected_drive_valueContext _localctx = new Unconnected_drive_valueContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_unconnected_drive_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(UNCONNECTED_DRIVE_VALUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Undef_directiveContext extends ParserRuleContext {
		public TerminalNode GA() { return getToken(VerilogPreParser.GA, 0); }
		public TerminalNode UNDEF_DIRECTIVE() { return getToken(VerilogPreParser.UNDEF_DIRECTIVE, 0); }
		public Macro_identifierContext macro_identifier() {
			return getRuleContext(Macro_identifierContext.class,0);
		}
		public Undef_directiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_undef_directive; }
	}

	public final Undef_directiveContext undef_directive() throws RecognitionException {
		Undef_directiveContext _localctx = new Undef_directiveContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_undef_directive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(GA);
			setState(315);
			match(UNDEF_DIRECTIVE);
			setState(316);
			macro_identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Version_specifierContext extends ParserRuleContext {
		public TerminalNode VERSION_SPECIFIER() { return getToken(VerilogPreParser.VERSION_SPECIFIER, 0); }
		public Version_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_version_specifier; }
	}

	public final Version_specifierContext version_specifier() throws RecognitionException {
		Version_specifierContext _localctx = new Version_specifierContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_version_specifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(VERSION_SPECIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00f7\u0143\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\3\2\7\2b\n\2\f\2\16\2e\13\2\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3x\n\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3"+
		"\r\3\16\3\16\7\16\u009f\n\16\f\16\16\16\u00a2\13\16\3\17\3\17\3\20\3\20"+
		"\3\20\3\20\3\20\7\20\u00ab\n\20\f\20\16\20\u00ae\13\20\3\20\5\20\u00b1"+
		"\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\7\21\u00ba\n\21\f\21\16\21\u00bd"+
		"\13\21\3\21\5\21\u00c0\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3"+
		"\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\7"+
		"\33\u00e6\n\33\f\33\16\33\u00e9\13\33\3\34\3\34\3\35\3\35\3\36\3\36\3"+
		"\36\3\37\3\37\3 \3 \3 \3 \3 \3 \7 \u00fa\n \f \16 \u00fd\13 \5 \u00ff"+
		"\n \3!\3!\3!\5!\u0104\n!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\7$\u0110\n$\f"+
		"$\16$\u0113\13$\3$\3$\3$\3$\3$\5$\u011a\n$\3%\3%\3%\3&\3&\3\'\3\'\3(\3"+
		"(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3"+
		".\3.\3/\3/\3/\3/\3\60\3\60\3\60\2\2\61\2\4\6\b\n\f\16\20\22\24\26\30\32"+
		"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\2\2\u0137\2c\3\2\2"+
		"\2\4w\3\2\2\2\6y\3\2\2\2\b\177\3\2\2\2\n\u0082\3\2\2\2\f\u0086\3\2\2\2"+
		"\16\u0088\3\2\2\2\20\u008c\3\2\2\2\22\u0091\3\2\2\2\24\u0094\3\2\2\2\26"+
		"\u0097\3\2\2\2\30\u009a\3\2\2\2\32\u00a0\3\2\2\2\34\u00a3\3\2\2\2\36\u00a5"+
		"\3\2\2\2 \u00b4\3\2\2\2\"\u00c3\3\2\2\2$\u00c9\3\2\2\2&\u00cb\3\2\2\2"+
		"(\u00d3\3\2\2\2*\u00d5\3\2\2\2,\u00d7\3\2\2\2.\u00d9\3\2\2\2\60\u00db"+
		"\3\2\2\2\62\u00dd\3\2\2\2\64\u00e7\3\2\2\2\66\u00ea\3\2\2\28\u00ec\3\2"+
		"\2\2:\u00ee\3\2\2\2<\u00f1\3\2\2\2>\u00f3\3\2\2\2@\u0103\3\2\2\2B\u0107"+
		"\3\2\2\2D\u0109\3\2\2\2F\u0119\3\2\2\2H\u011b\3\2\2\2J\u011e\3\2\2\2L"+
		"\u0120\3\2\2\2N\u0122\3\2\2\2P\u0127\3\2\2\2R\u012a\3\2\2\2T\u012d\3\2"+
		"\2\2V\u0130\3\2\2\2X\u0136\3\2\2\2Z\u013a\3\2\2\2\\\u013c\3\2\2\2^\u0140"+
		"\3\2\2\2`b\5\4\3\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\3\3\2\2\2"+
		"ec\3\2\2\2fx\5\6\4\2gx\5\b\5\2hx\5\n\6\2ix\5\22\n\2jx\5\24\13\2kx\5\36"+
		"\20\2lx\5 \21\2mx\5\"\22\2nx\5&\24\2ox\5:\36\2px\5> \2qx\5H%\2rx\5N(\2"+
		"sx\5P)\2tx\5V,\2ux\5X-\2vx\5\\/\2wf\3\2\2\2wg\3\2\2\2wh\3\2\2\2wi\3\2"+
		"\2\2wj\3\2\2\2wk\3\2\2\2wl\3\2\2\2wm\3\2\2\2wn\3\2\2\2wo\3\2\2\2wp\3\2"+
		"\2\2wq\3\2\2\2wr\3\2\2\2ws\3\2\2\2wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2x\5\3"+
		"\2\2\2yz\7\u00a0\2\2z{\7\u00d6\2\2{|\7\u0097\2\2|}\5^\60\2}~\7\u0097\2"+
		"\2~\7\3\2\2\2\177\u0080\7\u00a0\2\2\u0080\u0081\7\u00d7\2\2\u0081\t\3"+
		"\2\2\2\u0082\u0083\7\u00a0\2\2\u0083\u0084\7\u00d8\2\2\u0084\u0085\5\f"+
		"\7\2\u0085\13\3\2\2\2\u0086\u0087\7\u00eb\2\2\u0087\r\3\2\2\2\u0088\u0089"+
		"\7\u00a0\2\2\u0089\u008a\7\u00da\2\2\u008a\u008b\5\32\16\2\u008b\17\3"+
		"\2\2\2\u008c\u008d\7\u00a0\2\2\u008d\u008e\7\u00db\2\2\u008e\u008f\5."+
		"\30\2\u008f\u0090\5\32\16\2\u0090\21\3\2\2\2\u0091\u0092\7\u00a0\2\2\u0092"+
		"\u0093\7\u00dc\2\2\u0093\23\3\2\2\2\u0094\u0095\7\u00a0\2\2\u0095\u0096"+
		"\7\u00dd\2\2\u0096\25\3\2\2\2\u0097\u0098\7\u00a0\2\2\u0098\u0099\7\u00de"+
		"\2\2\u0099\27\3\2\2\2\u009a\u009b\7\u00ed\2\2\u009b\31\3\2\2\2\u009c\u009f"+
		"\5J&\2\u009d\u009f\5\4\3\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f"+
		"\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\33\3\2\2"+
		"\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7\u00c8\2\2\u00a4\35\3\2\2\2\u00a5"+
		"\u00a6\7\u00a0\2\2\u00a6\u00a7\7\u00df\2\2\u00a7\u00a8\5.\30\2\u00a8\u00ac"+
		"\5\32\16\2\u00a9\u00ab\5\20\t\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2"+
		"\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac"+
		"\3\2\2\2\u00af\u00b1\5\16\b\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2"+
		"\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5\26\f\2\u00b3\37\3\2\2\2\u00b4\u00b5"+
		"\7\u00a0\2\2\u00b5\u00b6\7\u00e0\2\2\u00b6\u00b7\5.\30\2\u00b7\u00bb\5"+
		"\32\16\2\u00b8\u00ba\5\20\t\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2"+
		"\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb"+
		"\3\2\2\2\u00be\u00c0\5\16\b\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2"+
		"\u00c0\u00c1\3\2\2\2\u00c1\u00c2\5\26\f\2\u00c2!\3\2\2\2\u00c3\u00c4\7"+
		"\u00a0\2\2\u00c4\u00c5\7\u00e1\2\2\u00c5\u00c6\7\u0097\2\2\u00c6\u00c7"+
		"\5\30\r\2\u00c7\u00c8\7\u0097\2\2\u00c8#\3\2\2\2\u00c9\u00ca\7\u00cb\2"+
		"\2\u00ca%\3\2\2\2\u00cb\u00cc\7\u00a0\2\2\u00cc\u00cd\7\u00e2\2\2\u00cd"+
		"\u00ce\5<\37\2\u00ce\u00cf\7\u0097\2\2\u00cf\u00d0\5\30\r\2\u00d0\u00d1"+
		"\7\u0097\2\2\u00d1\u00d2\5$\23\2\u00d2\'\3\2\2\2\u00d3\u00d4\7\u00ee\2"+
		"\2\u00d4)\3\2\2\2\u00d5\u00d6\7\u00ef\2\2\u00d6+\3\2\2\2\u00d7\u00d8\7"+
		"\u00f0\2\2\u00d8-\3\2\2\2\u00d9\u00da\7\u00f7\2\2\u00da/\3\2\2\2\u00db"+
		"\u00dc\7\u00ec\2\2\u00dc\61\3\2\2\2\u00dd\u00de\7\u00f1\2\2\u00de\63\3"+
		"\2\2\2\u00df\u00e6\5\66\34\2\u00e0\u00e6\5(\25\2\u00e1\u00e6\5*\26\2\u00e2"+
		"\u00e6\5,\27\2\u00e3\u00e6\5\62\32\2\u00e4\u00e6\5L\'\2\u00e5\u00df\3"+
		"\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e5"+
		"\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2"+
		"\2\2\u00e7\u00e8\3\2\2\2\u00e8\65\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb"+
		"\7\u00f2\2\2\u00eb\67\3\2\2\2\u00ec\u00ed\7\u00e9\2\2\u00ed9\3\2\2\2\u00ee"+
		"\u00ef\7\u00a0\2\2\u00ef\u00f0\7\u00e3\2\2\u00f0;\3\2\2\2\u00f1\u00f2"+
		"\7\u00cb\2\2\u00f2=\3\2\2\2\u00f3\u00f4\7\u00a0\2\2\u00f4\u00f5\7\u00e4"+
		"\2\2\u00f5\u00fe\5D#\2\u00f6\u00fb\5@!\2\u00f7\u00f8\7\u0095\2\2\u00f8"+
		"\u00fa\5@!\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2"+
		"\2\u00fb\u00fc\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00f6"+
		"\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff?\3\2\2\2\u0100\u0101\5B\"\2\u0101\u0102"+
		"\7\u009c\2\2\u0102\u0104\3\2\2\2\u0103\u0100\3\2\2\2\u0103\u0104\3\2\2"+
		"\2\u0104\u0105\3\2\2\2\u0105\u0106\5F$\2\u0106A\3\2\2\2\u0107\u0108\7"+
		"\u00c8\2\2\u0108C\3\2\2\2\u0109\u010a\7\u00c8\2\2\u010aE\3\2\2\2\u010b"+
		"\u010c\7\u00a8\2\2\u010c\u0111\5@!\2\u010d\u010e\7\u0095\2\2\u010e\u0110"+
		"\5@!\2\u010f\u010d\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111"+
		"\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7\u00b6"+
		"\2\2\u0115\u011a\3\2\2\2\u0116\u011a\5<\37\2\u0117\u011a\5L\'\2\u0118"+
		"\u011a\5\34\17\2\u0119\u010b\3\2\2\2\u0119\u0116\3\2\2\2\u0119\u0117\3"+
		"\2\2\2\u0119\u0118\3\2\2\2\u011aG\3\2\2\2\u011b\u011c\7\u00a0\2\2\u011c"+
		"\u011d\7\u00e5\2\2\u011dI\3\2\2\2\u011e\u011f\7\u00f3\2\2\u011fK\3\2\2"+
		"\2\u0120\u0121\7\u00c9\2\2\u0121M\3\2\2\2\u0122\u0123\7\u00a0\2\2\u0123"+
		"\u0124\7\u00d9\2\2\u0124\u0125\5\60\31\2\u0125\u0126\5\64\33\2\u0126O"+
		"\3\2\2\2\u0127\u0128\7\u00a0\2\2\u0128\u0129\58\35\2\u0129Q\3\2\2\2\u012a"+
		"\u012b\7\u00f5\2\2\u012b\u012c\7\u00f4\2\2\u012cS\3\2\2\2\u012d\u012e"+
		"\7\u00f5\2\2\u012e\u012f\7\u00f4\2\2\u012fU\3\2\2\2\u0130\u0131\7\u00a0"+
		"\2\2\u0131\u0132\7\u00e6\2\2\u0132\u0133\5T+\2\u0133\u0134\7\u00b8\2\2"+
		"\u0134\u0135\5R*\2\u0135W\3\2\2\2\u0136\u0137\7\u00a0\2\2\u0137\u0138"+
		"\7\u00e7\2\2\u0138\u0139\5Z.\2\u0139Y\3\2\2\2\u013a\u013b\7\u00f6\2\2"+
		"\u013b[\3\2\2\2\u013c\u013d\7\u00a0\2\2\u013d\u013e\7\u00e8\2\2\u013e"+
		"\u013f\5.\30\2\u013f]\3\2\2\2\u0140\u0141\7\u00ea\2\2\u0141_\3\2\2\2\21"+
		"cw\u009e\u00a0\u00ac\u00b0\u00bb\u00bf\u00e5\u00e7\u00fb\u00fe\u0103\u0111"+
		"\u0119";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}