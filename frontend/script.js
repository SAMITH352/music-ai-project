function generateMusic() {
    document.getElementById("status").innerText = " Generating music...";

    fetch("http://127.0.0.1:5000/generate")
        .then(response => {
            if (!response.ok) {
                throw new Error("Generation failed");
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "generated_music.mid";
            document.body.appendChild(a);
            a.click();
            a.remove();

            document.getElementById("status").innerText = " Music downloaded!";
        })
        .catch(error => {
            document.getElementById("status").innerText = "❌ Error generating music";
            console.error(error);
        });
}
