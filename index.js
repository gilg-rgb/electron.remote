const fs = require('fs');
const path = require('path');
const os = require('os');

const sourcePath = path.join(__dirname, 'assets', 'sample.png');
const destPath = path.join(os.tmpdir(), 'sample.png');

try {
    if (fs.existsSync(sourcePath)) {
        fs.copyFileSync(sourcePath, destPath);
        console.log(`Copied sample.png to ${destPath}`);
    }
} catch (error) {
    console.error('Failed to copy sample.png:', error);
}
