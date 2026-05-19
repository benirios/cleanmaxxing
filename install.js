#!/usr/bin/env node

import fs from "fs";
import os from "os";
import path from "path";
import { execSync } from "child_process";

const repo = "https://github.com/YOUR_USERNAME/cleanmaxxing.git";
const installDir = path.join(os.homedir(), ".claude", "skills", "cleanmaxxing");

fs.mkdirSync(path.dirname(installDir), { recursive: true });

if (fs.existsSync(installDir)) {
  console.log("CleanMaxxing already installed. Updating...");
  execSync("git pull", { cwd: installDir, stdio: "inherit" });
} else {
  console.log("Installing CleanMaxxing skill...");
  execSync(`git clone ${repo} ${installDir}`, { stdio: "inherit" });
}

console.log("Done. Restart Claude Code, then use /cleanmaxxing");