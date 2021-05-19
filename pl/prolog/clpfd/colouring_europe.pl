% https://www.mathsisfun.com/activity/coloring.html
% GE = Germany
% PO = Poland
% CR = Czech Republic
% SL = Slovakia
% AU = Austria 
% SW = Switzerland
% SLO = Slovenia
% HU = Hungary
% IT = Italy

:- use_module(library(clpfd)).

colourable([GE,PO,CR,SL,AU,SW,SLO,HU,IT]) :-
                rgb(GE), rgb(PO), rgb(CR), rgb(SL), rgb(AU), rgb(SW), rgb(SLO), rgb(HU), rgb(IT), 
                GE #\= PO, GE #\= CR, GE #\= SW, GE #\= AU,
                PO #\= SL, PO #\= CR, PO #\= SL,
                CR #\= GE, CR #\= PO, CR #\= SL, CR #\= AU,
                SL #\= PO, SL #\= CR, SL #\= AU, SL #\= HU,
                AU #\= GE, AU #\= CR, AU #\=SL, AU #\= HU, AU #\= SW, AU #\= SLO, AU #\= IT,
                HU #\= SL, HU #\= AU, HU #\= SLO,
                SW #\= GE, SW #\= AU, SW #\= IT,
                SLO #\= AU, SLO #\= HU, SLO #\= IT,
                IT #\= SW, IT #\= AU, IT #\= SL.

rgb(1).
rgb(2).
rgb(3).
rgb(4).

% colourable(X).
% X = [1, 2, 3, 1, 2, 3, 1, 3, 4] .

