import tkinter.filedialog
import tkinter.messagebox
import pandas as pd
import ctypes
import json
import re
import tkinter
from tkinter import ttk

filename = tkinter.filedialog.askopenfilename

def manipular_planilha():

    file_path = filename(filetypes=[("Excel Files", "*.xlsx")])

    if not file_path:
        tkinter.messagebox.showerror("Erro", "Nenhum arquivo selecionado!")
        return
    
    confirm = tkinter.messagebox.askyesno(title="Confirmação", message=f"Você quer editar a planilha {file_path}?")

    if not confirm:
        return
    
    try:

        with open('keywords.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            keywords = data["keywords"]

        def contains_keywords(bio):
            bio = str(bio).lower() 
            return any(re.search(r'\b' + re.escape(keyword) + r'\b', bio) for keyword in keywords)

        df = pd.read_excel(file_path)

        # Filtra as linhas que contêm as palavras-chave na coluna "Biography"
        filtered_df = df[df['Biography'].apply(contains_keywords)]

        # Função para concatenar o código de país com o número de telefone
        def concatenate_phone(row):
            if pd.notna(row['Phone country code']) and pd.notna(row['Phone number']):
                return f"+{int(row['Phone country code'])}{int(row['Phone number'])}"
            else:
                return row['Phone number']  # Retorna apenas o número se o código estiver ausente

        # Aplicando a função de concatenação
        filtered_df['Phone number concatenated'] = filtered_df.apply(concatenate_phone, axis=1)

        # Criando DataFrames para cada aba com as colunas originais e a concatenada
        contacts_df = filtered_df.copy()  # Mantém a aba principal "contacts" sem alterações

        portugal_df = filtered_df[filtered_df['Phone country code'] == 351]
        espanha_df = filtered_df[filtered_df['Phone country code'] == 34]
        brasil_df = filtered_df[filtered_df['Phone country code'] == 55]
        mundo_df = filtered_df[(filtered_df['Phone country code'] != 351) & 
                            (filtered_df['Phone country code'] != 34) & 
                            (filtered_df['Phone country code'] != 55) & 
                            filtered_df['Phone country code'].notna()]
        sem_numero_df = filtered_df[filtered_df['Phone country code'].isna()]

        # Criando as abas formatadas
        portugal_formatado_df = portugal_df[['Username', 'Phone number concatenated', 'Public email', 'City', 'External url']].copy()
        portugal_formatado_df.columns = ['Username', 'Numero de Telefone', 'Email', 'Localidade', 'Links']

        espanha_formatado_df = espanha_df[['Username', 'Phone number concatenated', 'Public email']].copy()
        espanha_formatado_df.columns = ['Username', 'Numero de Telefone', 'Email']

        mundo_formatado_df = mundo_df[['Phone country code', 'Phone number', 'Username', 'Public email']].copy()
        mundo_formatado_df.columns = ['DDI', 'Numero de Telefone', 'Username', 'Email']

        brasil_formatado_df = brasil_df[['Phone number concatenated', 'Username', 'Public email', 'City']].copy()
        brasil_formatado_df.columns = ['Numero de Telefone', 'Username', 'Email', 'Localidade']

        # Salvando as abas principais em um arquivo Excel
        new_file_path = file_path.replace('.xlsx', '✅.xlsx')
        with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
            contacts_df.to_excel(writer, sheet_name='contacts', index=False)
            portugal_df.to_excel(writer, sheet_name='Contatos Portugal', index=False)
            espanha_df.to_excel(writer, sheet_name='Contatos Espanha', index=False)
            brasil_df.to_excel(writer, sheet_name='Contatos Brasil', index=False)
            mundo_df.to_excel(writer, sheet_name='Contatos Mundo', index=False)
            sem_numero_df.to_excel(writer, sheet_name='Sem Numero', index=False)

        # Salvando as abas formatadas em um arquivo Excel separado
        formatted_file_path = file_path.replace('.xlsx', '_formatados.xlsx')
        with pd.ExcelWriter(formatted_file_path, engine='openpyxl') as writer:
            portugal_formatado_df.to_excel(writer, sheet_name='Contatos Portugal Formatados', index=False)
            espanha_formatado_df.to_excel(writer, sheet_name='Contatos Espanha Formatados', index=False)
            mundo_formatado_df.to_excel(writer, sheet_name='Contatos Mundo Formatados', index=False)
            brasil_formatado_df.to_excel(writer, sheet_name='Contatos Brasil Formatados', index=False)

        # Mensagem de conclusão
        tkinter.messagebox.showinfo(title='Concluído!', message="Suas planilhas foram criadas com sucesso!")
    
    except Exception as e:
        tkinter.messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


#--------------------------------------------------------INTERFACE GRÁFICA---------------------------------------------------------#
root = tkinter.Tk()
root.title('ListImprovment')
root.iconbitmap('icon.ico')
root.geometry("600x250")

root.configure(bg='#cccccc')  # Cor de fundo suave

# Título da janela
title = tkinter.Label(root, text='SELECIONE A PLANILHA QUE VOCÊ DESEJA EDITAR', font=('Helvetica', 14, 'bold'), bg='#cccccc')
title.pack(pady=10)

# Texto informativo
instruction = tkinter.Label(root, text="Clique no botão e escolha sua planilha!", font=('Helvetica', 12, 'bold'), bg='#cccccc')
instruction.pack(pady=5)

# Função para adicionar efeito hover no botão
def on_enter(e):
    actionButton['background'] = '#006666'

def on_leave(e):
    actionButton['background'] = '#008584'

# Botão de ação
actionButton = tkinter.Button(root, text='Clique aqui para criar as planilhas', command=manipular_planilha, font=('Helvetica', 12, 'bold'), bg='#008584', fg='white')
actionButton.pack(pady=15)

# Efeito hover
actionButton.bind("<Enter>", on_enter)
actionButton.bind("<Leave>", on_leave)

# Inicia o loop da interface gráfica
root.mainloop()
