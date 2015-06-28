$(function(){
   $('#model').keyup(function(){
     $.ajax({
       type: "POST",
       url: "/compare_search",
       data: {
           'compare_search_text' : $('#model').val(),
     },
       success: csearchSuccess,
       dataType: 'html'
   });
  });
});
function csearchSuccess(data, textStatus, jqXHR)
{
  $('#search-result').html(data);
}