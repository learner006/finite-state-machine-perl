use strict;
use 5.010;
use Data::Dumper;

# a config
my %config;
init_config(\%config);

# an event transision rules hash
my %event_transition_rules;
{
	my $states_desc = $config{'states'};
	init_event_transition_rules($states_desc, \%event_transition_rules);
}

my $init_state = $config{'initial'};

# a transition table
my @transition_history;

clearHistory();

=pod
# Tests groud p 1
print getState();
trigger('study');
print getState();

#print Dumper getStates();
#print Dumper @transition_history;
=cut

=pod
# Tests group N 2
say getState();
changeState('busy');
say getState();
trigger('get_tired');
say getState();

changeState('busy');
trigger('get_hungry');
say getState();
=cut

# Tests group N 3
say join(', ' ,getStates('get_hungry'));






###########################################################################
# 'Member' functions
###########################################################################
#
sub getState
{
	my $state = $transition_history[-1];

	return $state;
};
###########################################################################
#
sub clearHistory
{
	@transition_history = ();
	push(@transition_history,$init_state);
}
###########################################################################
#
sub reset
{
	push(@transition_history,$init_state);	
}
###########################################################################
#
sub getStates()
{
	my ($p_transition_rule) = @_;

	

	unless (defined($p_transition_rule) and $p_transition_rule ne '')
	{
		my $states = $config{'states'};
		return keys(%$states);
    }
    else
    {
    	my $t = \%event_transition_rules;
    	if (exists($t->{$p_transition_rule}))
    	{
    		my $state_from = $t->{$p_transition_rule}->{'state_from'};

    		return keys(%$state_from);
    	}
    }
}
###########################################################################
# changeState('busy')
sub changeState
{
	my ($p_new_state) = @_;

	return if ($p_new_state eq getState());

	my @states_list = getStates();

	if (grep(/$p_new_state/, @states_list) )
	{
		push(@transition_history,$p_new_state);
	}
}
###########################################################################
sub trigger
{
	my ($p_event_name) = @_;
	if ( exists($event_transition_rules{$p_event_name}) )
	{
		my $event_transition_desc = $event_transition_rules{$p_event_name};
		my $h = $event_transition_desc;

		my $curr_machine_state = getState();

		# It is possible to do a transition _from_ the current state
		if ( exists($h->{'state_from'}->{$curr_machine_state}) )
		{
			changeState($h->{'state_to_transit'});
		}

	}
}
###########################################################################
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
# init_event_transition_rules($states_desc, \%event_transition_rules);
sub init_event_transition_rules
{
	my ($pin_states_desc, $pout_event_transition_rules) = @_;

	for my $state_name (sort keys %$pin_states_desc)
	{
		# it is a helper line above ;-)		
		# say "state_from: $state_name";
		my $state_transitions = $pin_states_desc->{$state_name}->{'transitions'};
    
		for my $event_name (keys %$state_transitions)
		{
			my $state_to_transit = $state_transitions->{$event_name};
			# it is a helper line above ;-)
			# say "evet_name: $event_name state_to: $state_to_transit";
    
			# There is no $event_name in transition rules.
			# Let's add it! :-)
			unless ( exists $event_transition_rules{$event_name} )
			{
				my %event_desc = (
					state_to_transit => $state_to_transit,
					state_from => {$state_name => 1}
				);
    
				$event_transition_rules{$event_name} = \%event_desc;
			}
			else {
				# We've already added a from state
				# Let's add another from state for the event
				my $t = $event_transition_rules{$event_name}->{'state_from'};
				$t->{$state_name} = 1;
			}
		}
	}

}