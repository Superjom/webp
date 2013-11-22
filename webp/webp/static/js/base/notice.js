var baseUrl = '/notice';

function Notice(){};

Notice.prototype = {
	list : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=list&keyword="+encodeURI($("#keyword").val())+"&ajaxid="+Math.random(),async:false});
		$("#notice_list").html(htmlobj.responseText);
		$("#notice_create").hide();
		$("#notice_update").hide();
		$("#notice_list").show();
		
	},
	
	del : function(notice_id){
		if(!confirm("您确定删除吗？")){
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=delete&notice_id="+notice_id+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			notice.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			notice.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	createinit : function(){
		htmlobj=$.ajax({url:baseUrl+"?action=createinit&ajaxid="+Math.random(),async:false});
		$("#notice_create").html(htmlobj.responseText);
		$("#notice_list").hide();
		$("#notice_update").hide();
		$("#notice_create").show();
	},
	
	create : function(){
		if(encodeURI($("#title").val())==""){
			$("#info_1").html("请输入标题");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=create&title="+encodeURI($("#title").val())+"&content="+encodeURI($("#content").val())+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			notice.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			notice.list();
		}else{
			alert(htmlobj.responseText);
		}
	},
	
	updateinit : function(notice_id){
		htmlobj=$.ajax({url:baseUrl+"?action=updateinit&notice_id="+notice_id+"&ajaxid="+Math.random(),async:false});
		$("#notice_update").html(htmlobj.responseText);
		$("#notice_list").hide();
		$("#notice_create").hide();
		$("#notice_update").show();
	},
	
	update : function(notice_id){
		if(encodeURI($("#title").val())==""){
			$("#info_1").html("请输入标题");
			return;
		}
		htmlobj=$.ajax({url:baseUrl+"?action=update&notice_id="+notice_id+"&title="+encodeURI($("#title").val())+"&content="+encodeURI($("#content").val())+"&ajaxid="+Math.random(),async:false});
		if (htmlobj.responseText=="1"){
			alert("操作成功");
			notice.list();
		}else if(htmlobj.responseText=="0"){
			alert("操作失败");
			notice.list();
		}else{
			alert(htmlobj.responseText);
		}
	}
};

var notice = null;
$(document).ready(function(){
	notice = new Notice();
	notice.list();
});