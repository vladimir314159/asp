set xlabel "number of queens"
set ylabel "time"
set terminal png
set ytics autofreq tc lt 1
set output 'time_n20.png'
plot  "queens1.txt" title "encoding 1" with lines, \
      "queens2.txt" title "encoding 2" with lines, \
      "queens3.txt" title "encoding 3" with lines, \
      "queens4.txt" title "encoding 4" with lines, \
      "queens10.txt" title "encoding 10" with lines, \
      "queens11.txt" title "encoding 11" with lines



