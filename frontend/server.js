const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

app.post("/submit", async (req, res) => {
    try {
        const response = await fetch("http://backend:5000/api/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(req.body)
        });

        const result = await response.json();
        res.status(response.status).json(result);

    } catch (error) {
        console.error(error);
        res.status(500).json({
            error: "Could not contact backend"
        });
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Frontend running on port ${PORT}`);
});
