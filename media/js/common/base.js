$(document).ready(function(){
	/* Menu 1 */
	var leido = leer();
	var act = Object();
	if(leido != ""){
		act = $("#"+leido);
		act.addClass("activo");
		$("#cuerpo").css("background-image","url(/media/img/fondos/"+leer()+".jpg)");
		guardar("");
	}
		
	$("#menu1 li").hover(function(){
		$("#menu1 li").removeClass("activo");
		$(this).addClass("activo");
		act.addClass("activo");
	},function() {
		$("#menu1 li").removeClass("activo");
		act.addClass("activo");
	});
	
	$("#menu1 li a").click(function(){
		guardar($(this).parent().attr("id"));
	});

	/* Menu 2 */
	var sub_des = true;
	var sub_leave = false;
	var li_leave = false;
	
	var act_2 =  $("#menu2 li.activo");
	$("#menu2 li").hover(function(){
		$("#menu2 li").removeClass("activo");
		act_2.addClass("activo");
		$(this).addClass("activo");
		},function() {
			$("#menu2 li").removeClass("activo");
			act_2.addClass("activo");
	});

	$("#sub-menu2").hover(function(){
		var ul = $(this).children("ul");
		if(sub_des){
			ul.css("display", "block");
			sub_des = false;
			ul.mouseleave(function(){sub_leave = true; leave();});
			$("#sub-menu2").mouseleave(function(){li_leave = true; leave();});
			$("#cabecera").hover(function(){sub_leave = true; leave();});
		}
	});
	
	function leave(){
		if(sub_leave && li_leave){
			$("#sub-menu2 ul").css("display", "none");
			sub_des = true;
			sub_leave = false;
			li_leave = false;
		}
	}
	
	/* Sesion */	
	function guardar(valor){window.name = valor;}
	function leer(){return window.name;}
		
});