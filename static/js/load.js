$(function() {

	// Focus on the textarea right away.  You're here to write.
	$('#id_body').focus();

	// Only show the Tags field if you really want it, or it's already populated.
	if ($('#id_tags').val() == "") {
		$('#id_tags').hide();
	};
	$('form .tags').not('.list').append('<a href="#">' + gettext('Add Tags') + '</a>');
	$('form .tags a').click(show_tag_field);
	function show_tag_field() {
		$('#id_tags').fadeIn();
		$('#id_tags').focus();
		$('form .tags a').hide();
		return false;
	}

	// Search form default text and reset on focus.
	if($('#q').val() == "") {
		$('#q').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#search div label').hide();
	}

	// Hide and show search form
	$('#search form').hide();
	$('#search').append('<a href="#">' + gettext('Search') + '</a>');
	function search_toggle () {
		$('#search form').toggle('fast');
		if ($('#search a').html() == gettext('Search')) {
			$('#search a').html(gettext('Close Search'));
			$('#q').focus();
		} else {
			$('#search a').html(gettext('Search'));
		};
		return false;
	}
	$('#search a').click(search_toggle);
	
	// $('.message').animate({ backgroundColor: '#FED078' }, "slow").animate({ opacity: "hide" }, 2500)

	// Keyboard shortcuts
    $(document).bind('keydown', 'Ctrl+s', search_toggle);
    $(document).bind('keydown', 'Ctrl+t', show_tag_field);

	// iPhone
	// --------------------------------------------

	// Detect User Agent (http://www.askdavetaylor.com/detect_apple_iphone_user_web_site_server.html)
	var agent=navigator.userAgent.toLowerCase();
	var is_iphone = ((agent.indexOf('iphone')!=-1));
	if (is_iphone) {
		$.scrollTo('#main');
	}

});
