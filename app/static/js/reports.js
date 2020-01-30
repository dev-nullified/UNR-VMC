$(document).ready(function() {

    //Render report cards
    function renderReports(jsonData) {
        console.log("JSON DATA RECEIVED");
        console.log(jsonData.Reports);
        console.log("Success Returned");


    //    render content
        $.each(jsonData.Reports, function (key, val) {

            //Create reportcard element
            // var $baseContainer = $('<div/>').addClass('col-md-6');
            var $reportCardBase = $('<div/>').addClass('reportCardBase').attr("data-reportid", key);
            var $title = $('<div/>').addClass('reportTitle').text(val.Name);
            var $fcnButtons =  $('<div/>').addClass('reportFunctions');
            var $lastRunDate = $('<div/>').addClass('reportRunDate').text(val.LastRun);
            var $description = $('<div/>').addClass('reportDescription').text(val.Description);

            //Routine to add run edit and delete buttons
            $fcnButtons.append($('<i/>').addClass('reportActionRun fas fa-play'));
            $fcnButtons.append($('<i/>').addClass('reportActionEdit fas fa-pen'));
            $fcnButtons.append($('<i/>').addClass('reportActionDelete fas fa-times'));


            $reportCardBase.append($title, $fcnButtons, $lastRunDate, $description);
            // $baseContainer.append($reportCardBase);

            //Add to page
            $("#reports").append($reportCardBase);

         });

        //Run logic
        $(".reportActionRun").click(function(event) {
            var reportParent = $(this).closest(".reportCardBase");
            console.log("Clicked Run on element with id " + $(reportParent).attr("data-reportid"));
        });

        //Edit logic
        $(".reportActionEdit").click(function(event) {
            var reportParent = $(this).closest(".reportCardBase");
            console.log("Clicked Edit on element with id " + $(reportParent).attr("data-reportid"));
        });

        //Delete logic
        $(".reportActionDelete").click(function(event) {
            var reportParent = $(this).closest(".reportCardBase");
            console.log("Clicked Delete on element with id " + $(reportParent).attr("data-reportid"));
        });

    }


    function onError() {
    //    do some error stuff
        console.log("Error getting data");
    }


    // Query Ajax
    $.when(
        $.ajax({
            url: '/api/reports',
            method: 'GET',
            dataType: 'json'

        })
    ).then(renderReports, onError);


//    Add generic event listener




    // function reportAction(element) {
    //     $(element).hide();
    //     var item = $(element).closest("div.reportFunctions");
    //     $(item).css("display", "none");
    //     // alert($(item).attr("data-reportid"));
    // }

});