import re
 
def read_file(filename):
    try:
      
      arr=[]
      
      #----------считать файлик html-----------
      
      f = open (filename , 'rb')
      for line in f:
        out_line=line.decode('utf8')
        arr.append(out_line)
        #print(out_line)
      
      return arr
  
    except Exception:
      print("Ошибка при обращении к файлу " + str(filename))
      return -1
    return f

 
mk=read_file("tab2(1).html")
 

#pattern4 = re.compile(r"""(?:[a-zA-Z0-9!#$%&amp;'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&amp;'*+/=?^_`{|}~-]+)*)@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9]+)?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)""")

#pattern42 = re.compile(r"""(?:[a-zA-Z0-9!#$%&amp;'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&amp;'*+/=?^_`{|}~-]+)*|"(?:[\x09\x0b\x0c\x0d\x21\x23-\x5b\x5d-\x7e]|\\[\x09\x0b\x0c\x0d])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9]+)?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|"(?:[\x09\x0b\x0c\x0d\x2d\x2e\x30-\x39\x41-\x5a\x61-\x7a]|\\[\x09\x0b\x0c])+")""")

pattern44 = re.compile(r"""(?:[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*(?:\-[a-zA-Z0-9]+)*(?:\_[a-zA-Z0-9]+)*)[a-zA-Z0-9]+@(?:[a-z]+\.)[a-z]{2,3}""")

#pattern44 = re.compile(r"""(?:[a-zA-Z0-9]+(?:[-._]?[a-zA-Z0-9]+)*)@(?:[a-z]+\.)[a-z]{2,3}""")


#pattern44 = re.compile(r"(?:[a-zA-Z0-9])+(?:[_\.\-])?(?:[a-zA-Z0-9])+\@[a-z]+\.[a-z]{2,3}");


print ("\n-------список e-mail----------")
strings = pattern44.findall(str(mk))

for string in strings:
    print (string)
 
print ("\n-----------------------")
