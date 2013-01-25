// JavaScript Document
	var editor;
			KindEditor.ready(function(K) {
				editor = K.create('textarea[name="edit_content"]', {
					cssPath : '/kindeditor/plugins/code/prettify.css',
					uploadJson : '/upload/',
					fileManagerJson : '/file_manager_json/',
					allowFileManager : true,
					afterCreate : function() {
					var self = this;
					K.ctrl(document, 13, function() {
						self.sync();
						document.forms['example'].submit();
					});
					K.ctrl(self.edit.doc, 13, function() {
						self.sync();
						document.forms['example'].submit();
					});
					},
					width : "900px",
					height : "580px",
					items:[
						'source', '|', 'undo', 'redo', '|', 'preview', 'print', 'template', 'code', 'cut', 'copy', 'paste',
						'plainpaste', 'wordpaste', '|', 'justifyleft', 'justifycenter', 'justifyright',
						'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'subscript',
						'superscript', 'clearhtml', 'quickformat', 'selectall', '/',
						'formatblock', 'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold',
						'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|', 'image','multiimage',
       				    'flash', 'media', 'insertfile','table', 'hr', 'emoticons', 'pagebreak','anchor', 'link', 'unlink'
					]
				});
				prettyPrint();
				
		    $( "#edit_btn" ).click(function(){//编辑
            $( "#show" ).hide();
			$( "#edit").show();
			$("#edit_subject" ).val($("#show_subject").html());//标题
			editor.html($( "#show_content" ).html());//内容
			$("#edit_id").html($("#show_id").html());//文章id
			return false;
        });
			
			$( "#save_btn" ).click(function(){//保存
            $( "#edit" ).hide();
			$( "#show").show();
			$( "#show_content").html(editor.html());//内容
			$("#show_subject").html($("#edit_subject").val());//标题
			$("#show_id").html($("#edit_id").html());//文章id
			param = {}
			if ($("#edit_id").html() != "0")//更新
			{
				param = {
					id : $("#edit_id").html(),
					subject : $("#edit_subject").val(),
					content : editor.html()
				}
				$.post("/update/", param,
				 	function(data){
						$(".nav.nav-tabs li").remove("li[class=active]");//移除以前的标题
						$(".active").removeClass("active", 1000, null);  
						$(".nav.nav-tabs").prepend("<li  class='active'><a href='' data-toggle='tab' onclick='switchTab(" + $("#edit_id").html() + ")'>" + $("#edit_subject").val() + "</a></li>");//更新标题栏并把标题栏置顶
					});
			}else //新建
			{
				param = {
					subject : $("#edit_subject").val(),
					content : editor.html()
				}
				$.post("/create/", param,
				   function(data){
					 $("#show_id").html(data);
					 $("li.active").html("<a href='' data-toggle='tab' onclick='switchTab(" + data + ")'>" + $("#edit_subject").val() + "</a>")//修改左侧主题
				  });
			}
		//	htmlspecialchars(editor.html());
			return false;
        });
			
			$( "#create_btn" ).click(function(){//新建
			$(".active").removeClass("active", 1000, null);  
			$(".nav.nav-tabs").prepend("<li class='active'><a href='' data-toggle='tab'>this is new subject</a></li>");//jquery获取多个类的元素
			$("#edit").show();
			$("#show").hide();
			editor.html("");
			$("#edit_id").html("0");
			$("#edit_content").html("");
			$("#edit_subject").html("this is new subject");
			//alert($("#edit_subject"));
			return false;
        });
			
			
			$( "#del_btn" ).click(function(){//删除
				note_id = $("#show_id").html();
				$.post("/del/", { id : note_id},
				 function(data){
					 if (data == "success")
					 {
						alert("删除成功");
					 	document.location.reload();
					 }
				 });
			return false;
        });
						
		$( "#show" ).show();
		$( "#edit").hide();
		
		getsubjects();//加载标题列表
	});