const check_strings = document.getElementById("S-button");

check_strings.onclick = function() {
    let codes = document.getElementById("strings").value;
    let word = document.getElementById("word").value;

    console.log(codes);
    console.log(word);

    const result = document.getElementById("result");
    const display = document.getElementById("highlighted");

    if (codes.toLowerCase().includes(word.toLowerCase())) {
        result.textContent = `"${word}" was found.`;

        let safe = codes.replace(/</g, "&lt;").replace(/>/g, "&gt;");
        let regex = new RegExp(`(${word})`, "gi"); // case-insensitive
        let highlighted = safe.replace(regex, `<mark>$1</mark>`);

        display.innerHTML = highlighted;
    } else {
        result.textContent = `"${word}" was NOT found.`;
        display.textContent = codes;
    }
};
