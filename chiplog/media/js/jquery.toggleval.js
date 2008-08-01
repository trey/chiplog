/* -------------------------------------------------- *
 * ToggleVal Plugin for jQuery                        *
 * Version 1.0                                        *
 * -------------------------------------------------- *
 * Author:   Aaron Kuzemchak                          *
 * URL:      http://kuzemchak.net/                    *
 * E-mail:   afkuzemchak@gmail.com                    *
 * Date:     8/18/2007                                *
 * -------------------------------------------------- */

jQuery.fn.toggleVal = function(focusClass) {
	this.each(function() {
		$(this).focus(function() {
			// clear value if current value is the default
			if($(this).val() == this.defaultValue) { $(this).val(""); }
			
			// if focusClass is set, add the class
			if(focusClass) { $(this).addClass(focusClass); }
		}).blur(function() {
			// restore to the default value if current value is empty
			if($(this).val() == "") { $(this).val(this.defaultValue); }
			
			// if focusClass is set, remove class
			if(focusClass) { $(this).removeClass(focusClass); }
		});
	});
}