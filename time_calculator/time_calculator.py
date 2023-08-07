def add_time(start_time, duration_time, starting_day="Monday"):
   HOUR_IN_MINUTES_CONSTANT = 60
   DAY_IN_MINUTES_CONSTANT = 1440
   DAYS_A_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
   
   # split start_time into hour and minutes
   start_time_part = start_time.split(":")
   start_hour = int(start_time_part[0])
   start_minute, am_pm = map(str.strip , start_time_part[1].split())
  
   # split duration_time into hour and minutes
   duration_time_part = duration_time.split(":")
   duration_hour = int(duration_time_part[0])
   duration_minute = int(duration_time_part[1])

   # change into minute
   total_minutes = start_hour * HOUR_IN_MINUTES_CONSTANT + int(start_minute)
   if am_pm == "PM":
        total_minutes += 12 * 60
   total_minutes += duration_hour * HOUR_IN_MINUTES_CONSTANT + duration_minute
   
   days_passed = total_minutes // DAY_IN_MINUTES_CONSTANT
   remaining_minutes = total_minutes % DAY_IN_MINUTES_CONSTANT
   
   new_hour = remaining_minutes // HOUR_IN_MINUTES_CONSTANT
   new_minute = remaining_minutes % HOUR_IN_MINUTES_CONSTANT
   
   new_am_pm = "AM"
   if new_hour >= 12:
      new_am_pm = "PM"
      if new_hour > 12:
         new_hour -= 12
   elif new_hour == 0:
      new_hour = 12
   
   if starting_day:
      starting_day = starting_day.lower().capitalize()
      starting_day_index = DAYS_A_WEEK.index(starting_day)
      new_day_index = (starting_day_index + days_passed) % 7
      new_day = DAYS_A_WEEK[new_day_index]
      new_day_text = f", {new_day}"
      if days_passed == 1:
         new_day_text = f", {new_day} (next day)"
      elif days_passed > 1:
         new_day_text = f", {new_day} ({days_passed} days later)"
   elif days_passed >= 1:
      new_day_text = f", (next day)"
      if days_passed > 1:
         new_day_text = f", ({days_passed} days later)"
   else:
      new_day_text = ""
   
   new_time = f"Return : {new_hour:02d}:{new_minute:02d} {new_am_pm}{new_day_text}"
   return new_time
