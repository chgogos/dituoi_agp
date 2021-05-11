parent(bill, jake).
parent(bill, shelley).
sibling(X, Y) :- parent(M, X), parent(M, Y).