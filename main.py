import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer


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


def column_addition(year, month, day, df):
    df['year'] = year
    df['month'] = month
    df['day'] = day
    return df


def prepare_vectorizer(df):
    D = []
    avg_price = []
    for index in range(len(df)):
        temp_dct = {}
        temp_dct['region'] = df['region'][index].lower()
        temp_dct['day'] = int(df['day'][index])
        temp_dct['month'] = df['month'][index]
        temp_dct['year'] = int(df['year'][index])
        temp_dct['tonnes'] = df['tonnes'][index]
        temp_dct['minimum_price'] = df['minimum_price'][index]
        temp_dct['maximum_price'] = df['maximum_price'][index]
        avg_price.append(df['avg_price'][index])
        D.append(temp_dct)
    return D, avg_price


def model_prediction(D, avg_price, user_input):
    v = DictVectorizer(sparse=False)
    X = v.fit_transform(D)
    Y = avg_price
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    r2_score = lr.score(x_test, y_test)
    test = []
    test.append(user_input)
    X_Pred = v.transform(test)
    price_prediction = lr.predict(X_Pred)
    print("Model score :", r2_score * 100, "\n")
    print("price predicted :", price_prediction[0])


def prediction(user_input):
    df = read_json()
    year, month, day = data_processing(df)
    df = column_addition(year, month, day, df)
    D, avg_price = prepare_vectorizer(df)
    model_prediction(D, avg_price, user_input)


if __name__ == '__main__':
    region = input(" Enter the region: ")
    day = input(" Enter the day: ")
    month = input(" Enter the month: ")
    year = input(" Enter the year: ")
    tonnes = input(" Enter the tonnes: ")
    minimum_price = input(" Enter the minimum price: ")
    maximum_price = input(" Enter the maximum price: ")
    user_input = {'region': region, 'day': int(day), 'month': int(month), 'year': int(year),
                  'tonnes': int(tonnes),
                  'minimum_price': float(minimum_price),
                  'maximum_price': float(maximum_price)}
    prediction(user_input)
