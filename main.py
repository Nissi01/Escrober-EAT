#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from random import*
import sqlite3
from flask import render_template, Flask, request
from RecupChoix import RecupBK,RecupMBK,Recup2,RecupMcdo,RecupMMcdo,RecupPiz,RecupMPiz
app = Flask(__name__) # Création de l'application

@app.route('/',methods = ['GET','POST']) # O
def index():

    return render_template("home.html")

@app.route('/Principal',methods = ['GET','POST']) # Ici on précise la méthode d'envoi des données (GET ou POST)
def Accueil():
    if request.method == 'POST' and 'Pseudo' in request.form and 'Adresse' in request.form: 
        pseudo = request.form['Pseudo']
        Adresse = request.form['Adresse']
        
        try:
            connexion = sqlite3.connect("info.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\info.db")
    ## Fin essai
        connexion.execute(f"DELETE FROM Client")#Afin de s'assurer qu'il y à bien qu'un seul utilisateur dans la base de donner
        connexion.execute(f"INSERT INTO Client(Utilisateur,Adresse) VALUES ('{pseudo}','{Adresse}')")
        connexion.commit()
        connexion.close()# On récupère le résultat de la requête sous forme de dictionnaire
    return render_template("Hub.html")








@app.route('/BurgerK',methods = ['GET','POST'])
def BurgerKing():
   
    Message=""#Cette variable texte à pour but d'etre modifier si l'une des 3 condition(Il manque un plat/accompagnement/boisson) est presente.Elle est initialement vide afin de ne pas etre vue lorsqu'il n'y à pas de problème
    
    
    #Ce "if" vérifie si les 3 options or celle du menu (d'ou leurs noms, "solo" ) ne sont pas concerner afin d'etre sur que c'est bel et bien un menu qui est demander par le client et non un produit seul.
    if request.method == 'POST' and 'solo' not in request.form and 'solo1' not in request.form and 'solo2' not in request.form and 'vide' not in request.form :
       #On prend ici les 3 composante d'un Menu selon la table SQL (Principal,Accompagnement,Boisson)
        Bois = request.form['Boisson'] 
        Acc= request.form['Accompagnement']
        Pri= request.form['Principal']
        
        
        #Cette vérification et les 2 autres qui suivent correspond champ rentrer initialement dans les choix possibles, leurs présence signifie donc que le client n'a donc rien choisis.
        if Pri == "--Veillez choisir un Plat Principale--":#Le but ici est de recréé la page en changeant la variable Message qui s'affichera signaler le problème.
            Message="IL MANQUE UN PLAT*"
            Princi=RecupBK("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupBK("Accompagnement")
            Boiss=RecupBK("Boisson")
            menu=RecupBK("Menu")
            Panier= RecupBK("Panier")
            NbrPanier = RecupMBK("Panier")
            return render_template("BurgerKing/BurgerK.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
            
        if Acc == "--Veillez choisir un Accompagnrment--":
            
            Message="IL MANQUE UN ACCOMPAGNEMENT*"
            Princi=RecupBK("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupBK("Accompagnement")
            Boiss=RecupBK("Boisson")
            menu=RecupBK("Menu")
            Panier= RecupBK("Panier")
            NbrPanier = RecupMBK("Panier")
            return render_template("BurgerKing/BurgerK.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
      
        if Bois == "--Veillez choisir une Boisson--":
            Message="IL MANQUE UNE BOISSON*"
            Princi=RecupBK("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupBK("Accompagnement")
            Boiss=RecupBK("Boisson")
            menu=RecupBK("Menu")
            Panier= RecupBK("Panier")
            NbrPanier = RecupMBK("Panier")
            return render_template("BurgerKing/BurgerK.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
        #Cette variable "txt" est un moyen que j'utilise afin de conserver le menu sous "une seul forme" et de pouvoir ainsi plus aisément le rentrer dans le panier
        txt=""
        txt+= "Menu : "+str(Pri)+" || "+str(Acc)+" || "+str(Bois)
          
        try:
            connexion = sqlite3.connect("RestoBK.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
    ## Fin essai
        connexion.execute(f"INSERT into Menu (Principal,Accompagnement,Boisson) VALUES('{Pri}','{Acc}','{Bois}')")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{txt}')")
        connexion.commit()
        connexion.close()
    #Parfois lors d'une commande on souhaite prendre quelque supplement, c'est le but ici des "solo" qui permet d'ajouter au panier certain composant d'un menu sans forcement en prendre un.    
    if request.method == 'POST' and 'solo' in request.form :
        SoloPri=request.form['bobo']
        try:
            connexion = sqlite3.connect("RestoBK.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloPri}')")
        connexion.commit()
        connexion.close()
        
    if request.method == 'POST' and 'solo1' in request.form :
        SoloAcc=request.form['bobo1']
        try:
            connexion = sqlite3.connect("RestoBK.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloAcc}')")
        connexion.commit()
        connexion.close()
    
    if request.method == 'POST' and 'solo2' in request.form :
        SoloBoi=request.form['bobo2']
        try:
            connexion = sqlite3.connect("RestoBK.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloBoi}')")
        connexion.commit()
        connexion.close()
    #Vide comme son nom l'indique à pour but de vider le panier si le client le souhaite. J'efface donc dans un premier temps la table "panier" puis "Menu" car le "panier" ne fait que retranscrire le "Menu".
    if request.method == 'POST' and 'vide' in request.form :
        try:
            connexion = sqlite3.connect("RestoBK.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
        connexion.execute(f"DELETE FROM Panier")
        connexion.execute(f"DELETE FROM Menu")
        connexion.commit()
        connexion.close()
        
    #La fonction Recup est tirée de la page RecupChoix(Explication la bas)  
    Princi=RecupBK("Principal")
    
    Accomp=RecupBK("Accompagnement")
    
    Boiss=RecupBK("Boisson")
    
    menu=RecupBK("Menu")
    
    Panier= RecupBK("Panier")
    NbrPanier = RecupMBK("Panier")
    #Je retourne ainsi tout les variable utile a ma page Html + la variable message (modifier ou non)
    
    return render_template("BurgerKing/BurgerK.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message2=Message,NbrPanier=NbrPanier)

@app.route('/ValiderBK',methods = ['GET','POST'])
def BurgerKingV():

    try:
        connexion = sqlite3.connect("RestoBK.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
    
    #Une récuperation séparer des éléments du panier car les Prix sont evidemment different dans le cas d'un Menu ou d'un element seul.
    Nbr=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu Not LIKE '%Menu%'")
    Nbr1=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE '%Menu%'")
    
    #Sous forme de liste car les info ne sont pas utilisable autrement
    Autre=list(Nbr)
    Menu=list(Nbr1)
   
    valeurFinal=0
    ValeurMenu=int(Menu[0][0])*9.99
    ValeurAutre=int(Autre[0][0])*4.99
    

    
    valeurFinal=ValeurMenu+ValeurAutre
    connexion.commit()
    connexion.close()
    Panier= RecupBK("Panier")
        
    return render_template("BurgerKing/ValiderBK.html",aa=valeurFinal,Panier=Panier)




#Mcdo________________________________________________________________________________________


@app.route('/Mcdo',methods = ['GET','POST'])
def Mcdo():
   
    Message=""#Cette variable texte à pour but d'etre modifier si l'une des 3 condition(Il manque un plat/accompagnement/boisson) est presente.Elle est initialement vide afin de ne pas etre vue lorsqu'il n'y à pas de problème
    
    
    #Ce "if" vérifie si les 3 options or celle du menu (d'ou leurs noms, "solo" ) ne sont pas concerner afin d'etre sur que c'est bel et bien un menu qui est demander par le client et non un produit seul.
    if request.method == 'POST' and 'solo' not in request.form and 'solo1' not in request.form and 'solo2' not in request.form and 'vide' not in request.form :
       #On prend ici les 3 composante d'un Menu selon la table SQL (Principal,Accompagnement,Boisson)
        Bois = request.form['Boisson'] 
        Acc= request.form['Accompagnement']
        Pri= request.form['Principal']
        
        
        #Cette vérification et les 2 autres qui suivent correspond champ rentrer initialement dans les choix possibles, leurs présence signifie donc que le client n'a donc rien choisis.
        if Pri == "--Veillez choisir un Plat Principale--":#Le but ici est de recréé la page en changeant la variable Message qui s'affichera signaler le problème.
            Message="IL MANQUE UN PLAT*"
            Princi=RecupMcdo("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupMcdo("Accompagnement")
            Boiss=RecupMcdo("Boisson")
            menu=RecupMcdo("Menu")
            Panier= RecupMcdo("Panier")
            NbrPanier = RecupMMcdo("Panier")
            return render_template("Mcdo/Mcdo.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
            
        if Acc == "--Veillez choisir un Accompagnrment--":
            
            Message="IL MANQUE UN ACCOMPAGNEMENT*"
            Princi=RecupMcdo("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupMcdo("Accompagnement")
            Boiss=RecupMcdo("Boisson")
            menu=RecupMcdo("Menu")
            Panier= RecupMcdo("Panier")
            NbrPanier = RecupMMcdo("Panier")
            return render_template("Mcdo/Mcdo.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
      
        if Bois == "--Veillez choisir une Boisson--":
            Message="IL MANQUE UNE BOISSON*"
            Princi=RecupMcdo("Principal")#La fonction Recup est tirée de la page RecupChoix(Explication la bas)
            Accomp=RecupMcdo("Accompagnement")
            Boiss=RecupMcdo("Boisson")
            menu=RecupMcdo("Menu")
            Panier= RecupMcdo("Panier")
            NbrPanier = RecupMMcdo("Panier")
            return render_template("Mcdo/Mcdo.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
        #Cette variable "txt" est un moyen que j'utilise afin de conserver le menu sous "une seul forme" et de pouvoir ainsi plus aisément le rentrer dans le panier
        txt=""
        txt+= "Menu : "+str(Pri)+" || "+str(Acc)+" || "+str(Bois)
          
        try:
            connexion = sqlite3.connect("RestoMcdo.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
        connexion.execute(f"INSERT into Menu (Principal,Accompagnement,Boisson) VALUES('{Pri}','{Acc}','{Bois}')")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{txt}')")
        connexion.commit()
        connexion.close()
    #Parfois lors d'une commande on souhaite prendre quelque supplement, c'est le but ici des "solo" qui permet d'ajouter au panier certain composant d'un menu sans forcement en prendre un.    
    if request.method == 'POST' and 'solo' in request.form :
        SoloPri=request.form['bobo']
        try:
            connexion = sqlite3.connect("RestoMcdo.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloPri}')")
        connexion.commit()
        connexion.close()
        
    if request.method == 'POST' and 'solo1' in request.form :
        SoloAcc=request.form['bobo1']
        try:
            connexion = sqlite3.connect("RestoMcdo.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloAcc}')")
        connexion.commit()
        connexion.close()
    
    if request.method == 'POST' and 'solo2' in request.form :
        SoloBoi=request.form['bobo2']
        try:
            connexion = sqlite3.connect("RestoMcdo.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloBoi}')")
        connexion.commit()
        connexion.close()
    #Vide comme son nom l'indique à pour but de vider le panier si le client le souhaite. J'efface donc dans un premier temps la table "panier" puis "Menu" car le "panier" ne fait que retranscrire le "Menu".
    if request.method == 'POST' and 'vide' in request.form :
        try:
            connexion = sqlite3.connect("RestoMcdo.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
        connexion.execute(f"DELETE FROM Panier")
        connexion.execute(f"DELETE FROM Menu")
        connexion.commit()
        connexion.close()
        
    #La fonction Recup est tirée de la page RecupChoix(Explication la bas)  
    Princi=RecupMcdo("Principal")
    
    Accomp=RecupMcdo("Accompagnement")
    
    Boiss=RecupMcdo("Boisson")
    
    menu=RecupMcdo("Menu")
    
    Panier= RecupMcdo("Panier")
    NbrPanier = RecupMMcdo("Panier")
    #Je retourne ainsi tout les variable utile a ma page Html + la variable message (modifier ou non)
    
    return render_template("Mcdo/Mcdo.html",Princip=Princi,Acco=Accomp,Boi=Boiss,Menu=menu,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)

@app.route('/ValiderMcdo',methods = ['GET','POST'])
def McdoV():

    try:
        connexion = sqlite3.connect("RestoMcdo.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
    
    #Une récuperation séparer des éléments du panier car les Prix sont evidemment different dans le cas d'un Menu ou d'un element seul.
    Nbr=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu Not LIKE '%Menu%'")
    Nbr1=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE '%Menu%'")
    
    #Sous forme de liste car les info ne sont pas utilisable autrement
    Autre=list(Nbr)
    Menu=list(Nbr1)
   
    valeurFinal=0
    ValeurMenu=int(Menu[0][0])*9.99
    ValeurAutre=int(Autre[0][0])*4.99
    

    
    valeurFinal=ValeurMenu+ValeurAutre
    connexion.commit()
    connexion.close()
    Panier= RecupMcdo("Panier")
        
    return render_template("Mcdo/ValiderMcdo.html",aa=valeurFinal,Panier=Panier)


#PizzaHut__________________________________________________________________
@app.route('/PizzaHut',methods = ['GET','POST'])
def Pizza():
    Message=""#Cette variable texte à pour but d'etre modifier si l'une des 3 condition(Il manque un plat/accompagnement/boisson) est presente.Elle est initialement vide afin de ne pas etre vue lorsqu'il n'y à pas de problème
    #PS:Je n'utilise pas cette technique exprès pour la pizza perso (ligne 454) car ne mettre aucun condiment dans sa Pizza représente aussi un choix de l'utilisateur
    
    #Ce "if" vérifie si les 3 options or celle du menu (d'ou leurs noms, "solo" ) ne sont pas concerner afin d'etre sur que c'est bel et bien un menu qui est demander par le client et non un produit seul.
    if request.method == 'POST' and 'solo' not in request.form and 'solo1' not in request.form and 'solo2' not in request.form and 'solo3' not in request.form and 'co' not in request.form and'vide' not in request.form :
       #On prend ici les 3 composante d'un Menu selon la table SQL (Principal,Accompagnement,Boisson)
        Bois = request.form['Boisson'] 
        Pizza1= request.form['Pizza1']
        Pizza2= request.form['Pizza2']
        Ent= request.form['Entrée']
        
        
        
        #Cette vérification et les 2 autres qui suivent correspond champ rentrer initialement dans les choix possibles, leurs présence signifie donc que le client n'a donc rien choisis.
        
        if Ent == "--Veillez choisir une Entrée--":
            Message="VOUS N'AVEZ PAS CHOISIS D'ENTREE"
            NbrPanier = RecupMPiz("Panier")    
            Panier= RecupPiz("Panier")    
            Pizza=RecupPiz("Pizza")
            Entrée=RecupPiz("Entrées")
            Boiss=RecupPiz("Boisson")
            sauce=RecupPiz("Sauce")
            return render_template("PizzaHut/Pizza.html",Pizza=Pizza,Boi=Boiss,Entre=Entrée,sauce=sauce,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
        
        if Pizza1 == "--Veillez choisir votre Pizza n°1--":#Le but ici est de recréé la page en changeant la variable Message qui s'affichera signaler le problème.
            Message="VOUS N'AVEZ PAS CHOISI VOTRE 1e PIZZA !*"
            NbrPanier = RecupMPiz("Panier")    
            Panier= RecupPiz("Panier")    
            Pizza=RecupPiz("Pizza")
            Entrée=RecupPiz("Entrées")
            Boiss=RecupPiz("Boisson")
            sauce=RecupPiz("Sauce")
            return render_template("PizzaHut/Pizza.html",Pizza=Pizza,Boi=Boiss,Entre=Entrée,sauce=sauce,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
            
        if Pizza2 == "--Veillez choisir votre Pizza n°2--":
            
            Message="VOUS N'AVEZ PAS CHOISIS VOTRE 2e PIZZA !*"
            NbrPanier = RecupMPiz("Panier")    
            Panier= RecupPiz("Panier")    
            Pizza=RecupPiz("Pizza")
            Entrée=RecupPiz("Entrées")
            Boiss=RecupPiz("Boisson")
            sauce=RecupPiz("Sauce")
            return render_template("PizzaHut/Pizza.html",Pizza=Pizza,Boi=Boiss,Entre=Entrée,sauce=sauce,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
      
        if Bois == "--Veillez choisir votre Boisson--":
            Message="IL MANQUE UNE BOISSON*"
            NbrPanier = RecupMPiz("Panier")    
            Panier= RecupPiz("Panier")    
            Pizza=RecupPiz("Pizza")
            Entrée=RecupPiz("Entrées")
            Boiss=RecupPiz("Boisson")
            sauce=RecupPiz("Sauce")
            return render_template("PizzaHut/Pizza.html",Pizza=Pizza,Boi=Boiss,Entre=Entrée,sauce=sauce,Panier=Panier,Message1=Message,NbrPanier=NbrPanier)
        
        
        
        #Cette variable "txt" est un moyen que j'utilise afin de conserver le menu sous "une seul forme" et de pouvoir ainsi plus aisément le rentrer dans le panier
        txt=""
        txt+= "Menu :-- "+str(Ent)+" || "+str(Pizza1)+" || "+str(Pizza2)+ " || " +str(Bois)+"--"
          
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"INSERT into Menu (Pizza1,Pizza2,Boisson,Entrée) VALUES('{Pizza1}','{Pizza2}','{Bois}','{Ent}')")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{txt}')")
        connexion.commit()
        connexion.close()
    #Parfois lors d'une commande on souhaite prendre quelque supplement, c'est le but ici des "solo" qui permet d'ajouter au panier certain composant d'un menu sans forcement en prendre un.    
    if request.method == 'POST' and 'solo' in request.form :
        SoloEnt=request.form['bobo1']
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloEnt}')")
        connexion.commit()
        connexion.close()
        
    if request.method == 'POST' and 'solo1' in request.form :
        SoloPiz=request.form['bobo']
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloPiz}')")
        connexion.commit()
        connexion.close()
    
    if request.method == 'POST' and 'solo2' in request.form :
        SoloBoi=request.form['bobo2']
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloBoi}')")
        connexion.commit()
        connexion.close()
        
    if request.method == 'POST' and 'solo3' in request.form :
        SoloSau=request.form['bobo3']
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{SoloSau}')")
        connexion.commit()
        connexion.close()
    #Vide comme son nom l'indique à pour but de vider le panier si le client le souhaite. J'efface donc dans un premier temps la table "panier" puis "Menu" car le "panier" ne fait que retranscrire le "Menu".
    if request.method == 'POST' and 'vide' in request.form :
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        connexion.execute(f"DELETE FROM Panier")
        connexion.execute(f"DELETE FROM Menu")
        connexion.commit()
        connexion.close()
    if request.method == 'POST' and 'co' in request.form :
        Condiment1=request.form['Condiment1']
        Condiment2=request.form['Condiment2']
        Condiment3=request.form['Condiment3']
        try:
            connexion = sqlite3.connect("RestoPiz.db")
        except:
            connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
        txt=""
        txt+= "Perso : "+str(Condiment1)+" || "+str(Condiment2)+" || "+str(Condiment3)+ ""
        connexion.execute(f"INSERT into Panier (Contenu) VALUES('{txt}')")
        connexion.commit()
        connexion.close()
        
        
    NbrPanier = RecupMPiz("Panier")    
    Panier= RecupPiz("Panier")    
    Pizza=RecupPiz("Pizza")
    Entrée=RecupPiz("Entrées")
    Boiss=RecupPiz("Boisson")
    sauce=RecupPiz("Sauce")
    condiment=RecupPiz("Condiment")
    return render_template("PizzaHut/Pizza.html",Pizza=Pizza,Boi=Boiss,Entre=Entrée,sauce=sauce,Panier=Panier,Message1=Message,NbrPanier=NbrPanier,condiment=condiment)


@app.route('/ValiderPiz',methods = ['GET','POST'])
def PizzaV():

    try:
        connexion = sqlite3.connect("RestoPiz.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
    
    #Une récuperation séparer des éléments du panier car les Prix sont evidemment different dans le cas d'un Menu/Perso/sauce ou d'un element seul.
    Nbr=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu Not LIKE '%Menu%' AND Contenu Not LIKE '%Perso%'AND Contenu Not LIKE '%Sauce%' AND Contenu Not LIKE '%Pizza%' AND Contenu Not LIKE '%Entrée%'")
    Nbr1=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE '%Menu%'")
    Nbr2=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE '%Perso%'")
    Nbr3=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE 'Sauce%'")
    Nbr4=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE 'Pizza%'")
    Nbr5=connexion.execute(f"SELECT count(Contenu) FROM Panier WHERE Contenu LIKE 'Entrée%'")
    #Sous forme de liste car les info ne sont pas utilisable autrement
    Autre=list(Nbr)
    Menu=list(Nbr1)
    Perso=list(Nbr2)
    Sauce=list(Nbr3)
    Pizza=list(Nbr4)
    Entrée=list(Nbr5)
    #Attribution des prix
    valeurFinal=0
    ValeurMenu=int(Menu[0][0])*25.99
    ValeurBois=int(Autre[0][0])*4.99
    ValeurPerso=int(Perso[0][0])*17.99
    ValeurSauce=int(Sauce[0][0])*0.70
    ValeurPizza=int(Pizza[0][0])*17.99
    ValeurEntre=int(Entrée[0][0])*5.99 
    
  
    valeurFinal=ValeurMenu+ValeurBois+ValeurPizza+ValeurSauce+ValeurPerso+ValeurEntre
    connexion.commit()
    connexion.close()
    Panier= RecupPiz("Panier")
        
    return render_template("PizzaHut/ValiderPizza.html",aa=valeurFinal,Panier=Panier)

@app.route('/Fin',methods = ['GET','POST'])
def Resultat():
  
    Info=Recup2("Client")
    
    return render_template("Fin.html",Info=Info)
app.run(debug=True) # On lance le serveur en mode debug

