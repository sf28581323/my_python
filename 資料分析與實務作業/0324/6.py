num1 = [i for i in range(1, 100, 2)]
num2 = [i for i in range(0, 101, 5)]
Intersection = set(num1).intersection(set(num2))
print('交集為:', sorted(Intersection))
union = set(num1).union(set(num2))
print('聯集為:', sorted(union))
difference1 = set(num1).difference(set(num2))
print('A-B差集為:', sorted(difference1))
difference2 = set(num2).difference(set(num1))
print('B-A差集為:', sorted(difference2))
symmetric_difference1 = set(num1).symmetric_difference(set(num2))
print('A-B對稱差集為:', sorted(symmetric_difference1))
symmetric_difference2 = set(num2).symmetric_difference(set(num1))
print('B-A對稱差集為:', sorted(symmetric_difference2))

