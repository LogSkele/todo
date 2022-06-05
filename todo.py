def deleteline(something):
  f = open('todo.txt')
  output = []
  for line in f:
    if something != line.strip():
      output.append(line)
  f.close()
  f = open('todo.txt', 'w')
  f.writelines(output)
  f.close()
try:
  f = open("todo.txt", "x")
except:
  pass
while True:
  f = open("todo.txt", "r")
  print(f.read())
  print('\n1.create\n2.delete')
  e=input('> ')
  if e=='1':
    f=open("todo.txt", "a")
    ee=input('content> ')
    f.write(f"\n{ee}")
    f.close()
  elif e=='2':
    eee=input('which todo> ')
    deleteline(eee)
