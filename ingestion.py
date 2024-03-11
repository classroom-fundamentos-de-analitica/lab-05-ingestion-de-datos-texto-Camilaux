import os
import pandas as pd

def extract(base_dir):
    data = []  # Lista para almacenar las filas del dataset
    for sentiment in ['negative', 'neutral', 'positive']:  # Nombres de las carpetas de sentimientos
        sentiment_dir = os.path.join(base_dir, sentiment)
        for filename in os.listdir(sentiment_dir):
            if filename.endswith('.txt'):
                file_path = os.path.join(sentiment_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'sentiment': sentiment})
    return data

# Ruta a la carpeta inicial 'data'
data_dir = '../lab-05-ingestion-de-datos-texto-Camilaux/data'

# Extraer datos para 'train' y 'test'
train_data = extract(os.path.join(data_dir, 'train'))
test_data = extract(os.path.join(data_dir, 'test'))

# Convertir las listas de datos en DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Guardar los DataFrames en archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)