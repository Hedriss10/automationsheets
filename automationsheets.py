import os
import polars as pl
from datetime import datetime
from tqdm import tqdm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from models import Base, Ro

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
DATABASE_URL = os.getenv("DEV_DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATAFRAMES = os.path.join(BASE_DIR, 'data')


class RoAutomationSpreedsheet:
    def __init__(self):
        self.session = Session()

    def extract(self) -> pl.DataFrame:
        df = pl.read_csv(
            os.path.join(DATAFRAMES, 'data.csv'),
            truncate_ragged_lines=True,
            separator=';'
        )

        rename_map = {
            'Nome': 'nome',
            'CPF': 'cpf',
            'NASCIMENTO': 'date_year',
            'IDADE': 'age',
            'SEXO': 'gender',
            'NOME DA M�E': 'nome_mae',
            'SITUA��O CPF': 'situacao_cpf',
            'DDD1': 'dd_one',
            'CELULAR1': 'phone_one',
            'POSSUI-WHATSAPP': 'have_whatsapp_one',
            'DDD2': 'dd_two',
            'CELULAR2': 'phone_two',
            'POSSUI-WHATSAPP_duplicated_0': 'have_whatsapp_two',
            'TELEFONE BASE ORIGINAL': 'phone_base',
            'EMAIL 1': 'email',
            'EMAIL 2': 'email_two',
            'ENDERECO ': 'endereco',
            'NUMERO': 'numero',
            'COMPLEMENTO': 'complemento',
            'BAIRRO': 'bairro',
            'CIDADE': 'cidade',
            'UF': 'uf',
            'CEP': 'cep',
            'DATA_OBITO': 'data_obito',
            'RISCO_CREDITO': 'risco_credito',
        }

        df = df.rename(rename_map, strict=False)

        # Limpeza do campo CPF
        if 'cpf' in df.columns:
            df = df.with_columns([
                pl.col('cpf').str.replace_all(r'[.\- ]', '').alias('cpf')
            ])

        return df

    def transform(self):
        df = self.extract()

        columns_select = [
            'cpf', 'age', 'nome', 'date_year', 'gender', 'uf', 'cep',
            'phone_base', 'dd_one', 'phone_one', 'have_whatsapp_one',
            'dd_two', 'phone_two', 'have_whatsapp_two',
            'email', 'email_two', 'email_three'
        ]

        colunas_presentes = [c for c in columns_select if c in df.columns]
        df = df.select(colunas_presentes)

        records = df.to_dicts()
        instances = []

        for record in tqdm(records, desc="Transformando registros"):
            try:
                instance = Ro(
                    cpf=record.get('cpf'),
                    name=record.get('nome'),
                    age=record.get('age'),
                    date_year=self._parse_date(record.get('date_year')),
                    gender=record.get('gender'),
                    uf=record.get('uf'),
                    cep=record.get('cep'),
                    phone_base=record.get('phone_base'),
                    dd_one=record.get('dd_one'),
                    phone_one=record.get('phone_one'),
                    have_whatsapp_one=record.get('have_whatsapp_one'),
                    dd_two=record.get('dd_two'),
                    phone_two=record.get('phone_two'),
                    have_whatsapp_two=record.get('have_whatsapp_two'),
                    email=record.get('email'),
                    email_two=record.get('email_two'),
                    email_three=record.get('email_three') if 'email_three' in record else None
                )
                instances.append(instance)
            except Exception as e:
                print(f"[ERRO] Registro inválido: {record} -> {e}")
        return instances

    def load(self):
        instances = self.transform()
        with self.session as session:
            try:
                session.add_all(instances)
                session.commit()
                print(f"[INFO] {len(instances)} registros inseridos com sucesso.")
            except Exception as e:
                session.rollback()
                print(f"[ERRO] Falha ao inserir dados no banco: {e}")

    def _parse_date(self, date_str: str | None) -> datetime | None:
        if not date_str:
            return None
        for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None


if __name__ == "__main__":
    RoAutomationSpreedsheet().load()
