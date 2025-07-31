# 🎓 Campus Admit

**Campus Admit** is a Python + SQL-based student portal system that streamlines the college admission process. It enables students to explore and apply to colleges based on filters like cutoff, domain, fee structure, and location. The system also supports profile management, application tracking, course listings, and scholarship details — all in one place.

---

## 🚀 Features

- 🔐 **User Authentication** – Secure login and account management for students.
- 🎯 **Advanced College Search** – Filter colleges by cutoff marks, domain, fees, and preferred location.
- 🧑‍🎓 **Student Profile Management** – Store and update personal and academic details.
- 📚 **Course Listings** – View available courses across multiple institutions.
- 📝 **Application Tracking** – Apply to colleges and track application status.
- 🎓 **Scholarship Information** – Display available scholarships with eligibility criteria.
- 📂 **Data-Driven** – Course and college information loaded via CSV (`courses.csv`, `colleges.csv`).

---

## 🧰 Technologies Used

- **Python 3.x** – Core programming language.
- **MySQL** – Relational database system for storing student and college data.
- **MySQL Connector for Python** – Facilitates communication with the database.
- **Pandas** – For loading and managing CSV datasets.

---

## 📁 Project Structure

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

---

## 🗃️ Database Schema

### 📄 `accounts` Table

| Field     | Type         | Null | Key | Extra  |
|-----------|--------------|------|-----|--------|
| `id`      | BIGINT       | YES  | UNI |        |
| `username`| VARCHAR(50)  | YES  |     |        |
| `password`| VARCHAR(10)  | YES  |     |        |

---

### 📄 `student_details` Table

| Field              | Type         | Description                   |
|--------------------|--------------|-------------------------------|
| `std_id`           | BIGINT       | Primary key                   |
| `name`             | VARCHAR(20)  | Student name                  |
| `college_id`       | INT          | Applied college ID            |
| `college_name`     | VARCHAR(60)  | Applied college name          |
| `mother_name`      | VARCHAR(20)  | Mother's name                 |
| `father_name`      | VARCHAR(20)  | Father's name                 |
| `address`          | VARCHAR(30)  | Residential address           |
| `major`            | VARCHAR(30)  | Chosen major/domain           |
| `date_of_admission`| DATE         | Admission date                |
| `course_duration`  | INT          | Course duration in years      |
| `email`            | VARCHAR(30)  | Contact email                 |
| `contact`          | BIGINT       | Phone number                  |

---

## ⚙️ How to Run

### Step 1: Set Up the Database

```bash
1. Create a new MySQL database (e.g., `campus_admit`).
2. Create the tables: `accounts`, `student_details`.
3. Optionally import CSV data into the database or let the app handle it during runtime.
```

### Step 2: Install Dependencies

```bash
pip install mysql-connector-python pandas
```

### Step 3: Run the Application

```bash
python main.py
```

---

## 🧭 Usage Flow

1. **Sign up or log in** using a username and password.
2. **Search colleges** by applying filters such as domain, fee range, and location.
3. **Explore available courses** offered by selected colleges.
4. **View scholarship details** and eligibility.
5. **Apply to colleges** directly from the portal.
6. **Update and manage your student profile.**

---

## 🌱 Future Enhancements

- 🌐 Web-based interface with Flask/Django frontend.
- 📈 Analytics dashboard for application insights.
- 📬 Email notifications for application status updates.
- 📅 Calendar integration for admission deadlines.
- 🔍 Enhanced filtering with entrance exam results or reservation categories.

---

## 🤝 Contribution

Contributions are welcome! Feel free to:

- 🐛 Report bugs  
- 🌟 Suggest new features  
- 📦 Submit pull requests with enhancements  

---

## 📄 License

This project is open-source and free to use.  
> You may include a license like MIT or Apache 2.0 here.

---

## 👩‍💻 Author

Developed with passion by **Vishwaridha S.** 🎉  
> Connect with me for collaboration or feedback!
