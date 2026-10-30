# `/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter`

iOS 27.2 dyld shared cache image. Version `2360.40.13.0.1`. **[DSC]**

## Linked libraries (6)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Strings (44)

```
DeviceClassNumber
IOServiceFirstPublish
T8027USBSetAssertion
IOHIDT8027USBAssertion
SessionFilterDebug
T8027USBAssertionTimeout
AssertLevel
bool IOHIDT8027USBSessionFilter::initTimer()
USB
usb-repeater
AssertionTimeout
Product
Class
IOHIDT8027USBSessionFilter
void IOHIDT8027USBSessionFilter::preventIdleSleepAssertion(CFStringRef)
RegID:0x%llx %@
SetProperty
usb-drd,t8027
void IOHIDT8027USBSessionFilter::timerHandler()
void IOHIDT8027USBSessionFilter::releaseIdleSleepAssertion()
usb-drd,t8130
prrt
HasT8027USB
USBHIDServiceCount
PreventUserIdleSystemSleep
Transport
IONameMatch
void IOHIDT8027USBSessionFilter::scheduleWithDispatchQueue(dispatch_queue_t)
Asserting
AssertionProperties
v8@?0
%s adding matching notification 0x%x\n
%s error turning on assertion 0x%x\n
T8027USB HID assertion timeout\n
T8027USB HID activity\n
Setting T8027 USB assertion timeout from %llu to %@\n
Setting T8027 USB assertion state %@\n
%s error creating assertion 0x%x\n
%s error releasing assertion 0x%x\n
%s error\n
%s error turning off assertion 0x%x\n
T8027 assertion previously timed out, not taking assertion\n
Creating T8027USB assertion for %@ (timeout:%llus)\n
Removing T8027USB assertion\n
```
