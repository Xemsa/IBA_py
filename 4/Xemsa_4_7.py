#4.7
#" 1  2   3"

def tr(n):
    try:
        return int(n)
    except:
        pass

    try:
        return float(n)
    except:
        pass

    return 0

#st = " 10  20   030"
st = input("Числа через пробел ")
print(f"Исходная строка {st}")

st = ' '.join(st.split())

print(f"Без лишних пробелов {st}")
li = list(map(tr,st.split(" ")))
print(f"Список чисел {li}")
print(sum(li)/len(li))

