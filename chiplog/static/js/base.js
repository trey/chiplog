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
		$('#header div label').hide();
	}

	// Timeago: http://timeago.yarp.com/
	// $('abbr[class*=timeago]').timeago();

});
