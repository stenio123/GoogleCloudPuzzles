# Puzzle 1: 2021 - 10 -01
## Cloud Function | Google Sheets | Big Query

### Challenge:
Based on the following table on Google Sheets

```
Team Name | Team member 1      | Team member 2      |
Aardvark  | john@google.com    | jane@google.com    |
Bear      | sue@google.com     | karthak@google.com |
Cat       | hongtao@google.com | samir@google.com   |
```

Select a team, and from this team a member, both randomly. Use Cloud Functions and BigQuery external table. 
Assume data location in spreadsheet won't change.

Example output would be:

```
{

  "team": "Aardvark",
  "members": ["john@google.com", "jane@google.com"],
  "presenter": "jane@google.com"
}
```

