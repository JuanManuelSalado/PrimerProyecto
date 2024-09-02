import tkinter as tk
from tkinter import font    
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.Util_ventana as util_ventana
import util.Util_imagenes as util_img

# contructor maestro de formulario principal
class formularioMaestroDesign(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.jpg", (560, 136))
        self.perfil = util_img.leer_imagen("./imagenes/perfil.jpg", (100, 100))
        self.config_windows()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_windows(self):
        # Configuracion inicial de la ventana
        self.title('Menu Principal')
        self.iconbitmap("./imagenes/icono.png")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    
    def paneles(self):
        self.barra_superior =tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)   
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both',expand=True)

    def controles_cuerpo(self):
        # imagen centrada del logo
        label = tk.Label(self.cuerpo_principal, image=self.logo, 
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    # barra superior
    def controles_barra_superior(self):
        font_awesome = font.Font(family='fontAwesome', size=12)

        # etiquetas de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="autodidacta")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Boton principal del menu lateral

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="MENU", font=font_awesome, 
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion

        self.labelTitulo = tk.Label(self.barra_superior, text="informacion general")
        self.labelTitulo.config(fg='#fff', font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)


     # CONFIGURAR MENU LATERAL
    def controles_menu_lateral(self):
        # Configuracion del menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='fontAwesome', size=15)

        # Configuracion de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Creacion de los botones

        self.ButtonPrueba1 = tk.Button(self.menu_lateral)
        self.ButtonPrueba2 = tk.Button(self.menu_lateral)
        self.ButtonPrueba3 = tk.Button(self.menu_lateral)
        self.ButtonPrueba4 = tk.Button(self.menu_lateral)
        self.ButtonPrueba5 = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Boton 1", "\uf109", self.ButtonPrueba1),
            ("Boton 2", "\uf007", self.ButtonPrueba2),
            ("Boton 3", "\uf03e", self.ButtonPrueba3),
            ("Boton 4", "\uf129", self.ButtonPrueba4),
            ("Boton 5", "\uf013", self.ButtonPrueba5),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f" {icon}  {text}",anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):  
        #asociar eventas Enter y leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, envent, button):
        # Cambia estilo al pasar el raton
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, envent, button):
        # Cambia estilo al salir con el raton
        button.config(bg=COLOR_MENU_LATERAL, fg='white')
    
    def toggle_panel(self):
        # alternar visibilidad del menu lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')