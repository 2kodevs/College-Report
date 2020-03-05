import json

def addCareer(career, group, path):
    with open(path, "a") as fd:
        fd.write(f"\t\"{career}\": \"{group}\",\n")

def addPerformance(career, list, path):
    with open(path, "a") as fd:
        pers = ""
        for v in list:
            pers += ", " + v.replace(",", ".")
        pers = pers[2:]
        fd.write(f"\t\"{career}\": [{pers}],\n")

def addGraduate(group, list, path):
    with open(path, "a") as fd:
        l = [ int(x.replace(".", "")) for x in list]
        fd.write(f"\t\"{group}\": {l},\n")

def parseMatriculas(path):
    groups = {}
    careers = {}
    data = []
    with open(path + "grupos.json", "r") as fd:
        groups = json.load(fd)
    with open(path + "carreras.json", "r") as fd:
        careers = json.load(fd)
    for k, _ in careers.items():
        careers[k] = [0, 0]
    with open(path + "matri", "r") as fd:
        data = fd.readlines()
    for l in data:
        i = parseLine(l)
        try:
            key = i[0]
            groups[key][0] += i[1]
            groups[key][1] += i[2]
        except KeyError:
            try:
                careers[key][0] += i[1]
                careers[key][1] += i[2]
            except KeyError:
                continue
    print(groups)
    with open(path + "grupos.json", "w") as fd:
        json.dump(groups, fd)
    with open(path + "matriculasCarreras.json", "w") as fd:
        json.dump(careers, fd)
    


def parseLine(line):
    aux = line.split(" ")
    aux[-1] = aux[-1].replace("\n", "")
    career = ""
    for s in aux[:-2]:
        if s == " ":
            continue
        career += s + " "
    career = career[:-1]
    return [career, int(aux[-2]), int(aux[-1])]
    



if __name__ == "__main__":
    import argparse 

    parser = argparse.ArgumentParser(description='json-creator')
    parser.add_argument('-c', '--career', type=str, default='', help='career')
    parser.add_argument('-g', '--group', type=str, default='', help='group of career')
    parser.add_argument('-p', '--path', type=str, default='./resources/data/carreras.json', help='path of json')
    parser.add_argument('-m', '--method', type=str, default='addCareer', help='method to call')
    parser.add_argument('-l', '--list', nargs='+', required=False)

    args = parser.parse_args()
    if args.method == "addCareer":
        addCareer(args.career, args.group, args.path)
    elif args.method == "addPerformance":
        addPerformance(args.career, args.list, args.path)
    elif args.method == "addGraduate":
        addGraduate(args.group, args.list, args.path)
    elif args.method == "parseMatriculas":
        parseMatriculas(args.path)