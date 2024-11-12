nums = [1,2,3]
print(type(nums))

nums.append(3) # adicionou o 3
nums.append(4)
nums.append(5)
print(len(nums))

nums[3] = 100 # trocou numero no indice 3
nums.insert(0,-200) # inserir no indice 0 no numero -200

print(nums[5])
print(nums[-1]) # pegar o utlimo elemento, -1 esta percorrendo de trás para frente
print(nums)