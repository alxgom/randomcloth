# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 19:06:51 2015

@author: Alexis
"""

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
import glob

"""
definir una funcion que tenga una imagen, posibles parametros y condiciones iniciales.
"""

"""
Cosas que tengo que agregar:
Definir una funcion global, a la que le diga si quiero tamanio random o predefinido
, si quiero posiciones random, o una red de n puntos.
Si quiero todos los angulos random, o un unico angulo random.
En caso de usar una red, podria usar una cantidad 'I' de imagenes como atomos de mi red
Otras Redes posibles.(hexagonos, etc...).
"""

plt.clf()
print '\n -Lista de achivos png en el directorio: \n', glob.glob('./*.png'), '\n'

a=18#cantidad de ptos totales
r=np.random.random((a,2)) #matriz de numeros random(es un vextor de pares de coordenadas)
#print r

im=Image.open('perrofeo.png')#carga la imagen
oldsize=im.size
print 'Datos de la imagen Original:' , 'tamano=', oldsize, 'mode=', im.mode #datos de la imagen original

size=np.array(oldsize) #tamanio para resize
im=im.rotate(float(np.random.random(1)*360),expand=1).resize(size)#angulo random
#im.show()#muestra la imagen rotanda
im.save('imt1.jpg')#graba la imagen rotada como jpg
'''
tamano random
imagen random
'''
########################
mesh = Image.new("RGBA", np.array(oldsize)*4,"white")#Crea Imagen en blanco de 4 veces el tamanio de la original para poner las otras imagenes
newsize=mesh.size
for b in r:
    #print 'b[0]*mesh.size=',  b[0]*mesh.size[0]#chequeo que de lo que quiero
    mesh.paste(im, (int(b[0]*mesh.size[0]), int(b[1]*mesh.size[1])), im )#pone las imagenes en las coordenadas random
mesh.show()
mesh.save('mesh.jpg')

########################

r=r*mesh.size[1]
#print 'r[:,0](deberia dar igual que los b[0])=', r[:,0]
for c in r:
    fig1=plt.plot(int(c[0]),mesh.size[1]-int(c[1]),'.r')
#plt.show()

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

def unit_vectors(distance, style='rectangular'):
    d=distance;
    styles=['rectangular', 'obl', 'centrectang', 'hexacent', 'cuadrada']    
    
    if style=='random':
        #codigo para estilo random
        style=styles[np.random.randint(5)]
        print 'random style= ', style
    
    
    if style=='rectangular':
        at1 = [d/2, 0]#posicion del primer atomo
        at2 = [0, d]#posocion del segundo atomo
        
    if style=='obl':
        at1 = [d, 0]#posicion del primer atomo
        at2 = [-d/4, d]#posocion del segundo atomo
        print 'angulo = ,,,'
        
    if style=='centrectang':
        at1 = [d, 0]#posicion del primer atomo
        at2 = [d/2, d/2]#posocion del segundo atomo
     
    if style=='hexacent':
        at1 = [-d/2, d]#posicion del primer atomo
        at2 = [d, 0]#posocion del segundo atomo
     
    if style=='cuadrada':
        at1 = [0, d]#posicion del primer atomo
        at2 = [d, 0]#posocion del segundo atomo
     
    if style=='manual':
        base= input('Escribir el primer vector y el secundo como: [[0, 1], [1, 0]]...  \n' 'base= ' )
        at1 = base[0]#posicion del primer atomo
        at2 = base[1]#posocion del segundo atomo
    
    return [at1, at2] 
    """
    unit_vectors define los dos vectores de la base de bravais.
    distance es una distancia en comun que van a tener los vectores de la base/
    para varios estilos.
    'style' da las 5 bases de bravais.
        style puede tomar los valores:
            'rectangular'(por default), 'obl'(oblicua), 'centrectang'()
            'hexacent'(hexagonal(con un atomo en el medio)), 'cuadrada'
            'manual'(Para especificar manualmente cada uno de los vectores de la base.)
            para mas info: https://en.wikipedia.org/wiki/Bravais_lattice
     La funcion devuelve dos vectores: at1 y at2. ambos vectores forman la base.
    """    
    
#a1 y a2 son los vectores de los atomos de la base de bravais

def atom_locations(basis, n, debug=False):
     print 'basis=', basis 
     
     # Atom definitions
     R = []
     
     # Basis vectors
     a1 = basis[0]
     a2 = basis[1]
     
     if debug == True : #para debuggear
         #chaquea que la base este bien asignada
         print 'a1,a2: ', basis

     for n1 in range(n):
         for n2 in range(n):
             if debug == True : print 'n1,n2=', n1, n2 #debuggear
             R.append( [n2*a2[0]+n1*a1[0], n2*a2[1]+n1*a1[1]] )
         if debug == True : print 'R=', R #debuggear

     return R #podria redefinir la funcion para n atomos.(imagenes.)  R=n1*at1+n2*at2  la red de bravais
'''
def new_atom(red, posicion, debug=False ):
    newatom=[]
    newatom= np.array(red)[]
'''    


    
R= atom_locations(unit_vectors(5.,'random'),6)#chequeo que funcione la red. 
#print 'l:', l,  'm:', m #chaqueo que funcione ly m

mesh2 = Image.new("RGBA", np.array(im.size)*10,"white")#Crea Imagen en blanco de 4 veces el tamanio de la original para poner las otras imagenes
#print 'l=', l
R=np.array(R)#combierto a l en un array para poder operar como vector.
R=R*im.size[0]/2
for b in R:
    #print 'b:',  b
    fig2=plt.plot(b[0],mesh2.size[1]-b[1],'.b')
    mesh2.paste(im, (int(b[0]), int(b[1])), im )#pone las imagenes en las coordenadas random
mesh2.save('mesh2.jpg')
plt.show()
mesh2.show()



'''
ideas:
otras redes en 2d posibles: proyeciones en 2d de redes en 3d!
'''

'''
paginas que sirven paraguiarme con las redes:
    http://www-personal.umich.edu/~sunkai/teaching/Winter_2013/honeycomb.html
    https://courses.cit.cornell.edu/mse5470/handout4.pdf
    https://en.wikipedia.org/wiki/Bravais_lattice
'''