import os
import subprocess
import pandas as pd

def download_dataset(dataset_name="rohanrao/formula-1-world-championship-1950-2020", data_path="../data"):
    """
    Descarga el dataset de Kaggle si no está disponible localmente usando Kaggle CLI.
    """
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    # Comando para descargar y extraer el dataset usando Kaggle CLI
    cmd = f"kaggle datasets download -d {dataset_name} -p {data_path} --unzip"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("Dataset descargado y extraído en:", data_path)
    except subprocess.CalledProcessError as e:
        print("Error al descargar el dataset:", e)
    
    return data_path

def load_csv(file_name, data_path="../data"):
    """
    Carga un archivo CSV en un DataFrame de Pandas.
    """
    file_path = os.path.join(data_path, file_name)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"El archivo {file_name} no se encuentra en {data_path}")

# Ejemplo de uso
if __name__ == "__main__":
    dataset_path = download_dataset()
    df_races = load_csv("races.csv")
    print(df_races.head())
