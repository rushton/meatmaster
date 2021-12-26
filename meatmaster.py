from datetime import datetime, timedelta
import ciso8601
import sys

def main():
    year = sys.argv[1]
    filepath = f"meat_log_{year}"
    meat_log = open(filepath, "a")
    while True:
        meat_temp = int(input("Enter degrees F:"))
        traeger_temp = input("Enter traeger temp setting (default:smoke):")
        if not traeger_temp:
            traeger_temp="smoke"
        now = datetime.now()
        start_time = get_start_time(filepath) or now
        time_in = int((now - start_time).total_seconds())

        start_temp = get_start_temp(filepath) or meat_temp
        diff_deg = meat_temp - start_temp

        deg_per_min = round((diff_deg / (time_in/60)),4) if time_in > 0 else 0
        line = f"{now.isoformat()} {traeger_temp} {meat_temp} {time_in} {diff_deg} {deg_per_min}\n"
        meat_log.write(line)
        meat_log.flush()

        if deg_per_min > 0:
            mins_to_done = (120 - meat_temp) / deg_per_min
            est_time_to_done = now + timedelta(minutes=mins_to_done)
            print(f"Estimated Done Time: {est_time_to_done.isoformat()}")

def get_start_time(filepath):
    meat_log = open(filepath, "r")
    lines = [line for line in meat_log]
    meat_log.close()
    if len(lines) < 1:
        return None

    start_time = ciso8601.parse_datetime(lines[0].split(" ")[0])
    return start_time

def get_start_temp(filepath):
    meat_log = open(filepath, "r")
    lines = [line for line in meat_log]
    meat_log.close()
    if len(lines) < 1:
        return None

    start_temp = int(lines[0].split(" ")[2])
    return start_temp

if __name__ == '__main__':
    main()
