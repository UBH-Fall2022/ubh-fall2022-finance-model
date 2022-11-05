// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received                                                              
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}
// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received                                                          
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}