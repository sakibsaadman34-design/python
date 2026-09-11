print("--- Smart School Day Planner ---")
print("Answer 3 question and I will plan your school day")

day = input("What day is it?(Monday - Sunday): ").strip().lower()

weather = input("Hows the weather today? (Rainy, Cloudy, Sunny): ").strip().lower()

homework = input("Have you done your homework? (Yes Or No): ").strip().lower()

print(f"your plan for {day}: ")

print("_" * 35)

if (day == "saturday" or day == "sunday"):
    print("It is weekend. Enjoy!")
elif (day == "friday"):
    print("The last school day of the week. return the library books you borrowed.")
elif (day == "tuesday" or day == "wednesday" or day == "thursday"):
    print("School day. stay focused.")
else:
    print("Day not recognised. Please check the spelling.")

print("_" * 35)

if (weather == "sunny" and homework == "yes"):
    print("You can go play.")
elif (weather == "rainy" or weather == "cloudy"):
    print("Bring an umbrella. The ground might be wet. You can go play now.")
elif (weather == "sunny" and homework == "no"):
    print("First complete your homework. then you can go play.")

elif (weather == "sunny") and not (homework == "yes"):
    print("Best Plan: Finish your homework.")

elif (weather == "sunny") and (homework == "yes") and not (day in ("Saturday", "Sunday")):
    print("Everything checks out. You are ready for a great school day.")

else:
    print("An Error Occured. Please Refresh the page and try again.")