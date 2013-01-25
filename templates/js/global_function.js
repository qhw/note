// JavaScript Document
function htmlspecialchars(html)
{
	html = html.replace(/"/g, "&quot;");
	return html
}

function specailcharstohtml(html)
{
	html = html.replace(/&quot;/g, '"');
	alert(html);
	return html
}

function switchTab(note_id)
{
	$.post("/one/", { id : note_id},
		 function(data){
			 result = eval('(' + data + ')');//解析json数据
			 $("#show_id").html(result["id"]);
			 $("#show_subject").html(result["subject"]);
			 $("#show_content").html(result["content"]);
		 });
	$( "#show" ).show();
	$( "#edit").hide();
}

function getsubjects()
{
	$.post("/subjects/", function(data){
			 results = eval('(' + data + ')');//解析json数据
			 note_id = [];
			 for (var key in results)
			 {
				 $(".nav.nav-tabs").append("<li><a href='' data-toggle='tab' onclick='switchTab(" + results[key][0] + ")'>" + results[key][1] + "</a></li>");
				 note_id.push(results[key][0]);
			 }
			 $(".active").removeClass("active", 1000, null); //移除所有当前活动项 
			 $(".nav.nav-tabs").find("li:first").addClass("active", 1000, null);//添加上活动项
			 switchTab(note_id[0]);
		 });
}