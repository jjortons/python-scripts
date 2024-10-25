import sys
from datetime import datetime
from faker import Faker
import random

    
def genr_data(n):    
    fake = Faker()

    stocks = []
    for i in range(n):
        code = fake.cryptocurrency_code()
        
        d1 = datetime.strptime(f'1-1-2021', '%m-%d-%Y')
        d2 = datetime.strptime(f'11-30-2022', '%m-%d-%Y')
        
        txn_date = fake.date_between(d1, d2)
        
        shares = random.randint(100, 900)
        price  = random.random() * 100
        
        stocks.append([code, txn_date, shares, price])
    return stocks
    
    
def main(fayl, *, no_of_items = 100):    
    try:
        with open(fayl, 'w') as f:
            f.write(f'code,date,shares,price\n')
            for s in genr_data(no_of_items):
                f.write(f'{s[0]},{s[1]},{s[2]},{s[3]:.2f}\n')
                
    except Exception as e:
        print('an error occured', e)
        
        
if __name__ == '__main__':
    '''
    if sys.argv[1] is not None:
        main(sys.argv[1])
    '''
    main('dummy_portfolio.csv', no_of_items= 50)        