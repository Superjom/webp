drop table if exists `tac`;
create table tac(
  id int auto_increment not null primary key,
  module_id int not null,
  name varchar(500) not null,
  description varchar(1000),
  dt timestamp default now(),
  key_1 varchar(100),
  value_1 varchar(500),
  key_2 varchar(100),
  value_2 varchar(500),
  key_3 varchar(100),
  value_3 varchar(500),
  key_4 varchar(100),
  value_4 varchar(500),
  key_5 varchar(100),
  value_5 varchar(500)
);
insert into tac(name,module_id,description,key_1,value_1,key_2,value_2,key_3,value_3) values("20130523",1,"20130523的线上数据作为测试策略","invlink_path","/app/ps/spider/dedup/jianglei04/link_online/invlink_bak","invlinkat_path","/app/ps/spider/dedup/jianglei04/link_online/invlink_oldformat_bak","invlinkc_path","/app/ps/spider/dedup/jianglei04/link_online/invlink_count_20130523");
insert into tac(name,module_id,description,key_1,value_1,key_2,value_2,key_3,value_3) values("20130529",1,"20130529的线上数据作为测试策略","invlink_path","/app/ps/spider/dedup/jianglei04/link_online/invlink","invlinkat_path","/app/ps/spider/dedup/jianglei04/link_online/invlink_oldformat","invlinkc_path","/app/ps/spider/dedup/jianglei04/link_online/invlink_count_20130529");