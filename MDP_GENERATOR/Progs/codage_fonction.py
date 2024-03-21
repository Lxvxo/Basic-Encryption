# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:52:13 2021

@author: singl
"""

alphabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet2 = 'abcdefghijklmnopqrstuvwxyz'
def Cesar(S,n):
    R = ''
    for i in S:
        b = 0
        for k in range(26):
            if i == ' ':
                R+= ' ' 
                break
            elif i in alphabet1:
                if i == alphabet1[k]:
                    b = k+n
                    if b <= 25:
                        R+=alphabet1[b]
                        break
                    else:
                        while b > 25:
                            b -= 26
                        R += alphabet1[b]
                        break
            else:
                if i == alphabet2[k]:
                    b = k+n
                    if b <= 25:
                        R+=alphabet2[b]
                        break
                    else:
                        while b > 25:
                            b -= 26
                        R += alphabet2[b]
                        break
    return R
                    
def Code(S,p,n=1):
    A = S
    for k in range(n):
        A = Cesar(A,p)
    return A
def decode(S,p,n=1):
    A = S
    for k in range(n):
        A = Cesar2(A,-p)
    return A


def codage(ficher,S,p,n=1):
    ouvert = open(ficher,'a')
    ouvert.write(Code(S,p,n)+'\n')
    ouvert.close()
def decodage(fichier,p,n=1):
    ouvert = open(fichier,'r')
    message_decode = decode(ouvert.read(),p,n)
    ouvert.close()
    ouvert = open(fichier,"w")
    ouvert.write(message_decode + "\n")
    

def Cesar2(S,n):
    R = ''
    for i in S:
        b = 0
        for k in range(26):
            if i == ' ':
                R+= ' ' 
                break
            elif i in alphabet1:
                if i == alphabet1[k]:
                    b = k+n
                    if b >=0:
                        R+=alphabet1[b]
                        break
                    else:
                        while b < 0:
                            b += 26
                        R += alphabet1[b]
                        break
            else:
                if i == alphabet2[k]:
                    b = k+n
                    if b >=0:
                        R+=alphabet2[b]
                        break
                    else:
                        while b < 0:
                            b += 26
                        R += alphabet2[b]
                        break
    return R

def trouver(code,S,n,l):
    m = decodage(code,S,n)
    if l in m:
        return (m,S,n)
    for k in range(100):
        S += 1
        for i in range(100):
            n=1
            m = decodage(code,S,n+i)
            if l in m:
                return (m,S,n+i)
    return "pas de résultat"
    

