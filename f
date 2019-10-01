$VAR1 = {
          'busy' => {
                      'transitions' => {
                                         'get_tired' => 'sleeping',
                                         'get_hungry' => 'hungry'
                                       }
                    },
          'normal' => {
                        'transitions' => {
                                           'study' => 'busy'
                                         }
                      },
          'sleeping' => {
                          'transitions' => {
                                             'get_up' => 'normal',
                                             'get_hungry' => 'hungry'
                                           }
                        },
          'hungry' => {
                        'transitions' => {
                                           'eat' => 'normal'
                                         }
                      }
        };
