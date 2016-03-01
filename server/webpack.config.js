var webpack = require('webpack');

var commonsPlugin = new webpack.optimize.CommonsChunkPlugin('common.js');

module.exports = {
    entry: {
        index: './src/js/index.js',
        testpage: './src/js/testpage.js'
    },
    output: {
        path:     'static',
        filename: '[name].js',
    },
    plugins: [commonsPlugin]
};
