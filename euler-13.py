# large sum
f = open("n13.txt", "r")
strs = f.readlines()

nums = [int(n[0:12]) for n in strs]
print(str(sum(nums))[0:10])