$(document).ready(function() {

    // Focus on the textarea right away.  You're here to write.
    $('#id_body').focus();

    // Only show the Tags field if you really want it.
    $('#id_tags').hide();
    $('.tags').append('<a href="#">Add Tags</a>');
    $('.tags a').click(function() {
        $('#id_tags').fadeIn();
        $('#id_tags').focus();
        $(this).hide();
    });
    

    if($('#s').val() == "") {
		$('#s').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#header div label').hide();
	}

});
