$( document ).ready(function() {
	
	$(".mdl-js-switch").change(function () {
    var allSwitches = $('input[type="checkbox"]');
    // console.log(allSwitches);    

    if ($(this).hasClass("is-checked")) {
      var teamName = $(event.target).closest("li").find(".mdl-list__item-primary-content").text();
      // console.log(jQuery.type(teamName));
      // grab the id associated with the team
      var teamId = $(event.target).closest("li").find("img").attr('id');

      // grab logo of team related to switch action
      var logo = $(event.target).closest("li").find("img").attr('src');

      // to keep the function short, am passing my variables to a next function below which does the DOM manipulation
      addToFavorites(teamName, logo, teamId);
        // allSwitches.not($(this)).parentElement.MaterialCheckbox.disable();
    }

    if (!$(this).hasClass("is-checked")) {
      console.log("unckecked?");
      var teamId = $(event.target).closest("li").find("img").attr('id');
      console.log(teamId);

      removeFromFavorites(teamId);
    }


  });

  function removeFromFavorites(teamId) {
    console.log($('.final-4').find(teamId).closest("li"));
    ($('.final-4').find(teamId)).remove();
    
  }

  function addToFavorites(teamName, logo, teamId) {      

      $('.final-4').append($('<li>').attr('class', 'mdl-list__item').append($('<span>').attr('class', 'mdl-list__item-primary-content').text(teamName).append($('<img>').attr({
        src: logo,
        class: 'team-logo',
        id: teamId
      }))));

  };

  $("#remove-team").click(function(){
    // alert("working?");
    $('.final-4 li:last-child').remove();
  });
});