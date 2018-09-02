# txtFormatter

Simple program that allows you to format a txt file into a presentable and pretty text (for documentation for example).

Basic Commands:
```
title('title')
br()
entry('text')
subtitle('subtitle')
content('text')
blockLine()
```

Using these commands give the following output:

```
+------------------------------------------------------------------------------+
|                                     title                                    |
+------------------------------------------------------------------------------+
|                                                                              |
| -> text                                                                      |
|      SUBTITLE:                                                               |
|        text                                                                  |
+------------------------------------------------------------------------------+
```



If you wish to use it similarly as a markup language, you can do that by writing to a <filename>.txt and running:
`python3 parser.py <filename>`

Where filename is the file with the markup commands for the pretty text to be done.

Commands you can use:
```
title
break
block
entry
subtitle
content
```

All commands are followed by the text you wish to prettify.


Things to be done:
- Improve parser to be more friendly to use

