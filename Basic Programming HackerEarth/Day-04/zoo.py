word = input().strip()

# count number of z's and o's
z_count = word.count('z')
o_count = word.count('o')

# check the condition
if o_count == 2 * z_count:
    print("Yes")
else:
    print("No")
