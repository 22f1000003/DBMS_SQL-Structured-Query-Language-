--DDL command;
1. **CREATE**
2. **ALTER**
3. **DROP**
4. **TRUNCATE**
5. **RENAME**



create table student (
rollno varchar(18) primary key,
name char(10) unique,
dob date not null,
age int not null,
active boolean,
check (age>16)
);
select * from student 

insert into student values ('22f1000003','satyam','10-06-2002',24,True)
insert into student(rollno ,name, dob, age) values('23f12345','madhav','24-10-2004',21)
alter table student
add credit numeric(3,0);


                                                  

alter table student
drop column credit 


