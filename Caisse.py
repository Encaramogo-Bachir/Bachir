# Bachir

from tkinter import *

clt= Tk()
clt.title('Caisse')
clt.minsize(width=700, height=500)
clt.maxsize(width=700, height=500)


mnu=Menu(clt)
fchr1=Menu(mnu, tearoff=0)
fchr1.add_command(label="Créer")
fchr1.add_command(label="Editer")
fchr1.add_command(label="Enregistrer")
fchr1.add_separator()
fchr1.add_command(label="Quiter", command=clt.quit)
mnu.add_cascade(label='Fichier', menu=fchr1)


fchr2=Menu(mnu, tearoff=0)
fchr2.add_command(label="Copier")
fchr2.add_command(label="Coller")
fchr2.add_command(label="Supprimer")
mnu.add_cascade(label='Editer', menu=fchr2)


fchr3=Menu(mnu, tearoff=0)
fchr3.add_command(label="Theme")
fchr3.add_command(label="zoom")
fchr3.add_command(label="Disposition")
mnu.add_cascade(label='Fichier', menu=fchr3)


fchr4=Menu(mnu, tearoff=0)
fchr4.add_command(label="Client")
fchr4.add_command(label="Caissier")
fchr4.add_command(label="Poduit")
fchr4.add_command(label="Commande fournisseur")
fchr4.add_command(label="Site")
fchr4.add_command(label="Prise en charge")
fchr4.add_command(label="stock produit")
fchr4.add_command(label="Fournisseur")
fchr4.add_command(label="Service")
mnu.add_cascade(label='Table', menu=fchr4)




clt.config(menu=mnu)

Label(clt, text='Espace du Caissier').pack()
Label(clt, text='Matricule du Caissier:').place(x=150, y=50)
Num_caissier=Entry(clt,).place(x=300, y=50)
Label(clt, text='Nom du Caissier:').place(x=150, y=100)
Nom_caissier=Entry(clt,).place(x=300, y=100)
Label(clt, text='Prénom du Caissier:').place(x=150, y=150)
prenom_caissier=Entry(clt,).place(x=300, y=150)
Label(clt, text='Contact du Caissier').place(x=150, y=200)
type_clent=Entry(clt,).place(x=300, y=200)
Button(clt, text='Suprimer').place(x=200, y=250)
Button(clt, text='Valider').place(x=400, y=250)
Label(clt, text='Viellez bien vérifier vos saisir avant de les valider').place(x=200, y=400)









clt.mainloop()
