var baseUrl = '/nonmarked/fieldcase';

function FieldCase(){};

FieldCase.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
		$("#fieldcase_list").html(htmlobj.responseText);
		$("#fieldcase_show").hide();
		$("#fieldcase_create").hide();
		$("#fieldcase_createschedule").hide();
		$("#fieldcase_list").show();
		
	},

	show : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=show&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#fieldcase_show").html(htmlobj.responseText);
		$("#fieldcase_create").hide();
		$("#fieldcase_createschedule").hide();
		$("#fieldcase_list").show();
		$("#fieldcase_show").show();
	},
	
	del : function(func_tac_id){
		if(!confirm("��ȷ��ɾ����")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			fieldcase.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			fieldcase.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#fieldcase_create").html(htmlobj.responseText);
		$("#fieldcase_list").hide();
		$("#fieldcase_show").hide();
		$("#fieldcase_createschedule").hide();
		$("#fieldcase_create").show();
	},
	
	create : function(){
		taca_id=$("input[name='taca']:checked").val();
		if(typeof(taca_id)=="undefined"){
			$("#info_1").html("��ѡ�����");
			$("#info_2").html("");
			return;
		}
		tacb_id=$("input[name='tacb']:checked").val();
		if(typeof(tacb_id)=="undefined"){
			$("#info_1").html("");
			$("#info_2").html("��ѡ�����");
			return;
		}
		if(taca_id==tacb_id){
			$("#info_1").html("");
			$("#info_2").html("����ѡ��ͬ���Ĳ���");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&taca_id="+taca_id+"&tacb_id="+tacb_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			fieldcase.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			fieldcase.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createschedule : function(func_tac_id){
		htmlobj=$.ajax({url:baseUrl+"?action=createschedule&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
		$("#fieldcase_createschedule").html(htmlobj.responseText);
		$("#fieldcase_show").hide();
		$("#fieldcase_create").hide();
		$("#fieldcase_list").show();
		$("#fieldcase_createschedule").show();
	}
};

var fieldcase = null;
$(document).ready(function(){
	fieldcase = new FieldCase();
	fieldcase.list();
});