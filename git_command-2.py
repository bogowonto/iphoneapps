# stash change 

import os
import subprocess
import sys

import os
import git
from git import Git
from git import GitCommandError

repo = git.Repo()
print(repo)


# build_tool = sys.argv[1]
# build_dir = sys.argv[2]
# pom_version = sys.argv[3]
# branch_name = sys.argv[4]
# git_url = sys.argv[5]
#
# #####################################
# # Wissel naar de juiste working dir #
# #####################################
# os.chdir(build_dir)
# repo = git.Repo()
# git = Git()
#
# #####################################################################################
# # Bepaal wat de versie is, als het een nieuwe build is kijkt hij naar de branchnaam #
# #####################################################################################
# version_nr = branch_name.split("/")[1]
#
# if version_nr in pom_version:
#     build_version = pom_version
# else:
#     build_version = version_nr + "-1"
#
# #########################################
# # Check de juiste branch uit binnen git #
# #########################################
# git.execute(['git', 'remote', 'set-url', 'origin', git_url])
# git.execute(['git', 'pull', 'origin', branch_name])
# upstream = '--set-upstream-to=origin/%s' % branch_name
# git.execute(['git', 'branch', upstream, branch_name])
# git.execute(['git', 'checkout', branch_name])
# git.execute(['git', 'pull', 'origin', branch_name])
#
# ##########################################################
# # Wijzig de pom versie met het mvn versions:set commando #
# ##########################################################
# mvnArgument = 'mvn versions:set -DnewVersion=%s' % build_version
# subprocess.call([mvnArgument], shell=True)
#
# #################################
# # Commit en push de wijzigingen #
# #################################
# git.execute(['git', 'add', '.'])
# message = 'mvn version to %s' % build_version
# git.execute(['git', 'commit', '-m', message])
# git.execute(['git', 'push', 'origin', branch_name])
#
# ################################
# # Creer en push een nieuwe tag #
# ################################
# tag_version = 'v%s' % build_version
# tag_message = 'tag %s is created' % tag_version
# git.execute(['git', 'tag', '-a', tag_version, '-m', tag_message])
# git.execute(['git', 'push', 'origin', tag_version])
#
# ################
# # Run de build #
# ################
# if 'maven' in build_tool:
#     subprocess.call(['mvn clean package -Dmaven.test.skip -Dfindbugs.skip'], shell=True)
# elif 'gradle' in build_tool:
#     subprocess.call(['./gradlew build -x test'], shell=True)
#
# ####################################
# # Bepaal wat de volgende versie is #
# ####################################
# snapshot_version, snapshot_build_nr = build_version.split("-")
# next_version = snapshot_version + "-" + str(int(snapshot_build_nr) + 1)
#
# ##########################################################
# # Wijzig de pom versie met het mvn versions:set commando #
# ##########################################################
# mvnSnapshotArgument = 'mvn versions:set -DnewVersion=%s-SNAPSHOT' % next_version
# subprocess.call([mvnSnapshotArgument], shell=True)
#
# #################################
# # Commit en push de wijzigingen #
# #################################
# git.execute(['git', 'add', '.'])
# snapshot_message = 'mvn version to %s-SNAPSHOT' % next_version
# git.execute(['git', 'commit', '-m', snapshot_message])
# git.execute(['git', 'push', 'origin', branch_name])
#
# #####################
# # Merge met develop #
# #####################
# git.execute(['git', 'pull', 'origin', 'develop'])
# git.execute(['git', 'checkout', 'develop'])
# git.execute(['git', 'branch', '--set-upstream-to=origin/develop', 'develop'])
# git.execute(['git', 'pull', 'origin', 'develop'])
# try:
#     git.execute(['git', 'merge', branch_name])
#     git.execute(['git', 'push', 'origin', 'develop'])
#     print('Mergen geslaagd')
# except GitCommandError:
#     git.execute(['git', 'merge', '--abort'])
#     print('###################################################')
#     print('###################################################')
#     print('##                                               ##')
#     print('##  MERGEN GEFAALD, HANDMATIG MERGEN IS VEREIST  ##')
#     print('##                                               ##')
#     print('###################################################')
#     print('###################################################')
