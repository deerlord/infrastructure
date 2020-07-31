import axios from "axios";

const InfluxDB = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  withCredentials: false
})

export default {
  current_temperature() {
    let url = "/query?chunked=true&db=weather&epoch=s&q=select+temp+from+current+where+time+%3E%3D+now%28%29+-+1h%3B";
    return InfluxDB.get(url);
  }
}




