#!/usr/bin/python
chmod +x /Users/jif/Documents/practice_transform_csv.py
python /Users/jif/Documents/practice_transform_csv.py

psql -c "DROP TABLE IF EXISTS public.enterprise_survey_2018;"

psql -c "CREATE TABLE public.enterprise_survey_2018 (
    year VARCHAR,
    industry_aggregation_nzsioc VARCHAR,
    industry_code_nzsioc VARCHAR,
    industry_name_nzsioc VARCHAR,
    units VARCHAR,
    variable_code VARCHAR,
    variable_name VARCHAR,
    variable_category VARCHAR
    );"

psql -c "\COPY public.enterprise_survey_2018 FROM '/Users/jif/Repos/Automation/Files/annual_enterprise_survey_2018_transformed.csv' WITH CSV HEADER DELIMITER ',';"
