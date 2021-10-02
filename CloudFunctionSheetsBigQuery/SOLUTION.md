# Solution

## Google Sheets
1. Create Google Sheet:
```
Team Name | Team member 1      | Team member 2      |
Aardvark  | john@google.com    | jane@google.com    |
Bear      | sue@google.com     | karthak@google.com |
Cat       | hongtao@google.com | samir@google.com   |
```

## Big Query
1. Enable BigQuery API if needed

2. Create a Dataset by selecting the project and "Create Dataset"

3. Follow the instructions to [create an external table](https://cloud.google.com/bigquery/external-data-drive#creating_and_querying_a_permanent_external_table) in BigQuery, from Google Drive. For Google Sheets, format is CSV

4. On the "Advanced" Options, you can specify "1" for "Header rows to skip", since we don't want to count the header

5. Test the table with query
```
SELECT * FROM `PROJECT_NAME.DATASET_NAME.TABLE_NAME` 
# Randomizes rows and picks first
ORDER BY  RAND()  LIMIT 1 
# In case you didnt skip header row in the Advanced Configs
# OFFSET 1
```

6. Hopefuly you got a permission error. Open the Cloud Console and execute:
```
gcloud components update
gcloud auth login --enable-gdrive-access
# Open the URL given and authorize access
```

7. Now test the query again and it should work

## Cloud Function

1. Enable Cloud Function API if needed

2. Create a new Cloud Function

3. (Optional) If you want to enable public access, select "Allow unauthenticated". If you need to change this setting after function deployed, instructions[here](https://cloud.google.com/functions/docs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) (Note that your organization might have a policy that prevents public access)

4. Copy the contentx of main.py and requirements.py from this repo

5. Update *"PROJECT_NAME.DATASET_NAME.TABLE_NAME"* as per your previous SQL query

6. Update "entry point" to *"runQuery"* and select "Python 3.9" for Runtime

7. Deploy, and once done click to test function. If you enabled public access, function should also be accessible by the URL