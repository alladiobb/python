def func(x,l=[]):
    for i in range (x):
        l.append(i*i)
        print(l)

func(2)
func(3,[3,2,1])
func(3)