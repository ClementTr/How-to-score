#Tailleur Clément;Tazi Mehdi;B3B

#Abeilles


import random
import os
import time

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Abeille():
    def initialisation(self):
        self.x_abeille=1
        self.y_abeille=1
        

    def déplacement_x(self,A):                 #Une variable A définie aléatoirement et de façon répété tant qu'on est en phase 0
            if (A==0):                         #Si A vaut 0 l'abeille va se déplacer à gauche
                self.x_abeille-=1
                if(self.x_abeille<0):          #On maintient l'abeille dans une zone de dessin [0-20]
                    self.x_abeille+=1
            if (A==1):                         #Si A vaut 1 l'abeille va se déplacer à droite
                self.x_abeille+=1
                if(self.x_abeille>19):         #On maintient l'abeille dans la zone de dessin [0-20]
                    self.x_abeille-=1

    
    def déplacement_y(self,B):                 #Même procédé avec la variable C    
            if (B==0):
                self.y_abeille-=1              #L'abeille se déplace vers le bas
                if(self.y_abeille<0):          #On maintient l'abeille dans la zone de dessin 
                    self.y_abeille+=1
            if (B==1):
                self.y_abeille+=1              #L'abeille se déplace vers le haut
                if(self.y_abeille>19):         #On maintient l'abeille dans la zone de dessin
                    self.y_abeille-=1
                    
    def retour_maison(self,x_ruche,y_ruche):   #On a une fonction de retour, une fois la fleur trouvée
    
        if(self.x_abeille<x_ruche):            #On va compare la position de l'abeille avec celle de la ruche, jusqu'à ce qu'elles soient égales
            self.x_abeille+=1                 
        
        if(self.x_abeille>x_ruche):
            self.x_abeille-=1

        if(self.y_abeille<y_ruche):
            self.y_abeille+=1
        
        if(self.y_abeille>y_ruche):
            self.y_abeille-=1
 
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
def ajout_abeilles(abeille,x_ruche,y_ruche,nombre_abeilles):     #Fonction qui ajoute un nombre d'abeille demandé par l'utilisateur dans la zone de dessin
    for i in range(nombre_abeilles):                             #On va créer un tableau pour donner à chaque abeille des coordonnées x et y différentes
        abeille.append(Abeille())                                #On associe ce tableau à la classe à l'aide de la fonction append
        abeille[i].x_abeille=x_ruche                             #On initialise les coordonnées des abeilles à celles de la ruche pour qu'elles s'y trouvent au début
        abeille[i].y_abeille=y_ruche
        
def main():

    x_ruche=random.randint(1,19)                                 #On va créer les coordonnées de la ruche aléatoirement choisies et comprises dans la zone de dessin
    y_ruche=random.randint(1,19)

    x_fleur=random.randint(1,19)                                 #Puis on fait la même chose pour la fleur
    y_fleur=random.randint(1,19)

    action,étape,pixel=0,0,0                                     #Variables binaires 1 ou 0. action(1:abeilles dans la ruche);étape(0:recherche de la fleur)
    abeille=[]                                                   #Variable binaire 1 ou 0. Pixel(0:coordonnées où les abeilles se déplacent);abeille selon un tableau
    ligne="ligne"                                                #On initialise la valeur ligne que l'on utilisera plus tard pour l'affichage

    if (x_ruche==x_fleur and y_ruche==y_fleur):                  #On fait en sorte que la fleur ne se situe pas sur la ruche
        x_fleur=random.randint(1,19)
        y_fleur=random.randint(1,19)
                                                               
    nombre_abeilles=int(input("Combien d'abeilles voulez vous afficher ? ")) #L'utilisateur rentre un nombre d'abeille                    
    ajout_abeilles(abeille,x_ruche,y_ruche,nombre_abeilles)      #On appelle la fonction ajout_abeilles qui va créer n fois la même abeille initiale

    while(action<nombre_abeilles):                               #Tant que les abeilles ne sont pas dans la ruche, cherchent (étape0) ou ont trouvé la fleur (étape1)            
        time.sleep(1/70)                                         #Représente la vitesse des abeilles en seconde
        action=0                                                 
        if(étape==0):        
            for i in range(nombre_abeilles):
                A=random.randint(0,1)                            #Variable aléatoire créée pour le déplacement droite/gauche 
                B=random.randint(0,1)                            #Variable aléatoire créée pour le déplacement haut/bas
                C=random.randint(0,1)                        
                if(C==0):                                        #La variable C sert à choisir aléatoirement un déplacement horizontal ou vertical 
                    abeille[i].déplacement_x(A)
                else: 
                    abeille[i].déplacement_y(B)
        for i in range(nombre_abeilles):
            if(abeille[i].x_abeille==x_fleur and abeille[i].y_abeille==y_fleur): #Quand une abeille i trouve la fleur, on passe à l'étape 1(retour maison) 
                étape=1                                           
        if (étape==1):                                         
            for i in range(nombre_abeilles):
                abeille[i].retour_maison(x_ruche,y_ruche)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
        os.system('cls' if os.name == 'nt' else 'clear')                                   
        for y in range (20) :                                                              #On va parcourir la zone de dessin en ordonnées(y) et en abscisses(x)
            for x in range (20):                                                           
                if (x_fleur==x and y_fleur==y):                                            #Quand on arrive aux coordonnées de la fleur on met un 'O'
                    ligne += "O" 
                    pixel = 1                                                              #Quand pixel=1 <-> la coordonnée est "bloquée"                                                          
                elif (x_ruche==x and y_ruche==y):                                          #Quand on arrive aux coordonnées de la ruche, on met un '#'
                     ligne += "#" 
                     pixel = 1                                                             
                for i in range(nombre_abeilles):                                           #On va parcourir les toutes les abeilles 1 à 1
                    if (abeille[i].x_abeille==x and abeille[i].y_abeille==y and pixel==0): #Si elle est sur une coordonnée "non bloquée", on l'affiche (-)
                        ligne += "-" 
                        pixel = 1                                                          #Puis on bloque sa coordonnée
                if (pixel==0) :                                                            #Les autres pixels non bloqué sont représentés par " "
                    ligne += " "
                pixel=0
            ligne += "|"                                                                   #On affiche le coté droit
            print (ligne)                                                                  #On affichage la ligne 
            ligne="|"                                                                      #Puis on réinitialise la ligne à "|" pour la boucle for
        for i in range(nombre_abeilles):                                          
            if(abeille[i].x_abeille==x_ruche and abeille[i].y_abeille==y_ruche and étape==1):#On va parcourir les abeilles 1 à 1
                action+=1                                                                  #Si une abeille est dans la ruche après avoir trouvé la fleur (étape1)
        if (action==1):                                                                
            print("La fleur a été trouvée !")                                        
            os.system("pause")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
main()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
