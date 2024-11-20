#import needed libraries
import pandas as pd
import pyodbc

def connect_to_db():
    conn = pyodbc.connect(Driver='{SQL Server}',
                          server='(local)',
                          Database='dqthon',
                          Trusted_Connection='yes')
    src_data = pd.read_sql('select * from [dbo].' + 'participants', conn)
    return src_data
