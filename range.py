print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))


*/output:
range(5): 
0
1
2
3
4
range(0,5): 
0
1
2
3
4
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
