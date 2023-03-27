
    const images = document.querySelectorAll('img');

        images.forEach(img => {
        img.addEventListener("mouseover", function () {
            this.style.transform = "scale(2.2)";
        });
        });

        images.forEach(img => {
        img.addEventListener("mouseout", function () {
            this.style.transform = "scale(1)";
        });
        });


        images.forEach(img => {
        img.addEventListener("click", function () {
            this.style.transform = "scale(1)";
        });
        });
