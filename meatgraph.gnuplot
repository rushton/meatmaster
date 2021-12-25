set title "Meat Temp"

set xdata time
set style data lines

set timefmt "%Y-%m-%dT%H:%M:%S"
set format x "%H:%M"
set xlabel "Time"
set ylabel "Degrees F"
set autoscale y

plot "~/meat_log" using 1:3 title "deg"
set style line 1 linewidth 100 
pause 1
reread
