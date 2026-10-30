# `IOGPUDeviceUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x130` (304 bytes)
- Metaclass: `0xfffffe000b9f4380`; metaclass vtable `0xfffffe0008372c30`; class vtable `0xfffffe0008372630`
- Registration (init): `0xfffffe000a1015e8`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AGXDeviceUserClient`](AGXDeviceUserClient.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (27)

- `IOReturn IOGPUDeviceUserClient::t_signal_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOReturn IOGPUDeviceUserClient::t_signal_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `static IOReturn IOGPUDeviceUserClient::s_submit_command_buffers(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_create_vniodesc(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.struct IOGPUDeviceUserClientPrivate`
- `IOReturn IOGPUDeviceUserClient::t_wait_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_group_add_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_set_io_notification_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn IOGPUDeviceUserClient::t_wait_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOGPUDeviceUserClient`
- `virtual bool IOGPUDeviceUserClient::deviceUserClientStart()`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_perform_io(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_async_signal_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_group_remove_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_query_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_new_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_submit_io_commands(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_try_cancel_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_delete_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_barrier_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUDeviceUserClient`
- `static IOReturn IOGPUDeviceUserClient::s_new_resource(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
