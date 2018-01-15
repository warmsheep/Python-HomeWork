iphone7 = ['Jane','Elle','Dinli','Dragon','Alex']
iphone8 = ['Paul','Susan','Elle','Jane']
A = set(iphone7)
B = set(iphone8)
A.symmetric_difference_update(B)
print(A)