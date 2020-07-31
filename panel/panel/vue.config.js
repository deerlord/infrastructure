module.exports = {
  devServer: {
    proxy: {
      "/weather": {
        target: "https://influxdb.deerlord.lan",
        secure: false,
        changeOrigin: true
      }
    }
  }
};
