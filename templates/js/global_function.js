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
			 result = eval('(' + data + ')');//����json����
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
			 results = eval('(' + data + ')');//����json����
			 note_id = [];
			 for (var key in results)
			 {
				 $(".nav.nav-tabs").append("<li><a href='' data-toggle='tab' onclick='switchTab(" + results[key][0] + ")'>" + results[key][1] + "</a></li>");
				 note_id.push(results[key][0]);
			 }
			 $(".active").removeClass("active", 1000, null); //�Ƴ����е�ǰ��� 
			 $(".nav.nav-tabs").find("li:first").addClass("active", 1000, null);//����ϻ��
			 switchTab(note_id[0]);
		 });
}