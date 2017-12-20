Heading  :fa:`book`
-------------------

:h1:`Heading 1 Role :fa:`book``

:h1:`Heading 1 Role :fa:`book\` , the space before the command should be removed.`

:h2:`Heading 2 Role :fa:`book``

:h3:`Heading 3 Role :fa:`book``

:h4:`Heading 4 Role :fa:`book``

:h5:`Heading 5 Role :fa:`book``

:h6:`:fa:\`book\` Heading 6 Role`

:h6:`:fa:`book\` Heading 6 Role`

:fa:`book` the whitespace should be collapsed, in the middle :fa:`book` and at the end :fa:`book`

:fa:`book`  the whitespace should not be collapsed, in the middle :fa:`book`  or the end  :fa:`book`

.. Here, we are testing that the space (between "Role" and ":fa:" is collapsed in the HTML
.. If a user wants a space they can add an extra one (use 2 spaces, we only remove 1 space).
.. This allows users to butt up icons right next to the header text
.. If you want a space, add another space (2 - we strip 1 only) - view the Title "Heading  :fa:`book`"
.. The final line tests paragraph, we should be able to use icons everywhere, and spaces should collapse and be readable
.. Notice the extra spaces in the final paragraph.
