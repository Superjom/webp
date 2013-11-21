drop table if exists `notice`;
create table notice(
  id int auto_increment not null primary key,
  title varchar(500) not null,
  content varchar(4000),
  user_id int not null,
  dt timestamp default now()
);
insert into notice(title,content,user_id) values("The first notice","The content of notice",1);