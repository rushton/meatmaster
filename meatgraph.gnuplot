set title "Meat Temp"

set xdata time
set style data lines

set timefmt "%Y-%m-%dT%H:%M:%S"
set format x "%H:%M"
set xlabel "Time"
set ylabel "Degrees F"
set yrange [0:140]

plot "meat_log_".year using 1:3 title "deg", 125 title "target"
set style line 1 linewidth 100 
pause mouse keypress
if (MOUSE_KEY == 27) exit 0
reread
