x = []
y = []
for i in range(1, 3):
    a = input(f"\nEnter Player{i} Name\n")
    x.append(a)
    b = int(input(f"\n1.Stone\n2.Paper\n3.Scissor\nEnter Player{i} Your Choice (1/2/3)\n"))
    y.append(b)
p1 = y[0]
p2 = y[1]
def win(p, q):
    if (p==1 and q==2) or (p==2 and q==3) or (p==3 and q==1):
        w = "wq"
    else:
        w = "wp"
    return w
if p1<=3 and p2<=3:
    ans = win(p1, p2)
else:
    print("Wrong Value Entered")
    exit()
if ans == "wp":
    print(f"\n{x[0]} win")
else:
    print(f"\n{x[1]} win")
