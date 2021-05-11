my_append([], List, List).
my_append([Head | List_1], List_2, [Head | List_3]) :-
            my_append(List_1, List_2, List_3).