# Travel Agent - Rule Based Agent

# -----------------------------
# Get User Input
# -----------------------------

destination = input("Enter your destination: ")
budget = int(input("Enter your budget (PKR): "))
days = int(input("Enter number of days: "))


# -----------------------------
# Rule 1: Budget Classification
# -----------------------------

if budget < 30000:
    budget_type = "Low Budget"

elif budget <= 70000:
    budget_type = "Medium Budget"

else:
    budget_type = "High Budget"


# -----------------------------
# Rule 2: Trip Duration
# -----------------------------

if days <= 3:
    trip_type = "Short Trip"

elif days <= 7:
    trip_type = "Standard Trip"

else:
    trip_type = "Long Trip"


# -----------------------------
# Rule 3: Destination
# -----------------------------

if destination.lower() == "hunza":

    places = "Attabad Lake, Baltit Fort, Altit Fort, Passu Cones"

elif destination.lower() == "murree":

    places = "Mall Road, Patriata, Kashmir Point, Pindi Point"

elif destination.lower() == "skardu":

    places = "Shangrila Lake, Deosai, Upper Kachura Lake"

elif destination.lower() == "swat":

    places = "Malam Jabba, Kalam, Bahrain, Mingora"

else:

    places = "Explore the famous local attractions of your destination."


# -----------------------------
# Rule 4: Hotel Recommendation
# -----------------------------

if budget_type == "Low Budget":

    hotel = "Budget Guest House"

elif budget_type == "Medium Budget":

    hotel = "3-Star Hotel"

else:

    hotel = "Luxury Hotel"


# -----------------------------
# Final Travel Recommendation
# -----------------------------

print("\n===== Travel Agent Recommendation =====")

print("Destination:", destination)
print("Budget:", budget_type)
print("Trip Duration:", trip_type)
print("Recommended Places:", places)
print("Hotel Recommendation:", hotel)