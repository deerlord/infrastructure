import axios from "axios";

const InfluxDB = axios.create({
  withCredentials: false,
  headers: {
    "Content-Type": "text/plain"
  }
})

export default {
  current_temperature() {
    let url = "https://influxdb.deerlord.lan/query?chunked=true&db=weather&epoch=s&q=select+temp+from+current+where+time+%3E%3D+now%28%29+-+1h%3B";
    return InfluxDB.get(url);
  }
}




