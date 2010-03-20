import runkeeper.user

user = runkeeper.user.User("bnmrrs")
activities = user.get_all_activities()

total_distance = 0
for activity in activities:
  total_distance += activity.get_distance()

print "%dkm" % total_distance
