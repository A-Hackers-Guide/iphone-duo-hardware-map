# `/usr/lib/libmav_ipc_router_dynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 184,224 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 2416)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/libmav_ipc_router_dynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libPCITransport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (77)

```
unknown channel
MAV_ROUTER_MAV_DIAG
v8@?0
router
MAV_ROUTER_HSIC_0
MAV_ROUTER_PCI_1
virtual mav_router_result_t mav_router::device::controller::engage(engage_callback_t)
basic_string
virtual mav_router_result_t mav_router::device::pci_shim::tearDown()
void mav_router::device::pci_shim::setErrorReason_sync(const std::string &)
MAV_ROUTER_QMI_0
MAV_ROUTER_HSIC_3
MAV_ROUTER_HSIC_7
MAV_ROUTER_PCI_0
v28@?0i8^v12^v20
PCI
unknown device
MAV_ROUTER_HSIC_1
mav_router::service::transport_shim::transport_shim(const parameters &)
MAV_ROUTER_DIAG
MAV_ROUTER_HSIC_11
virtual mav_router_result_t mav_router::device::pci_shim::recover()
static void mav_router::service::transport_shim_private::log_write(const unsigned char *, unsigned int)
static void mav_router::service::transport_shim_private::log_received(mav_buffer_t)
MAV_ROUTER_QMI_1
MAV_ROUTER_HSIC_4
v12@?0i8
v24@?0i8^v12I20
/var/wireless/Library/Logs/CoreTelephonyTraceScratch
com.apple.telephony.ipc
device_shim
MAV_ROUTER_PCI_2
virtual mav_router_result_t mav_router::device::pci_shim::engage(dispatch_group_t)_block_invoke
MAV_ROUTER_CTL
MAV_ROUTER_QMI_5
MAV_ROUTER_NULL
. failed on I/O 0x
MAV_ROUTER_NMEA
MAV_ROUTER_HSIC_6
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
void mav_router::device::controller_ios::determine_mappings()
MAV_ROUTER_QMI_3
v16@?0^v8
\n
MAV_ROUTER_QMI_4
MAV_ROUTER_HSIC_5
MAV_ROUTER_HSIC_10
MAV_ROUTER_QMI_2
MAV_ROUTER_HSIC_2
MAV_ROUTER_HSIC_9
virtual mav_router_result_t mav_router::device::pci_shim::enterLowPower()
virtual mav_router_result_t mav_router::device::pci_shim::exitLowPower()
pci error: 
service_shim
mav_router::device::controller_ios::controller_ios(mav_router_weak_ptr_t)
MAV_ROUTER_UART
MAV_ROUTER_HSIC_8
MAV_ROUTER_DUN
virtual mav_router_result_t mav_router::device::pci_shim::handle_transmit(mav_buffer_t)
void mav_router::device::pci_shim::handleError(IOReturn)
bool mav_router::device::pci_shim::init()
virtual mav_router_result_t mav_router::device::pci_shim::engage(dispatch_group_t)
[%04x.%04u.%04u] %s:%u:%s (%u bytes): %.*P
[%04x.%04u.%04u] %s:%u:Number of local QMI instances %u
[%04x.%04u.%04u] %s:%u:engaging
[%04x.%04u.%04u] %s:%u:failed to create mapping of buffer %p
[%04x.%04u.%04u] %s:%u:reason %s
[%04x.%04u.%04u] %s:%u:status %u, arg1 %p, arg2 %p
[%04x.%04u.%04u] %s:%u:invalid interface %u
[%04x.%04u.%04u] %s:%u:mav_router_device_error returned 0x%x
[%04x.%04u.%04u] %s:%u:PCI supported with %u control channels
[%04x.%04u.%04u] %s:%u:Create pci control for interface %u
[%04x.%04u.%04u] %s:%u:service %u
[%04x.%04u.%04u] %s:%u:failed to create pci transport
[%04x.%04u.%04u] %s:%u:got error (%s)
[%04x.%04u.%04u] %s:%u:router %p, device %u
[%04x.%04u.%04u] %s:%u:with channel %s
```
