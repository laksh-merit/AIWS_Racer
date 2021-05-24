const sio = io();
        sio.on('connect',() => {
            console.log("connected")
        });

        sio.on('disconnect',() => {
            console.log("disconnected")
        });


var a = 1;
var btnDown1 = false;
function mDown1() {
    btnDown1 = true;
    }
    function mUp1() {
        btnDown1 = false;
    }
    function test() {
        if (btnDown1) {
            var val = "forward";
            sio.send(val)
            }
        }
   setInterval(test, 100);

var current;
function onInput() {
    current = document.getElementById("sliderRange").value;
    sio.send(current)
}

function onChange() {
    current = 50;
    document.getElementById("sliderRange").value = current;
    var cur = current.toString();
    sio.send(cur)
}