#! /bin/bash

#This piece of code scans through the files in bandpass_raw folder
#looking for the words "energy" or "photons" inside them and then
#copies the files into a folder named bandpass_giovanni and renames
#their extensions respectively as *.energy.filt and *.photons.filt.
#It is a very basic and poorly optimized code, but works for this simple example

#I create a new folder to store the ordered data
mkdir bandpass_giovanni

#I enter the original data folder
cd bandpass_raw

#This is a simple version where we know the kinds of extensions we have,
#in this case .dat, .asc, .ASCII 
array1=($a*.dat)
array2=($a*.asc)
array3=($a*.ASCII)

#Here I count how many there are for each extension
l1=${#array1[@]}
l2=${#array2[@]}
l3=${#array3[@]}

#I show the number of files for each extension
text1=( We have $l1 .dat files )
text2=( We have $l2 .asc files )
text3=( We have $l3 .ASCII files )

echo ${text1[@]}
echo ${text2[@]}
echo ${text3[@]}

#We loop over each extension array
for (( i=0; i<$l1; i++ ))
do
    #I obtain the temporary value for the second line of each i-th file 
    tmp=$(head -2 ${array1[$i]}| tail -1)
    
    #I also get the name without the extension of the i-th file
    filename=$(basename -- "${array1[$i]}")
    filename="${filename%.*}"

    #Since I am doing a very basic string comparison,
    #I need to include all cases of the word "energy" I saw listing the second line 
    if [[ "$tmp" == "# energy" ]] || [[ "$tmp" == "#energy" ]]
    then
	cp ${array1[$i]} ../bandpass_giovanni/"${filename}".energy.filt
    #If it is not "energy" it's "photons"
    else
	cp ${array1[$i]} ../bandpass_giovanni/"${filename}".photons.filt 
    fi
    
done

#Do the same process for the other big array
for (( i=0; i<$l2; i++ ))
do
    tmp=$(head -2 ${array2[$i]}| tail -1)

    filename=$(basename -- "${array2[$i]}")
    filename="${filename%.*}"

    if [[ "$tmp" == "# energy" ]] || [[ "$tmp" == "#energy" ]]
    then
	cp ${array2[$i]} ../bandpass_giovanni/"${filename}".energy.filt
    else
	cp ${array2[$i]} ../bandpass_giovanni/"${filename}".photons.filt
    fi
    
done

#Looking through the data files I noticed we only have one ASCII file
#and it does not have neither "energy" nor "photons", thus
#it is faster to avoid using another for loop  and directly copy this file to the other folder
cp ${array3[0]} ../bandpass_giovanni/"${array3[0]}"

#we exit from bandpass_raw
cd ..

#We confirm that we created a new folder with the renamed files
final_text=( Created renamed files in the new folder bandpass_giovanni )
echo ${final_text[@]}
