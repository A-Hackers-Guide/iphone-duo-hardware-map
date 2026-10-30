# Kernel MIG subsystems and routines (ipsw kernel mig)

From `kernelcache.release.v6x-pandia`, Darwin 27.2.0, `xnu-13432.52.2~7/RELEASE_ARM64_T8160`. These are the kernel's entry points from userland. **[KC]**

```
   • Found                     mig_kern_subsystem table=0xfffffe000b78cb58
0xfffffe000ace0afc: mach_vm_subsystem                                     start=4800 end=4830 max_sz=8240
    0xfffffe000ace0a04: _Xmach_vm_allocate_external                       num=4800 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ace094c: _Xmach_vm_deallocate                              num=4801 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace0874: _Xmach_vm_protect                                 num=4802 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace079c: _Xmach_vm_inherit                                 num=4803 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace0660: _Xmach_vm_read                                    num=4804 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ace058c: _Xmach_vm_read_list                               num=4805 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=4140
    0xfffffe000ace0480: _Xmach_vm_write                                   num=4806 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace03e8: _Xmach_vm_copy                                    num=4807 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace0324: _Xmach_vm_read_overwrite                          num=4808 impl=0x0 argc=08 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ace0274: _Xmach_vm_msync                                   num=4809 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace01dc: _Xmach_vm_behavior_set                            num=4810 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace0018: _Xmach_vm_map_external                            num=4811 impl=0x0 argc=14 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdff30: _Xmach_vm_machine_attribute                       num=4812 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdfda0: _Xmach_vm_remap_external                          num=4813 impl=0x0 argc=14 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdfc88: _Xmach_vm_page_query                              num=4814 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdfb80: _Xmach_vm_region_recurse                          num=4815 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=152
    0xfffffe000acdfa30: _Xmach_vm_region                                  num=4816 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=120
    0xfffffe000acdf898: _X_mach_make_memory_entry                         num=4817 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=68
    0xfffffe000acdf7e4: _Xmach_vm_purgable_control_external               num=4818 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdf6e8: _Xmach_vm_page_info                               num=4819 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=176
    0xfffffe000acdf61c: _Xmach_vm_page_range_query                        num=4820 impl=0x0 argc=08 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdf4c4: _Xmach_vm_remap_new_external                      num=4821 impl=0x0 argc=14 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdf3c0: _Xmach_vm_deferred_reclamation_buffer_init        num=4822 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdf29c: _Xmach_vm_deferred_reclamation_buffer_synchronize num=4823 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdf1dc: _Xmach_vm_range_create                            num=4825 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdf0b8: <unknown>                                         num=4826 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdef94: <unknown>                                         num=4827 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=8240
    0xfffffe000acdeea8: <unknown>                                         num=4828 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000acdedc8: <unknown>                                         num=4829 impl=0x0 argc=12 descr=0 reply_descr=0 max_reply_msg=52

0xfffffe000acded7c: mach_port_subsystem                           start=3200 end=3243 max_sz=576
    0xfffffe000acdec0c: _Xmach_port_names                         num=3200 impl=0x0 argc=05 descr=0 reply_descr=2 max_reply_msg=84
    0xfffffe000acdeb14: _Xmach_port_type                          num=3201 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdea18: _Xmach_port_allocate_name                 num=3203 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde90c: _Xmach_port_allocate                      num=3204 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acde848: _Xmach_port_destroy                       num=3205 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde784: _Xmach_port_deallocate                    num=3206 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde68c: _Xmach_port_get_refs                      num=3207 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acde5c4: _Xmach_port_mod_refs                      num=3208 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde488: _Xmach_port_peek                          num=3209 impl=0x0 argc=08 descr=0 reply_descr=0 max_reply_msg=128
    0xfffffe000acde3c4: _Xmach_port_set_mscount                   num=3210 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde2d4: _Xmach_port_get_set_status_from_user      num=3211 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acde210: _Xmach_port_move_member                   num=3212 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acde088: _Xmach_port_request_notification          num=3213 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acddf38: _Xmach_port_insert_right                  num=3214 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdddac: _Xmach_port_extract_right                 num=3215 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acddce8: _Xmach_port_set_seqno                     num=3216 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acddc20: _Xmach_port_get_attributes_from_user      num=3217 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=116
    0xfffffe000acddb2c: _Xmach_port_set_attributes                num=3218 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdda14: _Xmach_port_allocate_qos                  num=3219 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000acdd890: _Xmach_port_allocate_full                 num=3220 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000acdd7d8: _Xtask_set_port_space                     num=3221 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdd6e0: _Xmach_port_get_srights                   num=3222 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdd5a8: _Xmach_port_space_info_from_user          num=3223 impl=0x0 argc=06 descr=0 reply_descr=2 max_reply_msg=108
    0xfffffe000acdd4ac: _Xmach_port_dnrequest_info                num=3224 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdd3e8: _Xmach_port_insert_member                 num=3226 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdd324: _Xmach_port_extract_member                num=3227 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdd28c: _Xmach_port_get_context_from_user         num=3228 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdd1c4: _Xmach_port_set_context                   num=3229 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdd124: _Xmach_port_kobject_from_user             num=3230 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000acdcfc4: _Xmach_port_construct                     num=3231 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdcefc: _Xmach_port_destruct                      num=3232 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdce30: _Xmach_port_guard                         num=3233 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdcd68: _Xmach_port_unguard                       num=3234 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdcc78: _Xmach_port_space_basic_info              num=3235 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=68
    0xfffffe000acdcb8c: _Xmach_port_special_reply_port_reset_link num=3236 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acdcac0: _Xmach_port_guard_with_flags              num=3237 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdc9f4: _Xmach_port_swap_guard                    num=3238 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdc91c: _Xmach_port_kobject_description_from_user num=3239 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=576
    0xfffffe000acdc824: _Xmach_port_is_connection_for_service     num=3240 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdc72c: _Xmach_port_get_service_port_info         num=3241 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=300
    0xfffffe000acdc638: _Xmach_port_assert_attributes             num=3242 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000acdc5ec: mach_host_subsystem                      start=200 end=236 max_sz=1072
    0xfffffe000acdc520: _Xhost_info                          num=200 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=320
    0xfffffe000acdc438: _Xhost_kernel_version                num=201 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=564
    0xfffffe000acdc398: _Xhost_page_size                     num=202 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acdc26c: _Xmach_memory_object_memory_entry    num=203 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdc178: _Xhost_processor_info                num=204 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=68
    0xfffffe000acdc0b4: _Xhost_get_io_main                   num=205 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdbfbc: _Xhost_get_clock_service             num=206 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdbeec: _Xkmod_get_info                      num=207 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acdbe78: _Xhost_virtual_physical_table_info   num=209 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acdbda8: _Xprocessor_set_default              num=213 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdbc7c: _Xmach_memory_object_memory_entry_64 num=215 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdbbb0: _Xhost_statistics_from_user          num=216 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=320
    0xfffffe000acdbae4: _Xhost_request_notification          num=217 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdba70: _Xhost_lockgroup_info                num=218 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acdb9a4: _Xhost_statistics64_from_user        num=219 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=1072
    0xfffffe000acdb874: _Xmach_zone_info                     num=220 impl=0x0 argc=05 descr=0 reply_descr=2 max_reply_msg=84
    0xfffffe000acdb7fc: _Xmach_zone_force_gc                 num=221 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdb6d8: _Xhost_create_mach_voucher           num=222 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acdb660: _Xhost_set_atm_diagnostic_flag       num=225 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdb4e8: _Xmach_memory_info                   num=227 impl=0x0 argc=07 descr=0 reply_descr=3 max_reply_msg=104
    0xfffffe000acdb44c: _Xhost_set_multiuser_config_flags    num=228 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdb358: _Xmach_zone_info_for_zone            num=231 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=108
    0xfffffe000acdb2bc: _Xmach_zone_info_for_largest_zone    num=232 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=188
    0xfffffe000acdb248: _Xmach_zone_get_zlog_zones           num=233 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acdb1d4: _Xmach_zone_get_btlog_records        num=234 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acdb048: <unknown>                            num=235 impl=0x0 argc=07 descr=0 reply_descr=3 max_reply_msg=104

0xfffffe000acd9eac: host_priv_subsystem                   start=400 end=426 max_sz=4148
    0xfffffe000acd9dbc: _Xhost_get_boot_info              num=400 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=4148
    0xfffffe000acd9d24: _Xhost_reboot                     num=401 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd9c58: _Xhost_priv_statistics            num=402 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=320
    0xfffffe000acd9b20: _Xhost_default_memory_manager     num=403 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acd99e0: _Xvm_wire                         num=404 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd9880: _Xthread_wire                     num=405 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd9790: _Xhost_processors                 num=407 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acd96c4: _Xhost_get_special_port_from_user num=412 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acd95f8: _Xhost_set_special_port_from_user num=413 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd9524: _Xhost_set_exception_ports        num=414 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd9224: _Xhost_get_exception_ports        num=415 impl=0x0 argc=07 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000acd8ecc: _Xhost_swap_exception_ports       num=416 impl=0x0 argc=10 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000acd8d8c: _Xmach_vm_wire_external           num=418 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd8c9c: _Xhost_processor_sets             num=419 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acd8b04: _Xhost_processor_set_priv         num=420 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acd8a70: _Xhost_set_UNDServer              num=423 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd8a00: _Xhost_get_UNDServer              num=424 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acd8884: _Xkext_request                    num=425 impl=0x0 argc=09 descr=0 reply_descr=2 max_reply_msg=88

0xfffffe000acd7a68: clock_subsystem            start=1000 end=1003 max_sz=52
    0xfffffe000acd7988: _Xclock_get_time       num=1000 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acd7874: _Xclock_get_attributes num=1001 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acd7774: _Xclock_alarm          num=1002 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000ace8a1c: processor_subsystem             start=3000 end=3006 max_sz=144
    0xfffffe000ace8970: _Xprocessor_start_from_user num=3000 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace88c4: _Xprocessor_exit_from_user  num=3001 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace876c: _Xprocessor_info            num=3002 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=144
    0xfffffe000ace86b8: _Xprocessor_control         num=3003 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace8658: _Xprocessor_assign          num=3004 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace854c: _Xprocessor_get_assignment  num=3005 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52

0xfffffe000ace8f40: processor_set_subsystem               start=4000 end=4011 max_sz=84
    0xfffffe000ace8e24: _Xprocessor_set_statistics        num=4000 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=68
    0xfffffe000ace8d00: _Xprocessor_set_tasks             num=4005 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ace8b9c: _Xprocessor_set_info              num=4009 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=84
    0xfffffe000ace8a68: _Xprocessor_set_tasks_with_flavor num=4010 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=64

0xfffffe000ad9bb94: is_iokit_subsystem                               start=2800 end=2892 max_sz=4296
    0xfffffe000ad9baac: _Xio_object_get_class                        num=2800 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad9b984: _Xio_object_conforms_to                      num=2801 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad9b84c: _Xio_iterator_next                           num=2802 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9b744: _Xio_iterator_reset                          num=2803 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9b680: _Xio_service_get_matching_services           num=2804 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9b51c: _Xio_registry_entry_get_property             num=2805 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad9b3ac: _Xio_registry_create_iterator                num=2806 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9b314: _Xio_registry_iterator_enter_entry           num=2807 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9b27c: _Xio_registry_iterator_exit_entry            num=2808 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9b128: _Xio_registry_entry_from_path                num=2809 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9b040: _Xio_registry_entry_get_name                 num=2810 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad9afb0: _Xio_registry_entry_get_properties           num=2811 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad9ae58: _Xio_registry_entry_get_property_bytes       num=2812 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ad9acd4: _Xio_registry_entry_get_child_iterator       num=2813 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9ab50: _Xio_registry_entry_get_parent_iterator      num=2814 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9a91c: _Xio_service_open                            num=2815 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=4160
    0xfffffe000ad9a884: _Xio_service_close                           num=2816 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9a74c: _Xio_connect_get_service                     num=2817 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9a644: _Xio_connect_set_notification_port           num=2818 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9a470: _Xio_connect_map_memory                      num=2819 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ad9a2f8: _Xio_connect_add_client                      num=2820 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9a1bc: _Xio_connect_set_properties                  num=2821 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad9a08c: _Xio_connect_method_scalarI_scalarO          num=2822 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=112
    0xfffffe000ad99f58: _Xio_connect_method_scalarI_structureO       num=2823 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ad99e3c: _Xio_connect_method_scalarI_structureI       num=2824 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad99ccc: _Xio_connect_method_structureI_structureO    num=2825 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ad99b74: _Xio_registry_entry_get_path                 num=2826 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=564
    0xfffffe000ad99a48: _Xio_registry_get_root_entry                 num=2827 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad9990c: _Xio_registry_entry_set_properties           num=2828 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad997e8: _Xio_registry_entry_in_plane                 num=2829 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad996fc: _Xio_object_get_retain_count                 num=2830 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad995c0: _Xio_service_get_busy_state                  num=2831 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad99518: _Xio_service_wait_quiet                      num=2832 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad99374: _Xio_registry_entry_create_iterator          num=2833 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad99240: _Xio_iterator_is_valid                       num=2834 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad99150: _Xio_catalog_send_data                       num=2836 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad99054: _Xio_catalog_terminate                       num=2837 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad98fa4: _Xio_catalog_get_data                        num=2838 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad98f28: _Xio_catalog_get_gen_count                   num=2839 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad98e34: _Xio_catalog_module_loaded                   num=2840 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad98d84: _Xio_catalog_reset                           num=2841 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad98c6c: _Xio_service_request_probe                   num=2842 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad98b14: _Xio_registry_entry_get_name_in_plane        num=2843 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad98a04: _Xio_service_match_property_table            num=2844 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad98824: _Xio_async_method_scalarI_scalarO            num=2845 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=112
    0xfffffe000ad98640: _Xio_async_method_scalarI_structureO         num=2846 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ad98484: _Xio_async_method_scalarI_structureI         num=2847 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9829c: _Xio_async_method_structureI_structureO      num=2848 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ad98118: _Xio_service_add_notification                num=2849 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad97f20: _Xio_service_add_interest_notification       num=2850 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad97df4: _Xio_service_acknowledge_notification        num=2851 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad97ce4: _Xio_connect_get_notification_semaphore      num=2852 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad97b48: _Xio_connect_unmap_memory                    num=2853 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad979f0: _Xio_registry_entry_get_location_in_plane    num=2854 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad97810: _Xio_registry_entry_get_property_recursively num=2855 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad9773c: _Xio_service_get_state                       num=2856 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=64
    0xfffffe000ad97600: _Xio_service_get_matching_services_ool       num=2857 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad974c0: _Xio_service_match_property_table_ool        num=2858 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ad972a0: _Xio_service_add_notification_ool            num=2859 impl=0x0 argc=09 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad97184: _Xio_object_get_superclass                   num=2860 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad97068: _Xio_object_get_bundle_identifier            num=2861 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=180
    0xfffffe000ad96e60: _Xio_service_open_extended                   num=2862 impl=0x0 argc=08 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad96ca0: _Xio_connect_map_memory_into_task            num=2863 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000ad96b00: _Xio_connect_unmap_memory_from_task          num=2864 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad968d4: _Xio_connect_method                          num=2865 impl=0x0 argc=17 descr=0 reply_descr=0 max_reply_msg=4284
    0xfffffe000ad965e8: _Xio_connect_async_method                    num=2866 impl=0x0 argc=20 descr=0 reply_descr=0 max_reply_msg=4284
    0xfffffe000ad964e0: _Xio_connect_set_notification_port_64        num=2867 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9635c: _Xio_service_add_notification_64             num=2868 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad96164: _Xio_service_add_interest_notification_64    num=2869 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad95f44: _Xio_service_add_notification_ool_64         num=2870 impl=0x0 argc=09 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad95e14: _Xio_registry_entry_get_registry_entry_id    num=2871 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ad95ba4: _Xio_connect_method_var_output               num=2872 impl=0x0 argc=16 descr=0 reply_descr=1 max_reply_msg=4296
    0xfffffe000ad95ae0: _Xio_service_get_matching_service            num=2873 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad959a4: _Xio_service_get_matching_service_ool        num=2874 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad958d8: _Xio_service_get_authorization_id            num=2875 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ad957f0: _Xio_service_set_authorization_id            num=2876 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad95798: _Xio_server_version                          num=2877 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000ad95680: _Xio_registry_entry_get_properties_bin       num=2878 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad95498: _Xio_registry_entry_get_property_bin         num=2879 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad95358: _Xio_service_get_matching_service_bin        num=2880 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad95218: _Xio_service_get_matching_services_bin       num=2881 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad95104: _Xio_service_match_property_table_bin        num=2882 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad94f00: _Xio_service_add_notification_bin            num=2883 impl=0x0 argc=08 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad94cfc: _Xio_service_add_notification_bin_64         num=2884 impl=0x0 argc=08 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ad94b4c: _Xio_registry_entry_get_path_ool             num=2885 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=4168
    0xfffffe000ad949a0: _Xio_registry_entry_from_path_ool            num=2886 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000ad948b8: _Xio_device_tree_entry_exists_with_name      num=2887 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ad9478c: _Xio_registry_entry_get_properties_bin_buf   num=2888 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=72
    0xfffffe000ad94594: _Xio_registry_entry_get_property_bin_buf     num=2889 impl=0x0 argc=09 descr=0 reply_descr=1 max_reply_msg=72
    0xfffffe000ad944e8: _Xio_service_wait_quiet_with_options         num=2890 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ad9438c: <unknown>                                    num=2891 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=208

0xfffffe000acec9b0: task_subsystem                                   start=3400 end=3466 max_sz=5232
    0xfffffe000acec8e8: _Xtask_terminate                             num=3401 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acec7fc: _Xtask_threads_from_user                     num=3402 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acec6c4: _X_kernelrpc_mach_ports_register3            num=3403 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acec568: _X_kernelrpc_mach_ports_lookup3              num=3404 impl=0x0 argc=04 descr=0 reply_descr=3 max_reply_msg=84
    0xfffffe000acec4a4: _Xtask_info_from_user                        num=3405 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=424
    0xfffffe000acec3b4: _Xtask_set_info                              num=3406 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acec308: _Xtask_suspend                               num=3407 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acec25c: _Xtask_resume                                num=3408 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acec198: _Xtask_get_special_port_from_user            num=3409 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acec088: _Xtask_set_special_port_from_user            num=3410 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acebf40: _Xthread_create_from_user                    num=3411 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acebdd0: _Xthread_create_running_from_user            num=3412 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acebcb8: _Xtask_set_exception_ports                   num=3413 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceb9b8: _Xtask_get_exception_ports_from_user         num=3414 impl=0x0 argc=07 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000aceb618: _Xtask_swap_exception_ports                  num=3415 impl=0x0 argc=10 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000aceb4f8: _Xsemaphore_create                           num=3418 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000aceb3a0: _Xsemaphore_destroy                          num=3419 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceb2bc: _Xtask_policy_set                            num=3420 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceb19c: _Xtask_policy_get                            num=3421 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=116
    0xfffffe000aceb080: _Xtask_get_state                             num=3433 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=5232
    0xfffffe000aceaf88: _Xtask_set_state                             num=3434 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceae70: _Xtask_set_phys_footprint_limit              num=3435 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acead54: _Xtask_suspend2_mig                          num=3436 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000aceace4: _Xtask_resume2_mig                           num=3437 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceabfc: _Xtask_purgable_info                         num=3438 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=316
    0xfffffe000aceab08: _Xtask_get_mach_voucher                      num=3439 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acea960: _Xtask_set_mach_voucher                      num=3440 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acea7b8: _Xtask_swap_mach_voucher                     num=3441 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acea6ac: _Xtask_generate_corpse                       num=3442 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acea4c8: _Xtask_map_corpse_info                       num=3443 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000acea388: _Xtask_register_dyld_image_infos             num=3444 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acea248: _Xtask_unregister_dyld_image_infos           num=3445 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acea1a8: _Xtask_get_dyld_image_infos                  num=3446 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acea0a4: _Xtask_register_dyld_shared_cache_image_info num=3447 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acea000: _Xtask_register_dyld_set_dyld_state          num=3448 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace9f34: _Xtask_register_dyld_get_process_state       num=3449 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=116
    0xfffffe000ace9d70: _Xtask_map_corpse_info_64                    num=3450 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000ace9c54: _Xtask_inspect                               num=3451 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=64
    0xfffffe000ace9b80: _Xtask_get_exc_guard_behavior                num=3452 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ace9aa8: _Xtask_set_exc_guard_behavior                num=3453 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace99bc: _Xmach_task_is_self                          num=3455 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ace98b4: _Xtask_dyld_process_info_notify_register     num=3456 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace9798: _Xtask_create_identity_token                 num=3457 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ace96b4: _Xtask_identity_token_get_task_port          num=3458 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ace95f8: _Xtask_dyld_process_info_notify_deregister   num=3459 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace9458: _Xtask_get_exception_ports_info              num=3460 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=688
    0xfffffe000ace9388: _Xtask_test_sync_upcall                      num=3461 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace92e4: _Xtask_set_corpse_forking_behavior           num=3462 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace9214: _Xtask_test_async_upcall_propagation         num=3463 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace90a0: _Xtask_map_kcdata_object_64                  num=3464 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=60
    0xfffffe000ace8f8c: _Xtask_register_hardened_exception_handler   num=3465 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000aceeba0: thread_act_subsystem                       start=3600 end=3634 max_sz=5232
    0xfffffe000aceead0: _Xthread_terminate_from_user           num=3600 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee9ac: _Xact_get_state_to_user                num=3601 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=5232
    0xfffffe000acee898: _Xact_set_state_from_user              num=3602 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee77c: _Xthread_get_state_to_user             num=3603 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=5232
    0xfffffe000acee680: _Xthread_set_state_from_user           num=3604 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee5d8: _Xthread_suspend                       num=3605 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee530: _Xthread_resume                        num=3606 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee488: _Xthread_abort                         num=3607 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee3e0: _Xthread_abort_safely                  num=3608 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee338: _Xthread_depress_abort_from_user       num=3609 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee274: _Xthread_get_special_port_from_user    num=3610 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acee148: _Xthread_set_special_port              num=3611 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acee030: _Xthread_info                          num=3612 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=176
    0xfffffe000acedf20: _Xthread_set_exception_ports           num=3613 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acedc20: _Xthread_get_exception_ports_from_user num=3614 impl=0x0 argc=07 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000aced878: _Xthread_swap_exception_ports          num=3615 impl=0x0 argc=10 descr=0 reply_descr=32 max_reply_msg=944
    0xfffffe000aced78c: _Xthread_policy                        num=3616 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aced6a8: _Xthread_policy_set                    num=3617 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aced580: _Xthread_policy_get                    num=3618 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=116
    0xfffffe000aced3b8: _Xthread_set_policy                    num=3624 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aced2a8: _Xthread_get_mach_voucher              num=3625 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000aced10c: _Xthread_set_mach_voucher              num=3626 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acecf74: _Xthread_swap_mach_voucher             num=3627 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acece14: _Xthread_convert_thread_state          num=3628 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=5232
    0xfffffe000acecc74: _Xthread_get_exception_ports_info      num=3630 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=688
    0xfffffe000acecb68: _Xthread_adopt_exception_handler       num=3631 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceca68: <unknown>                              num=3632 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000acec9fc: <unknown>                              num=3633 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000acf09dc: vm32_map_subsystem         start=3800 end=3834 max_sz=2092
    0xfffffe000acf085c: _Xregion               num=3800 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=112
    0xfffffe000acf0758: _Xallocate             num=3801 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acf0680: _Xdeallocate           num=3802 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acf059c: _Xprotect              num=3803 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acf04b8: _Xinherit              num=3804 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acf038c: _Xread                 num=3805 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acf01ac: _Xread_list            num=3806 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=2092
    0xfffffe000acf00a0: _Xwrite                num=3807 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acf0008: _Xcopy                 num=3808 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceff30: _Xread_overwrite       num=3809 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acefe80: _Xmsync                num=3810 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acefddc: _Xbehavior_set         num=3811 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acefc48: _Xmap                  num=3812 impl=0x0 argc=11 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acefb5c: _Xmachine_attribute    num=3813 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000acef9c0: _Xremap                num=3814 impl=0x0 argc=11 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000acef938: _X_task_wire           num=3815 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acef794: _Xmake_memory_entry    num=3816 impl=0x0 argc=06 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acef67c: _Xmap_page_query       num=3817 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=52
    0xfffffe000acef604: _Xregion_info          num=3818 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=104
    0xfffffe000acef58c: _Xmapped_pages_info    num=3819 impl=0x0 argc=03 descr=0 reply_descr=1 max_reply_msg=64
    0xfffffe000acef488: _Xregion_recurse       num=3821 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=144
    0xfffffe000acef35c: _Xregion_recurse_64    num=3822 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=144
    0xfffffe000acef2e4: _Xregion_info_64       num=3823 impl=0x0 argc=05 descr=0 reply_descr=1 max_reply_msg=108
    0xfffffe000acef17c: _Xregion_64            num=3824 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=112
    0xfffffe000aceefe4: _Xmake_memory_entry_64 num=3825 impl=0x0 argc=07 descr=0 reply_descr=1 max_reply_msg=68
    0xfffffe000aceee4c: _Xmap_64               num=3826 impl=0x0 argc=12 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000aceed68: _Xpurgable_control     num=3830 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000aceece4: _X_map_exec_lockdown   num=3831 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000aceebec: <unknown>              num=3833 impl=0x0 argc=08 descr=0 reply_descr=0 max_reply_msg=48

0xfffffe000ace1118: mach_voucher_subsystem                      start=5400 end=5405 max_sz=5168
    0xfffffe000ace0ffc: _Xmach_voucher_extract_attr_content     num=5400 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ace0ee0: _Xmach_voucher_extract_attr_recipe      num=5401 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ace0dc8: _Xmach_voucher_extract_all_attr_recipes num=5402 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=5168
    0xfffffe000ace0c60: _Xmach_voucher_attr_command             num=5403 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=4144
    0xfffffe000ace0b4c: _Xmach_voucher_debug_info               num=5404 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=5168

0xfffffe000ace14c0: memory_entry_subsystem                      start=4900 end=4905 max_sz=148
    0xfffffe000ace13f8: _Xmach_memory_entry_purgable_control    num=4900 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=48
    0xfffffe000ace1390: _Xmach_memory_entry_access_tracking     num=4901 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=56
    0xfffffe000ace12d8: _Xmach_memory_entry_ownership_from_user num=4902 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace123c: <unknown>                               num=4903 impl=0x0 argc=04 descr=0 reply_descr=0 max_reply_msg=68
    0xfffffe000ace1168: <unknown>                               num=4904 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=148

0xfffffe000ace1a4c: task_restartable_subsystem                start=8000 end=8002 max_sz=44
    0xfffffe000ace195c: _Xtask_restartable_ranges_register    num=8000 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000ace18b0: _Xtask_restartable_ranges_synchronize num=8001 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000acd840c: catch_exc_subsystem                  start=2401 end=2404 max_sz=5236
    0xfffffe000acd82f4: _Xexception_raise                num=2401 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd824c: _Xexception_raise_state          num=2402 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=5236
    0xfffffe000acd8170: _Xexception_raise_state_identity num=2403 impl=0x0 argc=11 descr=0 reply_descr=0 max_reply_msg=5236

0xfffffe000acdaffc: catch_mach_exc_subsystem                            start=2405 end=2411 max_sz=5236
    0xfffffe000acdaee4: _Xmach_exception_raise                          num=2405 impl=0x0 argc=06 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdae3c: _Xmach_exception_raise_state                    num=2406 impl=0x0 argc=09 descr=0 reply_descr=0 max_reply_msg=5236
    0xfffffe000acdad60: _Xmach_exception_raise_state_identity           num=2407 impl=0x0 argc=11 descr=0 reply_descr=0 max_reply_msg=5236
    0xfffffe000acdaccc: _Xmach_exception_raise_identity_protected       num=2408 impl=0x0 argc=07 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdac38: _Xmach_exception_raise_backtrace                num=2409 impl=0x0 argc=05 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acdab6c: _Xmach_exception_raise_state_identity_protected num=2410 impl=0x0 argc=12 descr=0 reply_descr=0 max_reply_msg=5236

0xfffffe000acd8834: mach_eventlink_subsystem          start=716200 end=716204 max_sz=68
    0xfffffe000acd86d0: _Xmach_eventlink_create       num=716200 impl=0x0 argc=03 descr=0 reply_descr=2 max_reply_msg=68
    0xfffffe000acd8654: _Xmach_eventlink_destroy      num=716201 impl=0x0 argc=01 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd84e4: _Xmach_eventlink_associate    num=716202 impl=0x0 argc=11 descr=0 reply_descr=0 max_reply_msg=44
    0xfffffe000acd8458: _Xmach_eventlink_disassociate num=716203 impl=0x0 argc=02 descr=0 reply_descr=0 max_reply_msg=44

0xfffffe000ace84fc: SubsystemStart(866900) start=866900 end=866903 max_sz=1072
    0xfffffe000ace83ac: <unknown>          num=866900 impl=0x0 argc=04 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ace8290: <unknown>          num=866901 impl=0x0 argc=02 descr=0 reply_descr=1 max_reply_msg=52
    0xfffffe000ace8150: <unknown>          num=866902 impl=0x0 argc=03 descr=0 reply_descr=0 max_reply_msg=1072

```
