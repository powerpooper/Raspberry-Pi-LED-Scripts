<?php

$newvar = $_GET["newvar"];

switch ($newvar) {
case "off":
	exec('bash /usr/lib/cgi-bin/halloween.sh off > /dev/null 2>&1 &');
	break;
case "on":
	exec('bash /usr/lib/cgi-bin/halloween.sh on > /dev/null 2>&1 &');
	break;
}

?>
