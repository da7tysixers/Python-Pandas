contacts = {
    'number': 4,
    'students': [
        { 'name': 'Sarah Holderness', 'email': 'sarah.holderness@example.com' },
        { 'name': 'John Doe', 'email': 'john.doe@example.com' },
        { 'name': 'Jane Smith', 'email': 'jane.smith@example.com' },
        { 'name': 'Bob Johnson', 'email': 'bob.johnson@example.com' }

    ]
}

for student in contacts['students']:
    for key, value in student.items():
        if value.find('@') != -1:
            print(value)