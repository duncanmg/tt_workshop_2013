#! /usr/bin/perl

use strict;
use warnings;
use CGI;
use Template;

my $tt = Template->new(
    {
        INCLUDE_PATH => '../../htdocs/tt2/part3',
        PRE_PROCESS  => 'macros.tt2'
    }
) || die "$Template::ERROR\n";

$tt->process(
    'macros2.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg' },
            { something => 'pears',  something_else => '2 kg' }
        ]
    }
) || die $tt->error() . "\n";

