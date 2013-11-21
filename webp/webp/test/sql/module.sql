drop table if exists `module`;
create table module(
  id int auto_increment not null primary key,
  flag varchar(50) not null,
  name varchar(500) not null,
  description varchar(1000),
  sequence int not null
);
insert into module(flag,name,description,sequence) values("qx","Ȩ��","��������ϵͳ��Ȩ��",1);
insert into module(flag,name,description,sequence) values("nonmarked","�Ǳ�ע","���ڷǱ�ע��������",2);
insert into module(flag,name,description,sequence) values("marked","��ע","���ڱ�ע��������",3);
insert into module(flag,name,description,sequence) values("dcg","DCG����","����DCG������",4);
insert into module(flag,name,description,sequence) values("monitor","���","��sortmerge���ݵļ��",5);