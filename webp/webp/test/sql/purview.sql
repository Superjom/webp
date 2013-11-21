drop table if exists `purview`;
create table purview(
  id int auto_increment not null primary key,
  flag varchar(50) not null,
  name varchar(500) not null
);
insert into purview(flag,name) values("query","查询");
insert into purview(flag,name) values("update","修改");
insert into purview(flag,name) values("create","创建");
insert into purview(flag,name) values("delete","删除");
insert into purview(flag,name) values("download","下载");