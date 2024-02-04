import csv
from datetime import datetime
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def read_csv_data(file_path):
    """Reads the CSV data and returns a dictionary mapping IDs to person info."""
    persons = {}
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            try:
                datetime.strptime(row['birthday'], '%d/%m/%Y')
                persons[row['id']] = row
            except ValueError as e:
                logging.error(f"Error parsing date for ID {row['id']} with birthday {row['birthday']}: {e}")
    return persons

def get_person_info(persons, person_id):
    """Retrieves person's information by ID."""
    return persons.get(person_id, "No information found for the provided ID.")

def main():
    file_path = 'birthdays100.csv'
    persons = read_csv_data(file_path)
    
    while True:
        person_id = input("Enter ID to get person's info or 'exit' to quit: ")
        if person_id.lower() == 'exit':
            break
        print(get_person_info(persons, person_id))

if __name__ == "__main__":
    main()