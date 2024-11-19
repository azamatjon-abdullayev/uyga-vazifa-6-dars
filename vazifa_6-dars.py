import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='shop',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_table_teachers(self):
        sql = '''create table if not exists students(
        student_id integer generated always as identity primary key,
        age integer check(age>=0),
        email varchar(50) UNIQUE not null
    );'''
        self.manager(sql, commit=True)

    def create_table_courses(self):
        sql = '''create table if not exists courses(
	course_id integer generated always as identity primary key,
	course_code numeric(7,2) unique not null
    );'''
        self.manager(sql, commit=True)

    def create_table_enrollments(self):
        sql = '''create table if not exists enrollments(
	enrollment_id integer generated always as identity primary key,
	student_id INTEGER REFERENCES students(student_id) on delete cascade,
	course_id integer REFERENCES courses(course_id) on delete cascade
    );'''
        self.manager(sql,commit=true)

    def create_table_teachers2(self):
        sql = '''create table if not exists teachers(
	teacher_id integer generated always as identity primary key,
	experience_years integer check(experience_years>0)
);'''
        self.manager(sql, commit=true)

    def create_table_course_assignments(self):
        sql = '''create table if not exists course_assignments(
	assigment_id integer generated always as identity primary key,
	teacher_id integer REFERENCES students(student_id) on delete cascade,
	course_id INTEGER references courses(course_id) on delete cascade
);'''
        self.manager(sql, commit=true)

    def insert_teachers(self, age,email):
        sql = '''insert into students(age,email)  values (%s,%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, age,email, commit=True)

    def insert_courses(self, course_code):
        sql = '''insert into courses(course_code) values
        (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, course_code, commit=True)

    def insert_enrollments(self,student_id,course_id):
        sql = '''insert into enrollments(student_id,course_id) VALUES
        (%s,%s) on conflict do nothing'''
        self.manager(sql,student_id,course_id, commit=true)

    def insert_teachers1(self,experience_years):
        sql = '''insert into teachers(experience_years)VALUES
        (%s) on conflict do nothing'''
        self.manager(sql,experience_years, commit=true)

    def insert_couse(self,teacher_id,course_id):
        sql = '''insert into course_assignments(teacher_id,course_id)VALUES
        (%s) on conflict do nothing'''
        self.manager(sql,teacher_id,course_id,commit=true)

    def select_students(self):
        sql = '''select * from students;'''
        return self.manager(sql, fetchall=True)


    def alter_students(self):
        sql = '''alter table students
                rename table talabalar;
                
                alter table students
                alter COLUMN age to yosh;'''
        self.manager(sql,commit=true)

    def update_students(self):
        sql = '''update students set age = 14 where student_id =3;
                update students set age = 674 where student_id =5;'''
        self.manager(sql,commit=true)

db = DataBase()
