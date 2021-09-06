import PySimpleGUI as sg

sg.ChangeLookAndFeel("DarkBlue")

WIN_W = 90
WIN_H = 25
filename = None

file_new = "Novo      (CTRL+N)"
file_open = "Abrir     (CTRL+O)"
file_save = "Salvar     (CTRL+S)"

sg.Text()
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save, "Salvar como", "---", "Sair"]],
    ["Ferramentas", ["Transformar caixa alta", "Transformar caixa baixa", "Palavras Contadas"]],
    ["Caminho", ["Segredo dos Campeões", "Começos", "Tempestades", "Visão", "Impossível?", "Limites"]],
)

layout = [
    [sg.MenuBar(menu_layout)],
    [
        sg.Multiline(
            font=("Baskerville", 15), text_color="white", size=(WIN_W, WIN_H), key="_BODY_"
        )
    ],
]

window = sg.Window(
    "Notepad",
    layout=layout,
    margins=(0, 0),
    resizable=True,
    return_keyboard_events=True,
)
window.read(timeout=1)

window["_BODY_"].expand(expand_x=True, expand_y=True)


def new_file() -> str:
    window["_BODY_"].update(value="")
    filename = None
    return filename

def open_file() -> str:
    try:
        filename: str = sg.popup_get_file("Open file", no_window=True)
    except:
         return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            window["_BODY_"].update(value=f.read())
    return filename

def save_file(filename: str):
    if filename not in (None, ""):
        with open(filename,"w") as f:
            f.write(values.get("_BODY_"))
    else:
        save_file_as()


def save_file_as() -> str:
    try:
        filename: str = sg.popup_get_file(
            "Salvar como",
            save_as=True,
            no_window=True,
            default_extension=" .txt",
            file_types=(("Text", " .txt"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    return filename       

def transformar_caixa_baixa():
    window["_BODY_"].update(value=str(values["_BODY_"]).lower())

def transformar_caixa_alta():
    window["_BODY_"].update(value=str(values["_BODY_"]).upper())

def contar_palavras():
    palavras: list = [w for w in values["_BODY_"].split(" ") if w != "\n"]
    contar_palavras: int = len(palavras)
    sg.PopupQuick("Palavras Contadas: {:,d}".format(contar_palavras), auto_close=False)

def exibir_segredo_dos_campeoes():
    sg.PopupOK(
        """ Constância constrói caráter - Pedro Marins"""       
    )

def exibir_comecos():
    sg.PopupOK(
        """ Todas as grandes coisas têm pequenos começos - Peter Senge"""
    )

def exibir_tempestades():
    sg.PopupOK(
        """ A vida é uma tempestade(...) Um dia você está tomando sol
        e no dia seguinte o mar te lança contra as rochas.
        O que faz de você um homem é o que você faz quando a tempestade vem - Alexandre Dumas """        
    )

def exibir_visao():
    sg.PopupOK(
        """" Tudo depende do tipo de lente que você utiliza para ver as coisas - Jostein Gaarder"""
    )

def exibir_impossivel():
    sg.PopupOK(
        """ O Homem não teria alcançado o possível se, repetidas vezes,
        não tivesse tentado o impossível - Max Weber"""
    )

def exibir_forca():
    sg.PopupOK(
        """ A única maneira de saber o quão forte você é,
        é continuar testando seus limites - Superman"""
        )

while True:
    event, values = window.read()

    if event in (None, "Sair"):
        window.close()
        break
    if event in (file_new, "n:78"):
        filename = new_file()
    if event in (file_open, "o:79"):
        filename = open_file()
    if event in (file_save, "s:83"):
        save_file(filename)
    if event in ("Salvar como",):
        filename = save_file_as()
    if event == "Transformar caixa alta":
        transformar_caixa_alta()
    if event == "Transformar caixa baixa":
        transformar_caixa_baixa()
    if event == "Palavras Contadas":
        contar_palavras()
    if event == "Segredo dos Campeões":
        exibir_segredo_dos_campeoes()
    if event == "Começos":
        exibir_comecos()
    if event == "Tempestades":
        exibir_tempestades()
    if event == "Visão":
        exibir_visao()
    if event == "Impossível?":
        exibir_impossivel()
    if event == "Limites":
        exibir_forca()

Notepad = Notepad()
Notepad.Iniciar()