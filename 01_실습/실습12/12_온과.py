dic = {'OS':'Operatin System','CG':'Computer Grapics','DB':'Data Base', 'ML':'Machine Learning'}
for _ in range(3):
    name = input()
    if name in dic:
        print(dic.get(name))
    else:
        print("NOT EXIST!")