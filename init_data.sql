INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$hsCrtCA4tSvw$1VHFE05Rq5CHBw5Y1BDuwVxPOPGC5ZvS8XX2yA/K8Kc=', NOW(), 1, 'Admin', '', '', 'admin@admin.com', 1, 1, NOW());

INSERT INTO `app_label` (`id`, `name`) VALUES
(1, 'other'),
(2, 'python'),
(3, 'php'),
(4, 'linux');

INSERT INTO `app_article` (`id`, `headline`, `content`, `pub_date`, `reporter_id`, `slug`) VALUES
(1, 'Google code prettify', 'The comments in prettify.js are authoritative but the lexer should work on a number of languages including C and friends, Java, Python, Bash, SQL, HTML, XML, CSS, Javascript, Makefiles, and Rust. It works passably on Ruby, PHP, VB, and Awk and a decent subset of Perl and Ruby, but, because of commenting conventions, but doesn''t work on Smalltalk.\r\n<br>\r\n<br>\r\nTo add the new style to your code snippets you just need to wrap them up using the pre tag and the class "prettyprint".\r\n<xmp class="prettyprint"><pre class="prettyprint">\r\nYour code goes here.\r\n</pre></xmp>\r\nYou might be thinking where are my line numbers?  To do this you need to add the linenums class to to your pre tag, you will also need to use the code tag to wrap your code as follows.\r\n<xmp class="prettyprint linenums"><pre class="prettyprint linenums">\r\n Your code goes here.\r\n</pre></xmp>\r\nTo show HTML/JS code, you need to use xmp tag (you need to remove indentation between "<" and "/xmp>" for closed xmp tag).\r\n<xmp class="prettyprint"><xmp class="prettyprint">\r\n<html>\r\n<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n <meta charset="UTF-8">\r\n <title></title>\r\n</head>\r\n<body>\r\n<script type="text/javascript">\r\n function fib(n) {\r\n   var a = 1, b = 1;\r\n   var tmp;\r\n   while (--n >= 0) {\r\n     tmp = a;\r\n     a += b;\r\n     b = tmp;\r\n   }\r\n   return a;\r\n }\r\n\r\n document.writeln(fib(10));\r\n</script>\r\n</body>\r\n</html>\r\n< /xmp>\r\n</xmp>', NOW(), 1, 'google-code-prettify');

INSERT INTO `app_article_labels` (`id`, `article_id`, `label_id`) VALUES
(1, 1, 1);