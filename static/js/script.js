var block_indices = []
$(document).ready(function () {
    $('#mine').click(function () {
        $.ajax({
            url: "/mine",
            type: "get",
            success: function (response) {
                block_indices.push(response)
                console.log(response)
            },
            error: function (xhr) {
                //Do Something to handle error
            }
        });
    });
    $('#chain').click(function () {
        $.each(block_indices, function (index, value) {
            $(".modal-body").append("<div class=\"row\"><div class=\"box arrow-bottom\">" + value.Timestamp + "</div></div>")
        });
        block_indices = []
    });
});