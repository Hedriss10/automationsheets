import pandas as pd
import os

# config columns display max dataframe
pd.set_option('display.max_columns', 500)


# required columns
REQUIRED_COLLUMNS = ['CPF', 'NUMERO_PROPOSTA', 'COD_TAB', 'VALOR_OPERACAO']

def helper_files(filename: str):
    try:
        data = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(data, 'data')
    
        for filename in path.endswith(".csv"):
            if filename in filename:
                return filename
    
    except Exception as e:
        print(f"Error processing helper files {e}")


class ReportCreedFranco:
    
    def __init__(self, file: str) -> None:
        self.file = file
        self.df = None
        
    def load_dataframe(self):
        self.df = pd.read_csv(self.file, sep=';', encoding='utf-8')
        df_renamed = self.__rename_dataframe(df_renamed=self.df) # renamed daraframe
        newdf = self.__check_summary(newdf=self.__required_columns(df_renamed))
        return newdf
    
    def __required_columns(self, df_required_columns: pd.DataFrame) -> pd.DataFrame:
        newdf = df_required_columns[['CPF', 'NOME', 'FLAT', 'BONUS', 'NUMERO_PROPOSTA', 'VALOR_OPERACAO']]
        return newdf
    
    def __rename_dataframe(self, df_renamed: pd.DataFrame) -> pd.DataFrame:
        df_renamed.rename(
            columns={
                'CPF': 'CPF',
                'NOME': 'NOME',
                'VALOR FLAT': 'FLAT',
                'VALOR BONUS': 'BONUS',
                'CODIGO PROPOSTA BANCO': 'NUMERO_PROPOSTA',
                'VALOR BRUTO': 'VALOR_OPERACAO'
            }, inplace=True
        )
        return df_renamed
    
    def __check_summary(self, newdf: pd.DataFrame) -> pd.DataFrame:
        """
            1. Tratamento automático do CPF (mantendo só números)
            2. Formatar o NOME em letras maiúsculas
            3. Limpar campos monetários (FLAT, BONUS, VALOR_OPERACAO) e converter pra float
            4. Somar BONUS no FLAT
        """
        try:
            newdf['CPF'] = newdf['CPF'].astype(str).str.replace(r'\D', '', regex=True)

            newdf['NOME'] = newdf['NOME'].astype(str).str.upper()

            money_cols = ['FLAT', 'BONUS', 'VALOR_OPERACAO']
            for col in money_cols:
                newdf[col] = (newdf[col]
                        .astype(str)
                        .str.replace('R$', '', regex=False)
                        .str.replace('.', '', regex=False)
                        .str.replace(',', '.', regex=False)
                        .astype(float)
                        )

            newdf['FLAT'] += newdf['BONUS']

            return newdf
        except Exception as e:
            print(f"invalid check: {e}")
            return newdf



class ExploreData:
    
    
    def __init__(self):
        pass

    def load_dataframe(self):
        try:
            df = pd.read_csv("/Users/hedrispereira/Desktop/automationsheets/data/daycoval-cartao.xls", sep=";")
            print(df.head())
            # tables = pd.read_html("/Users/hedrispereira/Desktop/automationsheets/data/daycoval-cartao.xls")
            # df = tables[0]
            # df.to_csv("resultado_creed_franco.csv", sep=";", index=False)
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            try:
                df = pd.read_excel(
                    "/Users/hedrispereira/Desktop/automationsheets/data/daycoval-cartao.xls",
                    engine='xlrd'
                )
            except Exception as e2:
                print(f"Erro na segunda tentativa: {e2}")
                raise
        
        df.to_csv("resultado_creed_franco.csv", sep=";", index=False)


if __name__ == "__main__":
    # file = helper_files()
    # exe = ReportCreedFranco(file="/Users/hedrispereira/Desktop/automationsheets/data/CREDFRANCO - COMISSÃO MASTER RECEBIDA segundaVia.xlsx").load_dataframe()
    ExploreData().load_dataframe()