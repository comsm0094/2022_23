
set yrange [0:1.5]

plot "chasing_pw_freq1.0.dat" us 1:2 w lines title "fast"

replot "chasing_pw_freq0.2.dat" us 1:2 w lines  title "slow"