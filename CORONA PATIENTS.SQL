create table coronapatients(
name varchar(20),
age int(5),
bodytemperature int(5),
bloodgroup varchar(10),
gender varchar(10)
);
insert into coronapatients values(
'rishi','30','105','b+ve','male'
);
insert into coronapatients values(
'rocky','10','106','b-ve','male'
);
insert into coronapatients values(
'riya','26','104','o+ve','female'
);
insert into coronapatients values(
'banu','40','105','b+ve','female'
);
insert into coronapatients values(
'priya','19','102','a+ve','female'
);
select * from coronapatients;
select distinct bloodgroup from coronapatients;
select * from coronapatients where age<20;
select * from coronapatients where bloodgroup='b+ve' and bodytemperature>100;
select * from coronapatients where gender='male'

