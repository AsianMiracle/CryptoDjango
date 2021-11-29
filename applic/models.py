from Crypto.Util.number import *
from random import *


class RSA():
    def __init__(self, bitsize, e = 65537):
        self.p = getPrime(bitsize)
        self.q = getPrime(bitsize)
        self.n = self.p * self.q
        self.phi = (self.p - 1)* (self.q - 1)
        
        while GCD(e , self.phi) != 1:
            e += 1
        self.e = e
        self.d = inverse(e, self.phi)

    def encrypt(self,M):
        M = bytes_to_long(M.encode())
        C = pow(M , self.e, self.n)
        return C
        
    def decrypt(self,C):
        M_ = pow(C , self.d , self.n)
        M_ = long_to_bytes(M_)
        return M_


class Rabin():
    def __init__(self, bitsize):
        p = getPrime(bitsize)
        q = getPrime(bitsize)
        while p%4 != 3:
            p = getPrime(bitsize)
        
        while q%4 != 3:
            q = getPrime(bitsize)
        self.p = p
        self.q = q
        self.n = p*q
        self.e = 2
    def encrypt(self,M):
        M = bytes_to_long(b"Mes:"+M.encode())
        C = pow(M,self.e, self.n)
        return C
    def decrypt(self, C):
        mp1 = pow(C , (self.p+1)//4,self.p)
        mq1 = pow(C , (self.q +1)//4, self.q)
        mp2 = (self.p - pow(C , (self.p+1)//4,self.p))% self.p
        mq2 = (self.q - pow(C , (self.q +1)//4, self.q)) % self.q
        a = self.q * inverse(self.q , self.p)% self.n
        b = self.p * inverse(self.p , self.q)% self.n
        M1 = (mp1 * a + mq1 * b)%self.n
        M2 = (mp1 * a + mq2 * b)%self.n
        M3 = (mp2 * a + mq1 * b)%self.n
        M4 = (mp2 * a + mq2 * b)%self.n
        M1 = long_to_bytes(M1)
        M2 = long_to_bytes(M2)
        M3 = long_to_bytes(M3)
        M4 = long_to_bytes(M4)
        return mp1,mq1,mp2,mq2,a,b,[M1,M2,M3,M4]


class EL_Gamal():
    def __init__(self,bitsize):
        try:
            self.p = getStrongPrime(bitsize)
        except:
            self.p = getPrime(bitsize)
        self.g = 2
    def public_key(self):
        x = randint(1,self.p - 1)
        y = pow(self.g,x,self.p)
        return x,y
    def encrypt(self,M , y):
        M = bytes_to_long(M.encode())
        R = randint(1 , self.p - 1)
        C_ = pow(self.g,R,self.p)
        C__ = pow(y, R,self.p)*M%self.p
        return (C_,C__),R
    def decrypt(self, C_,C__,x):
        Z = pow(C_,x,self.p)
        Z_inv = inverse(Z,self.p)
        M_ = C__ * Z_inv % self.p
        M_ = long_to_bytes(M_)
        return Z,Z_inv,M_


class Diffie_Hellman():
    def __init__(self,bitsize):
        try:
            self.p = getStrongPrime(bitsize)
        except:
            self.p = getPrime(bitsize)
        self.g = 2
    def public_key_gen(self):
        x = randint(1,self.p - 1)
        y = pow(self.g,x,self.p)
        return x,y
    def Shared_secret_gen(self,x1,y2):
        shared = pow(y2,x1,self.p)
        return shared


class EDS_RSA():
    '''ЭЦП RSA'''
    def __init__(self,bitsize, e = 65537):
        self.p = getPrime(bitsize)
        self.q = getPrime(bitsize)
        self.n = self.p * self.q
        self.phi = (self.p - 1)* (self.q - 1)
        
        while GCD(e , self.phi) != 1:
            e += 1
        self.e = e
        self.d = inverse(e, self.phi)
    def sign(self,M):
        M = bytes_to_long(M.encode())
        S = pow(M , self.d, self.n)
        return(S)
    def verify(self,S,M):
        M_ = pow(S , self.e , self.n)
        M_ = long_to_bytes(M_).decode()
        if M_ == M:
            return "Подпись верна"
        else:
            return "Подпись неверна"
