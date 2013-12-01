#! /usr/bin/perl

# Using a vmethod to do a simple sort on a select list.

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
    's5.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg' },
            { something => 'pears',  something_else => '2 kg' },
            { something => 'turnips > pears > grapes',  something_else => '2 & 3 kg' },
            { something => '<>peas',  something_else => '2 & 3 kg' },
            { something => 'apricots',  something_else => '2 & 3 kg' },
        ],
        suppliers => [ 'Fred', 'Alan', 'Joe', 'Bert' ]
    }
) || die $tt->error() . "\n";

