res = {}
trace=[]
newBF_FirstCheck=[]
newBF_FinalCheck=[]
BF=[]
class File ():
    def __init__(self,arg):
        self.arg=arg
    def read(self):
        global res
        i=1
        hashtable={}
        with open(self.arg,"r") as text:
            for line in text:
                key, value = line.split("->", 1)
                res["R"+str(i)] = key+" "+value.replace('\n','', 1)
                i=i+1
                
        return res
    def chainage_avant(self,BF,Fait):
        res=self.read()
        print("Votre base de connaissance initialle")
        print(res)
        if Fait in BF:
            return "false"
        else:
            global newBF_FinalCheck
            newBF_FinalCheck=File.first_choice_avant(self,BF,Fait)
            
            while Fait not in newBF_FinalCheck and res!={}:
                
                print("****************************")
                print("\n")
                lastFait=newBF_FinalCheck[-1]
                print("le nouveau fait a ajouté dans la base : "+lastFait)
                BDA={}
                for key in res:
                    h=res.get(key)
                    s,y=h.split(" ")
                    z=s.split(",")
                    print("la régle : "+key)
                    print(z)
                    k=0
                    
                    
                    if lastFait in z:
                        for val in newBF_FinalCheck:
                            if val in z:
                                k=k+1
                        BDA[key]=k
                        
                        print(BDA)
                
                ss=max(BDA,key=BDA.get)
                print("la règle séléctionnéé : "+ss)
                restleft=None
                for key in res:
                    if ss==key:
                        restleft=res.get(ss)
                oldFait,newFait=restleft.split(" ")
                if newFait not in newBF_FinalCheck:
                    newBF_FinalCheck.append(newFait)
                print("BF après changement : ")
                print(newBF_FinalCheck)
                global trace
                trace.append(ss)
                print("trace d'exécution : ")
                print(trace)
                del res[ss]
                print("Base de connaissance après changement : ")
                print(res)
                                
            
            
            
    def first_choice_avant(self,BF,Fait):
            BDA={}
            global trace
            if Fait in BF:
                return "False"
            else:
                #while Fait not in BF and res!={}:
                for key in res:
                    h=res.get(key)
                    s,y=h.split(" ")
                    z=s.split(",")
                    print(z)
                    k=0
                    for val in BF:
                        if val in z:
                            k=k+1
                    BDA[key]=k
                    print(BDA)
                    print("\n")
                ss=max(BDA,key=BDA.get)
                print("la règle séléctionnéé : "+ss)
            
                restleft=None
                for key in res:
                    if ss==key:
                        restleft=res.get(ss)
                oldFait,newFait=restleft.split(" ")
                BF.append(newFait)
                global newBF
                newBF=BF
                print("BF après changement : ")
                print(newBF)
                global trace
                trace=[ss]
                print("trace d'exécution : ")
                print(trace)
                del res[ss]
                print("Base de connaissance après changement : ")
                print(res)
                return newBF
    def chainage_arriere(self,Fait):
            global res
            res=self.read()
            print("Votre base de connaissance initialle")
            print(res)
            print("\n")
            while res!={}:
                ha=File.firstarriere(self,Fait)
                for val in ha:
                        
                        ha=File.firstarriere(self,val)
                        for i in ha:
                                za=File.firstarriere(self,i)
                                print(za)
                print(ha)
                
    def firstarriere(self,Fait):
            global res
            for key in list(res.keys()):
                h=res.get(key)
                s,y=h.split(" ")
                if Fait==y:
                        z=s.split(",")
                        print(Fait)
                        print(z)
                        trace.append(key)
                        print("trace d'exécution :")
                        print(trace)
                        print("\n")
                        del res[key]
                        print("Base de connaissance après changement : ")
                        print(res)
                        print("\n")
                        return z

    def interface_user(self):
        maxLengthList=0
        while 1:
                print ("Voulez vos faire un chainage avant ou arriere (1,2) ? exit 0")
                choix =-1 # cchoix de l'utilisateur
                entree = "" # l'entree de l'utilisateur
                while choix >2 or choix <0 :
                        choix = int(input())
                        if choix >2 or choix <0:
                                print ("votre choix hors [0-2]")
                if choix ==1 :
                    print("Veuillez saisir la taille de votre  base de faits initial")
                    maxLengthList=int(input())
                    global BF
                    while len(BF)<maxLengthList:
                            print("Veuillez saisir vos faits")
                            entree=input()
                            BF.append(entree)
                    print("Votre Base de faits initialle :")
                    print(BF)
                    print("Veuillez saisir le fait à démontrer :")
                    Fait=input()
                    File.chainage_avant(self,BF,Fait)
                    if Fait in BF:
                        print(Fait+" établi :Succès")
                    else:
                        print("Echec")
                elif choix==2:
                    print("Veuillez saisir le fait à démontrer :")
                    Fait=input()
                    File.chainage_arriere(self,Fait)
                else:
                    exit(0)
		
                           
        
