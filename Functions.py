from pygame import mixer
import os

class Functions:
    def __init__(self, tokens, token, i, ListOfVars):
        self.tokens = tokens
        self.token = token
        self.i = i
        self.ListOfVars = ListOfVars
        
        
    def isvar(self, d):
        for i, var in enumerate(self.ListOfVars):
            if(d == var[0]):
                return True, var[1]
        return None, None

    
    def Print(self):
        if self.token == "print" and len(self.tokens) == 2:
            ToPrint = self.tokens[self.i+1][1:-1]
            if self.tokens[self.i+1][0] == "'" and self.tokens[self.i+1][len(self.tokens[self.i+1]) - 1] == "'":
                print(ToPrint)
            elif self.tokens[self.i+1][0] == '"' and self.tokens[self.i+1][len(self.tokens[self.i+1]) - 1] == '"':
                print(ToPrint)
            else:
                S, D = self.isvar(self.tokens[self.i+1])
                if S:
                    print(D[1:-1])
    
    def Play(self):
        if self.token == "play" and len(self.tokens) == 2 or self.token == "play" and len(self.tokens) == 3:
                if self.tokens[self.i+1][0] == "'" and self.tokens[self.i+1][len(self.tokens[self.i+1]) - 1] == "'":
                    if(len(self.tokens) > 2):
                        if(self.tokens[self.i+2][1:-1] == "1" and self.tokens[self.i+2][1:-1] == "1"):
                            mixer.music.load(self.tokens[self.i+1][1:-1])
                            mixer.music.play(loops=-1) 
                    else:
                        mixer.music.load(self.tokens[self.i+1][1:-1])
                        mixer.music.play()   

                elif self.tokens[self.i+1][0] == '"' and self.tokens[self.i+1][len(self.tokens[self.i+1]) - 1] == '"':
                    if(len(self.tokens) > 2 and self.tokens[self.i+2][1:-1] == "1"):
                        mixer.music.load(self.tokens[self.i+1][1:-1])
                        mixer.music.play(loops=-1)   
                    else:
                        mixer.music.load(self.tokens[self.i+1][1:-1])
                        mixer.music.play()
                else:
                    S, D = self.isvar(self.tokens[self.i+1])
                    if(S):
                        if(len(self.tokens) > 2):
                            S2, D2 = self.isvar(self.tokens[self.i+2])
                            if(self.tokens[self.i+2][1:-1] == "1.0"):
                                mixer.music.load(D[1:-1])
                                mixer.music.play(loops=-1)   
                            elif(S2 and D2[1:-1] == "1.0"):
                                if(len(self.tokens) > 2 and D2[1:-1] == "1.0"):
                                    mixer.music.load(D[1:-1])
                                    mixer.music.play(loops=-1)
                            else:
                                mixer.music.load(D[1:-1])
                                mixer.music.play()
                        else:
                            mixer.music.load(D[1:-1])
                            mixer.music.play()
                    else:
                        S2, D2 = self.isvar(self.tokens[self.i+2])
                        if(len(self.tokens) > 2 and self.tokens[self.i+2][1:-1] == "1.0"):
                            mixer.music.load(D[1:-1])
                            mixer.music.play(loops=-1)   
                        elif(S2 and D2[1:-1] == "1.0"):
                            if(len(self.tokens) > 2 and D2[1:-1] == "1.0"):
                                mixer.music.load(D[1:-1])
                                mixer.music.play(loops=-1)
                        else:
                            mixer.music.load(D[1:-1])
                            mixer.music.play()
                                
                        
                        
    def Stop(self):
        if self.token == "stop" and len(self.tokens) == 1:
            mixer.music.pause()
            

            
    def Cls(self):
        if self.token == "cls" and len(self.tokens) == 1:
            os.system("cls")
            
            
    def Exit(self):
        if self.token == "exit" and len(self.tokens) == 1:
            os.system("cls")
            exit()
            
 
            
