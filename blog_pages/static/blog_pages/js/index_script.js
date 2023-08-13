document.addEventListener("DOMContentLoaded", function() {
    var textContainers = document.querySelectorAll(".collapse");

    textContainers.forEach(function(textContainer) {
        var dots = textContainer.querySelector(".dots");
        var moreText = textContainer.querySelector(".more");
        var less = textContainer.querySelector(".less");

        dots.addEventListener("click", function() {
            if (textContainer.classList.contains("collapse")) {
                textContainer.classList.remove("collapse");
                textContainer.classList.add("expanded");
                dots.style.display = "none";
            }
        });

        less.addEventListener("click", function() {
            if (textContainer.classList.contains("expanded")) {
                textContainer.classList.remove("expanded");
                textContainer.classList.add("collapse");
                dots.style.display = "inline";
            }
        });
    });
});
document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll("a.button");
    
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function(event) {
            event.preventDefault();
            var wrap = this.parentElement.previousElementSibling;
            wrap.classList.toggle("active");
            this.classList.toggle("active");
        });
    }
});