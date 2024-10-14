#Question 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
#1
mutual_routes = our_routes.intersection(competitor_routes)
print(mutual_routes)
#2
unique_routes = our_routes.difference(competitor_routes)
print(unique_routes)
#3
no_routes = our_routes.symmetric_difference(competitor_routes)
print(no_routes)