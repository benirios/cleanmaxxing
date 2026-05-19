#!/usr/bin/env node

import { spawn } from "child_process";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const target = process.argv[2];

if (!target) {
    console.log("Usage:");
    console.log("npx cleanmaxxing <folder-or-file>");
    process.exit(1);
}

const pythonFile = path.join(__dirname, "cleanmaxxing.py");

const processPy = spawn("python3", [pythonFile, target], {
    stdio: "inherit"
});

processPy.on("close", (code) => {
    process.exit(code);
});