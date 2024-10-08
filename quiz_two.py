#Variables that Stores the names of the members.
memOne = "Bryan Kenneth Sabuquel"
memTwo = "Adrian Joel Sanchez"
memThree = "Iba-o"

#Variables that Stores the Age of each member of the group.
memOneAge = 22
memTwoAge = 22
memThreeAge = 20

#Variables that contains the weekly allowance of the member of the group.
memOneAllowance = float(1000)
memTwoAllowance = float(2000)
memThreeAllowance = float(1200)

#Store the leangth of the names of the members.
memOne_name_Length = len(memOne)
memTwo_name_Length = len(memTwo)
memThree_name_Length = len(memThree)

#Perrform 4. Print the following math options for all the age and allowances:
#Addition
ageAdd_result = memOneAge + memTwoAge + memThreeAge
print(ageAdd_result)

#Subtraction
ageSub_result = memOneAge - (memTwoAge - memThreeAge)
print(ageSub_result)

#Multiplacation
ageMulti_result = memOneAge * memTwoAge * memThreeAge
allowanceMulti_result = memOneAllowance * memTwoAllowance * memThree_name_Length
print(ageMulti_result)
print(allowanceMulti_result)

#Compare Age
print(memOneAge == memTwoAge)
print(memTwoAge == memThreeAge)

#Compare length
print(memOne_name_Length == memTwo_name_Length)
print(memTwo_name_Length == memThree_name_Length)

