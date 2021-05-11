my_member(Element, [Element|_]).
my_member(Element, [_|List]) :-  my_member(Element, List).