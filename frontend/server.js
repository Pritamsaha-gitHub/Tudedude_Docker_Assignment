const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();   // ✅ THIS WAS MISSING

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

// Home page
app.get("/", (req, res) => {
  res.render("form", { error: null });
});

// Submit form
app.post("/submit", async (req, res) => {
  try {
    await axios.post("http://backend:5000/submit", req.body, {
      headers: { "Content-Type": "application/json" }
    });

    res.render("success");
  } catch (err) {
    res.render("form", { error: err.message });
  }
});

// Start server
app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});