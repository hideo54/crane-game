const http = require('http');
const pug = require('pug');
const exec = require('child_process').exec;

http.createServer((req, res) => {
    if (req.method === 'GET') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end((pug.compileFile('index.pug', {
            'pretty': true
        }))());
    } else if (req.method === 'POST') {
        var body = '';
        req.on('data', data => {
            body += data;
        });
        req.on('end', () => {
            exec('python motor-ctl.py ' + body);
            res.end();
        });
    }
}).listen(3000);
