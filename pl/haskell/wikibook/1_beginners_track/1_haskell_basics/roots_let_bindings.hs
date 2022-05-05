roots a b c =
  let sdisc = sqrt (b * b - 4 * a * c)
   in ( (- b + sdisc) / (2 * a),
        (- b - sdisc) / (2 * a)
      )