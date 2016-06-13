$(document).ready(function(){
   $('#btnTask').click(function(){
      if ($.trim($('#txtTask').val()).length>0 ){
         task = $('#txtTask').val();
         desc = $('#txtDescription').val();
         $.ajax({
            url: '/_add',
            data: { task: task, desc: desc },
            success: function(e){
               $(".content").append(e);
            },error: function(xhr, status, error){
               alert(error)
            }
         });
      }
      $('#txtTask').val('');
      $('#txtDescription').val('');
      $('#txtTask').focus();
   });
   $('.content').on('click', '.dele', function(e) {
      var target = $(e.target), article;
      var i = e.target.id;
      $('#'+i).fadeOut('slow', function(){
         $('#'+i).remove();
      });
      $.getJSON('/_delete',{
         id: i,
      });
   });
   $('.content').on('click', '.edit', function(e) {
      //$('.edit').prop("disabled",true);
      var target = $(e.target), article;
      var i = e.target.id;
      $(this).hide();
      $('#'+i+' .h2').hide();
      $('#'+i+' .p').hide();
      $('#'+i+' .txtDesc').show();
      $('#'+i+' .save').show();
      $('#'+i+' .txtTask').show();
      $('#'+i+' .txtTask').focus();


      
   });
   $('.content').on('click', '.save', function(e) {
      if ($.trim($('.txtTask').val()).length>0){
         var target = $(e.target), article;
         var i = e.target.id;
         $(this).hide();
         $('#'+i+' .txtDesc').hide();
         $('#'+i+' .save').hide();
         $('#'+i+' .txtTask').hide();
         $('#'+i+' .h2').text($('#'+i+' .txtTask').val());
         $('#'+i+' .p').text($('#'+i+' .txtDesc').val());
         $('#'+i+' .edit').show();
         $('#'+i+' .h2').show();
         $('#'+i+' .p').show();
         task = $('#'+i+' .txtTask').val(),
         desc = $('#'+i+' .txtDesc').val(),
         $.ajax({
            url: '/_edit',
            data: { task: task, desc: desc, id: i },
         });
      }
   });

   $('.slider').click(function(){
      $('.form').slideToggle('slow');
      $('#txtTask').focus();
   });
});