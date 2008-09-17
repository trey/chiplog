$(document).ready(function() {

	// Focus on the textarea right away.  You're here to write.
	$('#id_body').focus();

	// Only show the Tags field if you really want it, or it's already populated.
	if ($('#id_tags').val() == "") {
		$('#id_tags').hide();
	};
	$('.tags').not('.list').append('<a href="#">Add Tags</a>');
	$('.tags a').click(function() {
		$('#id_tags').fadeIn();
		$('#id_tags').focus();
		$(this).hide();
		return false;
	});

	// Search form default text and reset on focus.
	if($('#s').val() == "") {
		$('#s').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#search div label').hide();
	}

	// Hide and show search form
	$('#search form').hide();
	$('#search').append('<a href="#">Search</a>');
	$('#search a').click(function() {
		$('#search form').toggle('fast');
		if ($(this).html() == 'Search') {
			$(this).html('Close Search');
			$('#s').focus();
		} else {
			$(this).html('Search');
		};
		return false;
	});

	// Timeago: http://timeago.yarp.com/
	// $('abbr[class*=timeago]').timeago();

});
