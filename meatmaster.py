from datetime import datetime, timedelta
import ciso8601

def main():
    meat_log = open("/Users/christina/meat_log", "a")
    while True:
        prev_time, prev_traeger_temp, prev_temp, prev_time_in, prev_deg_diff, prev_deg_rate = get_prev_temp()
        meat_temp = int(input("Enter degrees F:"))
        traeger_temp = input("Enter traeger temp setting (default:smoke):")
        if not traeger_temp:
            traeger_temp="smoke"
        now = datetime.now()
        time_in = int((now - get_start_time()).total_seconds())
        diff_deg = meat_temp - get_start_temp()
        deg_per_min = round((diff_deg / (time_in/60)),4)
        line = f"{now.isoformat()} {traeger_temp} {meat_temp} {time_in} {diff_deg} {deg_per_min}"
        print(line + "\n")
        mins_to_done = (120 - meat_temp) / deg_per_min
        est_time_to_done = now + timedelta(minutes=mins_to_done)
        print(f"Estimated Done Time: {est_time_to_done.isoformat()}")
        meat_log.write(line + "\n")
        meat_log.flush()

def get_start_time():
    meat_log = open("/Users/christina/meat_log", "r")
    start_time = ciso8601.parse_datetime([line for line in meat_log][0].split(" ")[0])
    meat_log.close()
    return start_time

def get_start_temp():
    meat_log = open("/Users/christina/meat_log", "r")
    start_temp = int([line for line in meat_log][0].split(" ")[2])
    meat_log.close()
    return start_temp

def get_prev_temp():
    meat_log = open("/Users/christina/meat_log", "r")
    last_line = [line for line in meat_log][-1]
    time, t_temp, temp, time_in, deg_diff, deg_rate = last_line.split(" ")
    meat_log.close()
    time = ciso8601.parse_datetime(time)
    temp = int(temp)
    time_in = int(time_in)
    deg_diff = int(deg_diff)
    deg_rate = float(deg_rate)
    return time, t_temp, temp, time_in, deg_diff, deg_rate


if __name__ == '__main__':
    main()
