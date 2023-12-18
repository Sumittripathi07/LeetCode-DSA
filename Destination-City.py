# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are:
# "D" -> "B" -> "C" -> "A".
# "B" -> "C" -> "A".
# "C" -> "A".
# "A".

paths = [["B", "C"], ["D", "B"], ["C", "A"]]
start_cities = []
end_cities = []
for i in paths:
    start_cities.append(i[0])
    end_cities.append(i[1])
str_set = set(start_cities)
end_set = set(end_cities)
print(list(end_set - str_set)[0])
