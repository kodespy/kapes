
jQuery(function ( $ ) {

	$.fn.color = function(){		
		this.removeAttr('class');
		this.attr('class','btn btn-blue btn-round');
		return this;
	}

});

	
