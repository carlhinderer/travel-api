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
    raw_csv = hotels_csv()
    renamed = raw_csv.rename(COLUMN_MAPPINGS)
    return renamed

def hotels_csv():
    csv_file = os.getcwd() + DATA_FILE_NAME
    return pd.read_csv(csv_file, encoding=DATA_FILE_ENCODING)


def import_hotels():
    print('Importing hotels from csv...')
    hotels_df = hotels_dataframe()
    print(hotels_df.head(10))



if __name__ == '__main__':
    import_hotels()
