import random
 
def t_num_tahdid(status): # tahdid ha ra moshkhas mokonad
  num_tahdid = 0;
  for col1 in range(0, 7):
    for col2 in range(col1+1, 8):
       if (status[col1] == status[col2]) or ((col2 - col1) == abs(status[col1] - status[col2])) : #teen hamle
        num_tahdid += 1;
  return 28 - num_tahdid #hamle be yekdigar nist
 
def valed(all_status, tanaghos_num):  #gerftan valed ha 
  entekhab_valed = random.randint(0, sum(tanaghos_num) - 1)
  if entekhab_valed < tanaghos_num[0]:
    return all_status[0]
  elif entekhab_valed >= tanaghos_num[0] and entekhab_valed < (tanaghos_num[0] + tanaghos_num[1]):
    return all_status[1]
  elif entekhab_valed >= (tanaghos_num[0] + tanaghos_num[1]) and entekhab_valed < (tanaghos_num[0] + tanaghos_num[1] + tanaghos_num[2]):
    return all_status[2]
  return all_status[3]
 
 
def jahesh(all_status):  #jahesh
  for i in range(0, 4):
    col = random.randint(0, 7)
    row = random.randint(0, 7)
    all_status[i][col] = row
  return all_status
 
def inheritance(all_status):  #tabdil
  tanaghos_num = []
  new_all_status = []
  for i in range(0, 4):
    tanaghos_num.append(t_num_tahdid(all_status[i]))
  for t in range(0, 2): #do farzand tolid mikonad 
    father = valed(all_status, tanaghos_num);
    mother = valed(all_status, tanaghos_num);
    while father == mother:
      mother = valed(all_status, tanaghos_num);
    first_child = father[:]
    second_child = mother[:]
    num = random.randint(0, 6)  #add 0 add moshtarek baray marz farzandan
    for i in range(0, num+1):
      first_child[i] = second_child[i]
      second_child[i] = father[i]
    new_all_status.append(first_child)
    new_all_status.append(second_child)
  return new_all_status #bazgasht be tolid
 
def find_answer(all_status): #mosabeghe ghabel hal ast ya na 
  for i in range(0, 4):
    if t_num_tahdid(all_status[i]) == 28:
      print("find a answer:")
      print(all_status[i])
      return True
  return False
 
 
all_status = []
for i in range(0, 4):  #4 ta halat dorost mikonad 
  status = [0, 0, 0, 0, 0, 0, 0, 0]
  for col in range(0, 8):
    row = random.randint(0, 7)
    status[col] = row
  all_status.append(status)


print("4 ta valed hastand: ")
print(all_status)
all_status = inheritance(all_status) #joft giri
while find_answer(all_status) == False:  #farzand matlob ro peyda nakard
  che_jaheshi = random.randint(1, 10) #10 dar saehtemal taghiir
  if che_jaheshi == 1:
    #print("have a jahesh,and the all_status:")
    all_status = jahesh(all_status)
    #print(all_status)
  else:
    all_status = inheritance(all_status)
   # print("the next all_status: ")
   # print(all_status)
