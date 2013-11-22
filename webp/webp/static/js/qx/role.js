var baseUrl = '/qx/role';

function Role(){};

Role.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&keyword="+encodeURI($("#keyword").val())+"&ajaxid="+Math.random(),async:false});
		$("#role_list").html(htmlobj.responseText);
		$("#role_create").hide();
		$("#role_update").hide();
		$("#role_list").show();
	},

	del : function(role_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&role_id="+role_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			rolee.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			rolee.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#role_create").html(htmlobj.responseText);
		$("#role_list").hide();
		$("#role_update").hide();
		$("#role_create").show();
	},
	
	create : function(){
		if($("#name").val()==""){
			$("#info_1").html("请输入名称");
			return;
		}
		var fps = "";
		$("input[name='func_purview']:checked").each(function(){
			fps += "&fp="+$(this).val();
		});
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&name="+encodeURI($("#name").val())+"&description="+encodeURI($("#description").val())+fps+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			rolee.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			rolee.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	updateinit : function(role_id){
		htmlobj=$.ajax({url:baseUrl+"?action=updateinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&role_id="+role_id+"&ajaxid="+Math.random(),async:false});
		$("#role_update").html(htmlobj.responseText);
		$("#role_list").hide();
		$("#role_create").hide();
		$("#role_update").show();
	},
	
	update : function(role_id){
		if($("#name").val()==""){
			$("#info_1").html("请输入名称");
			return;
		}
		var fps = "";
		$("input[name='func_purview']:checked").each(function(){
			fps += "&fp="+$(this).val();
		});
		htmlobj=$.ajax({url:baseUrl+"?action=update&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&role_id="+role_id+"&description="+encodeURI($("#description").val())+fps+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			rolee.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			rolee.list();
		}else{
			alert(htmlobj.responseText);
		}
	}
};

var rolee = null;
$(document).ready(function(){
	rolee = new Role();
	rolee.list();
});