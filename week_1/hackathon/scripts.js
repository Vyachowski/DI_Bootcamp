const navMain = document.querySelector('.navbar');
const navToggle = document.querySelector('.main-nav-toggle');

navToggle.addEventListener('click', function () {
  navMain.classList.toggle('navbar-opened');
  navToggle.classList.toggle('main-nav-toggle-opened');
});

const selector = document.getElementById("Country_search");
if (selector) {
  $(function () {
    $("#Country_search").select2();
  });
}
