  $(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/compare/<id>', {
        a: window.location.pathname
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });