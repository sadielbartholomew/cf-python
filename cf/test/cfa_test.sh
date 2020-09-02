# -----------------------------------------------------------------------
# Test cfa
# -----------------------------------------------------------------------
# Note: 'command || exit N' cases here are to ensure cfa command errors
# are passed through to the Python unittest which runs this. Otherwise
# commands can fail (give non-zero exit status) silently. Different
# numbers mean the specific command failing (first) can be distinguished.
# Note that 'set -e' would make it harder to find the relevant line.

sample_files=$PWD

test_file=delme_cfa.nc
test_dir=delme_cfa_dir

rm -fr $test_dir $test_file
mkdir $test_dir

for opt in vs vm vc
do
    #  echo $opt
    cfa    -$opt $sample_files/[a-be-zD]*.[np][cp] >/dev/null || exit 2
    cfa -1 -$opt $sample_files/[a-be-zD]*.[np][cp] >/dev/null || exit 3
  for f in `ls $sample_files/[a-be-zD]*.[np][cp] | grep -v $test_file`
  do
#    echo $f
    cfa -$opt $f >/dev/null || exit 4
    if [ $opt = vs ] ; then
      cfa --overwrite -o $test_file $f >/dev/null || exit 5
      cfa --overwrite -d $test_dir  $f >/dev/null || exit 6
    fi
  done
  rm -f $test_file
done

#echo 0
rm -f $test_file
cfa --overwrite -d $test_dir $sample_files/[a-be-zD]*.[np][cp] >/dev/null || exit 7

#echo 1
rm -f $test_file
cfa -o $test_file $sample_files/test*.[np][cp] >/dev/null || exit 8

#echo 2
rm -f $test_file
cfa -n -o $test_file $test_dir/file*.[np][cp] >/dev/null || exit 9

#echo 3
rm -fr $test_dir $test_file >/dev/null || exit 10
