var baseUrl = '/nonmarked/linkfunction';

function LinkFunction(){};

LinkFunction.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#linkfunction_list").html(htmlobj.responseText);
		$("#linkfunction_show").hide();
		$("#linkfunction_create").hide();
		$("#linkfunction_createschedule").hide();
		$("#linkfunction_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#linkfunction_show").html(htmlobj.responseText);
		$("#linkfunction_create").hide();
		$("#linkfunction_createschedule").hide();
		$("#linkfunction_list").show();
		$("#linkfunction_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			linkfunction.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			linkfunction.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#linkfunction_create").html(htmlobj.responseText);
		$("#linkfunction_list").hide();
		$("#linkfunction_show").hide();
		$("#linkfunction_createschedule").hide();
		$("#linkfunction_create").show();
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
			linkfunction.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			linkfunction.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#linkfunction_createschedule").html(htmlobj.responseText);
		$("#linkfunction_show").hide();
		$("#linkfunction_create").hide();
		$("#linkfunction_list").show();
		$("#linkfunction_createschedule").show();
	}
};

var linkfunction = null;
$(document).ready(function(){
	linkfunction = new LinkFunction();
	linkfunction.list();
});