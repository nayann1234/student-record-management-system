import json
import os

FILENAME = "students_data.json"

def load_data():
    """Load student records from JSON file with exception handling."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Data file is corrupted. Starting with an empty record list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")
        return []

def save_data(students):
    """Save student records to JSON file."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def add_student(students):
    """Create a new student record."""
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()
    
    # Check if ID already exists using list comprehension & any()
    if any(s["id"] == student_id for s in students):
        print("Error: Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()
    
    # Exception handling for age input
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age! Please enter a numeric value.")
        return

    course = input("Enter Course: ").strip()

    # Using a dictionary for student record
    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(new_student)
    save_data(students)
    print(f"Success: Student {name} added successfully!")

def view_students(students):
    """Read and display all student records."""
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return

    # Using list comprehension for formatting output
    [print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}") for s in students]

def update_student(students):
    """Update an existing student record."""
    print("\n--- Update Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()
    
    for student in students:
        if student["id"] == student_id:
            print(f"Found student: {student['name']}. Leave blank to keep existing value.")
            
            new_name = input(f"New Name [{student['name']}]: ").strip()
            if new_name:
                student["name"] = new_name
                
            new_age_str = input(f"New Age [{student['age']}]: ").strip()
            if new_age_str:
                try:
                    student["age"] = int(new_age_str)
                except ValueError:
                    print("Invalid age input. Keeping old age.")
                    
            new_course = input(f"New Course [{student['course']}]: ").strip()
            if new_course:
                student["course"] = new_course
                
            save_data(students)
            print("Success: Student record updated!")
            return
            
    print("Error: Student ID not found.")

def delete_student(students):
    """Delete a student record."""
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()
    
    global students_list
    initial_length = len(students)
    
    # Lambda filter to remove the student
    updated_list = [s for s in students if s["id"] != student_id]
    
    if len(updated_list) < initial_length:
        students[:] = updated_list
        save_data(students)
        print("Success: Student record deleted!")
    else:
        print("Error: Student ID not found.")

def main():
    """Main program loop with user input/output."""
    students = load_data()
    
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student (Create)")
        print("2. View Students (Read)")
        print("3. Update Student (Update)")
        print("4. Delete Student (Delete)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
