import csv

def analyze_flight(filename):
    altitudes = []
    speeds = []
    batteries = []
    timestamps = []

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamps.append(float(row["timestamp"]))
            altitudes.append(float(row["altitude"]))
            speeds.append(float(row["speed"]))
            batteries.append(float(row["battery"]))

    duration = timestamps[-1] - timestamps[0]
    battery_drain = batteries[0] - batteries[-1]
    drain_rate = (battery_drain / duration) * 60
    avg_speed = round(sum(speeds)/len(speeds), 1)
    max_alt = max(altitudes)

    print("=== Flight Summary Report ===")
    print(f"Max Altitude:       {max_alt} m")
    print(f"Avg Speed:          {avg_speed} mph")
    print(f"Flight Duration:    {int(duration)} sec")
    print(f"Battery Start:      {int(batteries[0])}%")
    print(f"Battery End:        {int(batteries[-1])}%")
    print(f"Battery Drain Rate: {round(drain_rate, 1)}% / min")

    flight_assessment(max_alt, drain_rate, avg_speed)

def flight_assessment(max_alt, drain_rate, avg_speed):
    print("\n=== Flight Assessment ===")

    if max_alt > 120:
        print(f"WARN  Altitude: {max_alt}m exceeds FAA 120m limit")
    else:
        print(f"PASS  Altitude: {max_alt}m within FAA limit")

    if drain_rate > 15:
        print(f"WARN  Battery drain: {round(drain_rate,1)}% /min is high")
    else:
        print(f"PASS  Battery drain: {round(drain_rate,1)}% /min is normal")

    if avg_speed > 100:
        print(f"WARN  Speed: {avg_speed}mph exceeds safe limit")
    else:
        print(f"PASS  Speed: {avg_speed}mph within limits")

analyze_flight("flight_log.csv")