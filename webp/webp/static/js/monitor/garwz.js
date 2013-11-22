var baseUrl = '/monitor/garwz';

function GarWZ(){};

GarWZ.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#garwz_list").html(htmlobj.responseText);
		$("#garwz_show").hide();
		$("#garwz_create").hide();
		$("#garwz_createschedule").hide();
		$("#garwz_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#garwz_show").html(htmlobj.responseText);
		$("#garwz_create").hide();
		$("#garwz_createschedule").hide();
		$("#garwz_list").show();
		$("#garwz_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("��ȷ��ɾ����")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			garwz.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			garwz.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#garwz_create").html(htmlobj.responseText);
		$("#garwz_list").hide();
		$("#garwz_show").hide();
		$("#garwz_createschedule").hide();
		$("#garwz_create").show();
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
			garwz.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			garwz.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#garwz_createschedule").html(htmlobj.responseText);
		$("#garwz_show").hide();
		$("#garwz_create").hide();
		$("#garwz_list").show();
		$("#garwz_createschedule").show();
	}
};

var garwz = null;
$(document).ready(function(){
	garwz = new GarWZ();
	garwz.list();
});