nums = input()
for i in range(2**3):
  binary=format(i, 'b').zfill(5)[2:]
  val = int(nums[0])
  val_str = nums[0]
  for j in range(1,len(nums)):
    if binary[j-1] == '1':
      val += int(nums[j])
      val_str += '+'+nums[j]
    else:
      val -= int(nums[j])
      val_str += '-'+nums[j]
  if val==7:
    print(val_str,'=7',sep='')
    break
