# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following two topics:

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

# To acces an array is O(1) constant time.
# To add to the front of the array is O(n) because we have to shift each node over to the right one before adding to the front.
# To add to the back of the array is usually O(1) but sometime can be O(n)

* What is the worse case scenario if you try to extend the storage size of a dynamic array?

# O(n) because it has to copy each element from the old space to the new space one at a time.

Explain how blockchain networks remain in consensus:
* What does a node do if it gets a message from another in the network with a new block?

# Must validate a Proof of Work solution and confirm if it's correct before it can be added to the chain securing the transaction.

* Why can't someone cheat by changing a transaction from an earlier block to give themselves coins?

# It's hard to cheat by changing a transaction from an earlier block because the previous hash stored in the block you want to change and the hash before it will no longer match. The hash will be completely different even if you change one character or digit. Meaning you will have to go back and change all the previous blocks and at the same time try to outmine all the other computers trying to mine a new block making it extremely difficult.  

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
