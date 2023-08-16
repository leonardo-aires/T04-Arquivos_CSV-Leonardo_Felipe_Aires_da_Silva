import pandas as pd


# URL do arquivo CSV
url = "https://raw.githubusercontent.com/emmendorfer/idwr/main/demo/datasets/amazon.csv"


# Carregar o arquivo CSV em um DataFrame sem cabeçalho
df = pd.read_csv(url, header=None)


# Exibir o DataFrame
print(df)


# Converter o DataFrame para uma matriz NumPy
matriz_numpy = df.to_numpy()


# Exibir a matriz NumPy
print(matriz_numpy)