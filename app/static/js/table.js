$(document).ready(function() {
  $('.RowToClick').click(function () {
    $(this).nextAll('tr').each( function() {
      if($(this).is('.RowToClick')) {
        return false;
      }
      $(this).toggle(50);
    });
  });
  $('.RowToClick').nextAll('tr').each( function() {
    if(!($(this).is('.RowToClick')))
      $(this).hide();
  });
});