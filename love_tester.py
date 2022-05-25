from tkinter import *
import tkinter as tk
from tkinter import messagebox

lovecount = 0

win = tk.Tk()
win.title('Love Calculator') #ini untuk membuat judul dari program nya, yang ada disebelah ujung kiri atas

frameBoy = tk.Frame(win) #ini untuk membuat frame baru untuk sebagai wadah dari label dan input/entry prianya
labelBoy = tk.Label(frameBoy, text="Enter Boy's Name : ") #ini untuk membuat label
entryBoy = tk.Entry(frameBoy) #ini untuk membuat input textbox

#berikut juga sama fungsinya tetapi ini untuk wanitanya
frameGirl = tk.Frame(win)
labelGirl = tk.Label(frameGirl, text="Enter Girl's Name : ")
entryGirl = tk.Entry(frameGirl)

frame3 = tk.Frame(win) #frame ini untuk memberi space pada label,digunakan pada function label_spacer

frame4 = tk.Frame(win) #frame untuk menampung label chancesLabel
chancesLabel = tk.Label(frame4, text='') #label untuk menampilkan chance kecocokan
frame5 = tk.Frame(win) #frame untuk menampung label resultsLabel
resultsLabel = tk.Label(frame5, text='') #label untuk menampilkan hasil dari kecocokannya

chancesLabel.config(text="") # config ini untuk meng-konfigurasi text dari label
resultsLabel.config(text="") # config ini untuk meng-konfigurasi text dari label

#function untuk membuat spasi dari label sesuai namanya
def label_spacer(parent):
    label = tk.Label(parent, text="    ")
    label.pack(side='left')

#function untuk membuat spasi vertical atau row spacer alias untuk membuat jarak antar frame a dengan frame lainnya secara vertical
def row_spacer():
    new_row = tk.Frame(win)
    label = tk.Label(text=" ")
    label.pack()
    new_row.pack()
    
# untuk pack disini merupakan salah satu fungsi penempatan dari tkinter, ada pula grid 
# untuk lebih lanjutnya bisa baca saja documentation tkinter di internet, cukup banyak penjelasannya


#function calculate disini merupakan function yang sudah kamu buat sebelumnya yang saya modifikasi sedikit agar bisa tampil dalam bentuk GUI
def calculate():
    
    #.get() merupakan function untuk mengambil nilai dari Entry alias input textbox
    boy = entryBoy.get() #ini untuk mengambil nilai dari input nama pria nya
    girl = entryGirl.get() #ini untuk mengambil nilai dari input nama wanitanya nya
    
    if(len(boy) > 0 and len(girl) > 0) : #ini kondisi untuk cek apakah input nama pria dan wanita tidak kosong, baru jalankan code calculate
        consonants = 'qwrtypsdfghjklzxcvbnm'
        vowels = 'aeiou'
        lovecount = 0
        for vowels in boy:
            for vowels in girl:
                if vowels in boy and vowels in girl:
                    lovecount += 2
        for consonants in boy:
            for consonants in girl:
                if consonants in boy and consonants in girl:
                    lovecount + 1
        if len(boy) + len(girl) >= 25:
            lovecount -= lovecount
            messagebox.showerror("Error", "Dont type in surnames or random input") #disini print nya saya gantikan dengan messagebox, yaitu pesan popup error
        if lovecount > 100:
            lovecount = 100
        impossible = (1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97)
        enemies = (2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98)
        shyness = (3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99)
        friends = (4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100)
        slightlove = (5, 13, 21, 29, 37, 45, 53, 61, 69, 77, 85, 93)
        deeplove = (6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86, 94)
        marriage = (7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95)
        tilldeath = (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96)
        
        
        # untuk semua print dari masing-masing condition saya ubah dengan saya masukkan ke dalam variabel result yang nantinya akan ditampilkan
        # di label resultsLabel
        if lovecount in impossible:
            result = """
            \t TOTALLY HORRIBLE MATCH!!!
            \tIMPOSSIBLE
        {0} and {1} two will never be together, not even friends\n
        NEVER!!!
        """.format(boy, girl)
            lovecount = -100
        if lovecount in enemies:
            result = """
            \tENEMIES
        With {0} and {1} are enemies. They hate each other. 
        """.format(boy, girl)
            lovecount = -5
        if lovecount in shyness:
            result = """
            \tSHYNESS
        {0} and {1} atleast have a chance, but its being hindered by both of them being shy.
        """.format(boy, girl)
            lovecount = 15
        if lovecount in friends:
            result = """
            \tFRIENDS
        {0} and {1} are just friends. 
        """.format(boy, girl)
            lovecount = 20
        if lovecount in slightlove:
            result = """
            \tLSlIGHT LOVE
        With {0} and {1} there is a chance this two will fall in love and break up.
        """.format(boy, girl)
            lovecount = 30
        if lovecount in deeplove:
            result = """
            \tDEEP LOVE
        {0} and {1} will probably last long. 
        """.format(boy, girl)
            lovecount = 60
        if lovecount in marriage:
            result = """
                \tMARRIAGE
            {0}'s and {1}'s love can end up being really deep.  
            """.format(boy, girl)

            lovecount = 80

        elif lovecount in tilldeath:
            result = """
                \tTILL DEATH
            {0} and {1} will get married, and live happy life together.  
            """.format(boy, girl)

            lovecount = 100
        elif lovecount == 0:
            result = """
                \tUNKNOWN
            It is impossible to determine if {0} and {1} are compatible.
            TOO BAD!
        """.format(boy, girl)
        
        #lalu untuk menampilkan bentuk heartnya berikut code nya
        chancesLabel.config(text="""
        LOVE METER:
        ___    ___
        (   \__/   )
        \         /
       >>----- \ {0}% /------>
         \    /
         \  /
         \/
        """.format(lovecount), font=("Courier", 10)) #font disini fungsinya untuk menentukan jenis fontnya dan size hurufnya, formatnya ('nama font', size_huruf)
        
        resultsLabel.config(text=result) #lalu code ini untuk menampilkan result yang sudah saya jelaskan pada code line 78 & 79, disini lah variabel tersebut digunakan
    else : 
        #jika kondisi tidak terpenuhi alis input nama pria dan wanita kosong maka tmapilkan alert error/ pesan popup error dengan pesan berikut
        messagebox.showerror("Error", "Boys's and Girl's name can't be empty!") #format nya messagebox.jenistampilan(judul_msgbox, pesannya)
        #untuk jenis tampilan nya ada banyak bisa kamu coba lihat disini contohnya https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/

button = tk.Button(frame3,text=" CALCULATE ", command=calculate) #ini untuk membuat button calculate dengan command calculate, alias saat di klik maka akan menjalankan function calculate()

#untuk penjelasan dibawah sudah paham lah ya untuk apa, sudah ada penjelasanya diatas
#tambahan, untuk side didalam pack tersebut untuk mengatur posisinya ada top,bottom,left,right
row_spacer() 
label_spacer(frameBoy)
labelBoy.pack(side='left')
entryBoy.pack(side='left')
label_spacer(frameBoy)
frameBoy.pack()

labelGirl.pack(side='left')
entryGirl.pack(side='right')
frameGirl.pack()

row_spacer()
label_spacer(frame3)
button.pack(side='right')
frame3.pack()

row_spacer()
chancesLabel.pack()
frame4.pack()

resultsLabel.pack()
frame5.pack()
row_spacer()

#thread
win.mainloop()# ini merupakan function untuk menjalankan program nya
