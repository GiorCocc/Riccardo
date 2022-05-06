


from multiprocessing import Queue


class Processo:
    def __init__(self,pid, burstTime, priority):
        self.pid = pid
        self.burstTime = burstTime
        self.priority = priority
    def getPID(self):
        return self.pid
    def getBurstTime(self):
        return self.burstTime
    def getPriority(self):
        return self.priority
    def setBurstTime(self, burstTime):
        self.burstTime = burstTime
    def stampa(self):
      print(f"{self.getPID()} con burstTime {self.getBurstTime()} e priorità {self.getPriority()}")
def orderbypriority(processi):
    processi.sort(key=lambda x: x.getPriority()) # Ordina i processi in base alla priorità
def orderbybursttime(processi):
    processi.sort(key=lambda x: x.getBurstTime()) # Ordina i processi in base al tempo di esecuzione
def orderbypid(processi):
    processi.sort(key=lambda x: x.getPID()) # Ordina i processi in base al PID    
class RRPID:
  def __init__(self,pid, num):
    self.pid = pid
    self.num = num
  def getPID(self):
    return self.pid
  def getNum(self):
    return self.num
  def setPID():
    self.pid = pid
  def setNum():
    self.num = num

def RR(processi):
  rr = []
  tmpPID=[]
  bt = 0
  tot = 0
  for i in range(len(processi)):
    rr.append(processi[i])
    tmp = RRPID(processi[i].getPID(),0)
    tmpPID.append(tmp)
    print(f"- processo {rr[i].getPID()} con burst time: {rr[i].getBurstTime()}")
  print("\n")
  i=0
  while len(rr) != 0:
    if  rr[i].getBurstTime() <= 10 :
      for i in range(len(tmpPID)):
        if tmpPID[i].getPID() == rr[i].getPID():
          bt -= 10*tmpPID[i].getNum()
      print(f"- processo {rr[i].getPID()} con burst time: {bt}")
      bt+=rr[i].getBurstTime()
      tot+=bt
      rr.pop(i)
    elif rr[i].getBurstTime() >= 10 : 
      bt+=10
      remain = rr[i].getBurstTime()- 10
      for p in range(len(tmpPID)):
        if tmpPID[p].getPID() == rr[i].getPID():
          tmpPID[p].setNum = tmpPID[p].getNum()+1
      rr.append(Processo(rr[i].getPID(),remain,rr[i].getPriority()))
      rr.pop(i) 
       
  media = tot/len(processi)
  return media # Ritorna il tempo medio di esecuzione


def FCFS(processi):
  orderbypid(processi)

  bt = 0
  tot = 0
  for i in range(len(processi)):
    if i != 0:
      bt += processi[i-1].getBurstTime()
      tot += bt
      print(f"- processo {processi[i].getPID()} con burst time: {tot}")
    else:
      print(f"- processo {processi[i].getPID()} con burst time: 0 ")
  
  media = tot/len(processi)
  return media # Ritorna il tempo medio di esecuzione

def Priority(processi):
  bt = 0
  tot = 0
  orderbypriority(processi)
  for i in range(len(processi)):
    if i != 0:
      bt += processi[i-1].getBurstTime()
      tot += bt
      print(f"- processo {processi[i].getPID()} con burst time: {tot} ")
    else:
      print(f"- processo {processi[i].getPID()} con burst time: 0 ")
  
  media = tot/len(processi)
  return media # Ritorna il tempo medio di esecuzione


def SJF(processi):
  bt = 0
  tot = 0
  orderbybursttime(processi)
  for i in range(len(processi)):
    if i != 0:
      bt += processi[i-1].getBurstTime()
      tot += bt
      print(f"- processo {processi[i].getPID()} con burst time: {tot}")
    else:
      print(f"- processo {processi[i].getPID()} con burst time: 0")

  media = tot/len(processi)
  return tot # Ritorna il tempo medio di esecuzione
def menu():
  print("\n")
  print("----MENU'----")
  print("(1) FCFS : First Come First Served")
  print("(2) SJF : Short Job Served")
  print("(3) Priority: Priority order")
  print("(4) RR: Round Robin")
  print("(0) exit")
  print("\n")

def main():
    
    # Definizione delle variabili
    processArray = []
    # Lettura del file
    with open("test.txt","r") as txt:
      for line in txt:
        pid,burst,pr = line.split()
        numB = int(burst)
        numP = int(pr)
        temp = Processo(pid,numB,numP)
        processArray.append(temp)

    for i in range(len(processArray)):
      processArray[i].stampa()
    
    print("\n")
    menu()
    var = (int(input("Scegli un ordinamento : ")))
    
    while var != 0 :
      if var == 1:
        print(f"           ottengo una media di attesa di {FCFS(processArray)}")
      elif var == 2:
        print(f"           ottengo una media di attesa di {SJF(processArray)}")
      elif var ==3:
        print(f"           ottengo una media di attesa di {Priority(processArray)}")
      elif var ==4:
        print(f"           ottengo una media di attesa di {RR(processArray)}")
      menu()
      var= (int(input("scegli un ordinamento : ")))

main()    
  
    
    

