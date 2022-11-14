const express = require("express");
const fs = require("fs");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(express.json(), cors());

app.post("/", function (req, res) {
  console.log(req.body);
  const date = new Date();
  const filename = req.query.filename;

  if (!filename) {
    console.log("filename is not contained");
    res.status(400);
    res.send("E_NO_FILENAME_QUERY");
    return;
  }

  const dirName = `${date.getFullYear()}-${
    date.getMonth() + 1
  }-${date.getDate()}`;

  const dir = path.resolve(__dirname, "../", "data", dirName);
  console.log(dir);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir);
  }

  fs.writeFileSync(`${dir}/${filename}`, JSON.stringify(req.body), (e) => {
    console.log(e);
  });

  res.status(200);
  res.send("succeeded");
});

app.listen(8888, () => console.log("listening on port 8888!"));
