drop table if exists `module`;
create table module(
  id int auto_increment not null primary key,
  flag varchar(50) not null,
  name varchar(500) not null,
  description varchar(1000),
  sequence int not null
);
insert into module(flag,name,description,sequence) values("qx","权限","用来管理系统的权限",1);
insert into module(flag,name,description,sequence) values("nonmarked","非标注","关于非标注集的评估",2);
insert into module(flag,name,description,sequence) values("marked","标注","关于标注集的评估",3);
insert into module(flag,name,description,sequence) values("dcg","DCG评估","关于DCG的评估",4);
insert into module(flag,name,description,sequence) values("monitor","监控","对sortmerge数据的监控",5);