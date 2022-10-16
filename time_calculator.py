def add_time(start, duration,day_of_week=None):
  day_of_week_index={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
  day_of_week_array=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]                     
  s=start.split(":")
  start_hr=int(s[0])
  s=s[1].split()
  start_min=int(s[0])
  am_or_pm=s[1]
  if am_or_pm=="PM":
    start_hr+=12
  d=duration.split(":")
  duration_hr=int(d[0])
  duration_min=int(d[1])
  end_min=start_min+duration_min
  extra_hr=end_min//60
  end_min=end_min%60
  total_hr=start_hr+duration_hr+extra_hr
  end_hr=(total_hr%24)%12
  end_hr=12 if end_hr==0 else end_hr
  amount_days=(total_hr)//24
  end_min=end_min if end_min>9 else "0"+str(end_min)
  if (duration_hr+extra_hr)%24==0: end_am_pm=am_or_pm
  elif total_hr%24>11:end_am_pm="PM"
  else:end_am_pm="AM"
  new_date=str(end_hr)+":"+str(end_min)+" "+str(end_am_pm)
  if day_of_week:
    day_of_week=day_of_week.lower()
    index=day_of_week_index[day_of_week]
    index=(index+amount_days)%7
    day=day_of_week_array[index]
    new_date+=", {}".format(day)
  if amount_days==1:
    new_date+=" (next day)"
  if amount_days>1:
    new_date+=" ({} days later)".format(amount_days)
  return new_date