#! /usr/bin/perl

use strict;
use Template;
my $tt = Template->new({
        INCLUDE_PATH => '../../htdocs/tt2/part1',
        INTERPOLATE  => 1,
}) || die "$Template::ERROR\n";


my $vars = { debtors => [
   {
        name     => 'Count Edward van Halen',
        debt     => '3 riffs and a solo',
        deadline => 'the next chorus',
   },
   {
        name     => 'Baron Eric Clapton',
        debt     => '1 badge',
        deadline => 'tomorrow',
        final    => 1,
        angry    => 1,
    } 
  ]
};
    
 $tt->process('s4.tt2', $vars)
        || die $tt->error(), "\n";

