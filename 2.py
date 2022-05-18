sec = int(input())
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
print("{}:{}:{}".format(hour_value, min_value, sec_value))