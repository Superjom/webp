var baseUrl = '/nonmarked/fieldstat';

function FieldStat(){};

FieldStat.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#fieldstat_list").html(htmlobj.responseText);
		$("#fieldstat_show").hide();
		$("#fieldstat_create").hide();
		$("#fieldstat_createschedule").hide();
		$("#fieldstat_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#fieldstat_show").html(htmlobj.responseText);
		$("#fieldstat_create").hide();
		$("#fieldstat_createschedule").hide();
		$("#fieldstat_list").show();
		$("#fieldstat_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			fieldstat.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			fieldstat.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#fieldstat_create").html(htmlobj.responseText);
		$("#fieldstat_list").hide();
		$("#fieldstat_show").hide();
		$("#fieldstat_createschedule").hide();
		$("#fieldstat_create").show();
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
			fieldstat.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			fieldstat.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#fieldstat_createschedule").html(htmlobj.responseText);
		$("#fieldstat_show").hide();
		$("#fieldstat_create").hide();
		$("#fieldstat_list").show();
		$("#fieldstat_createschedule").show();
	}
};

var fieldstat = null;
$(document).ready(function(){
	fieldstat = new FieldStat();
	fieldstat.list();
});