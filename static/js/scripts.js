function submitBtnClicked() {
    console.log("yay")
    $("#youtube_url_form_container").addClass("animate__animated");
    $("#youtube_url_form_container").addClass("animate__fadeOut");
    $("#search_results").addClass("animate__animated");
    $("#search_results").addClass("animate__fadeOut");
    // $("#youtube_url_form_container").addClass("hidden");

    $("#loading").removeClass("hidden");
    $("#loading").addClass("animate__fadeIn");

    // $("#box-er").addClass("hidden");
    // $("#box-sc").addClass("hidden");
    // $("#box-wr").addClass("hidden");
}

function arrayRemove(arr, value) {
    return arr.filter(function(ele) {
        return ele != value;
    });
}

function startBtn() {

    $("#startButton").addClass("animate__animated");
    $("#startButton").addClass("animate__fadeOut");


    setInterval(function() {
        scores = [1, 2, 3]

        score = Math.floor(Math.random() * 3) + 1;
        element_id = "#score" + score;
        $(element_id).removeClass("hidden")
        $(element_id).addClass("animate__animated");
        $(element_id).addClass("animate__fadeIn");
        console.log("faded in")
        setTimeout(function() {
            console.log("fading out")
            element_id = "#score" + score;
            $(element_id).removeClass("animate__fadeIn");
            $(element_id).addClass("animate__fadeOut");
            setTimeout(function() {
                $(element_id).removeClass("animate__fadeOut");
                $(element_id).removeClass("animate__animated");
                $(element_id).addClass("hidden");
            }, 700)
        }, 800);

    }, 1000)

}