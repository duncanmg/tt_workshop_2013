#! /usr/bin/perl

# Header and footer will be the same on all pages %]

use strict;
use warnings;
use CGI;
use Template;

my $tt = Template->new(
    {
        INCLUDE_PATH => "../../htdocs/tt2/part2",
        INTERPOLATE  => 1,
    }
) || die "$Template::ERROR\n";

$tt->process(
    's1.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg' },
            { something => 'pears',  something_else => '2 kg' }
        ]
    }
) || die $tt->error() . "\n";

