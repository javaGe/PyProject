var page = require('webpage').create();
var system = require('system');
url = system.args[1]
name = system.args[2]
page.open(url, function(status){
    console.log('Status:' + status);
    if(status === "success") {
        page.render(name);
    }
   phantom.exit();
});
