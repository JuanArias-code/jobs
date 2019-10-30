# -*- coding: utf-8 -*-
import os
import win32com.client
import pyttsx3
import time
from tkinter import *
from tkinter import messagebox

class Grafo(object):

	def __init__(self, vertice,indicador):
		self.__vertice = vertice
		self.__aceptacion = indicador
		self.__caminos = []
		self.__condicionesS = []

	def addArista(self,arista):
		validar=True

		for x in range(0,len(self.__caminos)):
			if arista== self.__caminos[x]:
				validar=False

		if validar:
			self.__caminos.append(arista)

	def addCondition(self,tupla):
		validar=True

		for x in range(0,len(self.__condicionesS)):
			if tupla==self.__condicionesS[x]:
				validar=False

		if validar:
			self.__condicionesS.append(tupla)

	def isCondition(self,actual,enPila):

		for x in range(0,len(self.__condicionesS)):
			if self.__condicionesS[x][1]==actual and self.__condicionesS[x][2]==enPila:
				return self.__condicionesS[x]


		return ""

	def getVertice(self):
		return self.__vertice

	def getAccept(self):
		return self.__aceptacion

	def resetG(self):
		del self.__condicionesS[:]


class PintarGrafo():

	def __init__(self, vertice,indicador,segundos):
		self.__vertice = vertice
		self.__indicador = indicador
		self.__lienzo = []
		self.__segundos = segundos

	def setSegundos(self,segundos):
		self.__segundos=segundos

	def pintarFiguras(self):
		
		if self.__vertice=="i":
			self.__lienzo = [paint.create_line(50,450,94,450,width=3.0,arrow=LAST)]
			root.update()

		elif self.__vertice=="p":
			self.__lienzo = [paint.create_arc( 105, 375,175.5 ,470,star=0,extent=180,style='arc',width=3.0),
			paint.create_line(165,405,175,420,widt=3),
			paint.create_line(185,405,175,420,widt=3),
			paint.create_oval(95,495,185,405,width=1.5,fill='#eff5fc'),
			paint.create_text(140,450,text='p',font=('Comic Sans MS',20)),
			paint.create_line(185,450,284,450,width=3.0,arrow=LAST)]
			root.update()


		elif self.__vertice=="q":
			self.__lienzo = [paint.create_arc( 295, 375,365.5 ,470,star=0,extent=180,style='arc',width=3.0,outline="black"),
			paint.create_line(355,405,365,420,widt=3,fill="black"),
			paint.create_line(375,405,365,420,widt=3),
			paint.create_oval(285,495,375,405,width=1.5,fill='#eff5fc'),
			paint.create_text(330,450,text='q',font=('Comic Sans MS',20)),
			paint.create_line(375,450,474,450,width=3.0,arrow=LAST)]
			root.update()

		elif self.__vertice=="r":
			self.__lienzo = [paint.create_oval(475,495,565,405,width=1.5,fill='#eff5fc'),
			paint.create_oval(485,485,555,415,width=1.5),
			paint.create_text(520,450,text='r',font=('Comic Sans MS',20))]
			root.update()


	def editarFigura(self,camino):

		verificar.config(state="disabled")
		
		if self.__vertice=="i":
			paint.itemconfigure(self.__lienzo[0],fill="yellow")
			root.update()
			paint.after(self.__segundos,paint.itemconfigure(self.__lienzo[0],fill="black"))

		elif self.__vertice=="p" or self.__vertice=="q":
			if camino==self.__vertice:
				paint.itemconfigure(self.__lienzo[0],outline='yellow')
				paint.itemconfigure(self.__lienzo[1],fill='yellow')
				paint.itemconfigure(self.__lienzo[2],fill='yellow')
				root.update()
				paint.after(self.__segundos)
				paint.itemconfigure(self.__lienzo[0],outline='black')
				paint.itemconfigure(self.__lienzo[1],fill='black')
				paint.itemconfigure(self.__lienzo[2],fill='black')

				root.update()
				paint.after(self.__segundos)
				paint.itemconfigure(self.__lienzo[3],fill='yellow')
				root.update()
				paint.after(self.__segundos)
				paint.itemconfigure(self.__lienzo[3],fill='white')
				root.update()

			else:
				paint.itemconfigure(self.__lienzo[3],fill='yellow')
				root.update()

				paint.after(self.__segundos)
				paint.itemconfigure(self.__lienzo[3],fill='white')
				paint.itemconfigure(self.__lienzo[5],fill='yellow')
				root.update()

				paint.after(self.__segundos)
				paint.itemconfigure(self.__lienzo[5],fill='black')
				root.update()

		elif self.__vertice=="r":
			paint.itemconfigure(self.__lienzo[1],fill='yellow')
			root.update()
			paint.after(self.__segundos)
			paint.itemconfigure(self.__lienzo[1],fill='white')
			root.update()


	def definirEstado(self):
		voz=pyttsx3.init()
		voz.setProperty('rate',230)
		
		if self.__indicador:
			paint.itemconfigure(self.__lienzo[0],fill='green')
			texto.set("Validado")
			mensaje.config(textvariable=texto,fg='green',bg="white")
			voz.say("La palabra es palíndroma")
			root.update()
			voz.runAndWait()

		else:
			paint.itemconfigure(self.__lienzo[3],fill='red')
			texto.set("Incorrecto")
			mensaje.config(textvariable=texto,fg='red')
			voz.say("ERROR, la palabra no es palíndroma")
			root.update()
			voz.runAndWait()

		reiniciar.config(state="normal",command=lambda:iniciar())




class ListaCondiciones():

	def __init__(self,camino,x,y,segundos):
		self.__condiciones = []
		self.__camino = camino
		self.__lista = Listbox(root,width=15, height=5,font=("Comic Sans MS",10),bg="#eff5fc")
		self.__x = x
		self.__y = y
		self.__segundos = segundos


	def pintarLista(self):
		self.__lista.place(x=self.__x,y=self.__y)

	def setCondiciones(self,condiciones):
		
		self.__condiciones.append(condiciones)

	def setSegundos(self,segundos):
		self.__segundos=segundos

	def viewInList(self):
		
		self.__lista.insert(END, *self.__condiciones)

	def presentar(self,condicion):
		
		for x in range(0,len(self.__condiciones)):
			if self.__condiciones[x]==condicion:
				self.__lista.see(x)
				self.__lista.itemconfigure(x,bg='#00aa00',fg='#fff')
				root.update()
				paint.after(self.__segundos,self.__lista.itemconfigure(x,bg='green',fg='white'))
				root.update()




def proceso(palabra,listaCon,listaEs,pilaI):
	
	#aqui se declaran los nodos del grafo (vertice,condicion)
	vertice0=Grafo("i",False)
	vertice1=Grafo("p",False)
	vertice2=Grafo("q",False)
	vertice3=Grafo("r",True)

	lista=[vertice0,vertice1,vertice2,vertice3]
	pila=["#"]

	#aqui las aristas del grafo (camino)
	lista[0].addArista("p")
	lista[1].addArista("p")
	lista[1].addArista("q")
	lista[2].addArista("q")
	lista[2].addArista("r")

	if (len(palabra)-2)%2==1 or palabra=="":
		voz=pyttsx3.init()
		voz.setProperty('rate',230)
		
		texto.set("Solo palabras impares")
		mensaje.config(textvariable=texto,fg='black')
		voz.say("Ingrese una palabra impar con mas de dos letras")
		voz.runAndWait()
		root.update()

	elif (len(palabra)-1)>=3:

		#cantidad de palabras que entran en la pila
		letrasB=int((len(palabra)-2)/2)

		#define la velocidad del programa a cada parte del canvas
		for x in range(0,len(listaCon)):
			listaCon[x].setSegundos(seg.get())

		for x in range(0,len(listaEs)):
			listaEs[x].setSegundos(seg.get())


		#añade la primera lista de condiciones tanto al canvas como al grafo teniendo en cuenta ciertos patrones
		#addCondition((camino a donde lleva, **estructura de la condicion))
		#listaCon((tupla con la estructura de la condicion))
		for x in range(0,letrasB):
			vertice0.addCondition(("p",palabra[x],"#","#"+palabra[x]))
			listaCon[0].setCondiciones((palabra[x]+",","#","/#"+palabra[x]))

		#pinta las condiciones en el lienzo
		listaCon[0].viewInList()

		#el mismo proceso que el anterior y asi para cada lista
		for x in range(0,letrasB):
			for n in range(0,letrasB):
				lista[1].addCondition(("p",palabra[n],palabra[x],palabra[x]+palabra[n]))
				listaCon[1].setCondiciones((palabra[n]+",",palabra[x],"/"+palabra[x]+palabra[n]))

		listaCon[1].viewInList()

		lista[1].addCondition(("q",palabra[letrasB],"#","#"))
		listaCon[2].setCondiciones((palabra[letrasB]+",","#","/#"))

		for x in range(0,letrasB):
			lista[1].addCondition(("q",palabra[letrasB]+"λ",palabra[x],palabra[x]))
			lista[2].addCondition(("q",palabra[x],palabra[x],"λ"))

			listaCon[2].setCondiciones((palabra[letrasB]+",",palabra[x],"/"+palabra[x]))
			listaCon[3].setCondiciones((palabra[x]+",",palabra[x],"/λ"))

		listaCon[2].viewInList()
		listaCon[3].viewInList()

		lista[2].addCondition(("r","λ","#","#"))
		listaCon[4].setCondiciones(("λ,","#","/#"))

		#aqui pinta la ultima lista
		listaCon[4].viewInList()


		#le quita a la palabra el salto de linea que viene al final de esta
		actual=palabra[0:len(palabra)-1]
		palabra=actual


		#guarda la primera instancia de la pila mostrada en el canvas
		listaPila=[]
		listaPila.append(pilaI.create_text(50,470,text="#",font=("forte",20)))
		#posicion inicial en Y
		posicion=470


		#crea las demas instancias a usar dentro de la pila, dependiendo del numero de letras
		for x in range(0,letrasB*2):
			posicion-=40
			listaPila.append(pilaI.create_text(50,posicion,text='',font=('forte',20)))

		#condicion de inicio del grafo
		actual="i"
		#a la palabra original se le agrega lambda para simular el vacio
		newpalabra=palabra+"λ"
		#instancia de inicio dentro de la pila
		tope=0

		#recorre la palabra
		for x in range(0,len(newpalabra)):
			
			for n in range(0,len(lista)):

				#si encuentra la instancia actual dentro de la lista de vertices. entre
				if lista[n].getVertice()==actual:

					#si va por la mitad de la palabra,agregue un lambda para encontrar la condicion y evitar ambiguedades
					if x==letrasB:
						valor=lista[n].isCondition(newpalabra[x]+"λ",pila[len(pila)-1])

					else:
						valor=lista[n].isCondition(newpalabra[x],pila[len(pila)-1])


					#si encuentra la condicion. entre
					if valor!="":

						#saca de la pila el tope que indique la condicion y luego lo muestra en pantalla
						for y in range(0,len(valor[2])):
							pila.pop()
							pilaI.itemconfigure(listaPila[tope],text="")
							pilaI.after(seg.get())
							root.update()
							#el siguiente elemento pasa a ser el nuevo tope
							tope-=1

						#pinta la condicion actual
						for y in range(n,len(listaCon)):
							listaCon[y].presentar((valor[1][0]+",",valor[2][0],"/"+valor[3]))

						#pinta la instancia en el grafo
						listaEs[n].editarFigura(valor[0])
						root.update()


						for y in range(0,len(valor[3])):

							#si la condicion de agragacion es diferente a vacio, agrege la nueva palabra indicada
							#y pintela en la pila
							if valor[3][y]=="λ":
								break
							else:
								#sube a un espacio vacio en la pila y agrega la nueva letra
								#siendo esta el nuevo tope
								tope+=1
								pila.append(valor[3][y])
								pilaI.itemconfigure(listaPila[tope],text=valor[3][y])
								pilaI.after(seg.get())
								root.update()

						#actualiza a la instancia actual en el grafo
						actual=valor[0]
						#rompe el ciclo una vez encontrada
						break


		for x in range(0,len(lista)):
			#pinta el resultado del analisis
			if lista[x].getVertice()==actual:
				listaEs[x].definirEstado()
				break






def iniciar():
	seg.set(500)

	paint.delete("all")
	pilaI.delete("all")

	reiniciar.config(state="disabled")
	verificar.config(state="normal")

	lento.config(bg="white")
	normal.config(bg="#efb810")
	rapido.config(bg="white")

	root.update()

	listaEs = [PintarGrafo("i",False,seg.get()),PintarGrafo("p",False,seg.get()),
	PintarGrafo("q",False,seg.get()),PintarGrafo("r",True,seg.get())]

	for x in range(0,len(listaEs)):
		listaEs[x].pintarFiguras()

	listaCon = [ListaCondiciones("p",40,395,seg.get()),ListaCondiciones("p",100,120,seg.get()),ListaCondiciones("q",200,395,seg.get())
	,ListaCondiciones("q",290,120,seg.get()),ListaCondiciones("r",370,395,seg.get())]

	for x in range(0,len(listaCon)):
		listaCon[x].pintarLista()


	casilla=Text(root,width=25,height=1)
	casilla.place(x=570,y=420)


	pilaI.create_rectangle(4,4,100,490,width=2)
	pilaI.place(x=800,y=85)
	pilaI.config(bg='#eff5fc')

	texto.set("Ingrese una palabra")
	mensaje.config(textvariable=texto,fg='black')
	mensaje.place(x=610,y=380)

	


	texto1=[pilaI.create_text(50,470,text="#",font=("forte",20))]

	rapido.config(command=lambda:velocidad(1))
	lento.config(command=lambda:velocidad(3))

	verificar.config(command=lambda:proceso(casilla.get(1.0,END),listaCon,listaEs,pilaI))



def velocidad(opcion):
		
	if opcion==1:
		seg.set(100)
		rapido.config(bg="#efb810")
		lento.config(bg="white")
		normal.config(bg="white")

	elif opcion==2:
		seg.set(500)
		rapido.config(bg="white")
		lento.config(bg="white")
		normal.config(bg="#efb810")

	elif opcion==3:
		seg.set(1000)
		rapido.config(bg="white")
		lento.config(bg="#efb810")
		normal.config(bg="white")




if __name__ == '__main__':
			root=Tk()

			root.title('Automata palindromo impar')
			root.geometry('1000x700')
			root.resizable(0,0)
			root.iconbitmap("artificial-intelligence.ico")
			root.config(bg='#0a0a0a') #color inferior


			paint = Canvas(root, width=1000, height=700,)
			paint.place(x=4,y=-125)
			paint.config(bg='#00aae4') #color superior

			reiniciar=Button(root,text="Reiniciar todo",state='disabled')
			reiniciar.place(x=600,y=450)

			verificar=Button(root,text="Verificar")
			verificar.place(x=700,y=450)

			mensaje=Label(root,text="",fg="black",font=("Comic Sans MS",10))
			mensaje.place(x=435,y=565)

			rapido=Button(root,text="Rapido")
			rapido.place(x=40,y=40)

			normal=Button(root,text="Normal")
			normal.place(x=40,y=80)

			lento=Button(root,text="Lento")
			lento.place(x=40,y=120)

			def clicked():
				messagebox.showinfo('¿Que es un automata?', 'Un autómata es un modelo matemático para una máquina de estado finito (FSM sus siglas en inglés). Una FSM es una máquina que, dada una entrada de símbolos, "salta" a través de una serie de estados de acuerdo a una función de transición (que puede ser expresada como una tabla). En la variedad común "Mealy" de FSMs, esta función de transición dice al autómata a qué estado cambiar dados unos determinados estado y símbolo.')
			btn = Button(root, text='Informacion', command=clicked)
			btn.grid(column=0, row=0,padx = 810, pady = 15)

			pilaI = Canvas(root,width=100,height=490)

			texto = StringVar()
			seg = IntVar()


			iniciar()

			root.mainloop()











