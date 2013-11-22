var baseUrl = '/personalset';

function PersonalSet(){};

PersonalSet.prototype = {
	update : function(){
		if($('#new_pwd').val() != "" && $('#old_pwd').val() == ""){
			$('#info_1').html("请输入原密码");
			return false;
		} else {
			$('#info_1').html("");
		}
		if($('#old_pwd').val() != "" && $('#new_pwd').val() == ""){
			$('#info_2').html("请输入新密码");
			return false;
		} else {
			$('#info_2').html("");
		}
		if($('#new_pwd').val() != $('#new_pwd_1').val()){
			$('#info_3').html("两次密码输入不一致");
			return false;
		} else {
			$('#info_3').html("");
		}
		return true;
	}
};

var personalset = null;
$(document).ready(function(){
	personalset = new PersonalSet();
});