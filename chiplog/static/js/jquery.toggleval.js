/* -------------------------------------------------- *
 * ToggleVal Plugin for jQuery                        *
 * Version 2.0                                        *
 * -------------------------------------------------- *
 * Author:   Aaron Kuzemchak                          *
 * URL:      http://aaronkuzemchak.com/               *
 * E-mail:   afkuzemchak@gmail.com                    *
 * Date:     6/5/2008                                 *
 * -------------------------------------------------- */

jQuery.fn.toggleVal = function(theOptions) {
	theOptions = jQuery.extend({
		focusClass: "tv-focused", // class during focus
		changedClass: "tv-changed", // class after focus
		populateFrom: "default", // choose from: default, label, or alt
		removeLabels: false // remove labels associated with the fields
	}, theOptions);
	
	return this.each(function() {
		// define our variables
		var defText = "";
		
		// let's populate the text, if not default
		switch(theOptions.populateFrom) {
			case "alt":
				defText = jQuery(this).attr("alt");
				jQuery(this).val(defText);
				break
			case "label":
				defText = jQuery("label[for='" + jQuery(this).attr("id") + "']").text();
				jQuery(this).val(defText);
				break
			default:
				defText = jQuery(this).val();
		}
		
		// let's give this field a special class, so we can identify it later
		jQuery(this).addClass("toggleval");
		
		// now that fields are populated, let's remove the labels if applicable
		if(theOptions.removeLabels == true) { jQuery("label[for='" + jQuery(this).attr("id") + "']").remove(); }
		
		// on to the good stuff... the focus and blur actions
		jQuery(this).focus(function() {
			if(jQuery(this).val() == defText) { jQuery(this).val(""); }
			
			// add the focusClass, remove changedClass
			jQuery(this).addClass(theOptions.focusClass).removeClass(theOptions.changedClass);
		}).blur(function() {
			if(jQuery(this).val() == "") { jQuery(this).val(defText); }
			
			// remove focusClass, add changedClass if, well, different
			jQuery(this).removeClass(theOptions.focusClass);
			if(jQuery(this).val() != defText) { jQuery(this).addClass(theOptions.changedClass); }
				else { jQuery(this).removeClass(theOptions.changedClass); }
		});
	});
};