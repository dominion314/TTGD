Hello IT breatheren, I am back with another video, thank you for joining me. Today I'm going to teach you how to do devops and in this video we're going to touch on a few things. We're going to review CI/CD, write some python code, create a policy, and then compare a customer request against that policy. As usual in tech, this sounds complicated but its easily demistified when we apply it practically. 

Simply stated, we're going to create a python script that reads a customer request for a new PSA and ensures that it meets all of our code requirements. 

This video is not meant to be a stand alone lesson, but rather to provide you some insight into the work of a devops engineer. I'm going to explain things to the best of my ability, but I will be moving fast so if you're unsure about something, post your questions in the comments below.

Be sure to like this video and subscribe to the channel, and without further ado lets get started. 

-The first thing we want to do with any project we're writing is to state our objective:

We are basically creating a system for validating a customers request for a new PSA. PSA is basically a way for app tedevelopers to allow 3rd party businesses to access their data securely. This occurs without the need for that outside business to take residence in your companies internal workspace, which provides a safe and cost effecting sharing platform. They simply hang off their own unqique connection so that they have access only to what they need from app developers, thus the name Private Services Access. 

By creating these script and parameters, we protect our source code from errors and are able to save the company money by streamlining the checks and deployments of this new cloud resource. 

Our goal is to write a script that will review a customer request for PSA and ensure it meets our code requirements. This is a very typical workflow in devops, to write policies that protect our source code and streamline customer requests. We will write a python script utilizing a library called Cerberus and additionally will define a YAML policy to enforce our PSA parameters. 

-Let start off by writing our python script.
-Now lets create the schema that will serve as a checklist for our parameters. We need to create this according to our customer request template. Ideally we would want them to only have to fill in their team name and the subnet they need.
-Breifly discuss PSA connecting to our mongo DB.
-Pass the MR
-Fail the MR
-Pass again

As you can see devops covers a wide array of different disciplines within IT. For my job I have to know a little networking, a little python scripting, and also CI/CD. However, one you understand the fundamentals all of those different areas are what produces the cloud landscape that we see today. With more businesses moving to the cloud, I can only imagine that demand for talented devops engineers is only going to increase. 

So I hope you enjoyed this walkthrough and the code for this video will be linked in the description below. Be sure to like and subscribe and as always, Ill see you in the next one!
