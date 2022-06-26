import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help=" Provide the date to predict the price of the crop",  nargs="?", required=False)
    parser.add_argument("--tonnes", help=" Provide the estimate tonnes reached the market yard", nargs="?", required=False)
    parser.add_argument("--state", help=" Provide the state to get price specific to the state", nargs="?", required=False)
    args = parser.parse_args()
