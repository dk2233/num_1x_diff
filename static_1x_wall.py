#!/usr/bin/python
# -*- coding: iso8859-2 -*- #
from math import *
import sys
import time

ss='''program dokonuje obliczen w stanie ustalonym w plaskiej scianie
z warunkiem brzegowym 2 rodzaju dla x=0 i trzeciego dla x=g
do porownania z analitycznymi
przy czym sciana wykonana z dwoch
roznych materialow o przewodnosc1 i przewodnosc2'''
print(ss,"\n")

#dane:
g=0.45
g1=0.2
g2=g-g1
przewodnosc1=1.3
przewodnosc2=0.2

# to=20.0
q1=100.0
alfa2=5.0

#liczba warstw geometrii
n1=10
n2=10
#ilosc punktow temperatury
nt=n1+2
#przy czym w tym programie temperatury
# obliczane beda umieszczone w srodkach
# warstw elementarnych obliczeniowych
iteracje=0
iteracje_end=1000
deltax1=g1/n1
deltax2=g2/n2
temp_otoczenia=-2.0
temp_poczatkowa=50.0
# print "dx = ",dx,"\n"
# wspolrzedne_t()
plik=open("wynik","w")
wspolrzedne_t=[0.0,deltax1/2]

for x in range(1,n1):
#   wspolrzedne_t[x+1]=wspolrzedne_t[x]+dx
	wspolrzedne_t.append(wspolrzedne_t[x]+deltax1) 
#   plik.write(str(wspolrzedne_t[x]))
x=len(wspolrzedne_t)-1
print(x)
wspolrzedne_t.append(wspolrzedne_t[x]+deltax1/2)
x=x+1
wspolrzedne_t.append(wspolrzedne_t[x]+deltax2/2)

for x in range(nt,n2+n1+1):
#          wspolrzedne_t[x+1]=wspolrzedne_t[x]+dx
	wspolrzedne_t.append(wspolrzedne_t[x]+deltax2) 
#          plik.write(str(wspolrzedne_t[x]))
x=len(wspolrzedne_t)-1
print(x)
wspolrzedne_t.append(wspolrzedne_t[x]+deltax2/2)

for x in range(len(wspolrzedne_t)):
    print(wspolrzedne_t[x])



dx=[]
for x in range(0,len(wspolrzedne_t)-1):
    dx.append(wspolrzedne_t[x+1]-wspolrzedne_t[x])
    #plik.write('\n')


przewodnosc=[]
for x in wspolrzedne_t:         
    if round(x,10) < round(g1,10):
        przewodnosc.append(przewodnosc1)
                
    else:
        przewodnosc.append(przewodnosc2)              
print("\n")
temp0=[]
temperatura=[]


for x in wspolrzedne_t:
    temperatura.append(temp_poczatkowa)         
#          temp1.append(temp_poczatkowa)         
#
print('dx      wspolrzedne     przewodnosc  temperatura')
for x in range(0,len(wspolrzedne_t)-1):         
    print(dx[x]," ",wspolrzedne_t[x+1]," ",przewodnosc[x+1]," ",temperatura[x+1])
        
         
# print wspolrzedne_t[len(wspolrzedne_t)-1]          
print("suma dx",sum(dx))                 
# sys.exit()         
print(len(dx))
# sys.exit()    



ilosc_geometrii=len(wspolrzedne_t)-1
print("ilosc w dx",len(dx)-1)
print(temperatura)
warunek=10.0
time_begin = time.time()
while warunek>1e-8:
# while czas<(dczas*1000):
#          plik.write(str(czas)+":\n")
    iteracje=iteracje+1
#temperatura w polowie warstwy 0 -> blisko powierzchni wewnetznej warunek brzegowy q=0
    temperatura[0]=temperatura[1]+dx[0]*q1/przewodnosc[0]

        
    for x in range(1,ilosc_geometrii):      
                temperatura[x]=(temperatura[x-1]*przewodnosc[x-1]*dx[x]+ \
                temperatura[x+1]*przewodnosc[x]*dx[x-1])/ \
                (przewodnosc[x-1]*dx[x] + przewodnosc[x]*dx[x-1])
                #print wspolrzedne_t[x]

        
    #print ilosc_geometrii," ",wspolrzedne_t[ilosc_geometrii]," ",przewodnosc[ilosc_geometrii]," dx:",dx[ilosc_geometrii-1]
    
    temperatura[ilosc_geometrii]=(temperatura[ilosc_geometrii-1]*przewodnosc[ilosc_geometrii-1]/dx[ilosc_geometrii-1]+ alfa2*temp_otoczenia)/(przewodnosc[ilosc_geometrii-1]/dx[ilosc_geometrii-1] + alfa2)
    #print iteracje
    #plik.write(str(n+1)+" "+str(temperatura[1][n+1])+"\n")
    warunek=q1-(temperatura[0]-temperatura[1])*przewodnosc[0]/dx[0]
    #sys.exit()


	
for x in range(ilosc_geometrii+1):
    plik.write(str(wspolrzedne_t[x])+" "+str(temperatura[x])+"\n")
# print temperatura
print("iteracje =",iteracje)
spadek_temp=q1*(g1/przewodnosc1+g2/przewodnosc2+1/alfa2)
t1=spadek_temp+temp_otoczenia
print("obliczone temperatury => t1= ",t1)
print("t2 = ",t1-q1*g1/przewodnosc1)
plik.close()
print("bye\n")
print("calculation took ",time.time()-time_begin)
