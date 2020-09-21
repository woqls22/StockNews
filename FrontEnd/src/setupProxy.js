const { createProxyMiddleware } = require('http-proxy-middleware');
const url = 'http://115.85.180.185:7749';

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: url,
      changeOrigin: true,
    })
  );
};