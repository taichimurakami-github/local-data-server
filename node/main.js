const express = require("express");
const fs = require("fs");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(express.json(), cors());

app.post("/", function (req, res) {
  console.log(req.body);
  const date = new Date();
  const filepath = req.query.filepath;

  if (!filepath) {
    console.log("filepath is not contained");
    res.status(400);
    res.send("E_NO_FILEPATH_QUERY");
    return;
  }

  const dir = path.resolve(__dirname, "./", "data", path.dirname(filepath));
  console.log(dir);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  fs.writeFileSync(
    `${path.resolve(dir, path.basename(filepath))}`,
    JSON.stringify(req.body),
    (e) => {
      console.log(e);
    }
  );

  res.status(200);
  res.send("succeeded");
});

app.listen(8888, () => console.log("listening on port 8888!"));
