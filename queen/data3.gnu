set terminal png
set output 'plot50.png'
set autoscale
set xlabel 'number blocked'
set ylabel 'sucsess%'


plot "data3.txt" title "sucsess rate"

set terminal png
set output 'plot_time.png'
set autoscale
set xlabel 'number blocked'
set ylabel 'time in(s)'

plot "datat.txt" title "sucseed", \
     "datatf.txt" title "fail"



