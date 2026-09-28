print("day planner")
print("ANSWER ... and ill plan ur day")
day = input("what day is it???? (monday to sunday):").strip().lower()
weather = input("what is da weather??? (sunny/ rainy/ couldy):").strip().lower()
homework = input("is ur homework done???? (yes/no):").strip().lower()
if day in ("saturday","sunday"):
    print("day type : weekend enjoy brother")
elif day == "monday":
    print("day type  : first day of da hell school")
elif day == "friday":
    print("day type  : last day of da school torture now playtime")
elif day == ("tueday", "wednesday","thursday"):
    print("day type  : screentime - 23:59:59")
else:
    print("day type: day not recognised,please check ur grammatical skill bro")

if weather =="sunny" and homework == "yes":
    print("after school:go down to play or play minecraft or smth")
if weather =="rainy" or weather == "cloudy":
    print("pack up my guy gotta take dat umbrella with u")
if not (homework == "yes"):
    print("homework not done:buddy ur cooked or else dont do jus play")

if weather =="rainy" and not (homework =="yes"):
    print("best plan get cooked or do ur homework my suggestion dont do it")
elif weather == "sunny" and homework == "yes" and not (day in("saturday","sunday")):
    print("ur good buddy jus go to da hell and come back for a 1v1")
elif day in ("saturday","sunday") and weather =="sunny":
    print("perfect day buddy time to increase ur screen time or jus go down to protect ur eyes")

else:
    print("buddy ur cooked just give up u dont got this :(")

print("thas it bro ur good to goo")
