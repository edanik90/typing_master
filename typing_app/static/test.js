var timeleft = 60;
var test_text = document.getElementById("content").value;
var words = test_text.split(" ");
var i = 0;
var temp = "";
var correctEntries = 0;
var errors = 0;
var speed = 0;
var entryCount = 0;

var downloadTimer = setInterval(function () {
    timeleft -= 1;
    document.getElementById("timer").innerHTML = timeleft;
    if (timeleft <= 0) {
        clearInterval(downloadTimer);
        document.getElementById("timer").innerHTML = "0";
        finalVerdict();
    }
}, 1000);

function compareInput() {
    if (temp != words[i]) {
        errors++;
        document.getElementById("errors_made").innerHTML = errors;
    }
    else {
        correctEntries += temp.length;
    }
    if ((i + 1) == words.length) {
        finalVerdict();
    }
    i++;
    temp = "";
}

document.getElementById("user_input").oninput = function record_word(e) {
    if (e.inputType != "deleteContentBackward"){
        entryCount++;
    }
    console.log(e);
    console.log(entryCount);
    if (e.data == " ") {
        compareInput();
    }
    else {
        temp = temp + e.data;
    }
}

function finalVerdict(){
    speed = entryCount / 5;
    $('#finalSpeed').attr("value", speed);
    $('#totalErrors').attr("value", errors);
    $('#accuracy').attr("value", ((correctEntries / entryCount) * 100).toPrecision(4)); 
    $('form').submit();
}