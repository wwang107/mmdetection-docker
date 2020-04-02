cp Dockerfile Dockerfile.bkp

#echo "RUN adduser --disabled-password --gecos \"\" -u 0 user"  >> Dockerfile
echo "RUN adduser --disabled-password --gecos \"\" -u $UID user"  >> Dockerfile
echo "USER user" >> Dockerfile


if [ "$#" == 2 ]; then
    echo "RUN echo \"source ~/.bashrc\ncd $1 && python $2\" >> /home/user/run.sh" >> Dockerfile
fi

./build.sh

rm Dockerfile
mv Dockerfile.bkp Dockerfile