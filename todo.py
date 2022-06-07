try:f=open("todo.txt", "x")
except:pass
while True:
  with open("todo.txt", "rt") as f:
    print(f.read())
    print('\n1.create\n2.delete')
    e=input('> ')
    if e=='1':
      with open("todo.txt", "at") as f:
        ee=input('content> ')
        f.write(f"\n{ee}")
    elif e=='2':
      eee=input('which todo> ')
      with open("todo.txt", "rt") as f:
        output=[]
        for line in f:
          if eee != line.strip():
            output.append(line)
      with open("todo.txt", "wt") as f:f.writelines(output)
