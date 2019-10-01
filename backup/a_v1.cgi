use strict;
use 5.010;

my %config = ( a=>1, b=>2 );

say %config;

for(keys(%config))
{
	say "$_  $config{$_}";
}