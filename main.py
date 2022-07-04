from tkinter import *
from tkinter import ttk

#----------------------------------------------------------------------------------------------

# Cores
cor_branca = '#ffffff'
cor_preta = '#000000'

#----------------------------------------------------------------------------------------------

# Estrutura janela
janela = Tk()
janela.title('Calculadora TMB')
janela.geometry('600x625')
janela.configure(bg=cor_branca)

#----------------------------------------------------------------------------------------------

# Divisões janela
frame_cima = Frame(janela, width=600, height=70, bg=cor_preta, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=600, height=730, bg=cor_branca, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#----------------------------------------------------------------------------------------------

# Método para descrição dos níveis de atividade
def texto(linha, string, fonte='Ivy 10'):
    app_descricaoTaxas = Label(frame_baixo, text=string, height=1, padx=0, relief='flat', anchor='center', font=(fonte), bg=cor_branca, fg=cor_preta)
    app_descricaoTaxas.grid(row=linha, column=0, sticky=NSEW, pady=0, padx=35)

#----------------------------------------------------------------------------------------------

# Conteúdo frame_cima
    
    # Nome da aplicação
app_nome = Label(frame_cima, text='Calculadora de Metabolismo Basal', width=45, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=cor_preta, fg=cor_branca)
app_nome.place(x=0, y=15)
    
    # Linha divisória dos frames
app_linha = Label(frame_cima, text='', width=600, height=0, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=cor_branca, fg=cor_branca)
app_linha.place(x=0, y=62)

#----------------------------------------------------------------------------------------------
# Conteúdo frame_baixo    
    
    # Entrada TAXA DE ATIVIDADE (Texto)
texto(0, 'Escolha a opção correspondente à sua taxa de atividade:', 'Ivy 10 bold')

    # Descrições TAXA DE ATIVIDADE
entrada_taxas = StringVar()

taxa_1 = Radiobutton(frame_baixo, text='Sedentário (pouco ou nenhum exercício)', font='Ivy 10', value='1', variable=entrada_taxas)
taxa_1.grid(row=1, column=0, sticky=NSEW, pady=1, padx=35)

taxa_2 = Radiobutton(frame_baixo, text='Levemente ativo (exercício leve - 1 a 3 dias por semana)', font='Ivy 10', value='2', variable=entrada_taxas)
taxa_2.grid(row=2, column=0, sticky=NSEW, pady=1, padx=35)

taxa_3 = Radiobutton(frame_baixo, text='Moderadamente ativo (exercício moderado - 3 a 5 dias por semana)', font='Ivy 10', value='3', variable=entrada_taxas)
taxa_3.grid(row=3, column=0, sticky=NSEW, pady=1, padx=35)

taxa_4 = Radiobutton(frame_baixo, text='Muito ativo (exercício pesado - 5 a 6 dias por semana)', font='Ivy 10', value='4', variable=entrada_taxas)
taxa_4.grid(row=4, column=0, sticky=NSEW, pady=1, padx=35)

taxa_5 = Radiobutton(frame_baixo, text='Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia)', font='Ivy 10', value='5', variable=entrada_taxas)
taxa_5.grid(row=5, column=0, sticky=NSEW, pady=1, padx=35)

#----------------------------------------------------------------------------------------------

    # Entrada Sexo (Texto)
texto(6, 'Escolha o sexo:', 'Ivy 10 bold')

    # Entrada Sexo (Entrada usuário)
values = ['Masculino','Feminino']

entrada_sexo = ttk.Combobox(frame_baixo, values=values)
entrada_sexo.grid(row=7, column=0, sticky=NSEW, pady=1, padx=35)

#----------------------------------------------------------------------------------------------

    # Entrada altura (Texto)
texto(8, 'Digite a sua altura (cm):', 'Ivy 10 bold')

    # Entrada altura (Entrada usuário)
entrada_altura = Entry(frame_baixo, width=10, relief='solid',font=('Ivy 10'))
entrada_altura.grid(row=9, column=0, sticky=NSEW, pady=5, padx=35)

#----------------------------------------------------------------------------------------------

    # Entrada peso (Texto)
texto(10, 'Digite o seu peso (kg):', 'Ivy 10 bold')

    # Entrada peso (Entrada usuário)
entrada_peso = Entry(frame_baixo, width=10, relief='solid',font=('Ivy 10'))
entrada_peso.grid(row=11, column=0, sticky=NSEW, pady=5, padx=35)

#----------------------------------------------------------------------------------------------

    # Entrada idade (Texto)
texto(12, 'Digite a sua idade (anos):', 'Ivy 10 bold')

    # Entrada idade (Entrada usuário)
entrada_idade = Entry(frame_baixo, width=10, relief='solid',font=('Ivy 10'))
entrada_idade.grid(row=13, column=0, sticky=NSEW, pady=5, padx=35)

#----------------------------------------------------------------------------------------------

    # Resultado do cálculo

saida_resultado = Label(frame_baixo, text='', width=36, height=2, padx=0, relief='flat', font=('Ivy 20 bold'), bg=cor_preta, fg=cor_branca)
saida_resultado.grid(row=14, column=0, sticky=NSEW, pady=20, padx=0)

#----------------------------------------------------------------------------------------------

# Função calcular
def calcular():
    
    taxa_entrada_usuario = int(entrada_taxas.get())
    sexo_rec = entrada_sexo.get()
    altura = int(entrada_altura.get())
    peso = int(entrada_peso.get())
    idade = int(entrada_idade.get())

    if taxa_entrada_usuario == 1:
            taxa_atividade = 1.2
    if taxa_entrada_usuario == 2:
            taxa_atividade = 1.375
    if taxa_entrada_usuario == 3:
            taxa_atividade = 1.55
    if taxa_entrada_usuario == 4:
            taxa_atividade = 1.725
    if taxa_entrada_usuario == 5:
            taxa_atividade = 1.9
            
    if sexo_rec == 'Feminino':
            tmb = taxa_atividade * (655 + (9.6 * peso)) + (1.8 * altura) - (4.7 * idade)
    else:
            tmb = taxa_atividade * (66 + (13.7 * peso)) + (5 * altura) - (6.8 * idade)

    saida_resultado['text'] = 'O seu gasto calórico diário é: ' + str(int(tmb)) + 'kcal'

#----------------------------------------------------------------------------------------------

    # Botão de calcular
botao_calculo = Button(frame_baixo, command=calcular, text='Calcular', width=40 , height=1, padx=0, overrelief=SOLID, relief='raised', font=('Ivy 10 bold'), bg=cor_preta, fg=cor_branca)
botao_calculo.grid(row=17, column=0, sticky=NSEW, pady=20, padx=35)

#----------------------------------------------------------------------------------------------

# Abrir janela
if __name__ == '__main__':
    janela.mainloop()