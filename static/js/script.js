// moz-script

document.getElementById("increment").addEventListener("click", function(e) {
    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ripple = this.querySelector("::after");
    
    this.style.setProperty("--ripple-x", x + "px");
    this.style.setProperty("--ripple-y", y + "px");

    this.classList.add("ripple-active");

    setTimeout(() => {
        this.classList.remove("ripple-active");
    }, 600);
});