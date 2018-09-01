# txtFormatter

Simple program that allows you to format a txt file into a presentable and pretty text (for documentation for example)

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

Things to be done:
- Create a grammar and implement a parser that automatically creates this file