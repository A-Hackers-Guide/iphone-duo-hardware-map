# `/usr/lib/libTelephonyUSBDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 79,136 bytes.

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
???
TelephonyUSBInterfaceOpen
_TelephonyUSBCreatePlugInInterface
USB Device Registration
%s::%p::%s: Opening IOUSBInterfaceInterface\n
bDeviceClass
%s::%p::%s: Adding Source %p\n
USB Interface Registration
_TelephonyUSBInterfaceRegistrationCheckInterfacesRemoved
%s::%p::%s: Failed to close interface, ret = 0x%08x\n
%s::%p::%s: Releasing IOUSBInterfaceInterface\n
_TelephonyUSBDeviceRegistrationCheckDeviceAdded
TelephonyUSBRegisterForInterfacesWithAllocator
_TelephonyUSBInterfaceRegistrationFreeCallbacks_block_invoke
_TelephonyUSBInterfaceFreeInterfaceInternal
bInterfaceSubClass
%s::%p::%s: valid = 0\n
_TelephonyUSBDeviceRegisterForDevicesInternal
%s::%p::%s: Failed to add added notfication, err = 0x%08x\n
%s::%p::%s: source %p\n
_TelephonyUSBInterfaceRegisterForInterfacesInternal
%s::%p::%s: Unable to create plugin. ret = 0x%08x, iodev = %p\n
idProduct
%s::%p::%s: Unable to create a device interface. ret = 0x%08x, device = %p\n
_TelephonyUSBInterfaceRegistrationUnregisterForInterfacesInternal_block_invoke
%s::%p::%s: Removing Source %p\n
IOServiceFirstMatch
IOServiceTerminate
_TelephonyUSBDeviceHandleDestroy
%s::%p::%s: Failed to release device, ret = 0x%08x\n
IOGeneralInterest
%s::%p::%s: Releasing io_service_t\n
%s::%p::%s: Unable to get vendor ID, ret = 0x%08x\n
%s::%p::%s: notificationPort is NULL\n
_TelephonyUSBDeviceRegisterForGeneralInterestInternal
idVendor
bInterfaceClass
_TelephonyUSBDeviceRegistrationUnregisterForDevicesInternal_block_invoke
USB Device
_TelephonyUSBInterfaceRegistrationHandleDestroy_block_invoke
%s::%p::%s: No resources, trying again\n
IOUSBDevice
bInterfaceNumber
v8@?0
%s::%p::%s: \n
_TelephonyUSBDeviceRegistrationFreeCallbacks_block_invoke
notificationContext->fNotificationCallback
_TelephonyUSBDeviceCreateInterfaceInternal
%s::%p::%s: Unable to get product ID, ret = 0x%08x\n
context->fNotificationContext
%s::%p::%s: Registered for notifications\n
%s::%p::%s: Found Interface with Vendor ID 0x%08x, Product ID 0x%08x, Interface Number %u\n
bConfigurationValue
_TelephonyUSBDeviceRegistrationHandleDestroy_block_invoke
%s::%p::%s: Closing IOUSBInterfaceInterface\n
_TelephonyUSBInterfaceCreateInterfaceInternal
%s::%p::%s: Failed to add removed notfication, err = 0x%08x\n
_TelephonyUSBDeviceFreeInterfaceInternal
%s::%p::%s: IOServiceAddInterestNotification failed, ret = 0x%08x\n
_TelephonyUSBInterfaceRegistrationCheckInterfacesAdded
_TelephonyUSBInterfaceHandleDestroy
bDeviceSubClass
_TelephonyUSBDeviceRegistrationCheckDeviceRemoved
%s::%p::%s: Found device with Vendor ID 0x%08x, Product ID 0x%08x\n
TelephonyUSBInterfaceCreateInterfaceWithAllocator
%s::%p::%s: Unable to open interface number %u, ret = 0x%08x\n
USB Interface
%s::%p::%s: Unable to create a Interface interface. ret = 0x%08x, Interface = %p\n
%s::%p::%s: Unable to get interface number, ret = 0x%08x\n
TelephonyUSBInterfaceIsValid
usb
IOUSBInterface
```
