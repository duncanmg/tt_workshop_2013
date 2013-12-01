#! /usr/bin/perl

# This relies on Lingua::EN::Numbers::Ordinate being available.

use strict;
use warnings;
use CGI;
use Template;
use Lingua::EN::Numbers::Ordinate qw/ ordinate /;

my $tt = Template->new(
    {
        INCLUDE_PATH => '../../htdocs/tt2/part3',
        PRE_PROCESS  => 'macros.tt2',
        FILTERS => { ord => sub { my ( $num ) = @_; ordinate $num; } } 
    }
) || die "$Template::ERROR\n";

$tt->process(
    'filters.tt2',
    {
        rows => [
            { something => 'apples', something_else => '1 kg' },
            { something => 'pears',  something_else => '2 kg' }
        ]
    }
) || die $tt->error() . "\n";

