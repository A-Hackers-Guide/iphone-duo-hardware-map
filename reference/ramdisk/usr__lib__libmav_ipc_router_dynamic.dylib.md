# `/usr/lib/libmav_ipc_router_dynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 184,224 bytes.

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
MAV_ROUTER_UART
MAV_ROUTER_QMI_5
MAV_ROUTER_HSIC_9
service_shim
PCI
MAV_ROUTER_HSIC_2
virtual mav_router_result_t mav_router::device::controller::engage(engage_callback_t)
/var/wireless/Library/Logs/CoreTelephonyTraceScratch
void mav_router::device::controller_ios::determine_mappings()
unknown device
pci error: 
mav_router::service::transport_shim::transport_shim(const parameters &)
MAV_ROUTER_HSIC_4
MAV_ROUTER_HSIC_6
virtual mav_router_result_t mav_router::device::pci_shim::enterLowPower()
. failed on I/O 0x
MAV_ROUTER_DIAG
MAV_ROUTER_HSIC_1
virtual mav_router_result_t mav_router::device::pci_shim::engage(dispatch_group_t)
com.apple.telephony.ipc
MAV_ROUTER_HSIC_3
static void mav_router::service::transport_shim_private::log_received(mav_buffer_t)
router
MAV_ROUTER_HSIC_5
\n
virtual mav_router_result_t mav_router::device::pci_shim::recover()
virtual mav_router_result_t mav_router::device::pci_shim::handle_transmit(mav_buffer_t)
MAV_ROUTER_QMI_3
MAV_ROUTER_PCI_1
device_shim
unknown channel
MAV_ROUTER_NMEA
bool mav_router::device::pci_shim::init()
static void mav_router::service::transport_shim_private::log_write(const unsigned char *, unsigned int)
MAV_ROUTER_DUN
MAV_ROUTER_HSIC_7
MAV_ROUTER_HSIC_11
v8@?0
v12@?0i8
v28@?0i8^v12^v20
MAV_ROUTER_QMI_0
MAV_ROUTER_MAV_DIAG
v24@?0i8^v12I20
virtual mav_router_result_t mav_router::device::pci_shim::tearDown()
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
MAV_ROUTER_QMI_1
MAV_ROUTER_HSIC_8
void mav_router::device::pci_shim::setErrorReason_sync(const std::string &)
mav_router::device::controller_ios::controller_ios(mav_router_weak_ptr_t)
MAV_ROUTER_HSIC_10
MAV_ROUTER_HSIC_0
MAV_ROUTER_NULL
virtual mav_router_result_t mav_router::device::pci_shim::engage(dispatch_group_t)_block_invoke
void mav_router::device::pci_shim::handleError(IOReturn)
MAV_ROUTER_CTL
MAV_ROUTER_QMI_2
MAV_ROUTER_PCI_0
MAV_ROUTER_QMI_4
MAV_ROUTER_PCI_2
v16@?0^v8
basic_string
virtual mav_router_result_t mav_router::device::pci_shim::exitLowPower()
[%04x.%04u.%04u] %s:%u:reason %s
[%04x.%04u.%04u] %s:%u:mav_router_device_error returned 0x%x
[%04x.%04u.%04u] %s:%u:status %u, arg1 %p, arg2 %p
[%04x.%04u.%04u] %s:%u:failed to create mapping of buffer %p
[%04x.%04u.%04u] %s:%u:with channel %s
[%04x.%04u.%04u] %s:%u:%s (%u bytes): %.*P
[%04x.%04u.%04u] %s:%u:Create pci control for interface %u
[%04x.%04u.%04u] %s:%u:engaging
[%04x.%04u.%04u] %s:%u:service %u
[%04x.%04u.%04u] %s:%u:router %p, device %u
[%04x.%04u.%04u] %s:%u:PCI supported with %u control channels
[%04x.%04u.%04u] %s:%u:invalid interface %u
[%04x.%04u.%04u] %s:%u:failed to create pci transport
[%04x.%04u.%04u] %s:%u:got error (%s)
[%04x.%04u.%04u] %s:%u:Number of local QMI instances %u
```
