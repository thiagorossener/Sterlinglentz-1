## Frontend Static Files

All of our frontend javascript and sass is managed by `node`, `bower` and `grunt`.
Everything is compiled and minified etc. from the `src/static/src` folder into the
`src/static/dist` using a number of Grunt tasks (that can be seen in the root
`Gruntfile.js`). This compilation will happen automatically when you have the
Grunt `watch` command running in the background. After compilation, these static
javascript and css files are also automatically inserted into our `template/_base.html`.
The destination of the compilation (`src/static/dist`) is corresponds to our
`STATIC_DIRS` setting which all gets copied to `STATIC_ROOT` upon `python manage.py
collectstatic`

## Frontend Setup

    # Install all node modules:
    npm install
    bower install
    