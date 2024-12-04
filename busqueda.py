#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

#modulos
import Centros as m

def obtener_indices(lista):
    #optenemos la lista de materiales
    Indices = lista.curselection()
    Opciones = []
    
    #optenemos las opcines de la lista
    for ind in Indices:
        Opciones.append(lista.get(ind))
    
    return Opciones

#busqueda por materiales
def busqueda_materiales(lista):
    #optenemos la lista de materiales
    Opciones = obtener_indices(lista)
    
    #filtramos los centros
    resultados = [] #aqui pondremos los materiales que cumplan con las condiciones
    for centro in m.centros: #primera condicion: accederemos a todos los centros
        for material in Opciones: #segunda condicion: accederemos a las opciones
            if material in centro["materiales"]: #tercera condicion: aqui verificamos si el "material" esta en el "centro" iterado
                if not centro in resultados: #esto es para evitar que se repitan (soy paranoico si?)
                    resultados.append(centro) #pues aqui nomas append jajaj salu2
    
    return resultados

def busqueda_key(key):
    #filtramos los centros
    resultados = [] #aqui pondremos los materiales que cumplan con las condiciones
    for centro in m.centros: #primera condicion: accederemos a todos los centros
        if key in centro["clave"]:
            resultados.append(centro) #pues aqui nomas append jajaj salu2
    
    return resultados
