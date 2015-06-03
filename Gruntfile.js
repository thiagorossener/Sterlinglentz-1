'use strict';

// # Globbing
// for performance reasons we're only matching one level down:
// 'test/spec/{,*/}*.js'
// use this if you want to recursively match all subfolders:
// 'test/spec/**/*.js'

module.exports = function (grunt) {

    // Load grunt tasks automatically
    require('load-grunt-tasks')(grunt);

    // Time how long tasks take. Can help when optimizing build times
    require('time-grunt')(grunt);

    // Configurable paths for the application
    var siteConfig = {
        baseDir: 'src/static',
        srcDir: 'src/static/src',
        distDir: 'src/static/dist'
    };

    // Define the configuration for all the tasks
    grunt.initConfig({

        // Project settings
        siteConfig: siteConfig,

        // Watches files for changes and runs tasks based on the changed files
        watch: {
            //bower: {
            //    files: ['bower.json'],
            //    tasks: ['copy:deps']
            //},
            js: {
                files: ['<%= siteConfig.srcDir %>/scripts/{,*/}*.js'],
                tasks: ['newer:jshint:all', 'concat:js'],
                options: {
                    livereload: '<%= connect.options.livereload %>'
                }
            },
            sass: {
                files: ['<%= siteConfig.srcDir %>/styles/**/*.{scss,sass}'],
                tasks: ['sass:dist', 'autoprefixer'],
                options: {
                    livereload: '<%= connect.options.livereload %>'
                }
            },
            gruntfile: {
                files: ['Gruntfile.js']
            },
            livereload: {
                options: {
                    livereload: '<%= connect.options.livereload %>'
                },
                files: [
                    '<%= siteConfig.srcDir %>/images/{,*/}*.{png,jpg,jpeg,gif,webp,svg}'
                ]
            }
        },

        // JSHint
        // https://github.com/gruntjs/grunt-contrib-jshint
        // Validates JS Make sure code styles are up to par and there are no obvious mistakes
        jshint: {
            options: {
                jshintrc: '.jshintrc',
                reporter: require('jshint-stylish')
            },
            all: {
                src: [
                    'Gruntfile.js',
                    '<%= siteConfig.srcDir %>/scripts/{,*/}*.js'
                ]
            },
        },

        // Grunt Clean
        // https://github.com/gruntjs/grunt-contrib-clean
        // Empties DIST folders to start fresh
        clean: {
            dist: {
                files: [{
                    dot: true,
                    src: [
                        '<%= siteConfig.distDir %>/{,*/}*',
                    ]
                }]
            },
            server: '.tmp'
        },

        // Autoprefixing
        // https://github.com/nDmitry/grunt-autoprefixer
        // Replaces relevant CSS with vendor specific css selectors
        autoprefixer: {
            options: {
                browsers: ['last 1 version']
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: '<%= siteConfig.distDir %>/styles/',
                    src: '{,*/}*.css',
                    dest: '<%= siteConfig.distDir %>/styles/'
                }]
            }
        },

        // Grunt SASS (via libsass)
        // https://github.com/sindresorhus/grunt-sass
        // Compile SASS to css
        /*sass: {
            options: {
                sourceMap: true,
                includePaths: [
                    '<%= siteConfig.baseDir %>/bower_components'
                ]
            },
            dist: {
                files: {
                    '<%= siteConfig.distDir %>/styles/screen.css':
                    '<%= siteConfig.srcDir %>/styles/screen.scss'
                }
            }
        },*/

        // Grunt Contrib SASS (via Ruby)
        // https://github.com/gruntjs/grunt-contrib-sass
        sass: {
            dist: {
                options: {
                    loadPath: [
                        '<%= siteConfig.baseDir %>/bower_components'
                    ],
                    style: 'expanded'
                },
                files: {
                    '<%= siteConfig.distDir %>/styles/screen.css':
                        '<%= siteConfig.srcDir %>/styles/screen.scss'
                }
            }
        },


        // Grunt Minify Images
        // https://github.com/gruntjs/grunt-contrib-imagemin
        imagemin: {
            dist: {
                files: [{
                    expand: true,
                    cwd: '<%= siteConfig.srcDir %>/images',
                    src: '{,*/}*.{ico,png,jpg,jpeg,gif}',
                    dest: '<%= siteConfig.distDir %>/images'
                }]
            }
        },

        // Grunt Minify SVG
        // https://github.com/sindresorhus/grunt-svgmin
        svgmin: {
            dist: {
                files: [{
                    expand: true,
                    cwd: '<%= siteConfig.srcDir %>/images',
                    src: '{,*/}*.svg',
                    dest: '<%= siteConfig.distDir %>/images'
                }]
            }
        },

        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: '<%= siteConfig.distDir %>/styles',
                    src: ['*.css', '!*.min.css'],
                    dest: '<%= siteConfig.distDir %>/styles',
                    ext: '.min.css'
                }]
            }
        },

        uglify: {
            dist: {
                files: {
                    '<%= siteConfig.distDir %>/app.min.js': ['<%= siteConfig.distDir %>/app.js']
                }
            }
        },

        concat: {
            js: {
                src: ['<%= siteConfig.srcDir %>/scripts/{,*/}*.js'],
                dest: '<%= siteConfig.distDir %>/scripts/app.js'
            }
        },


        // Grunt Copy
        // https://github.com/gruntjs/grunt-contrib-copy
        // Copies remaining files to places other tasks can use
        copy: {
            dist: {
                files: [{
                    expand: true,
                    dot: true,
                    cwd: '<%= siteConfig.srcDir %>',
                    dest: '<%= siteConfig.distDir %>',
                    src: [
                        '*.{ico,png,txt}',
                        'images/{,*/}*.{webp}',
                        'fonts/**/*.*'
                    ]
                }]
            }
        },

        // Grunt Concurrent
        // https://github.com/sindresorhus/grunt-concurrent
        // Run some tasks in parallel to speed up the build process
        concurrent: {
            test: [
                'sass:dist'
            ],
            dist: [
                'sass:dist',
                'imagemin',
                'svgmin'
            ]
        },
    });


    grunt.registerTask('serve', 'Compile then start a connect web server', function (target) {
        if (target === 'dist') {
            return grunt.task.run(['build', 'connect:dist:keepalive']);
        }

        grunt.task.run([
            'clean:server',
            'autoprefixer',
            'connect:livereload',
            'watch'
        ]);
    });

    grunt.registerTask('build', [
        'clean:dist',
        'concurrent:dist', // sass, imagemin, svgmin
        'concat',
        'cssmin',
        'uglify',
        'autoprefixer',
        'copy:dist',
    ]);

    grunt.registerTask('default', [
        'newer:jshint',
        'build'
    ]);
};
