function toTop(){window.scrollTo({top: 0, behavior: 'smooth'});}
// Get the button:
let myToTopButton = document.getElementById("toTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    myToTopButton.style.display = "flex";
  } else {
    myToTopButton.style.display = "none";
  }
}
