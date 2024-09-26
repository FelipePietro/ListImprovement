import pandas as pd

# Carrega a planilha
file_path = input('Digite o nome da sua planilha: ') # Substitua pelo caminho do seu arquivo
df = pd.read_excel(file_path)

# Função para concatenar o código de país com o número de telefone
def concatenate_phone(row):
    if pd.notna(row['Phone country code']) and pd.notna(row['Phone number']):
        return f"+{int(row['Phone country code'])}{int(row['Phone number'])}"
    else:
        return row['Phone number']  # Retorna apenas o número se o código estiver ausente

# Aplicando a função de concatenação
df['Phone number concatenated'] = df.apply(concatenate_phone, axis=1)

# Criando DataFrames para cada aba com as colunas originais e a concatenada
portugal_df = df[df['Phone country code'] == 351]
espanha_df = df[df['Phone country code'] == 34]
brasil_df = df[df['Phone country code'] == 55]
mundo_df = df[(df['Phone country code'] != 351) & 
              (df['Phone country code'] != 34) & 
              (df['Phone country code'] != 55) & 
              df['Phone country code'].notna()]
sem_numero_df = df[df['Phone country code'].isna()]

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
new_file_path = file_path.replace('.xlsx', '_edit.xlsx')
with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='contacts', index=False)
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

print(f"Planilhas salvas como {new_file_path} e {formatted_file_path}")
