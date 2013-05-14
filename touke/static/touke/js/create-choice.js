$(function(){
	
	$("#add-field").bind('click',function(){
		
		var length = $("#choice-fileds").find('input').length;
		
		if(length<=4){
			
			$("#choice-fileds").append('<input type="text" placeholder="新的选择" name="choice" class="create-field-choice"/>');
			
		}else{
			
			$("#choice-fileds").prepend(' <div class="alert alert-block"  id="create-choice-alert"><button type="button" class="close" data-dismiss="alert">&times;</button><h4>提示!</h4>达到选项上限，无法添加更多内容</div>');
			
		}
		
	});
	
});