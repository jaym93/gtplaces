<?php

require "Services/Twilio.php";

$account = getenv("TWILIO_ACCOUNT_SID");
$token = getenv("TWILIO_AUTH_TOKEN");

$client = new Services_Twilio($account, $token);

//print json_encode(array("hey" => "you"));

$calls = $client->account->calls->getList(array("From" => "+15305451766"));

print count($calls) . "\n";

foreach($calls as $call) {
	break;
}


print $call->date_updated . "\n";
print $call->date_created . "\n";

$call = $client->account->calls->get($call->sid);

print $call->sid . "\n";

$call = $client->account->calls->get($call->sid)->update(array(
    "Status" => "345",
));



/*
$filtered_calls = $client->account->calls->filter(array("From" => "+15305451766"));

foreach($filtered_calls as $call) {
    print $call->price . "\n";
	print $call->duration . "\n";
	}*/

$participant = $client->account->conferences
    ->get("CO123")->participants->get("PF123");
