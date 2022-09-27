from re import search


class Contact:
    def __init__(self, fullname, phonenum, mailad):
        self.fullname = fullname
        self.phonenum = phonenum
        self.mailad = mailad
        try:
            self.f = self.fullname.split(" ")[0]
        except:
            self.f = None
        try:
            self.i = self.fullname.split(" ")[1]
        except:
            self.i = None
        try:
            self.o = self.fullname.split(" ")[2]
        except:
            self.o = None

class DB:
    def __init__(self):
        path = input("Input full path to the data base:")
        self.Contacts = []
        with open(path) as f:
            lines = f.readlines()
        for l in lines:
            fullname, phonenum, mailad = list(l.split(","))
            k = Contact(fullname,phonenum,mailad)
            self.Contacts.append(k)
        self.run()
    def search(self,f,i,o,fio,phonenum,email,mode):
        arr = []
        for ii in range(0,len(self.Contacts)):
            c = self.Contacts[ii]
            if mode == "fio":
                fio_arr = fio.split(" ")
                carr = [c.f,c.i,c.o]
                B = True 
                for i in range(0,len(fio_arr)):
                    if fio_arr[i] not in carr:
                        B = False
                if B: 
                    arr.append((c,ii))
            elif mode == "f":
                if f == c.f:
                    arr.append((c,ii))
            elif mode == "i":
                if i==c.i:
                    arr.append((c,ii))
            elif mode == "o":
                if o==c.o:
                    arr.append((c,ii))
            elif mode == "phonenum":
                if phonenum.strip() == c.phonenum.strip():
                    arr.append((c,ii))
            elif mode == "email":
                if email.strip() == c.mailad.strip():
                    arr.append((c,ii))
        return arr
    def run(self):
        while True:
            n = input("Input command:")
            if n == "BREAK":
                print("Shutting down")
                break
            elif n=="SEARCH":
                #Пушкин,,,,,,fio
                #/Users/george/Desktop/Uni/bd.txt
                s = input("Type in what you want to search:")
                if s[0] == "+":
                    res = self.search("","","","",s,"","phonenum")
                elif "@" in s:
                    res = self.search("","","","","",s,"email")
                else:
                    res = self.search("","","",s,"","","fio")
                print("SEARCH RESULTS:")
                for i in res:
                    print(i[1], i[0].fullname, i[0].phonenum, i[0].mailad)
            elif n=="SEARCH EMPTY":
                for c in self.Contacts:
                    if c.phonenum == "" and c.mailad == "":
                        print(c.fullname, "", "")
            elif n=="CHANGE CONTACT":
                s = input("Input the fullname of the contact you would like to change:")
                aux = self.search("","","",s,"","","fio")
                for i in aux:
                    print(i[1], i[0].fullname)
                nn = input("Confirm your input by typing the number of the desired contact: ")
                edit_data = input("Input the changed fio,phonenum,email with commas in between: ")
                self.edit(int(nn),*list(edit_data.split(",")))
                print("Contact has been succesfully updated")
            elif n=="DISPLAY":
                for c in range(0,len(self.Contacts)):
                    print(c,self.Contacts[c].fullname, self.Contacts[c].phonenum, self.Contacts[c].mailad)
            elif n=="HELP":
                print('''
                The list of all commands:
                    BREAK
                    SEARCH
                    SEARCH EMPTY 
                    CHANGE CONTACT
                    DISPLAY
                    HELP
                ''')
            else:
                print("Command does not exist. Type HELP for the list of available commands.")
    def edit(self,n_contact,fio,phonenum,email):
        cc = self.Contacts[n_contact]
        cc.phonenum = phonenum
        cc.fullname = fio
        cc.mailad = email
        self.Contacts[n_contact] = cc 




db = DB()