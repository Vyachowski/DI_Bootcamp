import fs from 'node:fs';

export default function readFileContent(filePath) {
  console.log(fs.readFileSync(filePath, 'utf8'));
}