$(document).ready(function() {

	// Focus on the textarea right away.  You're here to write.
	$('#id_body').focus();

	// Only show the Tags field if you really want it, or it's already populated.
	if ($('#id_tags').val() == "") {
		$('#id_tags').hide();
	};
	$('.tags').not('.list').append('<a href="#">Add Tags</a>');
	$('.tags a').click(show_tag_field);
	function show_tag_field() {
		$('#id_tags').fadeIn();
		$('#id_tags').focus();
		$('.tags a').hide();
		return false;
	}

	// Search form default text and reset on focus.
	if($('#s').val() == "") {
		$('#s').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#search div label').hide();
	}

	// Hide and show search form
	$('#search form').hide();
	$('#search').append('<a href="#">Search</a>');
	function search_toggle () {
		$('#search form').toggle('fast');
		if ($('#search a').html() == 'Search') {
			$('#search a').html('Close Search');
			$('#s').focus();
		} else {
			$('#search a').html('Search');
		};
		return false;
	}
	$('#search a').click(search_toggle);

	// Keyboard shortcuts
    $(document).bind('keydown', 'Ctrl+s', search_toggle);
    $(document).bind('keydown', 'Ctrl+t', show_tag_field);

});
