## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git branch

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show ~1

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git diff 03f6124cd3670c0f8e064af707c285167d3fe9ca 00aee1030

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset --hard 00aee10309e1aa8b0323e98d51b2ecf92f332156

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git reset --hard HEAD~1