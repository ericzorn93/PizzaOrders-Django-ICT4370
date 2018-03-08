// Toggle Link
const toggleLink = document.getElementById("displayButtonToggle");

// Buttons Div Wrapper
const buttonsDivWrapper = document.getElementById("orderButtonWrapper");



// Simulates Button Fade In
function fadeIn(element) {
    element.style.opacity = 0;

    function counter() {
        element.style.opacity = +element.style.opacity + 0.03;

        if (+element.style.opacity <= 1) {
            setTimeout(counter, 18);
        }
    }

    counter();
}



toggleLink.addEventListener('click', function (ev) {

    buttonsDivWrapper.style.display = "inline-block";
    fadeIn(buttonsDivWrapper);

    toggleLink.style.display = "none";
});




