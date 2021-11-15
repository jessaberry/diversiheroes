// loads the babel loader, lets us use bable to transpile (transform) code
module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /\node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}