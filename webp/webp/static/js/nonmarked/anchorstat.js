var baseUrl = '/nonmarked/anchorstat';

function Anchorstat(){};

Anchorstat.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#anchorstat_list").html(htmlobj.responseText);
		$("#anchorstat_show").hide();
		$("#anchorstat_create").hide();
		$("#anchorstat_createschedule").hide();
		$("#anchorstat_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#anchorstat_show").html(htmlobj.responseText);
		$("#anchorstat_create").hide();
		$("#anchorstat_createschedule").hide();
		$("#anchorstat_list").show();
		$("#anchorstat_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("��ȷ��ɾ����")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			anchorstat.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			anchorstat.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#anchorstat_create").html(htmlobj.responseText);
		$("#anchorstat_list").hide();
		$("#anchorstat_show").hide();
		$("#anchorstat_createschedule").hide();
		$("#anchorstat_create").show();
	},
	
	create : function(){
		tac_id=$("input[name='tac']:checked").val();
		if(typeof(tac_id)=="undefined"){
			$("#info_1").html("��ѡ�����");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_id="+tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			anchorstat.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			anchorstat.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#anchorstat_createschedule").html(htmlobj.responseText);
		$("#anchorstat_show").hide();
		$("#anchorstat_create").hide();
		$("#anchorstat_list").show();
		$("#anchorstat_createschedule").show();
	}
};

var anchorstat = null;
$(document).ready(function(){
	anchorstat = new Anchorstat();
	anchorstat.list();
});