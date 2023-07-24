document.addEventListener("DOMContentLoaded", function() {
    
    // text usage
    const textUsedContainer = document.querySelector(".text-usage");
    const textTotalContainer = document.querySelector(".text-total");

    const textUsed = document.querySelector("textarea");
    textUsedContainer.innerHTML = textUsed.value.length;

    textUsed.addEventListener("input", function(){
        textUsedContainer.innerHTML = this.value.length;
    });

    const textTotal = document.querySelector("textarea").getAttribute("maxlength");
    textTotalContainer.innerHTML = textTotal;

});