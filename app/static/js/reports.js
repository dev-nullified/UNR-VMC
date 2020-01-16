$(document).ready(function() {

    //Render report cards
    function renderReports(jsonData) {
    //    pass
        console.log("JSON DATA RECEIVED");
        console.log(jsonData);
        console.log("Success Returned");

    //    render content
    //     $.each(jsonData, function (idx, obj) {
    //
    //     })
    }


    function onError() {
    //    do some error stuff
        console.log("Error getting data");
    }


    // Query Ajax
    $.when(
        $.ajax({
            url: '/api/listreports',
            method: 'GET',
            dataType: 'json'

        })
    ).then(renderReports, onError)







});