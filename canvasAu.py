# -*- coding: utf-8 -*-
import os
import win32com.client
import pyttsx3
import time
from tkinter import *


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
			#print(self.__caminos)
			#print(self.__vertice)
			#print(self.__condicionesS)

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
			paint.create_oval(95,495,185,405,width=1.5),
			paint.create_text(140,450,text='p',font=('Comic Sans MS',20)),
			paint.create_line(185,450,284,450,width=3.0,arrow=LAST)]
			root.update()
			#time.sleep(0.5)
			#paint.after(1000,self.pintarFiguras)

		elif self.__vertice=="q":
			self.__lienzo = [paint.create_arc( 295, 375,365.5 ,470,star=0,extent=180,style='arc',width=3.0,outline="black"),
			paint.create_line(355,405,365,420,widt=3,fill="black"),
			paint.create_line(375,405,365,420,widt=3),
			paint.create_oval(285,495,375,405,width=1.5),
			paint.create_text(330,450,text='q',font=('Comic Sans MS',20)),
			paint.create_line(375,450,474,450,width=3.0,arrow=LAST)]
			root.update()

		elif self.__vertice=="r":
			self.__lienzo = [paint.create_oval(475,495,565,405,width=1.5),
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
			mensaje.config(textvariable=texto,fg='green')
			voz.say("La palabra es palindroma")
			root.update()
			voz.runAndWait()

		else:
			paint.itemconfigure(self.__lienzo[3],fill='red')
			texto.set("Incorrecto")
			mensaje.config(textvariable=texto,fg='red')
			voz.say("ERROR, la palabra no es palindroma")
			root.update()
			voz.runAndWait()

		reiniciar.config(state="normal",command=lambda:iniciar())




class ListaCondiciones():

	def __init__(self,camino,x,y,segundos):
		self.__condiciones = []
		self.__camino = camino
		self.__lista = Listbox(root,width=15, height=5,font=("Comic Sans MS",10))
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
				paint.after(self.__segundos,self.__lista.itemconfigure(x,bg='white',fg='black'))
				root.update()




def proceso(palabra,listaCon,listaEs,pilaI):
	
	vertice0=Grafo("i",False)
	vertice1=Grafo("p",False)
	vertice2=Grafo("q",False)
	vertice3=Grafo("r",True)

	lista=[vertice0,vertice1,vertice2,vertice3]
	pila=["#"]

	lista[0].addArista("p")
	lista[1].addArista("p")
	lista[1].addArista("q")
	lista[2].addArista("q")
	lista[2].addArista("r")

	if (len(palabra)-2)%2==1 or palabra=="":
		voz=pyttsx3.init()
		voz.setProperty('rate',230)
		
		texto.set("Solo palabras impares")
		mensaje.config(textvariable=texto,fg='blue')
		voz.say("Ingrese una palabra impar con mas de dos letras")
		voz.runAndWait()
		root.update()

	elif (len(palabra)-1)>=3:
		letrasB=int((len(palabra)-2)/2)

		for x in range(0,len(listaCon)):
			listaCon[x].setSegundos(seg.get())

		for x in range(0,len(listaEs)):
			listaEs[x].setSegundos(seg.get())


		for x in range(0,letrasB):
			vertice0.addCondition(("p",palabra[x],"#","#"+palabra[x]))
			listaCon[0].setCondiciones((palabra[x]+",","#","/#"+palabra[x]))

		listaCon[0].viewInList()

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

		listaCon[4].viewInList()

		actual=palabra[0:len(palabra)-1]


		palabra=actual
		listaPila=[]
		listaPila.append(pilaI.create_text(50,470,text="#",font=("forte",20)))
		posicion=470


		for x in range(0,letrasB*2):
			posicion-=40
			listaPila.append(pilaI.create_text(50,posicion,text='',font=('forte',20)))

		actual="i"
		newpalabra=palabra+"λ"
		tope=0

		for x in range(0,len(newpalabra)):
			
			for n in range(0,len(lista)):
				
				if lista[n].getVertice()==actual:
					
					if x==letrasB:
						valor=lista[n].isCondition(newpalabra[x]+"λ",pila[len(pila)-1])
						#listaCon[n].presentar()
					else:
						valor=lista[n].isCondition(newpalabra[x],pila[len(pila)-1])


					if valor!="":
						for y in range(0,len(valor[2])):
							pila.pop()
							pilaI.itemconfigure(listaPila[tope],text="")
							pilaI.after(seg.get())
							root.update()
							tope-=1

						#listaCon[n].presentar((valor[1][0]+",",valor[2][0],"/"+valor[3]))
						for y in range(n,len(listaCon)):
							listaCon[y].presentar((valor[1][0]+",",valor[2][0],"/"+valor[3]))

						listaEs[n].editarFigura(valor[0])
						root.update()


						for y in range(0,len(valor[3])):
							if valor[3][y]=="λ":
								break
							else:
								tope+=1
								pila.append(valor[3][y])
								pilaI.itemconfigure(listaPila[tope],text=valor[3][y])#valor[3][y]
								pilaI.after(seg.get())
								root.update()

						actual=valor[0]
						break


		for x in range(0,len(lista)):
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

	'''listaCon[0].setCondiciones([("c,","#","/#c"),("b,","#","/#b"),("a,","#","/#a")])
	listaCon[0].viewInList()
	listaCon[0].presentar(("a,","#","/#a"))'''


	casilla=Text(root,width=25,height=1)
	casilla.place(x=400,y=510)


	pilaI.create_rectangle(4,0,100,490,width=2)
	pilaI.place(x=800,y=100)
	pilaI.config(bg='#51c4fa')

	texto.set("Ingrese una palabra")
	mensaje.config(textvariable=texto,fg='black')

	


	texto1=[pilaI.create_text(50,470,text="#",font=("forte",20))]

	rapido.config(command=lambda:velocidad(1))
	lento.config(command=lambda:velocidad(3))

	verificar.config(command=lambda:proceso(casilla.get(1.0,END),listaCon,listaEs,pilaI))

	'''for x in range(0,n):
		pos-=40
		texto.append(pila.create_text(50,pos,text='p',font=('forte',20)))

	pila.itemconfigure(texto[2],text=letra)'''

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
			root.iconbitmap("icono.jpeg")
			root.config(bg='white') #color inferior

			paint = Canvas(root, width=1000, height=700,)
			paint.place(x=4,y=-125)
			paint.config(bg='#3c6bc0') #color superior

			reiniciar=Button(root,text="Reiniciar todo",state='disabled')
			reiniciar.place(x=398,y=535)

			verificar=Button(root,text="Verificar")
			verificar.place(x=550,y=535)

			mensaje=Label(root,text="",fg="black",font=("Comic Sans MS",10))
			mensaje.place(x=435,y=565)

			rapido=Button(root,text="Rapido")
			rapido.place(x=40,y=40)

			normal=Button(root,text="Normal")
			normal.place(x=40,y=80)

			lento=Button(root,text="Lento")
			lento.place(x=40,y=120)

			pilaI = Canvas(root,width=100,height=1000)

			texto = StringVar()
			seg = IntVar()


			iniciar()

			root.mainloop()











