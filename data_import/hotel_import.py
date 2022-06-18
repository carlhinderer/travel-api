import os
import pandas as pd


DATA_FILE_NAME = '/data/ta-hotels.csv'
DATA_FILE_ENCODING = 'ISO-8859-1'

COLUMN_MAPPINGS = {
    'Hotel name': 'hotel_name',
    'Price': 'price',
    'Rating': 'rating',
    'reviews count': 'reviews_count',
    'info.1': 'info_1',
    'info.2': 'info_2',
    'info.3': 'info_3',
    'info.4': 'info_4',
    'info.5': 'info_5',
    'info.6': 'info_6',
    'info.7': 'info_7'
}


def hotels_dataframe():
    original_csv = hotels_csv()
    renamed = original_csv.rename(columns=COLUMN_MAPPINGS, errors='raise')
    return renamed

def hotels_csv():
    csv_file = os.getcwd() + DATA_FILE_NAME
    return pd.read_csv(csv_file, encoding=DATA_FILE_ENCODING)

def clean_hotel_data(df):
    df['city_name'] = df['city_name'].str[:-2]
    df['country_name'] = df['country_name'].str[:-2]
    df['info_1'] = df['info_1'].str.strip()
    df['info_2'] = df['info_2'].str.strip()
    df['info_3'] = df['info_3'].str.strip()
    df['info_4'] = df['info_4'].str.strip()
    df['info_5'] = df['info_5'].str.strip()
    df['info_6'] = df['info_6'].str.strip()
    df['info_7'] = df['info_1'].str.strip()


def import_hotels():
    print('Importing hotels from csv...')
    hotels_df = hotels_dataframe()
    print('Cleaning hotel data...')
    clean_hotel_data(hotels_df)
    return hotels_df


if __name__ == '__main__':
    import_hotels()
