$(document).ready(function () {

$("#id_usuario").keypress(function(tecla) {
        if(tecla.charCode < 97 || tecla.charCode > 122)
            return false;
    });


  $("#boton").click(function (){

         if( $("#id_usuario").val() == "" ){
                   $('#ModalUsuario').modal('show')
                   return false;
               }//id_celualr
            else{
                  if( $("#id_contrasena").val() == "" ){
                               $('#ModalContrasena').modal('show')
                                return false;
                       }//if id_nombre


                 }






      });

});
