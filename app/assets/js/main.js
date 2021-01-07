$(document).ready(function() {
    $("#alert-box").delay(5000).slideUp(300);
    $("#alert-box-validation").delay(0).slideUp(300);
    $("#newProductID").change(function() {
        $('#newFromLocation').empty().append('<option value=""></option>');

        $.get('/movements/Get_Product_Locations?productID=' + this.value,
            function(data) {
                console.log(data);
                $.each(data, function(key, value) {
                    $('#newFromLocation').append(`<option value="${value[1]}"> 
                    ${value[0]} 
               </option>`);

                    $("#newFromLocation").val([value[1]]);
                });
            });
    });

    $('#TotalsReport tr').each(function() {
        var sum = 0
        $(this).find('.qty').each(function() {

            var qty = $(this).text();

            if (!isNaN(qty) && qty.length !== 0) {
                sum += parseFloat(qty);
            }
        });

        $('.total-qty', this).html(sum);
    });

});