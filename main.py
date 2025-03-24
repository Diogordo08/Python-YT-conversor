import yt_dlp
import customtkinter as ctk
from tkinter import filedialog

# Funcoes 
def mudar_aparencia(value):
    ctk.set_appearance_mode(value)
    
    app.update_idletasks()

def baixar_video():
    label3.configure(text="Aguarde...", text_color=("#000", "#fff"))
    app.update_idletasks() # Força atualizar a pagina 
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")

    url = tb.get()
    
    if cbox.get() == "VIDEO":
        if checkBox.get() == 1:
            ydl_opts = {
                'format': 'bestvideo[height<=1080][vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', #[vcodec^=avc1] força a baixar um video com a resolução avc1 ao inves da av1 case possivel
                'outtmpl': f'{pasta_destino}/%(playlist)s/%(title)s.%(ext)s', 
                'merge_output_format': 'mp4',
            }
        else: 
            ydl_opts = {
                'format': 'bestvideo[height<=1080][vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s', 
                'merge_output_format': 'mp4',
            }

    elif cbox.get() == "MUSICA":
        if checkBox.get() == 1:
            ydl_opts = {
                'format': 'bestaudio/best', 
                'outtmpl': f'{pasta_destino}/%(playlist)s/%(title)s.mp3',
            }
        else:
            ydl_opts = {
                'format': 'bestaudio/best', 
                'outtmpl': f'{pasta_destino}/%(title)s.mp3',
            }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        label3.configure(text="SUCESSO", text_color="#1fcf00")

    except Exception as e:
        label3.configure(text="FALHA", text_color="#cf0a00")


# Config aparencia
ctk.set_appearance_mode('system')

# Config janela
app = ctk.CTk()
app.iconbitmap("_internal/.icon/icone.ico") # <-- LEMBRAR DE ALTERAR
app.grid_columnconfigure((0, 1, 2), weight=2, uniform="equal")
app.title("DOWNLOAD YT VIDEOS")
app.geometry("320x400")
app.resizable(False, False)


# Config camps
aparencia = ctk.CTkOptionMenu(app, width=100, height=10, values=["DARK", "LIGHT"], command=mudar_aparencia, fg_color=("#d6d6d6","#4f4f4f"), text_color=("#4f4f4f","#d6d6d6"), button_color=("#d6d6d6","#4f4f4f"), button_hover_color=("#4f4f4f","#d6d6d6"))
aparencia.pack(padx=(175,0), pady=(5,0))

label1 = ctk.CTkLabel(app, text="TIPO DE ARQUIVO")
label1.pack(pady=(10, 0))

cbox = ctk.CTkComboBox(app, width=75, height=15, values=["VIDEO", "MUSICA"])
cbox.pack(pady=(10, 0))

checkBox = ctk.CTkCheckBox(app, checkbox_width=20, checkbox_height=20, width=5, height=5, text="Playlist", fg_color=("#ff978a", "#ff1d00"), hover=False)
checkBox.pack(pady=(10, 0))

label2 = ctk.CTkLabel(app, text="COLE SUA URL")
label2.pack(pady=(10, 0))

tb = ctk.CTkEntry(app, placeholder_text="URL")
tb.pack(pady=(0, 10))

button = ctk.CTkButton(app, text='DOWNLOAD', command=baixar_video, fg_color=("#ff978a", "#ff1d00"), hover_color=("#ffc0b8", "#fa5f4b"), text_color=("#000", "#fff"))
button.pack(pady=10)

label3 = ctk.CTkLabel(app, text="")
label3.pack(pady=10)




labelcopy = ctk.CTkLabel(app, text="@Author: DIOGO LEITE \n@Version: 0.5", text_color="#b3b3b3")
labelcopy.pack(pady=(20, 10))

# Iniciar APP
app.mainloop()

# @Version: 0.5
# @Author: Diogo Leite