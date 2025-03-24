import requests
import time
from collections import deque


def fetch_results(version, query):
    # param version
    """Fetch autocomplete results for a given query from the API."""
    url = f"http://35.200.185.69:8000/{version}/autocomplete?query={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        elif response.status_code == 429:
            print("Rate limit reached. Retrying after Sleeping for 5 seconds...")
            time.sleep(5)  # Wait for rate limit reset
            return fetch_results(version, query)  # Retry request
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

def extract_all_names(version, cap):
    """Extracts all possible names from the autocomplete API using BFS traversal."""
    discovered_names = set()
    queue = deque([chr(i) for i in range(97, 123)])  # Start with 'a' to 'z'
    request_count = 0
    while queue:
        query = queue.popleft()
        # Fetch results from the API
        request_count +=1
        results = fetch_results(version, query)

        for name in results:
            if name not in discovered_names:
                discovered_names.add(name)
        
        print(f"query: {query} with result size : {len(results)} and result: {results}")
        # If we received exactly 10 results, there might be more under this prefix
        if len(results) == cap:
            last_result = results[-1]
            last_result_next_char = last_result[len(query)]
            for char in range(97, 123): # Append 'a' to 'z' to explore deeper
                if last_result_next_char<=chr(char):
                    queue.append(query + chr(char))
            print(f"last char: {last_result_next_char} and queue size left: {len(queue)}")
        time.sleep(0.5)
        
    
    return discovered_names, request_count

if __name__ == "__main__":
    version = "v1"
    cap = 10
    all_names, request_count = extract_all_names(version, cap)
    print(f'Version: {version} with capping: {cap}')
    print(f'Request counts: {request_count}')
    print(f"Total names extracted: {len(all_names)}")
    # Save results to a file
    with open("extracted_names.txt", "w") as f:
        for name in sorted(all_names):
            f.write(name + "\n")
    print("Names saved to extracted_names.txt")