
from tkinter import *
from Ventana.ConsultaReo import *


def main():
    root = Tk()
    root.wm_title("Consulta de presos")
    app = Ventana(root) 
    app.mainloop()
if __name__ == "__main__":
    main()