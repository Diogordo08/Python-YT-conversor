import yt_dlp
import customtkinter as ctk

# Funcoes 
def baixar_video():
    url = tb.get()

    if teste.get() == "VIDEO":
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'videos/%(title)s.%(ext)s', 
            'merge_output_format': 'mp4',
        }

    elif teste.get() == "MUSICA":
        ydl_opts = {
            'format': 'bestaudio/best', 
            'outtmpl': 'musicas/%(title)s.mp3',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        label2.configure(text="SUCESSO", text_color="green")
    except Exception as e:
        label2.configure(text="FALHA", text_color="red")
        print(f"Erro: {e}")

# Config aparencia
ctk.set_appearance_mode('dark')

# Config janela
app = ctk.CTk()
app.title("DOWNLOAD YT VIDEOS")
app.geometry("300x300")

# Config camps

teste = ctk.CTkOptionMenu(app, width=10, height=10, values=["VIDEO", "MUSICA"])
teste.pack(pady=10)
# Label
label1 = ctk.CTkLabel(app, text="COLE SUA URL")
label1.pack(pady=10)

# Entry
tb = ctk.CTkEntry(app, placeholder_text="URL")
tb.pack(pady=10)

# Button
button = ctk.CTkButton(app, text='DOWNLOAD', command=baixar_video)
button.pack()

# Label feedback
label2 = ctk.CTkLabel(app, text="")
label2.pack(pady=10)

# Iniciar APP
app.mainloop()

