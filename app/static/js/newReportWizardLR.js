$(document).ready(function(){


    // Wizard Pages
    let wizPages = $(".wizContnent");
    // Hide all but first one

    
    // wizPages.hide();
    $(wizPages[0]).css('left', '0%');
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

    let currentStep = 0;
    let posisition = 0;

//    Init set step 1 to active
    $(progressStep[0]).addClass("is-active");


    ////////////////////////
    // NEXT and BACK fcns //
    ////////////////////////

    // Increment the wizard
    buttons.on("action:next", function( event ) {
        // Only advance if we're not at end
        if (currentStep < progressStep.length-1) {
            $(progressStep[currentStep]).removeClass("is-active");
            currentStep = currentStep + 1
            $(progressStep[currentStep]).addClass("is-active");

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
            $(progressStep[currentStep]).removeClass("is-active");
            currentStep = currentStep - 1
            $(progressStep[currentStep]).addClass("is-active");
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

    // Slide left effect
    // Credit to https://stackoverflow.com/questions/4741880/slide-a-div-offscreen-using-jquery
    buttons.on("action:next", function( event ) {

        // Get current item
        page = $(wizPages[posisition]);
        pageNext = $(wizPages[posisition+1]);
        

        $(page).animate({
            left: '-50%'
        }, 500, function() {
            $(page).css('left', '150%');
            $(page).appendTo('#wizardContainer');
        });
    
        $(pageNext).animate({
            left: '0%'
        }, 500);


        posisition = posisition + 1

    });


    buttons.on("action:back", function( event ) {

        // Get current item
        page = $(wizPages[posisition]);
        pageLast = $(wizPages[posisition-1]);
        
        $(pageLast).prependTo('#wizardContainer');
        
        $(pageLast).css('left', '-50%');
          
        $(page).animate({
            left: '150%'
        }, 500, function() {
            console.log("MOVED BACK")
        });
          
          
      
        $(pageLast).animate({
            left: '0%'
        }, 500);
      
        posisition = posisition - 1;

    });






    nextBtn.click(function() {
        nextBtn.trigger("action:next");
    });

    backBtn.click(function(){
        backBtn.trigger("action:back");
    });
    


    // Show and reviel elements in the 
    // buttons.on("action:next", function(event) {
    //     $(wizPages[currentStep]).toggle("slide").direction("left");
    // });


});