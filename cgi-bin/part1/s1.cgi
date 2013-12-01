#! /usr/bin/perl

use strict;
use Template;
my $tt = Template->new({
        INCLUDE_PATH => '../../htdocs/tt2/part1',
        INTERPOLATE  => 1,
}) || die "$Template::ERROR\n";

my $vars = {
        name     => 'Count Edward van Halen',
        debt     => '3 riffs and a solo',
        deadline => 'the next chorus',
    };
    
 $tt->process('s1.tt2', $vars)
        || die $tt->error(), "\n";

