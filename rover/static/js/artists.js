let currentAudio = null;

// get all the play buttons and add event listeners to each one
const playBtns = document.querySelectorAll('.material-icons');
playBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const songId = btn.id;
        const audio = document.querySelector(`#${songId}-audio`);

        // pause the previously playing audio, if any
        if (currentAudio && currentAudio !== audio) {
            currentAudio.pause();
            currentAudio.previousElementSibling.innerText = 'play_circle_filled';
        }

        // play the new audio
        if (audio.paused) {
            audio.play();
            btn.innerText = 'pause_circle_filled';
            currentAudio = audio;
        } else {
            audio.pause();
            btn.innerText = 'play_circle_filled';
            currentAudio = null;
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
        direction: 'left'
    });
});