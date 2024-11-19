drop table if exists course_assignments;
drop table if exists teachers;
drop table if exists enrollments;
drop table if exists courses;
drop table if exists students;

create table if not exists students(
	student_id integer generated always as identity primary key,
	age integer check(age>=0),
	email varchar(50) UNIQUE not null
);

create table if not exists courses(
	course_id integer generated always as identity primary key,
	course_code numeric(7,2) unique not null
);

create table if not exists enrollments(
	enrollment_id integer generated always as identity primary key,
	student_id INTEGER REFERENCES students(student_id) on delete cascade,
	course_id integer REFERENCES courses(course_id) on delete cascade
);

create table if not exists teachers(
	teacher_id integer generated always as identity primary key,
	experience_years integer check(experience_years>0)
);

create table if not exists course_assignments(
	assigment_id integer generated always as identity primary key,
	teacher_id integer REFERENCES students(student_id) on delete cascade,
	course_id INTEGER references courses(course_id) on delete cascade
);

insert into students(age,email) VALUES
(15,'tohir1@gmail.com'),
(12,'tohir2@gmail.com'),
(24,'tohir3@gmail.com'),
(21,'tohir4@gmail.com'),
(364,'tohir5@gmail.com'),
(78,'tohir6@gmail.com'),
(105,'tohir7@gmail.com');

insert into courses(course_code) values
(1),
(2),
(3);

insert into enrollments(student_id,course_id) VALUES
(1,1),
(5,1),
(6,2);

insert into teachers(experience_years)VALUES
(5),
(4),
(999);

insert into course_assignments(teacher_id,course_id)VALUES
(1,2),
(2,2),
(1,2);

alter table students
rename table talabalar;

alter table students
alter COLUMN age to yosh;

update students set age = 14 where student_id =3;
update students set age = 674 where student_id =5;
select * from students;



