#! /usr/bin/perl

use strict;
use warnings;
use CGI;
use Template;

# Using a wrapper.

my $tt = Template->new(
    {
        INCLUDE_PATH => "../../htdocs/tt2/part2",
        INTERPOLATE  => 1,
        WRAPPER      => 'wrapper.tt2'
    }
) || die "$Template::ERROR\n";

$tt->process(
    's2.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg' },
            { something => 'pears',  something_else => '2 kg' }
        ]
    }
) || die $tt->error() . "\n";

