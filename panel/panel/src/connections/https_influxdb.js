import https from "https";

let options = {
  hostname: "influxdb.deerlord.lan",
  port: 443,
  path: "/query?chunked=true&db=weather&epoch=s&q=select+temp+from+current+where+time+%3E%3D+now%28%29+-+1h",
  method: "GET",
  rejectUnauthorized: false
}
options.agent = new https.Agent(options);

export default {
  current_temperature() {
    var result;
    result = https.request(options, (res) => {
      res.on('data', (d) => {
        console.log('data:', d)
      })
    });
    return result
  }
}
