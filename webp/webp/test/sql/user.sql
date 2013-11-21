drop table if exists `user`;
create table user(
  id int auto_increment not null primary key,
  userid varchar(50) not null,
  pwd varchar(200) not null,
  name varchar(500) not null,
  sex int not null default 1,
  dt timestamp default now(),
  role_id int not null
);
insert into user(userid,pwd,name,role_id) values("admin",password("admin"),"张三",1);