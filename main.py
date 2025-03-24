import yt_dlp
import customtkinter as ctk

# Funcoes 
def baixar_video():
    label3.configure(text="")
    app.update_idletasks() # Força atualizar a pagina 

    url = tb.get()

    if cbox.get() == "VIDEO":
        ydl_opts = {
            'format': 'bestvideo[height<=1080][vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', #[vcodec^=avc1] força a baixar um video com a resolução avc1 ao inves da av1 case possivel
            'outtmpl': 'videos/%(title)s.%(ext)s', 
            'merge_output_format': 'mp4',
        }

    elif cbox.get() == "MUSICA":
        ydl_opts = {
            'format': 'bestaudio/best', 
            'outtmpl': 'musicas/%(title)s.mp3',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        label3.configure(text="SUCESSO", text_color="green")

    except Exception as e:
        label3.configure(text="FALHA", text_color="red")


# Config aparencia
ctk.set_appearance_mode('system')

# Config janela
app = ctk.CTk()
app.iconbitmap("icone.ico")
app.title("DOWNLOAD YT VIDEOS")
app.geometry("300x300")
app.resizable(False, False)

# Config camps
label1 = ctk.CTkLabel(app, text="TIPO DE ARQUIVO")
label1.pack()

cbox = ctk.CTkComboBox(app, width=75, height=15, values=["VIDEO", "MUSICA"])
cbox.pack(pady=10)

label2 = ctk.CTkLabel(app, text="COLE SUA URL")
label2.pack()


tb = ctk.CTkEntry(app, placeholder_text="URL")
tb.pack(pady=10)


button = ctk.CTkButton(app, text='DOWNLOAD', command=baixar_video, fg_color="#fa3e25", text_color="#fff", hover_color="#fa5f4b")
button.pack()

label3 = ctk.CTkLabel(app, text="")
label3.pack(pady=10)


labelcopy = ctk.CTkLabel(app, text="@Author: DIOGO LEITE \n@Version: 0.1", text_color="#b3b3b3")
labelcopy.pack()

# Iniciar APP
app.mainloop()

# @Version: 0.1
# @Author: Diogo Leite