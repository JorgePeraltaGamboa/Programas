import json
lnames=[]
ldob=[]
data = json.load(open('personas.json'))


def recorre(data):
    for key in data:
        lnames.append(str(key))
        ldob.append(str(data[key]["dob"]))
        if("children" in data[key]):
            recorre(data[key]["children"])
"""def result():
    recorre(data)
    print min(ldob)
    print max(ldob)
    print lnames
"""

if __name__ == '__main__':
    recorre(data)
    print min(ldob)
    print max(ldob)
    print lnames
