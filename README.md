# Drone Flight Log Analyzer

A tool that parses UAV flight log CSV files and generates a flight summary report with FAA compliance assessment.

## What it does

- Parses drone flight log data (altitude, speed, battery, GPS)
- Generates a clean summary report including max altitude, average speed, flight duration, and battery drain rate
- Runs an automated FAA compliance assessment and flags warnings for altitude limits, battery drain, and speed

## Why it matters

UAV operators need fast, reliable ways to review flight data and ensure regulatory compliance. This tool automates that process, flagging potential issues before they become incidents.

## How to run it

1. Clone this repository
2. Add your flight log as `flight_log.csv` in the project folder
3. Run the script:

python3 analyzer.py

## Example output

=== Flight Summary Report ===
Max Altitude:       120.0 m
Avg Speed:          5.9 mph
Flight Duration:    25 sec
Battery Start:      100%
Battery End:        92%
Battery Drain Rate: 19.2% / min

=== Flight Assessment ===
PASS  Altitude: 120.0m within FAA limit
WARN  Battery drain: 19.2% /min is high
PASS  Speed: 5.9mph within limits

## Built with

- Python 3
- CSV module
- FAA Part 107 operational knowledge
