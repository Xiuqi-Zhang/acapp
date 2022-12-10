#! /bin/bash

#此文件将static/js下的src中的js文件合并，并存在dist文件夹中

JS_PATH=/home/yoichi/acapp/game/static/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/

find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js

echo yes | python3 manage.py collectstatic

