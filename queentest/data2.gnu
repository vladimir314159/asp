set xlabel "number of queens"
set ylabel "time"
set terminal png
set ytics autofreq tc lt 1
set output 'time_n50_for_2000to2500.png'
plot  "queens3.txt" title "encoding 3" with lines, \
      "queens4.txt" title "encoding 4" with lines
    



