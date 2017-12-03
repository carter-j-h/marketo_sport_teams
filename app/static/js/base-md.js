(function() {
  'use strict';
  var snackbarContainer = document.querySelector('#snackbar-container');
  var button = document.querySelector('#save-teams');
  
  var handler = function(event) {
    button.style.backgroundColor = '';
  };
  button.addEventListener('click', function() {
    'use strict';
    button.style.backgroundColor = '#' +
        Math.floor(Math.random() * 0xFFFFFF).toString(16);
    var data = {
      message: 'Favorite Teams Saved!',
      timeout: 3000,
      actionHandler: handler,
      actionText: 'Undo'
    };
    snackbarContainer.MaterialSnackbar.showSnackbar(data);
  });
}());