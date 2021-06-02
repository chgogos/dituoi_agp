colors :: [[Char]]
colors = ["red", "green", "blue"]

colourable :: ([Char], [Char], [Char], [Char], [Char], [Char], [Char], [Char],
 [Char], [Char], [Char], [Char], [Char], [Char])
colourable = head [("WA", wa, "SA", sa, "NT", nt, "Q", q, "NSW", nsw, "V", v, "T", t) | 
    wa <- colors,
    sa <- colors,
    nt <- colors,
    q <- colors,
    nsw <- colors,
    v <- colors,
    t <- colors, 
    wa /= nt, wa /= sa, 
    nt /= sa, nt /= q,
    sa /= q, sa /= nsw, sa /= v,
    q /= nsw,
    nsw /= v] 