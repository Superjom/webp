var baseUrl = '/dcg/rankla';

function RankLa(){};

RankLa.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#rankla_list").html(htmlobj.responseText);
		$("#rankla_show").hide();
		$("#rankla_create").hide();
		$("#rankla_createschedule").hide();
		$("#rankla_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#rankla_show").html(htmlobj.responseText);
		$("#rankla_create").hide();
		$("#rankla_createschedule").hide();
		$("#rankla_list").show();
		$("#rankla_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("��ȷ��ɾ����")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			rankla.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			rankla.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#rankla_create").html(htmlobj.responseText);
		$("#rankla_list").hide();
		$("#rankla_show").hide();
		$("#rankla_createschedule").hide();
		$("#rankla_create").show();
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
			rankla.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			rankla.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#rankla_createschedule").html(htmlobj.responseText);
		$("#rankla_show").hide();
		$("#rankla_create").hide();
		$("#rankla_list").show();
		$("#rankla_createschedule").show();
	}
};

var rankla = null;
$(document).ready(function(){
	rankla = new RankLa();
	rankla.list();
});