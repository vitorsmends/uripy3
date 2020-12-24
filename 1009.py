nome = input()
s = float(input()) # salario fixo
v = float(input()) # vendas

p = (v * 0.15)

t = (s + p)
round(t, 2)
print("TOTAL = R$ {:.2f}".format(t))