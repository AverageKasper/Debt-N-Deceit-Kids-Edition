const dumpster = document.createElementId("dumpster");

function show_inside(event) {
    event.target.stylebackgroundcolor = "red";
    event.target.textcontent = "u get this🥵";
}
dumpster.addEventListener("click", show_inside,)

dumpster.addEventListener("mouseover", event => {
    event.target.stylebacground = "yellow";
    event.target.textcontent = "press to reveal😫"
});

dumpster.addEventListener("mouseout", event => {
    event.target.style.background = "lightgreen";
    event.target.textcontent = "click me 😳";
});