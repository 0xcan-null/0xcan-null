<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Terminal</title>
    <style>
        body {
            background-color: #050505;
            color: #00ff66;
            font-family: 'Courier New', Courier, monospace;
            padding: 20px;
            margin: 0;
            overflow: hidden;
        }
        #terminal {
            white-space: pre-wrap;
            font-size: 16px;
            line-height: 1.4;
        }
        .cursor {
            display: inline-block;
            width: 8px;
            height: 18px;
            background-color: #00ff66;
            animation: blink 0.8s infinite;
            vertical-align: middle;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
    </style>
</head>
<body>

<div id="terminal"></div><span class="cursor"></span>

<script>
const codeSnippet = `[INITIALIZING SYSTEM OVERRIDE...]
> Connecting to remote host: 192.168.1.104... SUCCESS
> Bypassing firewall protocols... DONE
> Injecting custom payload...
> Accessing root directory: /usr/bin/local
> Status: ACCESS GRANTED

function initializeHack() {
    const status = "ONLINE";
    let securityLevel = 0;
    while(securityLevel < 100) {
        console.log("Decrypting packet: " + securityLevel + "%");
        securityLevel += 10;
    }
    return "SYSTEM OVERRIDDEN";
}

// Executing payload...
initializeHack();
> Process finished with exit code 0`;

let index = 0;
const speed = 3; // Yazma hızı (harf başına düşen karakter sayısı)
const terminal = document.getElementById("terminal");

document.addEventListener("keydown", () => {
    if (index < codeSnippet.length) {
        terminal.innerHTML += codeSnippet.substring(index, index + speed);
        index += speed;
        window.scrollTo(0, document.body.scrollHeight);
    }
});
</script>

</body>
</html>
