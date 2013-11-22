var baseUrl = '/marked/spam';

function Spam(){};

Spam.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#spam_list").html(htmlobj.responseText);
		$("#spam_show").hide();
		$("#spam_create").hide();
		$("#spam_createschedule").hide();
		$("#spam_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#spam_show").html(htmlobj.responseText);
		$("#spam_create").hide();
		$("#spam_createschedule").hide();
		$("#spam_list").show();
		$("#spam_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			spam.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			spam.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#spam_create").html(htmlobj.responseText);
		$("#spam_list").hide();
		$("#spam_show").hide();
		$("#spam_createschedule").hide();
		$("#spam_create").show();
	},
	
	create : function(){
		tac_id=$("input[name='tac']:checked").val();
		if(typeof(tac_id)=="undefined"){
			$("#info_1").html("请选择策略");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_id="+tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			spam.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			spam.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#spam_createschedule").html(htmlobj.responseText);
		$("#spam_show").hide();
		$("#spam_create").hide();
		$("#spam_list").show();
		$("#spam_createschedule").show();
	}
};

var spam = null;
$(document).ready(function(){
	spam = new Spam();
	spam.list();
});