T=[]
N=[]

for i in range(0,1):
    N.append(input(f"Donner le nom et prénom du client n'{i+1} : "))
    nbr_a=int(input(f"Donner le nombre d’article pour le client n`{i+1} : "))
    s=0
    pttc=0
    for j in range(0,nbr_a):
        p=float(input(f"Donner le prix de l’article {j+1} : "))
        pht=p-p*0.02
        tva=pht*0.15
        pttc=pht+tva
        s=s+pttc
    
    T.append(s)

for i in range(0,1):
    print(f"Le Total à payer pour le client {N[i]} est : {T[i]}")

 