# `Core_Audio_Driver_Protocol` (protocol)

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[Core_Audio_Driver_Protocol abort_device_configuration_change:action:change:reply:];
-[Core_Audio_Driver_Protocol is_property_settable:reply:];
-[Core_Audio_Driver_Protocol retain_reply_for_process_boost:];
-[Core_Audio_Driver_Protocol start_io:client_id:reply:];
-[Core_Audio_Driver_Protocol start_synchronous_messenger:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:reply:];
-[Core_Audio_Driver_Protocol unregister_io_buffer:reply:];
-[Core_Audio_Driver_Protocol get_property_data:qualifier:data_size:reply:];
-[Core_Audio_Driver_Protocol stop_synchronous_messenger:client_id:reply:];
-[Core_Audio_Driver_Protocol set_property_data:qualifier:data:reply:];
-[Core_Audio_Driver_Protocol create_device:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver_Protocol stop_io:client_id:reply:];
-[Core_Audio_Driver_Protocol get_property_data_size:qualifier:reply:];
-[Core_Audio_Driver_Protocol has_property:reply:];
-[Core_Audio_Driver_Protocol add_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver_Protocol destroy_device:reply:];
-[Core_Audio_Driver_Protocol initialize:reply:];
-[Core_Audio_Driver_Protocol register_io_buffer:reply:];
-[Core_Audio_Driver_Protocol remove_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver_Protocol object_was_destroyed:reply:];
-[Core_Audio_Driver_Protocol perform_device_configuration_change:action:change:reply:];
```
