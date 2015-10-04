# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 18:57:49 2015

@author: Alexis
"""
#%matplotlib inline
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image



"""
definir una funcion que tenga una imagen, posibles parametros y condiciones iniciales.
"""
"""
Cosas que tengo que agregar:
Definir una funcion global, a la que le diga si quiero tamanio random o predefinido
, si quiero posiciones random, o una red de n puntos.
Si quiero todos los angulos random, o un unico angulo random.
En caso de usar una red, podria usar una cantidad 'I' de imagenes como atomos de mi red
Otras Redes posibles.(hexagonos, etc...)
"""

a=18#cantidad de ptos totales
r=np.random.random((a,2)) #matriz de numeros random(es un vextor de pares de coordenadas)
#print r

im=Image.open("brain.png")#carga la imagen
print 'Datos de la imagen Original:' , 'tamano=', im.size #datos de la imagen original

size=600, 600 #tamanio para resize
im=im.rotate(float(np.random.random(1)*360),expand=1).resize(size)#angulo random
#im.show()#muestra la imagen rotanda
im.save('imt1.jpg')#graba la imagen rotada como jpg
'''
tamano random
imagen random
'''
########################
mesh = Image.new("RGBA", np.array(im.size)*4,"white")#Crea Imagen en blanco de 4 veces el tamanio de la original para poner las otras imagenes
for b in r:
    #print 'b[0]*mesh.size=',  b[0]*mesh.size[0]#chequeo que de lo que quiero
    mesh.paste(im, (int(b[0]*mesh.size[0]), int(b[1]*mesh.size[1])), im )#pone las imagenes en las coordenadas random
mesh.show()
mesh.save('mesh.jpg')

########################

r=r*mesh.size[1]
#print 'r[:,0](deberia dar igual que los b[0])=', r[:,0]
for c in r:
    plt.plot(int(c[0]),int(c[1]),'.r')
plt.show

'''
Hasta aca es puntos random .

###############################################################################

De aca para abajo es redes.
'''

'''
Intento de hacer redes de bravais de imagenes:
Red en 2*2
# [[0,0], [0,1], [1,1], [1,0]]]
#-----------------------------------------------
'''
def lattice_points(N):#crea los enteros para la base
     lattice = []
     for i in range(N+1):
         for j in range(N+1):
             lattice.append([i,j])
     return lattice
     

print 'Chaqueo que funcione mi lattice:'#Chequeo que funcione lattice
for i in lattice_points(4):
    plt.plot(i[0],i[1],'.r')
plt.show()


# Shown below is the unit vectors for a BCC 
# lattice, with lattice size 'distance'.
# Notice that BCC has 2 atoms in its unit cell.
# Thus you only provide only 2 atoms. 
#----------------------------------------------
def unit_vectors_BCC(distance):
    a = distance;
    point1 = [a, a]
    point2 = [a/2, a/2]
    return [point1, point2]
    
#----------------------------------------------
# This function returns a list of coordinates
# for each basis, given the basis, and the 
# lattice points. 
#----------------------------------------------
def atom_locations(basis, lattice, debug=False):
     print 'basis=', basis 
     print 'lattice=', lattice 
     
     # Atom definitions
     atom1 = []
     atom2 = []
 
     # Basis vectors
     a1, a2 = basis[0]
     b1, b2 = basis[1]
     
     if debug == True : #para debuggear
         #chaquea que la base este bien asignada
         print 'a1,a2: ', a1, a2
         print 'b1,b2:', b1, b2
     
     for n1, n2 in lattice:
         if debug == True : print 'n1,n2=', n1, n2 #debuggear
         atom1.append( [n1*a1, n2*a2] )
         atom2.append( [n1*a1 + b1, n2*a2 + b2] )
     return [atom1, atom2]#podria redefinir la funcion para n atomos.(imagenes.)


l, m= atom_locations(unit_vectors_BCC(1.),lattice_points(4))#chequeo que funcione la red. 
#print 'l:', l,  'm:', m #chaqueo que funcione ly m
for i0 in l:
    plt.plot(i0[0],i0[1],'.b')#plotea lo atomos1
    for i1 in m: 
        plt.plot(i1[0],i1[1],'.b')#plotea los atomos2
plt.show()

mesh2 = Image.new("RGBA", np.array(im.size)*4,"white")#Crea Imagen en blanco de 4 veces el tamanio de la original para poner las otras imagenes
#print 'l=', l
l=np.array(l)#combierto a l en un array para poder operar como vector.
l=l*im.size[0]/2
for b in l:
    #print 'b:',  b
    mesh2.paste(im, (int(b[0]), int(b[1])), im )#pone las imagenes en las coordenadas random
mesh2.save('mesh2.jpg')
mesh2.show()


'''ideas:
data=[0, 0]+im.size
im.transform(np.asarray(im.size*4),EXTENT, data)
mesh.paste(im, (500, 500), im )
puedo hacer la rotacoin pasando la imagen a un array y multiplicandolo por una matriz de rotacion

otras redes en 2d posibles: proyeciones en 2d de redes en 3d!

'''

'''
paginas que sirven paraguiarme con las redes:
    http://www-personal.umich.edu/~sunkai/teaching/Winter_2013/honeycomb.html
    https://courses.cit.cornell.edu/mse5470/handout4.pdf
    https://en.wikipedia.org/wiki/Bravais_lattice
'''