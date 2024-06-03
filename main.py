mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
missions_total = len(mission_names)
missions_successful = sum(mission_success)
rate_success = (missions_successful / missions_total) * 100
print("Number of total missions", missions_total)
print("Number of successful missions", missions_successful)
print("Rate of success: {:.2f}%".format(rate_success))
print("Missions before the year 2000:")
for i in range(missions_total):
    if mission_years[i] < 2000:
        print("-", mission_names[i])
