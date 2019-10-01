use strict;
use 5.010;

my %config;
init_config(\%config);

# Let's fill an event transision rules table! :-)
my %event_transition_rules;

my $states = $config{'states'};
say $states;

for my $state_name (sort keys %$states)
{
	say "state_from: $state_name";
	my $state_transitions = $states->{$state_name}->{'transitions'};

	for my $event_name (keys %$state_transitions)
	{
		my $state_to_transit = $state_transitions->{$event_name};
		say "evet_name: $event_name state_to: $state_to_transit";
	}

	say;
}





###########################################################################
# init_config(\%config);
sub init_config
{
	my ($pout_config) = @_;

	my %config = (
		initial => 'normal',
		states => {
			normal => {
				transitions => {
					study => 'busy'
				}
			},
            busy => {
                transitions => {
                    get_tired => 'sleeping',
                    get_hungry => 'hungry'
                }
            },
            hungry => {
                transitions => {
                    eat => 'normal'
                }
            },
            sleeping => {
                transitions => {
                    get_hungry => 'hungry',
                    get_up => 'normal'
                }
            }
		}
	);

	%$pout_config = %config;
}
###########################################################################

