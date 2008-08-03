$(document).ready(function() {

    if($('#s').val() == "") {
		$('#s').toggleVal({ populateFrom: 'label', removeLabels: true });
	} else {
		$('#header div label').hide();
	}

});
