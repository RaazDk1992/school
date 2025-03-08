document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modalImg");
    const closeBtn = document.querySelector(".close");

    document.querySelectorAll(".gallery-thumb").forEach(img => {
        img.addEventListener("click", function () {
            console.log("load..")
            modal.style.display = "flex";
            modalImg.src = this.getAttribute("data-full");
        });
    });

    closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    modal.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

function showAlert(){
    alert("xx");
}