#! /usr/bin/perl

# Using a plugin to format currency

use strict;
use warnings;
use CGI;
use Template;

my $tt = Template->new(
    {
        INCLUDE_PATH => "../../htdocs/tt2/part2",
        INTERPOLATE  => 1,
        WRAPPER      => 'wrapper.tt2'
    }
) || die "$Template::ERROR\n";

$tt->process(
    's6a.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg', cost => 5.67 },
            { something => 'pears',  something_else => '2 kg', cost => 3.333333333333333333 },
            { something => 'turnips > pears > grapes',  something_else => '2 & 3 kg', cost => 4.123 },
            { something => '<>peas',  something_else => '2 & 3 kg', cost => 2 },
            { something => 'apricots',  something_else => '2 & 3 kg', cost => 3 },
        ],
        suppliers => [ 'Fred', 'Alan', 'Joe', 'Bert' ]
    }
) || die $tt->error() . "\n";

