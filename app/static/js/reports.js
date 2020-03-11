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
            var $fcnButtons =  $('<div/>').addClass('reportFunctions');

            var $title = $('<div/>').addClass('reportTitle').text(val.Name);
            var $lastRunDate = $('<div/>').addClass('reportRunDate').text(val.LastRun);
            var $description = $('<div/>').addClass('reportDescription').text(val.Description);

            //Routine to add run edit and delete buttons
            $fcnButtons.append($('<i/>').addClass('reportAction run fas fa-play'));
            $fcnButtons.append($('<i/>').addClass('reportAction edit reportAction fas fa-pen'));
            $fcnButtons.append($('<i/>').addClass('reportAction remove reportAction fas fa-times'));


            $reportCardBase.append($fcnButtons, $title, $lastRunDate, $description);
            // $baseContainer.append($reportCardBase);

            //Add to page
            $("#reports").append($reportCardBase);

         });

        //Run logic
        $(".reportAction.run").click(function(event) {
            var reportParent = $(this).closest(".reportCardBase");
            console.log("Clicked Run on element with id " + $(reportParent).attr("data-reportid"));
        });

        //Edit logic
        $(".reportAction.edit").click(function(event) {
            var reportParent = $(this).closest(".reportCardBase");
            console.log("Clicked Edit on element with id " + $(reportParent).attr("data-reportid"));
        });

        //Delete logic
        $(".reportAction.remove").click(function(event) {
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