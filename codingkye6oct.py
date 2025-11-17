def convert_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes
total_time_in_minutes = 200
hours, remaining_minutes = convert_minutes(total_time_in_minutes)
print(f"{total_time_in_minutes} minutes id equal to {hours} hours and {remaining_minutes} mniutes.")