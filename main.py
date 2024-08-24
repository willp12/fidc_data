import pandas as pd
import os
import zipfile as zp


def extract_zipped_file_with_name_pattern(filename: str,  relative_output_path_folder: str, name_pattern: str) -> None:
    # Extrai apenas 1 das tabelas dos arquivos zipados
    tmp = zp.ZipFile(filename)
    for f in tmp.namelist():
        if f.startswith(name_pattern):
            tmp.extract(f, path=relative_output_path_folder)

def concat_csv(input_folder: str) -> pd.DataFrame:
    # Concatena todos os csvs em um único dataframe
    out = pd.DataFrame()
    for f in os.listdir(input_folder):
        if f.endswith('.csv'):
            tmp = pd.read_csv(input_folder+f, delimiter=';', encoding='latin-1')
            out = pd.concat([out, tmp])
    return out




if __name__ == '__main__':
    input_folder = 'data/raw/'
    for f in os.listdir(input_folder):
        extract_zipped_file_with_name_pattern(input_folder+f, 'data/output/', 'inf_mensal_fidc_tab_VII')
    concat_csv('data/output/').to_csv('data/output/inf_mensal_fidc_tab_VII_consolidado.csv')