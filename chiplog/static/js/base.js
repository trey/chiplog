$(document).ready(function() {

    // Focus on the textarea right away.  You're here to write.
    $('#id_body').focus();

    if($('#s').val() == "") {
		$('#s').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#header div label').hide();
	}

});
