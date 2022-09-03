/**
 * The theme.js file controls the theme switch mode selector.
 */

var themeSwitch = document.querySelector('input'); //Theme Switcher variable.

//Listens for when someone clicks on the slider to change the theme.
themeSwitch.addEventListener('change', function() {
document.body.classList.toggle('dark-theme');
});