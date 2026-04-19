names_list = ["Subin", "Neha", "Manu", "Mummy", "Papa"]
#
#for _ in range(len(names_list)):
#    print(names_list[_])

for name in names_list:
    print(name)

print(len(names_list))

team = {
    "Subin" : "Developer",
    "Neha" : "Developer2",
    "Manu" : "Developer3"
}

#print(team["Subin"])

#for loop on dictionary - by default iterate over keys

for name in team:
    print(name, team[name], sep=", ")


team = [
    {"name" : "Subin", "job" : "Developer", "dept" : "technology"},
    {"name" : "Neha", "job" : "Developer2", "dept" : "dataanalysis"},
    {"name" : "Manu", "job" : "Developer3", "dept" : "marketing"},
    {"name" : "Sheenu", "job" : "Developer4", "dept" : None}
]

for employee in team:
    print(employee["name"], employee["job"], employee["dept"], sep=", ")