import pandas as pd

def load_data():
    file_path = r'C:\Users\tress\OneDrive\Desktop\Posh Data Dive\data\all_data.csv'
    df = pd.read_csv(file_path)
    #df cleaning:
    df['price'] = df['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    df['price'] = df['price'].astype(int)
    #adding combo column of market and category
    df['market & category'] = df['market'] + " " + df['category']
    #adding combo column category and brand
    df['category & brand'] = df['brand'] + " " + df ['category']
    #adding combo column category and subcategory
    df['category & subcategory'] = df['category'] + ' ' + df['subcategory']
    #adding combo column market and category and subcategory
    df['market & category & subcategory'] = df['market'] + ' ' + df['category'] + ' ' + df['subcategory']
    #adding combo column market and category and brand
    df['market & category & brand'] = df['market'] + ' ' + df['category'] + ' ' + df['brand']
    #creating new columns and applying functions: range of days and price range:
    df['range of days'] = df['days on poshmark'].apply(get_range_of_days)
    df['price range'] = df['price'].apply(get_range_of_prices)

    return df

def get_range_of_days(value):
    if value > 0 and value < 16:
        return '0-15 days'
    elif value >= 16 and value < 41:
        return '16-40 days'
    elif value >= 41 and value < 61:
        return '41-60 days'
    elif value >= 61 and value < 81:
        return '61-80 days'
    elif value >= 81 and value < 101:
        return '81-100 days'
    else:
        return 'more than 100 days'
    
def get_range_of_prices(value):
    if value >= 3 and value < 11:
        return 'price $3-10'
    elif value >= 11 and value < 26:
        return 'price $11-26'
    elif value >= 26 and value < 51:
        return 'price $26-50'
    elif value >= 51 and value < 101:
        return 'price $51-100'
    elif value >= 101 and value < 151 :
        return 'price $101-150'
    elif value >= 151 and value < 201 :
        return 'price $151-200'
    elif value >= 201 and value < 301 :
        return 'price $201-300'
    elif value >= 301 and value < 401 :
        return 'price $301-400'
    elif value >= 401 and value < 501 :
        return 'price $401-500'
    elif value >= 501 and value < 701 :
        return 'price $501-700'
    elif value >= 701 and value < 901 :
        return 'price $701-900'
    elif value >= 901 and value < 1501 :
        return 'price $901-1500'
    else:
        return 'more than $1500'