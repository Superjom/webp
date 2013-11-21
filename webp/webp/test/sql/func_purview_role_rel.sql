drop table if exists `func_purview_role_rel`;
create table func_purview_role_rel(
  id int auto_increment not null primary key,
  func_id int not null,
  purview_id int not null,
  role_id int not null
);