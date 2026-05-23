checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook'),
        dict(
            type='MMDetWandbHook',
            init_kwargs=dict(
                project='pest-pvt',
                name='atss_pvtv2_dyhead3_ass_8gpu',
                entity=None,
            ),
            interval=50,
            log_checkpoint=False,
            log_checkpoint_metadata=True,
            num_eval_images=20),
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
