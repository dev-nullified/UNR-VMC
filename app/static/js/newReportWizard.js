$(document).ready(function(){


    // Wizard Pages
    let wizPages = $(".wizard-item");
    // Hide all but first one
    // wizPages.hide();

    //Title pages
    let titlePages = $(".title");
    // Counters
    let currentStep = 0;
    let currentPageCounter = 0;

    
    // wizPages.hide();
    $(wizPages[0]).removeClass('translate-left');
    console.log($(wizPages[0]));
    $(wizPages[0]).show();
    // console.log(wizPages[0])




    // Get the next and back buttons
    let nextBtn = $("#nextButon");
    let backBtn = $("#backButton");
    let buttons = $("#navButtons > button");
    // buttons.hide();

    // Hide the BackBtn
    backBtn.hide()



    //    Select the report wizard
    let reportWizProgressBar = $("#wizardProgress");

//    Get Dot elements
    let elems = document.getElementsByClassName("progress-step");
    let progressStep = jQuery.makeArray(elems);



//    Init set step 1 to active
    $(progressStep[0]).addClass("is-active");


    ////////////////////////
    // NEXT and BACK fcns //
    ////////////////////////

    // Increment the wizard
    buttons.on("action:next", function( event ) {
        // Only advance if we're not at end
        if (currentStep < progressStep.length-1) {

            $(titlePages[currentStep]).addClass("hidden");
            $(progressStep[currentStep]).removeClass("is-active");
            currentStep = currentStep + 1
            $(progressStep[currentStep]).addClass("is-active");
            $(titlePages[currentStep]).removeClass("hidden");


        }
        // Change text to finish if we're at the end
        if (currentStep == progressStep.length-1){
            nextBtn.text("Finish");
        } 

        // Reveal back button if applicable
        if (backBtn.is(":hidden")) {
            if (currentStep != 0) {
                backBtn.show();
            }
        }

        // Slide content in
        // $(wizPages[currentStep]).toggle("slide").direction("left");




    });

    // Decrement the wizard
    buttons.on("action:back", function( event ) {
        // Only decrement if we're not at end
        if (currentStep != 0) {

            $(titlePages[currentStep]).addClass("hidden");
            $(progressStep[currentStep]).removeClass("is-active");
            currentStep = currentStep - 1
            $(progressStep[currentStep]).addClass("is-active");
            $(titlePages[currentStep]).removeClass("hidden");
        }

        // Hide The back button if we're at the end
        if (currentStep == 0){
            backBtn.hide();
        }

        // Change text back if we're not at the end
        if (currentStep != progressStep.length-1){
            nextBtn.text("Next");
        } 
    });


    ////////////////////////
    // Title Change fcns  //
    ////////////////////////


    ///////////////////////////////
    // Content Advance Controls //
    //////////////////////////////
    buttons.on("action:next", function(event) {
        let currentPage = $(wizPages[currentPageCounter]).get();
        let nextPage = $(wizPages[currentPageCounter+1]).get();


        $(currentPage).addClass("hidden");
        $(nextPage).removeClass("hidden");

        currentPageCounter = currentPageCounter + 1;
    })


    buttons.on("action:back", function(event) {
        let currentPage = $(wizPages[currentPageCounter]).get();
        let nextPage = $(wizPages[currentPageCounter-1]).get();


        $(currentPage).addClass("hidden");
        $(nextPage).removeClass("hidden");

        currentPageCounter = currentPageCounter - 1;
    })




    ///////////////////////////////
    // Content Advance Controls with ANIMATION //
    //////////////////////////////

    // buttons.on("action:next", function(event) {
    //     let currentPage = $(wizPages[currentPageCounter]).get();
    //     let nextPage = $(wizPages[currentPageCounter+1]).get();

    //     console.log(currentPage)


    //     $(nextPage).css('opacity', '0').removeClass('hidden');

    //     anime({
    //         targets: currentPage,
    //         translateX: ['0', '150%'],
    //         opacity: 0,
    //         duration: 5000,
    //         easing: 'linear'
    //     });
    //     console.log("Anime Ran")
    //     // $(currentPage).hide()

        
    //     // $(page).addClass('hidden');
        

    //     anime({
    //         targets: nextPage,
    //         translateX: ['150%', 0],
    //         opacity: 1,
    //         duration: 250,
    //         easing: 'linear'
    //     });

    //     $(currentPage).addClass('hidden').css('opacity', '0');



    //     currentPageCounter = currentPageCounter + 1;
    // })

    // buttons.on("action:back", function(event) {
    //     let currentPage = $(wizPages[currentPageCounter]).get();
    //     let nextPage = $(wizPages[currentPageCounter-1]).get();

    //     console.log(currentPage)


    //     // $(nextPage).css('opacity', '0').removeClass('hidden');
    //     $(nextPage).removeClass('hidden');

    //     anime({
    //         targets: currentPage,
    //         translateX: ['0', '150%'],
    //         opacity: 0,
    //         duration: 1000,
    //         easing: 'linear'
    //     });
    //     // console.log("Anime Ran")
    //     // $(currentPage).hide()

        
        
        

    //     anime({
    //         targets: nextPage,
    //         translateX: ['-150%', '0'],
    //         opacity: 1,
    //         duration: 1000,
    //         easing: 'linear'
    //     });

    //     // $(currentPage).addClass('hidden').css('opacity', '');



    //     // currentPageCounter = currentPageCounter - 1;
    // })





    ////////////////////////////
    // NEXT and BACK Controls //
    ////////////////////////////

    nextBtn.click(function() {
        console.log(currentStep);
        if (currentStep == 2) {
            console.log("RAN REPORT");
            nextBtn.trigger("action:runReport");
        }
        nextBtn.trigger("action:next");
    });

    backBtn.click(function(){
        backBtn.trigger("action:back");
    });
    


    // Show and reviel elements in the 
    // buttons.on("action:next", function(event) {
    //     $(wizPages[currentStep]).toggle("slide").direction("left");
    // });

    var tabledata = null

    var retrievedFilters = function () {
        var tmp = null;
        $.ajax({
            'async': false,
            'type': 'GET',
            'url': '/api/report/filters',
            'success': function (data) {
                tmp = data;
            }
        });
        return tmp;
    }();
    
    
    var table = new Tabulator("#tablulator", {
        height:"311px",
        index:'id'
    });
    
    var operators = [
        {type: 'eq', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        {type: 'neq', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        {type: 'gt', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        {type: 'ge', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        {type: 'lt', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        {type: 'le', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
        
        // { type: 'begins_with', optgroup: 'basic' },
        // { type: 'not_begins_with', optgroup: 'basic' },
        // { type: 'contains', optgroup: 'basic' },
        // { type: 'not_contains', optgroup: 'basic' },
        // { type: 'ends_with', optgroup: 'basic' },
        // { type: 'not_ends_with', optgroup: 'basic' }
    
        { type: 'startswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
        { type: 'not_startswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
        { type: 'contains', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
        { type: 'not_contains', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
        { type: 'endswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
        { type: 'not_endswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] }
    
        // stringOps = ['startswith', 'not_startswith', 'contains', 'not_contains', 'endswith', 'not_endswith']
    
        
    ];
    
    // var operators_remap = {
    //     equal: '=',
    //     not_equal: '!=',
    //     greater: '>',
    //     greater_or_equal: '>=',
    //     less: '<',
    //     less_or_equal: '<='
    // };
    
    var operators_remap = {
        eq: '=',
        neq: '!=',
        gt: '>',
        ge: '>=',
        lt: '<',
        le: '<='
    };
    
    
    $('#query_builder').queryBuilder({
    
        operators: operators,
    
        // Change how the operators are displayed
        lang: {
            operators: operators_remap
        },
    
    
    
        // Populate the selectable filters
        filters: retrievedFilters 
        
    });
    
    // $('#get_rules').on('click', function() {
    buttons.on("action:runReport", function( event ) {
        var result = $('#query_builder').queryBuilder('getRules');
        
        // Print rules to console
        if (!$.isEmptyObject(result)) {
        //   alert(JSON.stringify(result, null, 2));
            console.log(JSON.stringify(result, null, 2))
        
    
            // Submit rules to system
            $.ajax({
                'async': false,
                'type': 'POST',
                'url': '/api/report/rules',
                'contentType': "application/json; charset=utf-8",
                'data': JSON.stringify(result, null, 2),
                'success': function (data) {
                    // var w = window.open('/report/display', 'Report Output');
                    // w.document.write(data)
                    var tabledata = JSON.parse(data);
                    var columnData = [];
                    // console.log(tabledata)
                    Object.entries(tabledata[0]).forEach(([key, value]) => {
                        // console.log(`${key} ${value}`);
                        columnData.push({title: key, field:key});
                    });
    
                    console.log(columnData);
    
    
                    // alert(data);
                    // var table = new Tabulator("#tablulator", {
                    //         height:"311px",
                    //         data: tabledata,
                    //         index:'id',
                    //         columns: columnData
                    //     });
                    table.setColumns(columnData);
                    table.setData(tabledata);
                },
                'failure': function(errMsg) {
                    // alert(errMsg)
                }
            });
    
        }
      });



});