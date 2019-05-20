set terminal png
set output 'plot50_time.png'
set autoscale
set xlabel 'number blocked'
set ylabel 'sucsess%'


plot "datat.txt" title "sucsess rate"

set terminal png
set output 'plot_time.png'
set autoscale
set xlabel 'number blocked'
set ylabel 'time in(s)'

plot "datat.txt" title "time in (s/100)"



