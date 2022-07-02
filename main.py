import argparse
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler


def read_json():
    df = pd.read_csv('karnataka_tomato_price.csv')
    df.rename(columns = { 'Arrival Date': 'date',
                       'Arrivals (Tonnes)': 'tonnes',
                       'Modal Price(Rs./Quintal)': 'avg_price',
                       'Market': 'region',
                       'Minimum Price(Rs./Quintal)': 'minimum_price',
                       'Maximum Price(Rs./Quintal)': 'maximum_price' },
              inplace = True)
    df = df.drop(columns={'Variety'})
    return df





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", help=" Provide the date to predict the price of the crop", nargs="?", required=True)
    parser.add_argument("--day", help=" Provide the date to predict the price of the crop",  nargs="?", required=True)
    parser.add_argument("--month", help=" Provide the date to predict the price of the crop", nargs="?", required=True)
    parser.add_argument("--year", help=" Provide the date to predict the price of the crop", nargs="?", required=True)
    parser.add_argument("--tonnes", help=" Provide the estimate tonnes reached the market yard", nargs="?", required=True)
    parser.add_argument("--minimum_price", help=" Provide the state to get price specific to the state", nargs="?", required=True)
    parser.add_argument("--maximum_price", help=" Provide the state to get price specific to the state", nargs="?", required=True)
    args = parser.parse_args()
    prediction(args)
