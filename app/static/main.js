$(document).ready(function(){
   $('#btnTask').click(function(){
      if ($('#txtTask').val()!=''){
         task = $('#txtTask').val()
         $.ajax({
            url: '/_add',
            data: { task: task },
            success: function(e){
               $(".content").append(e)
            },error: function(xhr, status, error){
               alert(error)
            }
         });
      }
      $('#txtTask').val('');
      $('#txtTask').focus();
   });
   $('.content').on('click', '.chkbk', function(e) {
      var target = $(e.target), article;
      var i = e.target.id;
      $('#'+i).remove();
      $.getJSON('/_delete',{
         id: i,
      });
   });
});