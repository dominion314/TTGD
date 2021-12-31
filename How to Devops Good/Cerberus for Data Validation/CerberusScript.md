Hello IT breatheren, I am back with another video, thank you for joining me. Today I'm going to teach you how to do devops and in this video we're going to touch on a few things. We're going to review write some python code, create a schema template, and then compare a customer request against that template. As usual in tech, this sounds complicated but its easily demistified when we apply it practically. 

Simply stated, we're going to create a python script that reads a customer request for a new PSA and ensures that it meets all of our code requirements. 

This video is not meant to be a stand alone lesson, but rather to provide you some insight into the work of a devops engineer. I'm going to explain things to the best of my ability, but I will be moving fast so if you're unsure about something, post your questions in the comments below.

Be sure to like this video and subscribe to the channel, and without further ado lets get started. 

-The first thing we want to do with any project we're working on is to state our objective:

We are basically creating a system for validating a customers request for a new PSA. What is PSA you ask? PSA is basically a way for app developers to allow 3rd party businesses to access their data securely. This occurs without the need for that outside business to take residence in your companies personal workspace. This provides a safe and cost effective way of sharing your teams resources, thus the name Private Services Access. 

By creating this script and the schema parameters, we protect our source code from errors and are able to save the company money by streamlining the deployments of this new cloud resource. 

Our goal is to write a script that will review a customer request for PSA and ensure it meets our code requirements. This is a very typical workflow in devops, to write schema policies that protect our source code and streamline customer requests. . 

-Let start off by writing our python script. We will be using a very useful library known as cerberus, which I will post in the description below. 
-Now lets create the schema that will serve as a checklist for our parameters. What is schema? Schema is term we use to describe the validation of data types. Basically schema outlines what words, letters, characters, and symbols are allowed within the customer request. For example, if a customer fat fingers their request and asks for 2 trillion IP address, schema will deny this request. Because the schema template is mirroring the customer request , we will need to use it as a reference. For the sake of time I've already written the customer request and schema template, but will discuss them briefly.

Ideally we would want them to only have to fill in their team name and the subnet they need.

-Breifly discuss PSA connecting to our mongo DB.
-Pass the MR
-Fail the MR
-Pass again

As you can see devops covers a wide array of different disciplines within IT. For my job I have to know a little networking, a little python scripting, and also YAML. However, one you understand the fundamentals all of those different areas are what produces the cloud landscape that we see today. With more businesses moving to the cloud, I can only imagine that demand for talented devops engineers is only going to increase. 

So I hope you enjoyed this walkthrough and the code for this video will be linked in the description below. Be sure to like and subscribe and as always, Ill see you in the next one!
