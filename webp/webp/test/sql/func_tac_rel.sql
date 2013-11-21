drop table if exists `func_tac_rel`;
create table func_tac_rel(
  id int auto_increment not null primary key,
  func_id int not null,
  taca_id int not null,
  tacb_id int,
  user_id int not null,
  status int not null,
  description varchar(100),
  dt timestamp default now()
);