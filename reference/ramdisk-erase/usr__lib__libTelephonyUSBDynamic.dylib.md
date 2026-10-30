# `/usr/lib/libTelephonyUSBDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 79,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2008)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libTelephonyUSBDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (72)

```
bInterfaceSubClass
IOGeneralInterest
TelephonyUSBInterfaceCreateInterfaceWithAllocator
_TelephonyUSBDeviceRegistrationUnregisterForDevicesInternal_block_invoke
_TelephonyUSBDeviceRegistrationFreeCallbacks_block_invoke
%s::%p::%s: Unable to get product ID, ret = 0x%08x\n
bDeviceSubClass
_TelephonyUSBDeviceRegistrationHandleDestroy_block_invoke
%s::%p::%s: Failed to add removed notfication, err = 0x%08x\n
_TelephonyUSBInterfaceRegistrationUnregisterForInterfacesInternal_block_invoke
%s::%p::%s: Unable to get interface number, ret = 0x%08x\n
%s::%p::%s: Unable to get vendor ID, ret = 0x%08x\n
%s::%p::%s: Unable to open interface number %u, ret = 0x%08x\n
%s::%p::%s: Failed to add added notfication, err = 0x%08x\n
IOServiceTerminate
%s::%p::%s: valid = 0\n
_TelephonyUSBCreatePlugInInterface
%s::%p::%s: \n
%s::%p::%s: Removing Source %p\n
v8@?0
TelephonyUSBInterfaceIsValid
_TelephonyUSBInterfaceRegisterForInterfacesInternal
%s::%p::%s: Closing IOUSBInterfaceInterface\n
%s::%p::%s: Releasing IOUSBInterfaceInterface\n
%s::%p::%s: Found Interface with Vendor ID 0x%08x, Product ID 0x%08x, Interface Number %u\n
usb
%s::%p::%s: Unable to create plugin. ret = 0x%08x, iodev = %p\n
%s::%p::%s: Opening IOUSBInterfaceInterface\n
???
idProduct
_TelephonyUSBDeviceCreateInterfaceInternal
%s::%p::%s: Registered for notifications\n
_TelephonyUSBInterfaceRegistrationCheckInterfacesAdded
notificationContext->fNotificationCallback
%s::%p::%s: notificationPort is NULL\n
TelephonyUSBInterfaceOpen
_TelephonyUSBInterfaceRegistrationHandleDestroy_block_invoke
IOUSBDevice
bInterfaceClass
USB Device
USB Interface
%s::%p::%s: No resources, trying again\n
_TelephonyUSBDeviceRegistrationCheckDeviceAdded
TelephonyUSBRegisterForInterfacesWithAllocator
_TelephonyUSBInterfaceRegistrationFreeCallbacks_block_invoke
%s::%p::%s: IOServiceAddInterestNotification failed, ret = 0x%08x\n
USB Interface Registration
idVendor
bDeviceClass
bInterfaceNumber
bConfigurationValue
%s::%p::%s: Adding Source %p\n
IOServiceFirstMatch
_TelephonyUSBDeviceRegisterForGeneralInterestInternal
IOUSBInterface
_TelephonyUSBDeviceRegistrationCheckDeviceRemoved
_TelephonyUSBDeviceHandleDestroy
%s::%p::%s: Failed to release device, ret = 0x%08x\n
_TelephonyUSBDeviceFreeInterfaceInternal
_TelephonyUSBInterfaceFreeInterfaceInternal
%s::%p::%s: Failed to close interface, ret = 0x%08x\n
USB Device Registration
context->fNotificationContext
_TelephonyUSBInterfaceRegistrationCheckInterfacesRemoved
_TelephonyUSBInterfaceHandleDestroy
%s::%p::%s: Releasing io_service_t\n
%s::%p::%s: Unable to create a Interface interface. ret = 0x%08x, Interface = %p\n
_TelephonyUSBDeviceRegisterForDevicesInternal
%s::%p::%s: source %p\n
%s::%p::%s: Unable to create a device interface. ret = 0x%08x, device = %p\n
%s::%p::%s: Found device with Vendor ID 0x%08x, Product ID 0x%08x\n
_TelephonyUSBInterfaceCreateInterfaceInternal
```
