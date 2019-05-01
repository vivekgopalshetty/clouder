import boto3 as aws
from botocore.handlers import disable_signing
import pandas as pd
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO # Check for python version to use correct library
else:
    from io import StringIO
    
def get_census_data(city): #given city name extract that data from AWS S3 storage

    filename = "acs2015.csv"
    s3 = aws.resource('s3')
    s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing) #disable signing
    obj = s3.Object(bucket_name="cloudcomputingj", key=filename) #connecting to your bucket
    
    res = obj.get()
    raw_data = res['Body'].read().decode('UTF-8') #decode data once fetched from server
    data = StringIO(raw_data)
    df = pd.read_csv(data)
    
    return df #return dataFrame required


def get_avg_pop(city): #given a city name finding average population of state using cencus tract
    
    df = get_census_data(city) # Makes a call to get the city data from S3
    condition=(df['State']==city)
    df=df[condition]
    
    # Calculate and return the average census tract population
    total_pop=df['TotalPop'].sum(axis=0)
    num_tracts=df.shape[0]
    return str(round(total_pop / num_tracts,2))
