#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:47:49 2022

@author: elinfo
"""
import time
from random import*
import sqlite3
from flask import render_template, Flask, request

#BUrgerKing_____________________________________
def RecupBK(Choix):
    """
    Afin de récuperer les informations au sein d'une table SQL,il faut systematiquement effectuer une connextion via celle-ci.
    Mon projet etant centrer sur les fast food(et donc leurs cartes),je devais à chaque fois récuperer manuellement la liste souhaité.
    Ces enchainements de fonction ont pour but de récuper la liste des tables souhaitée.

    Parameters
    ----------
    Choix : de type texte, va étre chercher au sein de la base de donnée afin d'etre exploitée.

    Returns
    -------
    Transforme sous la forme de liste tout les attributs de la table souhaitée et les renvoies.

    """
    try:
        connexion = sqlite3.connect("RestoBK.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
    ## Fin essai
    res=connexion.execute(f"SELECT * FROM '{Choix}' ")
    connexion.commit()
    resliste=list(res)
    connexion.close()
    return resliste

def RecupMBK(Choix):
    """
    Cette fonction est fait presque la meme chose que la 1er(RecupBK) sauf que l'attribut (count) y est ajoutée

    Parameters
    ----------
    Choix : de type texte, va être chercher au sein de la base de donnée afin d'etre exploitée.

    Returns
    -------
    Cette fonction va compter le nombre de ligne dans la table choisis (avec choix) puis le convertir sous forme de liste dont on obtiendra le nombre
    avec[0][0]
    """
    try:
        connexion = sqlite3.connect("RestoBK.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoBK.db")
    ## Fin essai
    res=connexion.execute(f"SELECT count(*) FROM '{Choix}' ")
    resliste=list(res)
    connexion.close()
    return resliste[0][0]

#Mcdo_____________________________________
def RecupMcdo(Choix):
    try:
        connexion = sqlite3.connect("RestoMcdo.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
    res=connexion.execute(f"SELECT * FROM '{Choix}' ")
    connexion.commit()
    resliste=list(res)
    connexion.close()
    return resliste

def RecupMMcdo(Choix):
    try:
        connexion = sqlite3.connect("RestoMcdo.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoMcdo.db")
    res=connexion.execute(f"SELECT count(*) FROM '{Choix}' ")
    resliste=list(res)
    connexion.close()
    return resliste[0][0]
#Pizza_________________________________
def RecupPiz(Choix):
    try:
        connexion = sqlite3.connect("RestoPiz.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
    res=connexion.execute(f"SELECT * FROM '{Choix}' ")
    connexion.commit()
    resliste=list(res)
    connexion.close()
    return resliste

def RecupMPiz(Choix):
    try:
        connexion = sqlite3.connect("RestoPiz.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\RestoPiz.db")
    res=connexion.execute(f"SELECT count(*) FROM '{Choix}' ")
    resliste=list(res)
    connexion.close()
    return resliste[0][0]


def Recup2(Choix):
    try:
        connexion = sqlite3.connect("info.db")
    except:
        connexion = sqlite3.connect("C:\\Users\\elnis\\OneDrive\\Bureau\\ESCROBER EAT\\info.db")
    res=connexion.execute(f"SELECT * FROM '{Choix}' ")
    resliste=list(res)
    connexion.close()
    return resliste



