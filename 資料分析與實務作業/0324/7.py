Math = ['Peter', 'Norton', 'Kevin', 'Mary', 'John', 'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom']
Computer = ['Curry', 'James', 'Mary', 'Turisa', 'Tracy', 'Judy', 'Lee', 'Jarmul', 'Damon', 'Ivan']
Physics = ['Eric', 'Lee', 'Kevin', 'Mary', 'Christy', 'Josh', 'Nelson', 'Kazil', 'Linda', 'Tom']
intersection1 = set(Math).intersection(Computer, Physics)
print('同時參加3個夏令營的名單:', intersection1)
intersection2 = set(Math).intersection(Computer)
print('同時參加Math與Computer夏令營的名單:', intersection2)
intersection3 = set(Math).intersection(Physics)
print('同時參加Math與Physics夏令營的名單:', intersection3)
intersection4 = set(Physics).intersection(Computer)
print('同時參加Physics與Computer夏令營的名單:', intersection4)
