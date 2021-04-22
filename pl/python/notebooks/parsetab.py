
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : expression TIMES termexpression : termterm : NUMBERterm : LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,4,5,6,],[3,3,3,3,]),'LPAREN':([0,4,5,6,],[4,4,4,4,]),'$end':([1,2,3,8,9,10,],[0,-3,-4,-1,-2,-5,]),'PLUS':([1,2,3,7,8,9,10,],[5,-3,-4,5,-1,-2,-5,]),'TIMES':([1,2,3,7,8,9,10,],[6,-3,-4,6,-1,-2,-5,]),'RPAREN':([2,3,7,8,9,10,],[-3,-4,10,-1,-2,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,],[1,7,]),'term':([0,4,5,6,],[2,2,8,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sols7_2.ipynb',4),
  ('expression -> expression TIMES term','expression',3,'p_expression_times','sols7_2.ipynb',8),
  ('expression -> term','expression',1,'p_expression_term','sols7_2.ipynb',12),
  ('term -> NUMBER','term',1,'p_term_num','sols7_2.ipynb',16),
  ('term -> LPAREN expression RPAREN','term',3,'p_term_expression','sols7_2.ipynb',20),
]