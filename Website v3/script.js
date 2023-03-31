let bpmInput = document.getElementById("bpm");
let bpm = parseInt(bpmInput.value);
let interval = 60000 / bpm;
let metronome;
let audio = new Audio('click.wav');

function tick() {
   audio.play();
}

document.getElementById("start").addEventListener("click", function() {
   console.log("Metronome set to interval of: " + interval);
   metronome = setInterval(tick, interval);
});

document.getElementById("stop").addEventListener("click", function() {
   clearInterval(metronome);
});

document.getElementById("increase").addEventListener("click", function() {
   bpm +=5;
   bpmInput.value = bpm;
   clearInterval(metronome);
   interval =60000 / bpm;
   metronome = setInterval(tick, interval);
});

document.getElementById("decrease").addEventListener("click", function() {
   bpm -=5;
   bpmInput.value = bpm;
   clearInterval(metronome);
   interval =60000 / bpm;
   metronome = setInterval(tick, interval);
});

bpmInput.addEventListener("change", function() {
   bpm = parseInt(this.value);
   clearInterval(metronome);
   interval =60000 / bpm;
   metronome = setInterval(tick, interval);
});