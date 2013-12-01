use strict;
use warnings;
use Params::Validate qw/:all/;
use Carp::Assert;
use Readonly;

Readonly my $ADDUSER => '/usr/sbin/adduser';
Readonly my $PASSWD => '/usr/bin/passwd';

sub create_user {
  my ( $user ) = validate_pos(@_,{ type => HASHREF });
  my $name = $user->{name};
  assert( $name, "Got a name" );
  my $password = $user->{password} || lc($name);
  my $gecos = $user->{gecos} || '"LPW 2013"';
  my $group = $user->{group} || 'tt_workshop';
  my $home = $user->{home} || "/home/".lc($name);
  
  my $cmd = "$ADDUSER --home $home --gecos $gecos --ingroup $group --disabled-password $name";
  print "$cmd\n";
  system($cmd);

  $cmd = "$PASSWD $name <<!
$password
$password
!";
  system($cmd);
 return 1;
}

for ( my $x=1;$x<=30;$x++){
my $name = sprintf( "tt_workshop%02d", $x );
create_user( { name => $name } );
}

