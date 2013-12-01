#! /usr/bin/perl

use strict;
use warnings;
use CGI;
use Template;
use Template::Constants qw/ :debug /;

my $tt = Template->new(
    {
        INCLUDE_PATH => '../../htdocs/tt2/part3',
        DEBUG => DEBUG_DIRS
    }
) || die "$Template::ERROR\n";

$tt->process(
    'debugging.tt2',
) || die $tt->error() . "\n";

