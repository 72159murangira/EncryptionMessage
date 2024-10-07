from tkinter import *
from tkinter import messagebox
import base64

# Function to decrypt the text
def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get("1.0", END).strip()  # Get the input text from the main screen
        try:
            base64_bytes = base64.b64decode(message.encode("ascii"))
            decrypted_message = base64_bytes.decode("ascii")
        except Exception:
            messagebox.showerror("Decryption Error", "An error occurred during decryption.")
            return

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "input Password")
    else:
        messagebox.showerror("encryption", "Invalid password")

# Function to encrypt the text
def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get("1.0", END).strip()  
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "input Password")
    else:
        messagebox.showerror("encryption", "Invalid password")

# Context menu functions
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def copy_text():
    screen.clipboard_clear()
    screen.clipboard_append(text1.selection_get())

def cut_text():
    copy_text()
    text1.delete("sel.first", "sel.last")

def paste_text():
    try:
        text = screen.clipboard_get()
        text1.insert(INSERT, text)
    except TclError:
        pass  

# Main application window
def main_screen():
    global screen, code, text1, context_menu
    screen = Tk()
    screen.geometry("375x398")

    # Icon
    image_icon = PhotoImage(file=r"C:\Users\Johnm\Desktop\Python\EncryptMe\images\security.png")
    screen.iconphoto(False, image_icon)
    screen.title("EncryptMe")

    Label(text="Enter text for Encryption or Decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=SUNKEN, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for Encryption and Decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    # Context menu for the Text widget
    context_menu = Menu(screen, tearoff=0)
    context_menu.add_command(label="Copy", command=copy_text)
    context_menu.add_command(label="Cut", command=cut_text)
    context_menu.add_command(label="Paste", command=paste_text)

    text1.bind("<Button-3>", show_context_menu)  # Bind right-click menu to text box

    Button(text="ENcrypt", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DEcrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=23, bg="#1089FF", fg="white", bd=0, command=lambda: text1.delete("1.0", END)).place(x=10, y=300)

    screen.mainloop()

main_screen()
