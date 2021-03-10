module.exports = {
  appName: 'customNotice',
  account: {
    username: 'pandora@qiniu.com',
    password: '12345678'
  },
  proxy: {
    '/api': {
      target: 'http://cs21:9220',
      changeOrigin: true
    }
  }
}
