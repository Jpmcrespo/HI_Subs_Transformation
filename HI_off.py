def sem_surdos():
    Input=open("input.txt", "r", encoding="utf8")
    Output= open("output.txt","w", encoding="utf8")
    apaga_tudo(Input, Output)
    Input.close()
    Output.close()

def apaga_tudo(In, Out):
    for line in In:
        if line=="\n" or 47<ord(line[0])<58:
            Out.write(line)
        else:
            new_line=check_names(line)
            new_line=check_didas(new_line)
            if new_line!="\n":    
                Out.write(new_line)

def check_names(line):
    i=0
    if ':' in line:
        while line[i]!= ":":
            i+=1
        i+=1
    return line[i:]

def check_didas(line):
    i=0
    e=0
    parenthesis= set("()[]")
    if any((c in parenthesis)for c in line):
        while line[i] not in "([" and i< len(line)-1:
            i+=1
        e=i
        while line[e] not in ")]" and e< len(line)-1:
            e+=1
        e+=1
    return line[:i] + line[e:]

        

sem_surdos()
