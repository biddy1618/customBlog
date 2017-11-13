jQuery(document).ready(function(){

jQuery(function() {
	jQuery('#search').keyup(function() {

		jQuery.ajax({
			type: 'POST',
			url: '/articles/search/',
			data: {
				'search_text' : jQuery('#search').val(),
				'csrfmiddlewaretoken' : jQuery('input[name=csrfmiddlewaretoken]').val()
			},
			success : function searchSuccess(data, textStatus, jqXHR){
				jQuery('#search_results').html(data);},
			dataType: 'html'
		});
	});

	jQuery('#commentsubmit').click(function(event) {

		if (jQuery('#commentbody').val() == '') {
			alert("Please, don't submit empty blank!");
			event.preventDefault();
		}else {
			jQuery.ajax({
				type: 'POST',
				url: '/articles/add_comment/',
				data: {
					'body' : jQuery('#commentbody').val(),
					'article_id' : jQuery('#commentarticle').val(),
					'csrfmiddlewaretoken' : jQuery('input[name=csrfmiddlewaretoken]').val()
				},
				success : function commentSuccess(data, textStatus, jqXHR){
					jQuery('#comment_container').append(data);
				},
				dataType: 'html'
			});
			jQuery('#commentbody').val('');
			event.preventDefault();
		}
	});

	jQuery('#likes').on('click','#like',function() {
		jQuery.ajax({
			type: 'POST',
			url: '/articles/like/',
			data: {
				'article_id' : jQuery('#commentarticle').val(),
				'csrfmiddlewaretoken' : jQuery('input[name=csrfmiddlewaretoken]').val()
			},
			success : function likeSuccess(data, textStatus, jqXHR){
				jQuery('#likes').html(data);
			},
			dataType: 'html'
		});
	});

	jQuery('#comment_container').on('click','.deletecomment', function() {
		var id = jQuery(this).closest('.comment').attr('id');
		jQuery.ajax({
			type: 'POST',
			url: '/articles/delete_comment/',
			data: {
				'comment_id' : id,
				'csrfmiddlewaretoken' : jQuery('input[name=csrfmiddlewaretoken]').val()
			},
			success : function deleteCommentSuccess(data, textStatus, jqXHR){
				jQuery('#' + id).remove();
			},
			dataType: 'html'
		});
	});

	jQuery('#editarticle').click(function(event) {
		if (jQuery('#edit_title').val() == '' || jQuery('#edit_body').val() == '') {
			alert("Please don't submit an empty blank!");
			event.preventDefault();
		}else {
			jQuery.ajax({
				type: 'POST',
				url: '/articles/edit_article/',
				data: {
					'article_id' : jQuery('#edit_article_id').val(),
					'title' : jQuery('#edit_title').val(),
					'body' : jQuery('#edit_body').val(),
					'csrfmiddlewaretoken' : jQuery('input[name=csrfmiddlewaretoken]').val()
				},
				success : function editArticleSuccess(data, textStatus, jqXHR){
					jQuery('#article_body').html(data);
				},
				dataType: 'html'
			});
		}
	});
});
});

