var baseUrl = '/qx/user';

function User(){};

User.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&keyword="+encodeURI($("#keyword").val())+"&ajaxid="+Math.random(),async:false});
		$("#user_list").html(htmlobj.responseText);
		$("#user_create").hide();
		$("#user_update").hide();
		$("#user_list").show();
		
	},

	del : function(user_id){
		if(!confirm("��ȷ��ɾ����")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&user_id="+user_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			user.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			user.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
		$("#user_create").html(htmlobj.responseText);
		$("#user_list").hide();
		$("#user_update").hide();
		$("#user_create").show();
	},
	
	create : function(){
		if(encodeURI($("#userid").val())==""){
			$("#info_1").html("�������˺�");
			$("#info_2").html("");
			$("#info_3").html("");
			$("#info_4").html("");
			$("#info_5").html("");
			return;
		}
		if(encodeURI($("#pwd").val())==""){
			$("#info_2").html("����������");
			$("#info_1").html("");
			$("#info_3").html("");
			$("#info_4").html("");
			$("#info_5").html("");
			return;
		}
		if(encodeURI($("#pwd_1").val())==""){
			$("#info_3").html("��������������");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_4").html("");
			$("#info_5").html("");
			return;
		}
		if(encodeURI($("#pwd").val())!=encodeURI($("#pwd_1").val())){
			$("#info_3").html("������������벻һ��");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_4").html("");
			$("#info_5").html("");
			return;
		}
		if(encodeURI($("#name").val())==""){
			$("#info_4").html("����������");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_3").html("");
			$("#info_5").html("");
			return;
		}
		role_id=$("input[name='role']:checked").val();
		if(typeof(role_id)=="undefined"){
			$("#info_5").html("��ѡ���ɫ");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_3").html("");
			$("#info_4").html("");
			return;
		}
		sex=$("input[name='sex']:checked").val();
		htmlobj=$.ajax({url:baseUrl+"?action=create&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&userid="+encodeURI($("#userid").val())+"&pwd="+encodeURI($("#pwd").val())+"&name="+encodeURI($("#name").val())+"&sex="+sex+"&role_id="+role_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			user.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			user.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	updateinit : function(user_id){
		htmlobj=$.ajax({url:baseUrl+"?action=updateinit&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&user_id="+user_id+"&ajaxid="+Math.random(),async:false});
		$("#user_update").html(htmlobj.responseText);
		$("#user_list").hide();
		$("#user_create").hide();
		$("#user_update").show();
	},
	
	update : function(user_id){
		if($.trim($("#isAdmin").val())=="0") {
			if(encodeURI($("#new_pwd").val())!=""&&encodeURI($("#old_pwd").val())==""){
				$("#info_1").html("������ԭ����");
				$("#info_2").html("");
				$("#info_3").html("");
				$("#info_4").html("");
				return;
			}
			if(encodeURI($("#old_pwd").val())!=""&&encodeURI($("#new_pwd").val())==""){
				$("#info_2").html("������������");
				$("#info_1").html("");
				$("#info_3").html("");
				$("#info_4").html("");
				return;
			}
		}
		if(encodeURI($("#new_pwd").val())!=""&&encodeURI($("#new_pwd_1").val())==""){
			$("#info_3").html("����������������");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_4").html("");
			return;
		}
		if(encodeURI($("#new_pwd").val())!=encodeURI($("#new_pwd_1").val())){
			$("#info_3").html("������������벻һ��");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_4").html("");
			return;
		}
		if(encodeURI($("#name").val())==""){
			$("#info_4").html("����������");
			$("#info_1").html("");
			$("#info_2").html("");
			$("#info_3").html("");
			return;
		}
		sex=$("input[name='sex']:checked").val();
		htmlobj=$.ajax({url:baseUrl+"?action=update&module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&user_id="+user_id+"&old_pwd="+encodeURI($("#old_pwd").val())+"&new_pwd="+encodeURI($("#new_pwd").val())+"&name="+encodeURI($("#name").val())+"&sex="+sex+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("�����ɹ�");
			user.list();
		}else if(htmlobj.responseText=="0"){
			alert("����ʧ��");
			user.list();
		}else{
			alert(htmlobj.responseText);
		}
	}
};

var user = null;
$(document).ready(function(){
	user = new User();
	user.list();
});