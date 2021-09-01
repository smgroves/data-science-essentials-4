## Week 1
What is Data Science?

 - Coding Skills/Statistics/Domain Expertise
 - The Data Science Process
 - Examples of Data Science in the world

**Coding tasks:** Create a new Jupyer Notebook to complete the following tasks.

A dataset containing information on US hospitals is contained in the data folder in the file `Hospitals.csv`. This datset was downloaded from [the Homeland Infrastructure Foundation-Level Data (HIFLD) database](https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals/explore).

1. Read this dataset into a DataFrame named `hospitals`.
2. Look at the first few rows and then look at the last few. What do you notice?
3. How many rows and columns does this DataFrame have?
4. We don't need all of the columns. Slice the dataframe down so that it only contains the following columns: 'NAME', 'ADDRESS', 'CITY', 'STATE', 'TYPE',  'POPULATION', 'COUNTY', 'COUNTYFIPS', 'NAICS_DESC', 'BEDS'
5. What are the different hospital types (contained in the `TYPE` column)? Which is the most common?
6. Find all hospitals in Nashville, Tennessee. Take a look at the BEDS column. What do you notice? Why do you think this is?
7. Which county in Tennessee has the most hospitals?
8. There are 95 counties in Tennessee. How many of them have no hospitals at all?