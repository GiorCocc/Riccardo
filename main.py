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
def FCFS(processi):
  orderbypid(processi)

  media = 0
  for i in range(len(processi)):
    if i != 0:
      media += processi[i-1].getBurstTime()
      print("- processo "+processi[i].getPID()+" con burst time:"+processi[i-1].getBurstTime()+"\n")
  media = media/len(processi)
  return media # Ritorna il tempo medio di esecuzione
def orderbypriority(processi):
    processi.sort(key=lambda x: x.getPriority()) # Ordina i processi in base alla priorità
def orderbybursttime(processi):
    processi.sort(key=lambda x: x.getBurstTime()) # Ordina i processi in base al tempo di esecuzione

def Priority(processi):
  media = 0
  orderbypriority(processi)
  for i in range(len(processi)):
    if i != 0:
      print("- processo "+processi[i].getPID()+" con burst time:"+processi[i-1].getBurstTime()+"\n")
      media += processi[i-1].getBurstTime()
  media = media/len(processi)
  return media # Ritorna il tempo medio di esecuzione
def orderbypid(processi):
    processi.sort(key=lambda x: x.getPID()) # Ordina i processi in base al PID
def SJF(processi):
  media = 0
  orderbybursttime(processi)
  for i in range(len(processi)):
    if i != 0:
      print("- processo "+processi[i].getPID()+" con burst time:"+processi[i-1].getBurstTime()+"\n")
      media += processi[i-1].getBurstTime()
  media = media/len(processi)
  return media # Ritorna il tempo medio di esecuzione



def main():
    # Definizione delle variabili
    processi = []

    # Lettura del file
    file = open("test.txt", "r")
    for line in file:
        line = line.split()
        processi.append(Processo(int(line[0]), int(line[1]), int(line[2])))
    file.close()
    print
    
    

