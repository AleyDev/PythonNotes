import tkinter as tk
from tkinter import ttk  # ComboBox (Açılır Liste) için gerekli modül,ya da "from tkinter import *" yaparak tüm tkinter'ı dahil edebiliriz



# Ana pencereyi oluşturuyorum
root = tk.Tk()
root.title("Tkinter Widget Örnekleri")  # Pencerenin başlığını ayarlıyorum
root.geometry("450x300")  # Pencere boyutunu ayarlıyorum
root.minsize(width=600, height=600)    # Pencerenin minimum boyutunu ayarlıyorum
root.config(padx=20, pady=20)          # Pencere çevresine boşluk ekliyorum




# Label (Etiket) Widget'ı
label = tk.Label(text="This is a label", font=('Arial', 20, 'italic'))
label.config(bg="black", fg="white")  # Arka plan ve yazı rengini ayarlıyorum
label.config(padx=20, pady=20)        # Etiket çevresine boşluk ekliyorum
# label.pack(side="top")
# label.place(x=0, y=0)
label.grid(row=0, column=0)           # Grid yöntemiyle etiketi konumlandırıyorum
label.pack()                          # Pack yöntemi ile etiketi pencereye yerleştiriyorum




# Button (Buton) Widget'ı
def button_clicked():
    user_input = entry.get()  # Entry widget'ından (tek satırlı giriş) kullanıcı girişini alıyorum
    print(user_input)            # Kullanıcı girişini konsola yazdırıyorum
    print("Butona tıklandı")     # Butona tıklama bilgisini konsola yazdırıyorum
    print(text.get("1.0", tk.END))  # Text widget'ından (çok satırlı metin) ilk satır ve sütundan başlayarak veriyi alıyorum

button = tk.Button(text="Tıkla", command=button_clicked)
# button.grid(row=1, column=1)  # Grid yöntemiyle butonu konumlandırıyorum
button.config(padx=10, pady=10)  # Buton çevresine boşluk ekliyorum
# button.place(x=225-22, y=150-26.5)
# button.update()
# print(button.winfo_height()) # Konum üstten 44 boşluk var, yarısını aldım
# print(button.winfo_width()) # Konum yandan 53 boşluk var, yarısını aldım
# button.grid(row=1, column=1)
button.pack()  # Pack yöntemi ile butonu pencereye yerleştiriyorum



# Entry (Tek Satırlık Giriş- Singleline) Widget'ı
entry = tk.Entry(width=20)
entry.focus()  # Program başladığında imleci giriş alanına odaklıyorum
# entry.grid(row=3, column=2)  # Grid yöntemiyle giriş alanını konumlandırıyorum
entry.place(x=300, y=200) # Konumlandırma 
entry.pack()



# Text (Çok Satırlı Giriş- Multiline) Widget'ı
text = tk.Text(width=30, height=10)
text.focus() # Program başladığında imleci giriş alanına odaklıyorum
text.pack()  # Pack yöntemiyle metin alanını pencereye yerleştiriyorum



# Scale (Kaydırma Çubuğu) Widget'ı
def scale_selected(value):
    print(value)  # Kaydırma çubuğunda seçilen değeri yazdırıyorum

scale = tk.Scale(from_=0, to=50, command=scale_selected)  # 0 ile 50 arasında bir kaydırma çubuğu oluşturuyorum

# scale = Scale(from_=0, to=50)
scale.pack()  # Pack yöntemiyle kaydırma çubuğunu pencereye yerleştiriyorum



# Spinbox (Değer Seçme Kutusu) Widget'ı
def spinbox_selected():
    print(my_spinbox.get())  # Spinbox'ta seçilen değeri yazdırıyorum

my_spinbox = tk.Spinbox(from_=0, to=10, command=spinbox_selected)
my_spinbox.pack()  # Pack yöntemiyle spinbox'ı pencereye yerleştiriyorum



# Checkbutton (Çoklu Seçenek) Widget'ı
def checkbutton_selected():
    print(check_state.get())  # Checkbutton durumunu yazdırıyorum
    
check_state = tk.IntVar()  # Durumu bir değişkende saklıyorum
my_checkbutton = tk.Checkbutton(text="Check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()  # Pack yöntemiyle checkbutton'ı pencereye yerleştiriyorum



# Radiobutton (Tek Seçenek) Widget'ı
def radio_selected():
    print(radio_checked_state.get())  # Seçili radiobutton'un durumunu yazdırıyorum

radio_checked_state = tk.IntVar()  # Durumu bir değişkende saklıyorum
my_radiobutton = tk.Radiobutton(text="1. Seçenek", value=10, variable=radio_checked_state)
my_radiobutton_2 = tk.Radiobutton(text="2. Seçenek", value=20, variable=radio_checked_state)

my_radiobutton.pack()  # Pack yöntemiyle ilk radiobutton'ı pencereye yerleştiriyorum
my_radiobutton_2.pack()  # Pack yöntemiyle ikinci radiobutton'ı pencereye yerleştiriyorum



# Listbox (Liste Kutusu) Widget'ı
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))  # Seçilen liste elemanını yazdırıyorum

my_listbox = tk.Listbox()
name_list = ["Aley", "Tu", "Abc", "Ugurlu"]  # Listeye ekleyeceğim elemanlar
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])  # Elemanları listeye ekliyorum
my_listbox.bind('<<ListboxSelect>>', listbox_selected)  # Liste elemanı seçildiğinde bir olay tetikliyorum
my_listbox.pack()  # Pack yöntemiyle liste kutusunu pencereye yerleştiriyorum



# ComboBox (Açılır Liste) Widget'ı
def combobox_selected(event):
    print(combo.get())  # Seçilen ComboBox elemanını yazdırıyorum

combo = ttk.Combobox(root)
combo['values'] = ("Python", "Java", "C++", "JavaScript")  # Açılır liste elemanlarını belirliyorum
combo.current(0)  # İlk elemanı varsayılan olarak seçili yapıyorum
combo.bind("<<ComboboxSelected>>", combobox_selected)  # Eleman seçildiğinde bir olay tetikliyorum
combo.pack()  # Pack yöntemiyle açılır listeyi pencereye yerleştiriyorum



# Menü Oluşturma
def new_file():
    print("Yeni dosya oluştur")

def open_file():
    print("Dosya aç")

def save_file():
    print("Dosyayı kaydet")

menubar = tk.Menu(root)  # Menü çubuğunu oluşturuyorum

# Dosya Menüsü
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Yeni", command=new_file)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çıkış", command=root.quit)
menubar.add_cascade(label="Dosya", menu=file_menu)

# Düzen Menüsü
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Kes")
edit_menu.add_command(label="Kopyala")
edit_menu.add_command(label="Yapıştır")
menubar.add_cascade(label="Düzen", menu=edit_menu)

# Yardım Menüsü
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Yardım Al")
menubar.add_cascade(label="Yardım", menu=help_menu)

# Menü çubuğunu pencereye ekliyorum
root.config(menu=menubar)

# Pencereyi çalıştır
root.mainloop()



"""
                Açıklamalar
Label (Etiket): Kullanıcıya bilgi veren bir etiket.
Button (Buton): Bir komutu çalıştıran buton. Butona tıklandığında Entry'den alınan girdi ve Text alanındaki metin konsola yazdırılıyor.
Entry (Tek Satırlık Giriş): Kullanıcıdan tek satırlık metin girdisi almak için kullanılır.
Text (Çok Satırlı Giriş): Kullanıcıdan çok satırlı metin girdisi almak için kullanılır.
Scale (Kaydırma Çubuğu): Belirli bir aralıkta değer seçimini sağlar.
Spinbox (Değer Seçme Kutusu): Sayısal bir değer seçimini sağlar.
Checkbutton (Çoklu Seçenek): Birden fazla seçenekten birini veya birkaçını seçmek için kullanılır.
Radiobutton (Tek Seçenek): Tek seçenek seçimini sağlar.
Listbox (Liste Kutusu): Liste kutusu, birden fazla elemanı içerebilir ve seçilen eleman konsola yazdırılır.
ComboBox (Açılır Liste): Kullanıcıya birden fazla seçenek sunar ve seçilen seçenek konsola yazdırılır.
Menü: Pencerenin üst kısmında görünen menü çubuğu, dosya işlemleri ve diğer eylemler için seçenekler sunar.

"""