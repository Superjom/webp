var baseUrl = '/monitor/interdiff';

function InterDiff(){};

InterDiff.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#interdiff_list").html(htmlobj.responseText);
		$("#interdiff_show").hide();
		$("#interdiff_create").hide();
		$("#interdiff_createschedule").hide();
		$("#interdiff_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#interdiff_show").html(htmlobj.responseText);
		$("#interdiff_create").hide();
		$("#interdiff_createschedule").hide();
		$("#interdiff_list").show();
		$("#interdiff_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			interdiff.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			interdiff.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#interdiff_create").html(htmlobj.responseText);
		$("#interdiff_list").hide();
		$("#interdiff_show").hide();
		$("#interdiff_createschedule").hide();
		$("#interdiff_create").show();
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
			interdiff.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			interdiff.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#interdiff_createschedule").html(htmlobj.responseText);
		$("#interdiff_show").hide();
		$("#interdiff_create").hide();
		$("#interdiff_list").show();
		$("#interdiff_createschedule").show();
	}
};

var interdiff = null;
$(document).ready(function(){
	interdiff = new InterDiff();
	interdiff.list();
});