var http = require('http'),
    pug = require('pug'),
    exec = require('child_process').exec;

console.log('Ready to start.');
http.createServer(function (req, res) {
    if (req.method == 'GET') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        var f = pug.compileFile('index.pug', {
            'pretty': true
        });
        res.end(f());
    } else if (req.method == 'POST') {
        var body = '';
        req.on('data', function (data) {
            body += data;
        });
        req.on('end', function () {
            exec('python motor-ctl.py ' + body);
            res.end();
        });
    }
}).listen(3000);
