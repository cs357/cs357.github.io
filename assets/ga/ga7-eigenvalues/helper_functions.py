#
# EXTRA INPUT FUNCTIONS THAT THE STUDENTS NEED TO ACCESS
# TO COMPLETE THE GENERALIZED EIGENSOLVER
#
import numpy as np

def compute_P(C,N):
    n,_ = C.shape
    P = np.zeros((n,n))

    for nu in range(n):
        for mu in range(n):

            for a in range(int(N/2)):
                P[mu,nu] += C[mu,a]*C[nu,a]
    P = 2.*P
    return P

def compute_Fock(C):

    H = np.load('H.npy')
    eri = np.load('eri.npy')
    P = compute_P(C,10)

    m,n  = H.shape
    F = np.zeros((m,n))

    #et = eri.transpose(0,3,2,1)
    for mu in range(n):
        for nu in range(n):
            F[mu,nu] = H[mu,nu]
            for lam in range(n):
                for sig in range(m):
                    F[mu,nu] = F[mu,nu] + P[lam,sig] * (eri[mu,nu,sig,lam] - 0.5*eri[mu,lam,sig,nu])
    #F = H + G
    return F
