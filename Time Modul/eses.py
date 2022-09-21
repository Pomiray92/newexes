import datetime

current_datetime = datetime.datetime.now()

sub_days = current_datetime - datetime.timedelta(days=15)

sub_days2 = sub_days.strptime("%Y-%M-%d")

print(sub_days2)