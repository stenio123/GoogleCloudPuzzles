from google.cloud import bigquery
import google.auth
import json
import random

def runQuery (request):
    # Create credentials with Drive & BigQuery API scopes.
    # Both APIs must be enabled for your project before running this code.
    credentials, project = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/bigquery",
        ]
    )
    client = bigquery.Client(credentials=credentials, project=project)
    query_job = client.query(
        """
        SELECT * 
        FROM `total-casing-317713.test.PuzzleData` 
        ORDER BY  RAND()  
        LIMIT 1 
        OFFSET 1
        """
    )

    results = query_job.result()  # Waits for job to complete.
    
    output = {}
    presenterIndex = random.randint(1, 2)

    for row in results:
        print("team={}, u1={}, u2={}".format(row[0], row[1], row[2]))
        output = {
            "team": row[0],
            "members":[row[1], row[2]],
            "presenter": row[presenterIndex]
        }

    return json.dumps(output)
