major_rivers = {
    'nile': 'egypt',
    'gold': 'sacramento',
    'volga': 'russia',
    }
for river, country in major_rivers.items():
  print(f"The {river.title()}, flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in major_rivers.keys():
  print(f"- {river.title()}.")

print("\nThe following countries are included in this data set:")
for country in major_rivers.values():
  print(f"- {country.title()}.")
