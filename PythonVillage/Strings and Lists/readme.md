<h1> Strings and Lists </h1>
<p> Python also has variable types that can
hold more than one piece of data at a time.  The simplest such variable is a <strong>list.</strong> </p>

<p> You can assign data to a list in the following way: <strong><code> list_name = [item_1, item_2, ..., item_n] </code></strong> </p>
<p> The items of the list can be of any other type: integer, float, string </p>

<p> Any item in a list can be accessed by its index, or the number that indicates its place in the list.  </p>

<pre><code>tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
print(tea_party[2])
</code></pre>

<p>Your output should be:</p>

<pre><code><strong> Dormouse</strong> </code></pre>

<p>
Note that the output was <em>not</em> <strong>Hatter</strong>, as you might have guessed.  This is because
in Python, indexing begins with 0, not 1.  This property is called 0-based numbering,
and it's shared by many programming languages.
</p>

<p> You can easily change existing list items by reassigning them.  Try running the following: </p>
<pre><code>tea_party[1] = 'Cheshire Cat'
print(tea_party)  </code></pre>

<p>This code should output the list with "Hatter" replaced by "Cheshire Cat":</p>
<pre><code><strong>March Hare, Cheshire Cat, Dormouse, Alice</strong></code></pre>

<p>You can also add items to the end of an existing list by using the function <strong>append()</strong></p>

<pre><code>tea_party.append('Jabberwocky')
print(tea_party) </code></pre>

<p>This code outputs the following:</p>

<pre><code><strong>March Hare, Cheshire Cat, Dormouse, Alice, Jabberwocky</strong></code></pre>

<p>
If you need to obtain only some of a list, you can use the notation <strong><code>list_name[a:b]</code></strong>
to get only those from index <strong><code>a</code></strong> up to but not including index <strong><code>b</code></strong>.
For example, <strong><code>tea_party[1:3]</code></strong> returns <strong><code>Cheshire Cat, Dormouse</code></strong>, not <code><strong>Cheshire Cat, Dormouse, Alice</code></strong>.
This process is called "list slicing".
</p>

<p>
If the first index  of the slice is unspecified, then Python assumes that the slice begins
with the beginning of the list (i.e., index 0);
if the second index of the slice is unspecified, then you will obtain the items
at the end of the list. For example, <code><strong>tea_party[:2]</strong></code> returns <code><strong>March Hare, Cheshire Cat</code></strong>
and <code><strong>tea_party[3:]</strong></code> returns <code><strong>Alice, Jabberwocky</strong></code>.

You can also use negative indices to count items backtracking from the end of the list.
So <code><strong>tea_party[-2:]</strong></code> returns the same output as <code><strong>tea_party[3:]</strong></code>: <code><strong>Alice, Jabberwocky</strong></code>.

Finally, Python equips you with the magic ability to slice strings the same way
that you slice lists. A string can be considered as a list of characters,
each of which having its own index starting from 0. For example, try running the following code
</p>

<pre><code>a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
print(c) </code></pre>
<p>
This code will output the string formed by the first character of <code><strong>miserable</strong></code> and the last four characters of <code><strong>flimsy</strong></code>:
</p>
<pre><code><strong>mimsy</strong></code></pre>

