drop table if exists `func_tac_log`;
create table func_tac_log(
  id int auto_increment not null primary key,
  func_tac_id int not null,
  path varchar(500) not null,
  kind int not null,
  dt timestamp default now()
);