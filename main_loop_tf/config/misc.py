import gflags


# Checkpoints
gflags.DEFINE_integer('checkpoints_to_keep', 2, 'The number of checkpoints '
                      'to keep', lower_bound=0)
gflags.DEFINE_integer('checkpoints_save_secs', 0, 'Save every N secs',
                      lower_bound=0)
gflags.DEFINE_integer('checkpoints_save_steps', 500, 'Save every N steps',
                      lower_bound=0)
gflags.DEFINE_string('checkpoints_basedir', 'checkpoints', 'The base path '
                     'where the model checkpoints are stored')
gflags.DEFINE_string('suite_name', '', 'Optional. The name of the set of '
                     'experiments. Ignored if empty string.')
gflags.DEFINE_string('model_name', '', 'Optional. If specified, the '
                     'checkpoints saved on disk will have this name. '
                     'If no name is given it will be replaced by '
                     'a hash of the config flags. The checkpoints will '
                     'be saved in checkpoints_basedir>/<exp_suite>/'
                     '<save_name>_<save_suffix>')
gflags.DEFINE_string('model_suffix', '', 'Optional. If specified, this '
                     'suffix will be concatenated to the name of the '
                     'model.')
gflags.DEFINE_string('restore_suite', '', 'Optional. The name of the suite '
                     'of the experiment to be restored. Ignored if empty '
                     'string.')
gflags.DEFINE_string('restore_model', 'True', 'It can be the name of the '
                     'model you want to relaod, True (string) if you '
                     'want to reload the experiment with the default hash '
                     'generated by the list of flags, or False/None if '
                     'you dont want to restore the model')
gflags.DEFINE_list('devices', None, 'A list of devices to use. If None '
                   'it will be inferred from the CUDA_VISIBLE_DEVICES '
                   'environment variable')
gflags.DEFINE_integer('random_seed', 8112017, 'Fixed random seed for '
                      'both tensorflow and numpy')

# Other flags we might want to define (see also config/flow.py):
# See https://www.tensorflow.org/versions/r0.10/tutorials/monitors/
#                customizing_the_evaluation_metrics
# metrics=[],  # TODO add additional metrics
# val_metrics=['dice_loss', 'acc', 'jaccard'],
# TODO parametrize according to which metric to save the model (best val loss?)
