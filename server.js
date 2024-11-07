const port = process.env.PORT || 5000,
    http = require('http'),
    fs = require('fs');

const { spawnSync } = require('child_process')

const server = http.createServer(function (req, res) {
    if (req.method === 'GET') {
        graphData = ""

        req.on('data', chunk => {
            graphData += chunk
        })

        req.on('end', () => {
            const python = spawnSync('python3', ["graph_partition.py", graphData])
            let output = python.stdout.toString()
            console.log(output)
            
            res.writeHead(200, {"Content-Type": "text/plain"});
            res.write('✅:' + output);
            res.end();
        })
    }
    else {
        res.writeHead(400);
        res.write('Unsupported Method');
        res.end();
    }
});

// Listen on port 5000
server.listen(port, '0.0.0.0');

console.log('Server running at http://0.0.0.0:' + port + '/');
