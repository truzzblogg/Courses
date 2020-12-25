# Python Exercise: Move all zeroes from a list to the end of that list.
# Rule 1: You should maintain the relative order of the non-zero elements
# Rule 2: You are not allowed to create a copy of that original list

# Method 1 - The user have to type some numbers:
# Getting user input - User type some numbers
nums = input("Enter some numbers separated by a space character: ").split(" ")
print(nums)
# Converting strings in a list to integers
nums = [int(i) for i in nums]
print(nums)

count = 0
for i in range(len(nums)):
    if (nums[i]) != 0:
        nums[count] = nums[i]
        count += 1

while (count < len(nums)):
    nums[count] = 0
    count += 1
print(nums)


# 🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️

# Method 2 - You define the original list:
nums = [44, 0, 1, 0, 22, 12, 0, 74]
count = 0
for i in range(len(nums)):
    if (nums[i]) != 0:
        nums[count] = nums[i]
        count += 1

while (count < len(nums)):
    nums[count] = 0
    count += 1
print(nums)


# 🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️🧙‍🌂♂️

# Method 3 - Using OOP:
class Zero(object):
    def moveZero(self, nums):

        count = 0
        for x in range(len(nums)):
            if (nums[x]) != 0:
                nums[count] = nums[x];
                count += 1;

        while (count < len(nums)):
            nums[count] = 0;
            count += 1;

        print(nums)

if __name__ == "__main__":
    nums = [22, 4, 10, 0, 44, 0, 2]
    Zero().moveZero(nums)