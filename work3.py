def  func(arg):
  arr = ["Element", "start"]
  for item in arg:
    arr.append(item)
  arr.append("finish")
  return arr

print(func(['hello', 5, 'John', ])) # ['Element', 'start', 'hello', 5, 'John', 'finish']


def func(list):
      a = 0
      dic ={}
      for i in list:
          a = a + 1
          dic.update({i:a})
      print(dic)
 
  list = ['x', 5, 'John',]
  dict = func(list)


def func(b):
      list1 = []
      list2 = []
      list3 = []
      list1=list(b)
      for i in list1:
          list3.append(i**2)
          if i % 2 == 0:
              list2.append(i)
 
      print(f'Список из кортежа : {list1}')
      print(f'Список с четными числами : {list2}')
      print(f'Список с числами в степени 2: {list3}')
 
  b = (1, 2, 3, 4, 5)
  func(b)
