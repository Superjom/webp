var baseUrl = '/nonmarked/pp';
var baseUrl = '/nonmarked/pp';

function Anchorstat(){};

Anchorstat.prototype = {
    list : function(){
        htmlobj=$.ajax({url:baseUrl+"/list?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
        $("#pp_list").html(htmlobj.responseText);
        $("#pp_list").html(htmlobj.responseText);
        $("#pp_show").hide();
        $("#pp_show").hide();
        $("#pp_create").hide();
        $("#pp_create").hide();
        $("#pp_createschedule").hide();
        $("#pp_createschedule").hide();
        $("#pp_list").show();
        $("#pp_list").show();
        
    },

    show : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/show?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#pp_show").html(htmlobj.responseText);
        $("#pp_show").html(htmlobj.responseText);
        $("#pp_create").hide();
        $("#pp_create").hide();
        $("#pp_createschedule").hide();
        $("#pp_createschedule").hide();
        $("#pp_list").show();
        $("#pp_list").show();
        $("#pp_show").show();
        $("#pp_show").show();
    },
    
    del : function(func_tac_id){
        if(!confirm("您确定删除吗？")){
            return;
        }
        htmlobj=$.ajax({url:baseUrl+"/delete?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        if (htmlobj.responseText=="1"){
            alert("操作成功");
            pp.list();
            pp.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            pp.list();
            pp.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createinit : function(){
        htmlobj=$.ajax({url:baseUrl+"/createinit?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
        $("#pp_create").html(htmlobj.responseText);
        $("#pp_create").html(htmlobj.responseText);
        $("#pp_list").hide();
        $("#pp_list").hide();
        $("#pp_show").hide();
        $("#pp_show").hide();
        $("#pp_createschedule").hide();
        $("#pp_createschedule").hide();
        $("#pp_create").show();
        $("#pp_create").show();
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
            pp.list();
            pp.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            pp.list();
            pp.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createschedule : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/createschedule?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#pp_createschedule").html(htmlobj.responseText);
        $("#pp_createschedule").html(htmlobj.responseText);
        $("#pp_show").hide();
        $("#pp_show").hide();
        $("#pp_create").hide();
        $("#pp_create").hide();
        $("#pp_list").show();
        $("#pp_list").show();
        $("#pp_createschedule").show();
        $("#pp_createschedule").show();
    }
};

var pp = null;
var pp = null;
$(document).ready(function(){
    pp = new Anchorstat();
    pp = new Anchorstat();
    pp.list();
    pp.list();
});
