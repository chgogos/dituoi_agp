import ply.yacc as yacc

from WAELexer import tokens

def p_waeStart(p):
    'waeStart : wae SEMI'
    p[0] = p[1]

def p_wae_1(p):
    'wae : NUMBER'
    p[0] = ['num',p[1]]

def p_wae_2(p):
    'wae : ID'
    p[0] = ['id',p[1]]

def p_wae_3(p):
    'wae : LBRACE PLUS wae wae RBRACE'
    p[0] = ['+',p[3],p[4]]

def p_wae_4(p):
    'wae : LBRACE MINUS wae wae RBRACE'
    p[0] = ['-',p[3],p[4]]

def p_wae_5(p):
    'wae : LBRACE TIMES wae wae RBRACE'
    p[0] = ['*',p[3],p[4]]

def p_wae_6(p):
    'wae : LBRACE DIV wae wae RBRACE'
    p[0] = ['/',p[3],p[4]]

def p_wae_7(p):
    'wae : LBRACE IF wae wae wae RBRACE'
    p[0] = ['if',p[3],p[4],p[5]]

def p_wae_8(p):
    'wae : LBRACE WITH LBRACE alist RBRACE wae RBRACE'
    p[0] = ['with',p[4],p[6]]

def p_alist_1(p):
    'alist : LBRACE ID wae RBRACE'
    p[0] = [[p[2],p[3]]]

def p_alist_2(p):
    'alist : LBRACE ID wae RBRACE alist'
    p[0] = [[p[2],p[3]]] + p[5]

def p_error(p):
    print("Syntax error in input!")
    parser = yacc.yacc()

parser = yacc.yacc()