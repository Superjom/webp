var baseUrl = '/monitor/tac';

function Tac(){};

Tac.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#tac_list").html(htmlobj.responseText);
		$("#tac_create").hide();
		$("#tac_update").hide();
		$("#tac_list").show();
	},

	del : function(tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_id="+tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			tac.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			tac.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#tac_create").html(htmlobj.responseText);
		$("#tac_list").hide();
		$("#tac_update").hide();
		$("#tac_create").show();
	},
	
	create : function(){
		if($("#name").val()==""){
			$("#info_1").html("请输入名称");
			return;
		}
		kvs = "&key_1="+encodeURI($("#key_1").val())+"&value_1="+encodeURI($("#value_1").val());
		kvs += "&key_2="+encodeURI($("#key_2").val())+"&value_2="+encodeURI($("#value_2").val());
		kvs += "&key_3="+encodeURI($("#key_3").val())+"&value_3="+encodeURI($("#value_3").val());
		kvs += "&key_4="+encodeURI($("#key_4").val())+"&value_4="+encodeURI($("#value_4").val());
		kvs += "&key_5="+encodeURI($("#key_5").val())+"&value_5="+encodeURI($("#value_5").val());
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&name="+encodeURI($("#name").val())+"&description="+encodeURI($("#description").val())+kvs+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			tac.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			tac.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	updateinit : function(tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=updateinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_id="+tac_id+"&ajaxid="+Math.random(),async:false});
		$("#tac_update").html(htmlobj.responseText);
		$("#tac_list").hide();
		$("#tac_create").hide();
		$("#tac_update").show();
	},
	
	update : function(tac_id){
		if($("#name").val()==""){
			$("#info_1").html("请输入名称");
			return;
		}
		kvs = "&key_1="+encodeURI($("#key_1").val())+"&value_1="+encodeURI($("#value_1").val());
		kvs += "&key_2="+encodeURI($("#key_2").val())+"&value_2="+encodeURI($("#value_2").val());
		kvs += "&key_3="+encodeURI($("#key_3").val())+"&value_3="+encodeURI($("#value_3").val());
		kvs += "&key_4="+encodeURI($("#key_4").val())+"&value_4="+encodeURI($("#value_4").val());
		kvs += "&key_5="+encodeURI($("#key_5").val())+"&value_5="+encodeURI($("#value_5").val());
		htmlobj=$.ajax({url:baseUrl+"?action=update&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&name="+encodeURI($("#name").val())+"&tac_id="+tac_id+"&description="+encodeURI($("#description").val())+kvs+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			tac.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			tac.list();
		}else{
			alert(htmlobj.responseText);
		}
	}
};

var tac = null;
$(document).ready(function(){
	tac = new Tac();
	tac.list();
});