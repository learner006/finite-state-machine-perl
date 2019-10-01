use strict;
use 5.010;

my %config;
init_config(\%config);

my $states = $config{'states'};




###########################################################################
# init_config(\%config);
sub init_config
{
	my ($p_config) = @_;

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
}
###########################################################################

