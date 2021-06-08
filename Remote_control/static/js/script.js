var socket = io.connect('http://127.0.0.1:5000');

socket.on('connect',() => {
console.log("connected")
});

socket.on('disconnect',() => {
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
            socket.send(val)
            }
        }
   setInterval(test, 100);

var current;
function onInput() {
    current = document.getElementById("sliderRange").value;
    socket.send(current)
}

function onChange() {
    current = 50;
    document.getElementById("sliderRange").value = current;
    var cur = current.toString();
    socket.send(cur)
}
