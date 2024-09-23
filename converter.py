a=int(input('Введите число...'))
b=int(input('В какую СС необходимо перевести?'))
if b<2:
    print('Данная СС не существует...')
else:
    nums=[a]
    ends=[]
    sum = ''
    while nums[len(nums)-1]>=b:
        nums.append(nums[len(nums)-1]//b)
        ends.append(nums[len(nums)-2]%b)
    ends=ends[::-1]
    sum+=str(nums[len(nums)-1])
    for i in range(len(ends)):
        sum+=str(ends[i])
    print(f'Число в {b}-ной системе:',sum)
