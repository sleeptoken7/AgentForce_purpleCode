import json

def find_path_recursive(data, term, current_path=[]):
    """
    Recursively searches a nested data structure for a term and prints the path.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = current_path + [f"'{key}'"] # Use key for dictionaries
            find_path_recursive(value, term, new_path)
    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_path = current_path + [index] # Use index for lists
            find_path_recursive(value, term, new_path)
    elif isinstance(data, str) and term in data:
        print(f"Found term '{term}' at path: {current_path}")

if __name__ == "__main__":
    # A unique name from one of the reviews we saw earlier
    search_term = "Jazeela Kunnakkadan" 

    try:
        with open('response.json', 'r') as f:
            json_data = json.load(f)

        print(f"Searching for the term '{search_term}' inside response.json...")
        find_path_recursive(json_data, search_term)
        print("\nSearch complete.")

    except FileNotFoundError:
        print("Error: response.json not found.")
    except Exception as e:
        print(f"An error occurred: {e}")