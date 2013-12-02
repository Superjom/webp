var baseUrl = '/nonmarked/linkcount';

function Anchorstat(){};

Anchorstat.prototype = {
    list : function(){
        htmlobj=$.ajax({url:baseUrl+"/list?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&tac_name="+encodeURI($("#tac_name").val())+"&ajaxid="+Math.random(),async:false});
        $("#linkcount_list").html(htmlobj.responseText);
        $("#linkcount_show").hide();
        $("#linkcount_create").hide();
        $("#linkcount_createschedule").hide();
        $("#linkcount_list").show();
        
    },

    show : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/show?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#linkcount_show").html(htmlobj.responseText);
        $("#linkcount_create").hide();
        $("#linkcount_createschedule").hide();
        $("#linkcount_list").show();
        $("#linkcount_show").show();
    },
    
    del : function(func_tac_id){
        if(!confirm("您确定删除吗？")){
            return;
        }
        htmlobj=$.ajax({url:baseUrl+"/delete?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        if (htmlobj.responseText=="1"){
            alert("操作成功");
            linkcount.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            linkcount.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createinit : function(){
        htmlobj=$.ajax({url:baseUrl+"/createinit?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&ajaxid="+Math.random(),async:false});
        $("#linkcount_create").html(htmlobj.responseText);
        $("#linkcount_list").hide();
        $("#linkcount_show").hide();
        $("#linkcount_createschedule").hide();
        $("#linkcount_create").show();
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
            linkcount.list();
        }else if(htmlobj.responseText=="0"){
            alert("操作失败");
            linkcount.list();
        }else{
            alert(htmlobj.responseText);
        }
    },
    
    createschedule : function(func_tac_id){
        htmlobj=$.ajax({url:baseUrl+"/createschedule?module_flag="+$("#module_flag").val()+"&func_flag="+$("#func_flag").val()+"&func_tac_id="+func_tac_id+"&ajaxid="+Math.random(),async:false});
        $("#linkcount_createschedule").html(htmlobj.responseText);
        $("#linkcount_show").hide();
        $("#linkcount_create").hide();
        $("#linkcount_list").show();
        $("#linkcount_createschedule").show();
    }
};

var linkcount = null;
$(document).ready(function(){
    linkcount = new Anchorstat();
    linkcount.list();
});
