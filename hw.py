training_hours = int(input("enter the hour"))
training_minutes = int(input("enter the minutes"))
arrival_hours = int(input("enter the hour of arrival"))
arrival_minutes = int(input("enter the minute of arrival"))

late="Late"
on_time="On time"
early="Early"

training_time = (training_hours * 60) + training_minutes
arrival_time = (arrival_hours * 60) + arrival_minutes
total_mins_diff = arrival_time - training_time

player_arrival = late
if total_mins_diff < -30:
    player_arrival = early
elif total_mins_diff <= 0:
    player_arrival = on_time

result = ""
if total_mins_diff != 0 :
    hours_difference = abs(total_mins_diff) // 60
    minutes_differnce = abs(total_mins_diff) % 60

    if hours_difference > 0:
        result = \
        f"{hours_difference}:{minutes_differnce:02}hours"
    else:
        result = f"{minutes_differnce} minutes"
    if total_mins_diff < 0:
        result += "Before the start"
    else:
        result += "after the start"
    
    print(player_arrival)
    if result :
        print(result)