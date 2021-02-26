import operator
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
   
    sorted_d=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    for i in sorted_d:
        print(i,"=",sorted_d[i])
str=input()
most_frequent(str)
