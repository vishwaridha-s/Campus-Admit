# Campus Admit

Campus Admit is a student portal system built using Python and SQL. It allows students to search for colleges based on cutoff, domain, fees, and location. The system also includes features for account creation, applications, scholarship details, course listings, and eligibility checks.

## Features

```
- User Authentication: Secure login and account management.
- College Search: Filter colleges based on cutoff, domain, fees, and location.
- Student Profile Management: Store and update student details.
- Course Listings: Browse available courses in different colleges.
- Application Tracking: Manage student applications for colleges.
- Scholarship Information: Display available scholarships and eligibility criteria.
- Data Storage: College and course data are loaded from CSV files (`courses.csv` and `colleges.csv`).
```

## Prerequisites

```
- Python (3.x recommended)
- MySQL (for database management)
- MySQL Connector for Python (to interact with the database)
- Pandas (for handling CSV data)
```

## Project Structure

```
CampusAdmit/
│── main.py             # Entry point of the program
│── database.py         # Handles database connection and queries
│── authentication.py   # Manages user login and account creation
│── search.py           # Implements college search functionality
│── apply.py            # Manages applications and scholarship information
│── courses.csv         # Dataset containing course details
└── colleges.csv        # Dataset containing college details
```

## Database Structure

### `accounts` Table

```
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| id       | bigint      | YES  | UNI | NULL    |       |
| username | varchar(50) | YES  |     | NULL    |       |
| password | varchar(10) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
```

### `student_details` Table

```
+-------------------+-------------+------+-----+---------+-------+
| Field             | Type        | Null | Key | Default | Extra |
+-------------------+-------------+------+-----+---------+-------+
| std_id            | bigint      | NO   | PRI | NULL    |       |
| name              | varchar(20) | YES  |     | NULL    |       |
| college_id        | int         | YES  |     | NULL    |       |
| college_name      | varchar(60) | YES  |     | NULL    |       |
| mother_name       | varchar(20) | YES  |     | NULL    |       |
| father_name       | varchar(20) | YES  |     | NULL    |       |
| address           | varchar(30) | YES  |     | NULL    |       |
| major             | varchar(30) | YES  |     | NULL    |       |
| date_of_admission | date        | YES  |     | NULL    |       |
| course_duration   | int         | YES  |     | NULL    |       |
| email             | varchar(30) | YES  |     | NULL    |       |
| contact           | bigint      | YES  |     | NULL    |       |
+-------------------+-------------+------+-----+---------+-------+
```

## How to Run

### Step 1: Set Up the Database

```
1. Create a MySQL database.
2. Create the `accounts` and `student_details` tables using the structure above.
3. Load data from `courses.csv` and `colleges.csv` into the respective tables.
```

### Step 2: Install Dependencies

```
pip install mysql-connector-python pandas
```

### Step 3: Run the Program

```
python main.py
```

## Usage

```
- Create an account or log in.
- Search for colleges based on criteria.
- View course details and eligibility.
- Apply to colleges and check scholarship options.
- Manage student profiles and admission status.
```

## Contribution

```
Contributions are welcome! Feel free to:
- Report bugs.
- Suggest new features.
- Open a pull request with improvements.
```

## License

```
This project is open-source and free to use. Add your preferred license here if needed.
```

## Author

```
Developed by Vishwaridha S. 🎉
```
