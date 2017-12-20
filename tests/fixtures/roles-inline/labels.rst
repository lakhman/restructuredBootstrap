.. [Important Note] Text roles inside labels are also parse
.. The LAST back-tick MUST be escaped (with a `\`) INSIDE the parent role

.. (Weirdly) you don't have to escape the backtick if it's at the end
.. This works (Notice: The last back tick for :small: is NOT escaped)

:label-default:`Default Label :small:`small``

.. This FAILS with error:
.. System Message: WARNING/2
.. Inline interpreted text or phrase reference start-string without end-string.
.. This will show as HTML output in your doc along the lines of:
.. <p><span class="..">..<a href="#id1"><span class="problematic" id="id2">..</span></a>..
.. <div class="system-message"><p class="system-message-title"></div></span>..`</p>

.. This will throw the error above:
.. :label-default:`Default Label :small:`small` Other Text`

.. Test other variations of inline roles for labels

:label-default:`Default :small:`small\` Label`

:label-primary:`Primary :bg-primary:`bg-primary\` Label`

:label-success:`Success :badge:`badge\` Label`

:label-info:`Info :label-warning:`label in label\` Label`

:label-warning:`Warning :text-info:`text-info\` Label`

:label-danger:`Danger :small:`small\` Label`

.. Note: This is slow, this test runs in approx 188ms
.. other tests with no nested inline parsing run in the 30-60ms range