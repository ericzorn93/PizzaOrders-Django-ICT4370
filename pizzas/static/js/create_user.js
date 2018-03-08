var inputs = document.querySelectorAll('input');

for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}





//check for navigation time API support
if (window.performance) {
  console.info("window.performance work's fine on this browser");
}

if (window.performance.navigation.type == 1) {
    var reloaded = document.getElementById("reloadOutput");
    reloaded.innerHTML = "*Username was Successfully Created. Please Proceed to Login Page Link";
    console.info( "This page is reloaded" );
} else {
    console.info( "This page is not reloaded");
}