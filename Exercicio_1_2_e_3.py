import pandas as pd


# Carregar o arquivo CSV em um DataFrame, pulando a primeira linha (cabeçalho)
df = pd.read_csv('actors.csv', header=None, skiprows=1)


# Exibir o DataFrame
print("               Original \n",df)


# Converter a última coluna em dados numéricos
df_novo = df.copy()
df_novo.iloc[:, -1] = pd.to_datetime(df_novo.iloc[:, -1], format='%B %d, %Y').dt.date


# Exibitir o Dataframe com datas numéricas
print("             Data Numéricas \n",df_novo)


# Cria Coluna com a Idade Atual deles
ano_atual = pd.Timestamp.now().year
df_novo['Idade'] = ano_atual - pd.to_datetime(df_novo.iloc[:, -1]).dt.year


# Exibir o novo DataFrame com a coluna de idade
print(df_novo)


# Calcular a média das idades
media_idade = df_novo['Idade'].mean()


# Exibir a média das idades
print(f"Média das idades: {media_idade:.2f} anos")