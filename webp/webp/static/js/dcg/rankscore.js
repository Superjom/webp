var baseUrl = '/dcg/rankscore';

function RankScore(){};

RankScore.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#rankscore_list").html(htmlobj.responseText);
		$("#rankscore_show").hide();
		$("#rankscore_create").hide();
		$("#rankscore_createschedule").hide();
		$("#rankscore_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#rankscore_show").html(htmlobj.responseText);
		$("#rankscore_create").hide();
		$("#rankscore_createschedule").hide();
		$("#rankscore_list").show();
		$("#rankscore_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			rankscore.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			rankscore.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#rankscore_create").html(htmlobj.responseText);
		$("#rankscore_list").hide();
		$("#rankscore_show").hide();
		$("#rankscore_createschedule").hide();
		$("#rankscore_create").show();
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
			rankscore.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			rankscore.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#rankscore_createschedule").html(htmlobj.responseText);
		$("#rankscore_show").hide();
		$("#rankscore_create").hide();
		$("#rankscore_list").show();
		$("#rankscore_createschedule").show();
	}
};

var rankscore = null;
$(document).ready(function(){
	rankscore = new RankScore();
	rankscore.list();
});