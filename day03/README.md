# Day 03 - Python Bootcamp

### Exercise 00: Innocent Prank

```
 <script>
        hacked = function() {
            alert('hacked');
        }
        window.addEventListener('load', 
          function() { 
            var f = document.querySelector("form");
            f.setAttribute("onsubmit", "hacked()");
          },
          false
        );
</script>
```

You need to write a Python script "exploit.py" that will do several things:

- First, it needs to read a file called "evilcorp.html".
- Second, it should change the page title (in `<title>` tags) to "Evil Corp - Stealing your money every day".
- Third, it should parse the user's name from the page (including the pronoun) and insert a new `<h1>' tag  into the `body' of a page, saying `<h1>Mr. Robot, you are hacked!</h1>`, where "Mr. Robot" is a parsed pronoun and name.
- Fourth, it must also insert a Trenton's script into the `body` of a page. If all goes well, you should see the word "hacked" appear in an alert window when you press the `Send' button.
- Finally, the link at the bottom of a page should now point to "https://mrrobot.fandom.com/wiki/Fsociety" with the actual name of the company on the page replaced with "Fsociety".

The new HTML file should be named "evilcorp_hacked.html" and placed in the same directory as the source "evilcorp.html" file.

### Exercise 01: Cash Flow

You need to write two scripts - `producer.py` and `consumer.py`.

Producer needs to generate JSON messages like this:

```
{
   "metadata": {
       "from": 1023461745,
       "to": 5738456434
   },
   "amount": 10000
}
```

and put it as payload into a Redis pubsub queue. All account numbers ('from' and 'to') should be exactly 10 digits. Additional points can be earned if the code uses the built-in `logging` module (instead of the `print` function) to write generated messages to stdout for manual testing.

Consumer should be given an argument with a list of account numbers like this:

`~$ python consumer.py -e 7134456234,3476371234`

where `-e` is a parameter receiving a list of bad guy account numbers. When started, it should read messages from a pubsub queue and print them to stdout, one line at a time. For accounts in the bad guys list, if they are specified as a recipient, the consumer should *swap* sender and recipient for the transaction. But this should *only* happen if "amount" is not negative.

For example, if producer generates three messages like this

```
{"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

consumer started like `~$ python consumer.py -e 2222222222,4444444444` should print out:

```
{"metadata": {"from": 2222222222,"to": 1111111111},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

Note that only the first line was changed. The second wasn't changed because "amount" was negative (even though the receiver is a bad guy). The third wasn't changed because the bad guy is a sender, not a receiver.

### Exercise 02: Deploy

You don't need to know Ansible intimately to complete this exercise. It would be nice if you could test your code through it, though it's not required. There is a list of tasks that should be placed in a generated deploy.yml file in YAML format:

- Install packages;
- Copy files;
- Execute files on a remote server using a Python interpreter with appropriate arguments.

These tasks should be generated in Ansible notation (e.g. look [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) for notation
on copying files). The script should be named 'gen_ansible.py'.

Thus, your code should convert Elliot's 'todo.yml' into 'deploy.yml' following this notation.
