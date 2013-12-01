#! /usr/bin/perl

use strict;
use warnings;
use CGI;
use Template;
use Template::Constants qw/ :debug /;

my $tt = Template->new(
    {
        INCLUDE_PATH => '../../htdocs/tt2/part4',
        WRAPPER => 'wrapper.tt2'
    }
) || die "$Template::ERROR\n";

$tt->process(
    'calendar.tt2',
) || die $tt->error() . "\n";

