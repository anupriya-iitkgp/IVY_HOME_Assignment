# IVY_HOME_Assignment
This project extracts all possible names from an autocomplete API using BFS traversal. It efficiently queries the API, handles rate limiting, and saves results in a text file.

 **API Details**

Base URL: http://35.200.185.69:8000

Endpoint: /v1/autocomplete?q Extractor - Documentation

uery=<string>

Response: JSON containing a list of names matching the query.

Rate Limiting: The API enforces a request limit (HTTP 429). The script handles this by implementing retries with delays.

**Implementation Approach**

**1. Fetching API Data**

The function fetch_results(version, query):

Sends a GET request to fetch autocomplete results.

Handles responses:

If 200 (OK), extracts results.

If 429 (Rate Limit), waits for 5 seconds before retrying.

Logs errors for other status codes.

**2. Breadth-First Search (BFS) Traversal**

The function extract_all_names(version, cap):

Initial Queries: Starts with single-character queries (a-z).
Fetching Results: Retrieves names for each query and stores them in a set.

Expanding Search:

If a query returns exactly cap (10) results, the script assumes more names exist under that prefix.

It appends characters (a-z) to the query and continues searching.

Rate Limit Handling: Implements a 0.5-second delay between requests to avoid excessive API calls.

**3. Saving Results**

Extracted names are stored in extracted_names.txt.

The script prints:

Total API requests made

Total unique names extracted
Execution

To run the script, use:
**python extractor.py**


**Output**

Extracted names are printed in the console.

All names are saved in extracted_names.txt.
