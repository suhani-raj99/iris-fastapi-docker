async function predict() {

    const sepal_length = parseFloat(document.getElementById("sl").value);
    const sepal_width = parseFloat(document.getElementById("sw").value);
    const petal_length = parseFloat(document.getElementById("pl").value);
    const petal_width = parseFloat(document.getElementById("pw").value);

    if (
        isNaN(sepal_length) ||
        isNaN(sepal_width) ||
        isNaN(petal_length) ||
        isNaN(petal_width)
    ) {
        alert("Please enter all values.");
        return;
    }

    const response = await fetch(
        "https://iris-fastapi-docker.onrender.com/predict",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerHTML =
        "🌸 Predicted Flower : <b>" + data.prediction + "</b>";
}