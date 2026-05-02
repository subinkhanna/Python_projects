import json
from urllib.request import urlopen

with urlopen("<<url>>") as response:
    jsonstring = response.read()


data = json.loads(jsonstring)   ##loads - when loading a json string.  load - when loading a file

print(json.dumps(data, indent=2))   ##dumps - when converting obj to json string.  dump - when dumping to file

with open("file_path_with_name", 'w') as f:
    json.dump(data, f)


