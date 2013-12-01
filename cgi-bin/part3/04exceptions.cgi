#! /usr/bin/perl

# This relies on Lingua::EN::Numbers::Ordinate being available.

use strict;
use warnings;
use CGI;
use Template;

my $tt = Template->new(
    {
        INCLUDE_PATH => '../../htdocs/tt2/part3',
    }
) || die "$Template::ERROR\n";

$tt->process(
    'exceptions.tt2',
) || die $tt->error() . "\n";

