var baseUrl = '/nonmarked/recallcase';

function RecallCase(){};

RecallCase.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#recallcase_list").html(htmlobj.responseText);
		$("#recallcase_show").hide();
		$("#recallcase_create").hide();
		$("#recallcase_createschedule").hide();
		$("#recallcase_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#recallcase_show").html(htmlobj.responseText);
		$("#recallcase_create").hide();
		$("#recallcase_createschedule").hide();
		$("#recallcase_list").show();
		$("#recallcase_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			recallcase.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			recallcase.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#recallcase_create").html(htmlobj.responseText);
		$("#recallcase_list").hide();
		$("#recallcase_show").hide();
		$("#recallcase_createschedule").hide();
		$("#recallcase_create").show();
	},
	
	create : function(){
		taca_id=$("input[name='taca']:checked").val();
		if(typeof(taca_id)=="undefined"){
			$("#info_1").html("请选择策略");
			$("#info_2").html("");
			return;
		}
		tacb_id=$("input[name='tacb']:checked").val();
		if(typeof(tacb_id)=="undefined"){
			$("#info_1").html("");
			$("#info_2").html("请选择策略");
			return;
		}
		if(taca_id==tacb_id){
			$("#info_1").html("");
			$("#info_2").html("不能选择同样的策略");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&taca_id="+taca_id+"&tacb_id="+tacb_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			recallcase.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			recallcase.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#recallcase_createschedule").html(htmlobj.responseText);
		$("#recallcase_show").hide();
		$("#recallcase_create").hide();
		$("#recallcase_list").show();
		$("#recallcase_createschedule").show();
	}
};

var recallcase = null;
$(document).ready(function(){
	recallcase = new RecallCase();
	recallcase.list();
});