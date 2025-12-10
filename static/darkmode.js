// Apply saved theme on first load
const savedTheme = localStorage.getItem("theme");

if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);

function handleThemeClick() {
    const current = document.documentElement.getAttribute("data-theme");
    const newTheme = current === "dark" ? "light" : "dark";
    if (newTheme === "light") {
        document.documentElement.removeAttribute("data-theme");
    } else {
        document.documentElement.setAttribute("data-theme", "dark");
    }
    localStorage.setItem("theme", newTheme);
}

// This ensures the DOM is fully loaded before trying to find the button
document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', handleThemeClick);
        console.log('Event listener attached to themeButton.');
    } else {
        console.error('themeButton element not found!');
    }
});