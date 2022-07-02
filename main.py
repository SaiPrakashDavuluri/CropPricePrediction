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


def data_processing(df):
    year = []
    temp_month = []
    day = []
    for index in range(len(df)):
        temp = str(df['date'][index])[-4:]
        year.append(temp)
    for index in range(len(df)):
        temp1 = str(df['date'][index])
        temp2 = ''
        for i in range(0, len(temp1), 1):
            if temp1[i] == '/':
                temp2 = temp1[i + 1]
                if temp1[i + 2] != '/':
                    temp2 = temp2 + temp1[i + 2]
                    break
                break
        temp_month.append(temp2)
    for index in range(len(df)):
        temp1 = str(df['date'][index])
        temp2 = ''
        for i in range(0, len(temp1), 1):
            if temp1[i] == '/':
                break
            else:
                temp2 = temp2 + temp1[i]
        day.append(temp2)
    month = []
    for values in temp_month:
        if values == '1' or values == '01':
            month.append(1)
        elif values == '2' or values == '02':
            month.append(2)
        elif values == '3' or values == '03':
            month.append(3)
        elif values == '4' or values == '04':
            month.append(4)
        elif values == '5' or values == '05':
            month.append(5)
        elif values == '6' or values == '06':
            month.append(6)
        elif values == '7' or values == '07':
            month.append(7)
        elif values == '8' or values == '08':
            month.append(8)
        elif values == '9' or values == '09':
            month.append(9)
        elif values == '10' or values == '10':
            month.append(10)
        elif values == '11' or values == '11':
            month.append(11)
        elif values == '12' or values == '12':
            month.append(12)
        elif values == '':
            month.append('NaN')

    return year, month, day






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
