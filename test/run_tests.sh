#!/bin/sh
script_dir=`dirname $0`
cd $script_dir/acceptance
pybot --exclude not_ready .
