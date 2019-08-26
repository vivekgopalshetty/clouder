# clouder

Census tracts are relatively permanent small-area geographic divisions of a
county or statistically equivalent entity defined for the tabulation and
presentation of data from the decennial census and selected other statistical
programs 

What does it do
All the data is stored in AWS S3 storage 
Data is extrcated from S3 according to User input(city name) and then cencus tract is calculated 
and displayed on a webiste which is bulit using flask 

Extra Features
parallel processing is done to handle requests by users.Threads are used for this purpose.
