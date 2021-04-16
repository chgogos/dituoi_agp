<!-- Sebesta page 218 -->

$day = "Monday";
$month = "January";

function calendar(){
$day = "Tuesday";
global $month;
print "local day is $day ";
$gday = $GLOBALS['day']
print "global day is $gday <br />";
print "global month is $month";

}

calendar()