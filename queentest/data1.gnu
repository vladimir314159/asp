set xlabel "number of queens"
set ylabel "time"
set terminal png
set ytics autofreq tc lt 1
set output 'time_n40_three.png'
plot  "queens3.txt" title "encoding 3" with lines, \
      "queens4.txt" title "encoding 4" with lines, \
      "queens11.txt" title "encoding 11" with lines



