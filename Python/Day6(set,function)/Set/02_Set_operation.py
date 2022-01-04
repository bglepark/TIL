# Set의 연산

A = {1,2,3}
B = {3,4,5}

# 1) 교집합 => Intersection
C = A & B
print(C)

C = A.intersection((B))
print(C)

# 2) 합집합 => Union
C = A|B
print(C)

C = A.union(B)
print(C)

# 3) 차집합 => Difference
C = A -B
print(C)

C = A.difference(B)
print(C)

D = B-A
print(D)