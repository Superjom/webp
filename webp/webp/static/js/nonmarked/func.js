var url = document.baseURI;
var index = url.lastIndexOf('?')
//console.log('url:' + url);
//console.log('index:' + index);
if(index == -1) {
    var baseUrl = url;
} else {
var baseUrl = url.substr(0, index);
}

console.log('baseUrl:' + baseUrl);

function Func(){};

Func.prototype = {
    list : function(){
        htmlobj=$.ajax({url:baseUrl+"/list?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
        $("#func_list").html(htmlobj.responseText);
        $("#func_show").hide();
        $("#func_create").hide();
        $("#func_createschedule").hide();
        $("#func_list").show();
        
    },

    show : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/show?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#func_show").html(htmlobj.responseText);
        $("#func_create").hide();
        $("#func_createschedule").hide();
        $("#func_list").show();
        $("#func_show").show();
    },
    
    del : function(func_tac_id){
        if(!confirm("您确定删除吗？")){
            return;
        }
        htmlobj=$.ajax({url:baseUrl+"/delete?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        if (htmlobj.responseText=="1"){
            alert("操作成功");
            func.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            func.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createinit : function(){
        htmlobj=$.ajax({url:baseUrl+"/createinit?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
        $("#func_create").html(htmlobj.responseText);
        $("#func_list").hide();
        $("#func_show").hide();
        $("#func_createschedule").hide();
        $("#func_create").show();
    },
    
    create : function(){
        tac_id=$("input[name='tac']:checked").val();
        if(typeof(tac_id)=="undefined"){
            $("#info_1").html("请选择策略");
            return;
        }
        htmlobj=$.ajax({url:baseUrl+"/create?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_id="+tac_id+"&ajaxid="+Math.random(),async:false});
        if (htmlobj.responseText=="1"){
            alert("操作成功");
            func.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            func.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createschedule : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/createschedule?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#func_createschedule").html(htmlobj.responseText);
        $("#func_show").hide();
        $("#func_create").hide();
        $("#func_list").show();
        $("#func_createschedule").show();
    }
};

var func_= null;
$(document).ready(function(){
    func = new Func();
    func.list();
});
