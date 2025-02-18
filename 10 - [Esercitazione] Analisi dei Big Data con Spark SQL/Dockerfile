#this Dockerfile is not used anymore. It was an attempt to download zip inside docker 
#and to expose it to other containers via volume defined in yml file. 
#The download works but I don't know how to expose the unzipped file in the shared volume.
#It seems that docker compose volume overwrites existing volume defined here (or something like that).
#Or maybe the download happens only in image and isn't loaded into container; idk.
#The workaround is to manually download and unzip the file in host directory that 
#will be used as common volume by docker compose.
FROM apache/zeppelin:0.11.2

# Install wget if not already present (might be in the base image, but good practice)
# Switch to root user to install packages
USER root 
RUN apt-get update && apt-get install -y wget unzip

WORKDIR /data

# These run commands could be merged in single run command (each command is separated with &&)
# but for now keep it separated for clarity in logs
RUN wget http://files.grouplens.org/datasets/movielens/ml-latest.zip
RUN unzip ml-latest.zip
RUN rm ml-latest.zip
RUN ls
RUN ls ml-latest
RUN pwd

# COPY /data/ml-latest /data/ml-latest
VOLUME /data

# Set permissions on /data (important!)
# Assuming 1000 is the user/group ID in the base image
RUN chown -R 1000:1000 /data

# Switch back to non-root user, if necessary (check your base image)
USER 1000 
WORKDIR /opt/zeppelin

# this cmd is the same as CMD["bin/zeppelin.sh"] since the workdir is /opt/zeppelin
CMD ["/opt/zeppelin/bin/zeppelin.sh"]
