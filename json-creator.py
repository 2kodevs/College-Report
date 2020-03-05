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
        l = [float(x) for x in list]
        fd.write(f"\t\"{group}\": {l},\n")

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
