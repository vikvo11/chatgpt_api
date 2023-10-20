Best way is to check how much space can be reclaimed due to unused images.
docker system df
If RECLAIMABLE amount is greater than zero (that would definitely the case) then run command
docker system prune -a

apk fix musl
apk update musl

docker images
docker rmi [IMAGE_ID or IMAGE_NAME]

docker-compose down --rmi all -v

RUN pip install --pre openai
