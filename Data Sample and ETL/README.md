## Sample data management

### FAPESP Schema

Scripts to create the tables and insert the data are in the ETL folder:  

 - **ETL/fapesp_create_tables.sql**: SQL commands to create the schema and tables *patient*, *exams* and *outcome*  
 - **ETL/fapesp_insert_data.sql**: SQL commands to insert data from the csv files for each table. Also, we provide regex commands to unify strings over examTypes and analytes. Finally, we provide SQL commands to create indexes over table *exams* to optimize queries  

The Jupyter script allows users to process the CSV files available at the official repository of FAPESP ([here](https://repositoriodatasharingfapesp.uspdigital.usp.br/handle/item/1)):  

 - **ETL/fapespDataProcessing.ipynb**: python notebook to process raw csv files, downloaded from FAPESP repository. We process files to create a unique csv file with data from all hospitals, for each table  

We also provide a sample data file to test our tool:

 -  **fapespSampleData**: sample with 2,500 tuples, joining tables *patient*, *exams* and *outcome*  
 -  **ctypes-fapesp**: attribute types required when working with CSV data files in Sketch-GUI  

### IEEE Schema

Scripts to create the tables and insert the data are in the ETL folder:  

- **ETL/ieee_create_table.sql**: SQL commands to create a schema and create table *casesCovid*, composed of textual, categorical, numeric and complex data  

We also provide a sample data file to test our tool, taken from the official repository of IEEE-Covid ([here](https://github.com/ieee8023/covid-chestxray-dataset)):  

- **ieeeData**: covid cases from source with 950 tuples, composed by patients information, including complex data, processed with several FEMS  
- **ctypes-ieee**: attribute types required when working with CSV data files in Sketch-GUI  

We also provide the visual features extracted from the images available in the repository:

- **ieeeImgFeatures**: data with 950 tuples, composed of extracted feature vectors of each covid case  
