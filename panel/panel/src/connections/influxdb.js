import axios from "axios";
import https from "https";

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

const InfluxDB = axios.create({
  baseURL: "https://influxdb.deerlord.lan",
  httpsAgent: new https.Agent({
    rejectUnauthorized: false
  })
})

export default {
  current_temperature() {
    return InfluxDB.get(
      "/query?chunked=true&db=weather&epoch=s&q=select+temp+from+current+where+time+%3E%3D+now%28%29+-+1h"
    );
  }
}
