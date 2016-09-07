$(function() {
	window.scrollReveal = new scrollReveal();
	"use strict";
	
	// PreLoader
	$(window).load(function() {
		$(".loader").fadeOut(400);
	});

	// Backstretchs
	
	
	
	// Countdown
	$('.countdown').downCount({
		date: '09/11/2016 11:00:00',
		offset: +5.5
	});			
    
});