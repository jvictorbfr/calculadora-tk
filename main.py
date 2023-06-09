# LAYOUT DE LOGIN E SENHA by jvictor
from tkinter import *
from tkinter import tix
from tkinter import messagebox

# FUNÇÕES--------------------------
credenciais = ["jvictor", "botafogo"]  # CREDENCIAL PADRÃO

# VERFICAR SENHA
def verifica_senha():
    login = entry_login.get()
    senha = entry_senha.get()

    if login == "usuario" and senha == "01234":
        # DELETA TELA 1
        for widget in tela1.winfo_children():
            widget.destroy()
        # INICIA TELA DA CONTA
        tela_userconta()
    elif credenciais[0] == login and credenciais[1] == senha:
        # DELETA TELA 1
        for widget in tela1.winfo_children():
            widget.destroy()
        # INICIA TELA DA CONTA
        tela_entrarconta()
    else:
        messagebox.showerror("Erro", "Verifique o login e a senha!")

# ESQUECEU SENHA
def esqueceu_senha():
    # DELETA TELA 1
    for widget in tela1.winfo_children():
        widget.destroy()
    # INICIA TELA ESQUECEU SENHA
    tela_esqsenha()

# FUNÇÃO NOVA CONTA
def nova_conta():
    # DELETA TELA 1
    for widget in tela1.winfo_children():
        widget.destroy()
    # INICIA TELA CRIAR CONTA
    tela_criarconta()

# TELA PARA CRIAR CONTA
def tela_criarconta():
    # LABEL EMAIL
    lb_email = Label(tela1, text="E-MAIL", bg='#EE964B', fg='#252525', font=('Ebrima', 9, 'bold'))
    lb_email.place(relx=0.1, rely=0.15)

    # LABEL USER
    lb_user = Label(tela1, text="USER", bg='#EE964B', fg='#252525', font=('Ebrima', 9, 'bold'))
    lb_user.place(relx=0.1, rely=0.35, relwidth=0.15)

    # LABEL SENHA 2
    lb_senha2 = Label(tela1, text="SENHA", bg='#EE964B', fg='#252525', font=('Ebrima', 9, 'bold'))
    lb_senha2.place(relx=0.1, rely=0.55)

    # ENTRY EMAIL
    entry_email = Entry(tela1, bd=0, bg='#F3F9E3', fg='#252525', font=('Ebrima', 10, 'bold'))
    entry_email.place(relx=0.27, rely=0.15, relwidth=0.6, relheight=0.083)

    # ENTRY USER
    entry_user = Entry(tela1, bd=0, bg='#F3F9E3', fg='#252525', font=('Ebrima', 10, 'bold'))
    entry_user.place(relx=0.27, rely=0.35, relwidth=0.6, relheight=0.083)

    # ENTRY SENHA 2
    entry_senha2 = Entry(tela1, bd=0, bg='#F3F9E3', fg='#252525', font=('Ebrima', 10, 'bold'))
    entry_senha2.place(relx=0.27, rely=0.55, relwidth=0.6, relheight=0.083)

    # BOTÃO JÁ POSSUO CONTA
    bt_possuoconta = Button(tela1, text="JÁ POSSUO CONTA", bd=0, bg='#EE964B', activebackground='#EE964B',
                         activeforeground='#252525', fg='#252525', font=('Ebrima', 7), command=quit)
    bt_possuoconta.place(relx=0.35, rely=0.7)

    # BOTÃO CRIAR
    bt_criar = Button(tela1, text="CRIAR", bd=2, bg='#252525', activeforeground='#EE964B',
                            fg='#EE964B', font=('Ebrima', 8, 'bold'), command=nova_conta)
    bt_criar.place(relx=0.2, rely=0.83, relwidth=0.6, relheight=0.083)

# TELA ENTRAR CONTA JVICTOR
def tela_entrarconta():
    # LABEL BEM-VINDO
    lb_bemvindo = Label(tela1, text="SEJA BEM-VINDO", bg='#EE964B', fg='#252525', font=('Ebrima', 15, 'bold'))
    lb_bemvindo.place(relx=0.2, rely=0.1)

    # LABEL LINHA 2
    lb_linha2 = Label(tela1, text="_____________________________________________________", bg='#EE964B', fg='#252525',
                 font=('Ebrima', 9, 'bold'))
    lb_linha2.place(relx=0.05, rely=0.25)

    # LABEL NOME
    lb_nome = Label(tela1, text="USER: " + credenciais[0], bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_nome.place(relx=0.1, rely=0.4)

    # LABEL LINK
    lb_link = Label(tela1, text="LINK: github.com/jvictorbfr",
                    bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_link.place(relx=0.1, rely=0.6)

    # BOTÃO SAIR
    bt_sair = Button(tela1, text="SAIR", bd=2, bg='#252525', activeforeground='#EE964B',
                            fg='#EE964B', font=('Ebrima', 8, 'bold'), command=quit)
    bt_sair.place(relx=0.35, rely=0.83, relwidth=0.3, relheight=0.083)

# TELA ENTRAR NA CONTA USUARIO
def tela_userconta():
    # LABEL BEM-VINDO
    lb_bemvindo2 = Label(tela1, text="SEJA BEM-VINDO", bg='#EE964B', fg='#252525', font=('Ebrima', 15, 'bold'))
    lb_bemvindo2.place(relx=0.2, rely=0.1)

    # LABEL LINHA 2
    lb_linha3 = Label(tela1, text="_____________________________________________________", bg='#EE964B', fg='#252525',
                 font=('Ebrima', 9, 'bold'))
    lb_linha3.place(relx=0.05, rely=0.25)

    # LABEL NOME
    lb_nome2 = Label(tela1, text="USER: usuario", bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_nome2.place(relx=0.1, rely=0.4)

    # LABEL LINK
    lb_link2 = Label(tela1, text="LINK: github.com/jvictorbfr",
                    bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_link2.place(relx=0.1, rely=0.6)

    # BOTÃO SAIR
    bt_sair2 = Button(tela1, text="SAIR", bd=2, bg='#252525', activeforeground='#EE964B',
                            fg='#EE964B', font=('Ebrima', 8, 'bold'), command=quit)
    bt_sair2.place(relx=0.35, rely=0.83, relwidth=0.3, relheight=0.083)

# TELA ESQUECEU A SENHA
def tela_esqsenha():
    # LABEL CREDENCIAIS DO USUARIO
    lb_usercred = Label(tela1, text="CREDENCIAIS", bg='#EE964B', fg='#252525', font=('Ebrima', 15, 'bold'))
    lb_usercred.place(relx=0.25, rely=0.1)

    # LABEL LINHA
    lb_linha4 = Label(tela1, text="_____________________________________________________", bg='#EE964B', fg='#252525',
                 font=('Ebrima', 9, 'bold'))
    lb_linha4.place(relx=0.05, rely=0.25)

    # LABEL LOGIN USER
    lb_userlog = Label(tela1, text="LOGIN: usuario", bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_userlog.place(relx=0.1, rely=0.4)

    # LABEL SENHA USER
    lb_usersenha = Label(tela1, text="SENHA: 01234",
                    bg='#EE964B', fg='#252525', font=('Ebrima', 13, 'bold'))
    lb_usersenha.place(relx=0.1, rely=0.6)

    # BOTÃO SAIR
    bt_sair3 = Button(tela1, text="SAIR", bd=2, bg='#252525', activeforeground='#EE964B',
                            fg='#EE964B', font=('Ebrima', 8, 'bold'), command=quit)
    bt_sair3.place(relx=0.35, rely=0.83, relwidth=0.3, relheight=0.083)

# MENU
def menu():
    menubar = Menu(janela)
    janela.config(menu=menubar)
    filemenu = Menu(menubar)

    def Quit(): janela.destroy()

    menubar.add_cascade(label="Opções", menu=filemenu)
    filemenu.add_cascade(label="Sair", command=Quit)

# JANELA---------------------------
janela = tix.Tk()
janela.title("LOGIN E SENHA by Jvictor")
janela.configure(background="#252525")
janela.geometry("500x400")
janela.resizable(False, False)
menu()

# TELA 1
tela1 = Frame(janela, bg="#EE964B", highlightbackground='#F3F9E3', highlightthickness=2)
tela1.place(relx=0.17, rely=0.15, relwidth=0.6, relheight=0.65)

# LABEL LOGIN
lb_login = Label(tela1, text="LOGIN", bg='#EE964B', fg='#252525', font=('Ebrima', 9, 'bold'))
lb_login.place(relx=0.1, rely=0.15)

# LABEL SENHA
lb_senha = Label(tela1, text="SENHA", bg='#EE964B', fg='#252525', font=('Ebrima', 9, 'bold'))
lb_senha.place(relx=0.1, rely=0.35)

# LABEL LINHA
lb_linha = Label(tela1, text="_____________________________________________________", bg='#EE964B', fg='#252525',
                 font=('Ebrima', 9, 'bold'))
lb_linha.place(relx=0.05, rely=0.7)

# ENTRY LOGIN
entry_login = Entry(tela1, bd=0, bg='#F3F9E3', fg='#252525', font=('Ebrima', 10, 'bold'))
entry_login.place(relx=0.27, rely=0.15, relwidth=0.6, relheight=0.083)

# ENTRY SENHA
entry_senha = Entry(tela1, bd=0, bg='#F3F9E3', show='*', fg='#252525', font=('Ebrima', 10, 'bold'))
entry_senha.place(relx=0.27, rely=0.35, relwidth=0.6, relheight=0.083)

# BOTÃO ESQUECEU SENHA
bt_esqsenha = Button(tela1, text="ESQUECEU A SENHA?", bd=0, bg='#EE964B', activebackground='#EE964B',
                              activeforeground='#252525', fg='#252525', font=('Ebrima', 7), command=esqueceu_senha)
bt_esqsenha.place(relx=0.1, rely=0.47)

balao_esqsenha = tix.Balloon(tela1)
balao_esqsenha.bind_widget(bt_esqsenha, balloonmsg="Esqueceu a senha")

# BOTÃO ENTRAR
bt_entrar = Button(tela1, text="ENTRAR", bd=2, bg='#252525', activeforeground='#EE964B',
                            fg='#EE964B', font=('Ebrima', 8, 'bold'), command=verifica_senha)
bt_entrar.place(relx=0.35, rely=0.62, relwidth=0.3, relheight=0.083)

balao_entrar = tix.Balloon(tela1)
balao_entrar.bind_widget(bt_entrar, balloonmsg="Entrar na conta")

# BOTÃO CRIAR CONTA
bt_criar_conta = Button(tela1, text="NOVA CONTA", bd=2, bg='#F3F9E3', activebackground='#EE964B',
                    activeforeground='#F3F9E3', fg='#EE964B', font=('Ebrima', 8, 'bold'), command=nova_conta)
bt_criar_conta.place(relx=0.2, rely=0.82, relwidth=0.6, relheight=0.083)

balao_criarconta = tix.Balloon(tela1)
balao_criarconta.bind_widget(bt_criar_conta, balloonmsg="Criar uma nova conta")

janela.mainloop()
