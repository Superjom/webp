drop table if exists `func`;
create table func(
  id int auto_increment not null primary key,
  module_id int not null,
  flag varchar(50) not null,
  name varchar(500) not null,
  description varchar(1000),
  sequence int not null
);
insert into func(module_id,flag,name,description,sequence) values(1,"qx","角色管理","用户组的管理",1);
insert into func(module_id,flag,name,description,sequence) values(1,"qx","用户管理","用户的管理",2);
insert into func(module_id,flag,name,description,sequence) values(2,"nonmarkedtac","策略","非标注模块的策略",1);
insert into func(module_id,flag,name,description,sequence) values(2,"anchorstat","基于anchor的统计评估","在新旧策略基础数据中，统计出tourl的总个数、锚文本的长度总和以及tourl的平均锚文本长度。",2);
insert into func(module_id,flag,name,description,sequence) values(2,"linkfunction","基于linkfunction的统计评估","在新旧策略基础数据中，统计出linkfunction字段(32位)中各位的含义以及非0个数。",3);
insert into func(module_id,flag,name,description,sequence) values(2,"fieldstat","基于field的统计评估","在新旧策略基础数据中，统计出其中17个字段中每一个字段的含义、字段号、非0个数以及位统计。",4);
insert into func(module_id,flag,name,description,sequence) values(2,"fieldcase","基于fieldcase的抽样评估","在新旧策略基础数据中，根据fromurl和tourl求交集并抽样，按照一定比例输出每一个待统计特征出现变化的case。",5);
insert into func(module_id,flag,name,description,sequence) values(2,"recallcase","基于反链数召回的统计评估","在新旧策略基础数据中，找出反链数增加(减少)topn的记录，然后输出这些url对应的超链基础数据记录。",6);
insert into func(module_id,flag,name,description,sequence) values(2,"googlepr","基于googlepr的统计评估","在新旧策略基础数据中，根据反链数的阀值和googlepr值过滤，找出符合条件的全部记录，并输出新旧策略的diff。",7);
insert into func(module_id,flag,name,description,sequence) values(2,"linkcount","反链数记录的pr平均值统计评估","在新旧策略反链统计数据中，统计出反链数topn的平均pr值。",8);
insert into func(module_id,flag,name,description,sequence) values(2,"pp","基于pp的统计评估","在新旧策略pagerank数据中，统计出pp准确率和召回率。",9);
insert into func(module_id,flag,name,description,sequence) values(3,"markedtac","策略","标注模块的策略",1);
insert into func(module_id,flag,name,description,sequence) values(3,"spam","作弊统计评估","根据计算和标注的数据，评估作弊的相关指标",2);
insert into func(module_id,flag,name,description,sequence) values(3,"quality","Top反链质量评估","根据计算和标注的数据，评估Top反链质量的相关指标",3);
insert into func(module_id,flag,name,description,sequence) values(4,"dcgtac","策略","DCG模块的策略",1);
insert into func(module_id,flag,name,description,sequence) values(4,"rankla","RankLa评估","RankLa评估",2);
insert into func(module_id,flag,name,description,sequence) values(4,"rankscore","RankScore评估","RankScore评估",3);
insert into func(module_id,flag,name,description,sequence) values(5,"monitortac","策略","监控模块的策略",1);
insert into func(module_id,flag,name,description,sequence) values(5,"garwz","Gar&百度文库&百度知道监控","Garbage、百度文库、百度知道相关指标的监控",2);
insert into func(module_id,flag,name,description,sequence) values(5,"interdiff","Inter&Diff监控","Inter、Diff相关指标的监控",3);
