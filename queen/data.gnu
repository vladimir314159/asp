set xlabel "number of queens"
set ylabel "time"
set terminal png
set ytics autofreq tc lt 1
set output 'plotlong_time.png'
plot "data_without_rules.txt" title "with rules", \
     "data_with_rules.txt" title "without rules"
