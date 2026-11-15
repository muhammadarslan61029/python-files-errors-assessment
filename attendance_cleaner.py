from pathlib import Path

INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"


def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            original_names = file.readlines()
    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' was not found.")
        print("Create the file and add one student name per line.")
        return

    original_count = len(original_names)

    # Strip extra spaces and standardize capitalization; ignore blank lines.
    cleaned_names = [
        name.strip().title()
        for name in original_names
        if name.strip()
    ]

    # A set removes duplicates after capitalization and spacing are normalized.
    unique_students = set(cleaned_names)
    sorted_students = sorted(unique_students)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as file:
        file.write("student_name\n")
        for name in sorted_students:
            file.write(f'"{name.replace(chr(34), chr(34) * 2)}"\n')

    print(f"Original number of records: {original_count}")
    print(f"Unique student count: {len(unique_students)}")
    print("\nCleaned attendance list:")
    for number, name in enumerate(sorted_students, start=1):
        print(f"{number}. {name}")

    print(f"\nCleaned list saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
