var dropdowns = document.querySelectorAll(".dropdown");

// Add a mouseover event listener to each dropdown
dropdowns.forEach(function(dropdown) {
    dropdown.addEventListener("mouseover", function() {
        // When hovered over, show the associated dropdown content
        var dropdownContent = this.querySelector(".dropdown-content");
        if (dropdownContent) {
            dropdownContent.classList.add("show");
        }
    });

    dropdown.addEventListener("mouseout", function() {
        // When the mouse leaves, hide the associated dropdown content
        var dropdownContent = this.querySelector(".dropdown-content");
        if (dropdownContent) {
            dropdownContent.classList.remove("show");
        }
    });
});