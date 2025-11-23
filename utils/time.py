from datetime import datetime, timedelta

def tick_to_time(ticks: int) -> str:
    start_date = datetime(2025, 1, 1, 0, 0)
    minutes_per_tick = 10
    delta = timedelta(minutes=ticks * minutes_per_tick)
    new_date = start_date + delta
    return new_date.strftime("%Y-%m-%d %H:%M")