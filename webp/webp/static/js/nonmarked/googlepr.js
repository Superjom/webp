var baseUrl = '/nonmarked/googlepr';

function GooglePr(){};

GooglePr.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#googlepr_list").html(htmlobj.responseText);
		$("#googlepr_show").hide();
		$("#googlepr_create").hide();
		$("#googlepr_createschedule").hide();
		$("#googlepr_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#googlepr_show").html(htmlobj.responseText);
		$("#googlepr_create").hide();
		$("#googlepr_createschedule").hide();
		$("#googlepr_list").show();
		$("#googlepr_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			googlepr.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			googlepr.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#googlepr_create").html(htmlobj.responseText);
		$("#googlepr_list").hide();
		$("#googlepr_show").hide();
		$("#googlepr_createschedule").hide();
		$("#googlepr_create").show();
	},
	
	create : function(){
		var params = "&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val();
		taca_id=$("input[name='taca']:checked").val();
		if(typeof(taca_id)=="undefined"){
			$("#info_1").html("请选择策略");
			$("#info_2").html("");
			return;
		}
		params += "&taca_id="+taca_id;
		tacb_id=$("input[name='tacb']:checked").val();
		if(typeof(tacb_id)!="undefined"){
			params += "&tacb_id="+tacb_id;
		}
		if(taca_id==tacb_id){
			$("#info_1").html("");
			$("#info_2").html("不能选择同样的策略");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create"+params+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			googlepr.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			googlepr.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#googlepr_createschedule").html(htmlobj.responseText);
		$("#googlepr_show").hide();
		$("#googlepr_create").hide();
		$("#googlepr_list").show();
		$("#googlepr_createschedule").show();
	}
};

var googlepr = null;
$(document).ready(function(){
	googlepr = new GooglePr();
	googlepr.list();
});