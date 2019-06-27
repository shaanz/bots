var http = require('http');

console.log("####################################################");
console.log("##           DEMO  CENTER                         ##");
console.log("####################################################");


http.createServer(function (req, res) {
  // set up some routes
  console.log ("REQ URL :  " + req.url);

  switch(req.url) {
    case '/':
      //console.log("[501] " + req.method + " to " + req.url);
      res.writeHead(501, "Not implemented", {'Content-Type': 'text/html'});
      res.end('<html><head><title>501 - Not implemented</title></head><body><h1>Not implemented!</h1></body></html>');
      break;
    
   case '/data*' :
   console.log("Data Captured :: " + req.url);
   break;     
    
    default:
      res.writeHead(200, {'Content-Type': 'text/javascript'});
      res.end('<script>alert("Test Successful")<script>');
      //console.log("No Match for Request");
       break;
  };
}).listen(9999); // listen on tcp port 9999 (all interfaces)
