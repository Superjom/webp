drop table if exists `role`;
create table role(
  id int auto_increment not null primary key,
  name varchar(500) not null,
  description varchar(1000),
  dt timestamp default now()
);
insert into role(name,description) values("系统管理员","百度管理员，拥有最高权限");