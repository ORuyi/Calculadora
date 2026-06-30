#!/usr/bin/env python

# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Aplicacao:

   def __init__(self):
       janela = Gtk.Window()
       janela.connect("delete-event", self.sair)
       janela.set_title("Cores")
       janela.set_border_width(10)
       box_hor = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False, spacing=10)
       box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False, spacing=10)
       
       barra_sup = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=True, spacing=10)
       botoes = Gtk.Grid()
       botoes.set_row_spacing(10)     
       botoes.set_column_spacing(10)  

       bt_arquivo = Gtk.Button(label="Arquivo")
       bt_ajuda = Gtk.Button(label="Ajuda")
       bt_sobre = Gtk.Button(label="Sobre")
       
       
       visor = Gtk.Frame(label="Escolha uma cor:")
       self.visor = Gtk.Label(label="<big>Oi leon</big>", use_markup=True)

       btn_on = Gtk.Button(label="ON")
       btn_clear = Gtk.Button(label="C")
       btn_raiz = Gtk.Button(label="\u221a")
       
       btn7 = Gtk.Button(label="7")
       btn8 = Gtk.Button(label="8")
       btn9 = Gtk.Button(label="9")
       btn_soma = Gtk.Button(label="+")

       btn4 = Gtk.Button(label="4")
       btn5 = Gtk.Button(label="5")
       btn6 = Gtk.Button(label="6")
       btn_subtracao = Gtk.Button(label="-")
       
       btn1 = Gtk.Button(label="1")
       btn2 = Gtk.Button(label="2")
       btn3 = Gtk.Button(label="3")
       btn_multiplicacao = Gtk.Button(label="*")
       
       btn0 = Gtk.Button(label="0")
       btn_igual = Gtk.Button(label="=")
       btn_divisao = Gtk.Button(label="/")

       # Coluna 0
       botoes.attach(btn_on,    0, 0, 1, 1)
       botoes.attach(btn_clear, 1, 0, 1, 1)
       botoes.attach(btn_raiz,  3, 0, 1, 1)

       # Coluna 1
       botoes.attach(btn7,      0, 1, 1, 1)
       botoes.attach(btn8,      1, 1, 1, 1)
       botoes.attach(btn9,      2, 1, 1, 1)
       botoes.attach(btn_soma,  3, 1, 1, 1)

       # Coluna 2
       botoes.attach(btn4,           0, 2, 1, 1)
       botoes.attach(btn5,           1, 2, 1, 1)
       botoes.attach(btn6,           2, 2, 1, 1)
       botoes.attach(btn_subtracao,  3, 2, 1, 1)
       
       # Coluna 3
       botoes.attach(btn1,              0, 3, 1, 1)
       botoes.attach(btn2,              1, 3, 1, 1)
       botoes.attach(btn3,              2, 3, 1, 1)
       botoes.attach(btn_multiplicacao, 3, 3, 1, 1)
       
       # Coluna 4
       botoes.attach(btn0,        0, 4, 1, 1)  
       botoes.attach(btn_igual,   1, 4, 2, 1)
       botoes.attach(btn_divisao, 3, 4, 1, 1)


       box_vert.add(barra_sup)
       box_vert.add(visor)
       visor.add(self.visor)
       box_vert.add(botoes)
       barra_sup.add(bt_arquivo)
       barra_sup.add(bt_ajuda)
       barra_sup.add(bt_sobre)

       box_hor.add(box_vert)

       janela.add(box_hor)
       janela.show_all()



   def sair(self, componente=None, dados=None):
       Gtk.main_quit()

if __name__ == '__main__':
   prog = Aplicacao()
   Gtk.main()