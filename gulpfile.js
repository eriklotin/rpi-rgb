var gulp = require('gulp');

gulp.task('default', [], function() {
    gulp.src("node_modules/bootstrap/dist/css/bootstrap.css")
        .pipe(gulp.dest('static/css'));

    gulp.src("node_modules/jquery/dist/jquery.min.js")
        .pipe(gulp.dest('static/js'));
});
