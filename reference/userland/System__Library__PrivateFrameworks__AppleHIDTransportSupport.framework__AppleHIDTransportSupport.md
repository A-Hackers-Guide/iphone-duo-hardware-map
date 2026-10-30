# `/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`

iOS 27.2 dyld shared cache image. Version `10110.1.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/usr/lib/libIOReport.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`

## Objective-C: 5 classes, 0 protocols, 142 methods, 30 properties

### Class pages

Every class and protocol, with its methods: [`AHTBootLoader`](../objc/AHTBootLoader_AppleHIDTransportSupport.md), [`AHTCommon`](../objc/AHTCommon_AppleHIDTransportSupport.md), [`AHTDevice`](../objc/AHTDevice_AppleHIDTransportSupport.md), [`AHTInterface`](../objc/AHTInterface_AppleHIDTransportSupport.md), [`AHTLoader`](../objc/AHTLoader_AppleHIDTransportSupport.md)

### Classes

`AHTBootLoader`, `AHTCommon`, `AHTDevice`, `AHTInterface`, `AHTLoader`

### Properties

```
@property (TI,N,V_service) service;
@property (TI,N,V_connect) connect;
@property (TI,N,V_machPort) machPort;
@property (T@"NSString",R,N,V_personality) personality;
@property (T@"AHTDevice",R,N,V_device) device;
@property (T@"AHTInterface",R,N,V_interface) interface;
@property (T@"NSString",R,N,V_type) type;
@property (TI,R,N,V_imageTag) imageTag;
@property (TB,R,N,V_needsRestoreUpdate) needsRestoreUpdate;
@property (TB,R,N,V_supportsMemoryDump) supportsMemoryDump;
@property (TI,R,N,V_service) service;
@property (TI,R,N,V_connect) connect;
@property (T@"NSString",C,N,V_name) name;
@property (TI,N,V_machPort) machPort;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_dispatchSource) dispatchSource;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T^{__CFMachPort=},N,V_cfMachPort) cfMachPort;
@property (T^{__CFRunLoopSource=},N,V_cfRunLoopSource) cfRunLoopSource;
@property (T@"NSRunLoop",&,N,V_runLoop) runLoop;
@property (T@"NSMutableData",&,N,V_pollingBuffer) pollingBuffer;
@property (T@"NSString",&,N,V_pollingFifoName) pollingFifoName;
@property (TB,V_pollingEnabled) pollingEnabled;
@property (T@?,C,N,V_pollingParsedAction) pollingParsedAction;
@property (T@?,C,N,V_pollingRawAction) pollingRawAction;
@property (TC,R,N,V_interfaceID) interfaceID;
@property (TI,N,V_service) service;
@property (TI,N,V_connect) connect;
@property (T@"NSString",R,N,V_name) name;
@property (TI,R,N,V_imageTag) imageTag;
@property (TI,R,N,V_loadingGroup) loadingGroup;
```

## Strings (74)

```
AHTBootload%sResult
kFWDownloadFailure
%@/%@
initial pollData timed out
Memory Dumps Level
Memory dump is not an array
\n\n%-20s | %-60s | %-20s\n
AHTBootloadLoadImageEnd
%@ (%@)
AIDFirmwareUpdateService
\n
IOService
AppleHIDTransportInterface
%@ (ifaceId:%d) (no bootloader)
@\"NSString\"16@?0r*8
LoadFirmware
queue is invalid
InterfaceName
v8@?0
q24@?0@\"AHTLoader\"8@\"AHTLoader\"16
%u
Unknown FWDownloadStatus: 0x%08X
AppleHIDTransport
PreventUserIdleSystemSleep
polling is not started
AHTLoaderName
Result
LoadImage
!
PowerMethod
%@ (ifaceId:%d) (%@)
AppleHIDTransportDevice
initial pollData failed
%@\n
kFWDownloadAsync
Needs Restore Update
AHTBootloadLoadImageResult
IOParentMatch
no bootloader
fail to create dispatch source
image-tag
registryEntryID: '0x%016llx', bootloader: '%s', imageTag: '%s', personality: '%@'
N/A
AIDNextLoadOptions
AHTDevice.pollData
AIDHIDSupport
%s | %s | %s\n
%@ (%c%c%c%c)
AHTBootload%sTimeMs
LoadingGroup
Description
i16@?0^{__CFDictionary=}8
AppleHIDTransportSupport
Image Tag
Fail to read mach message (err=0x%X)
AppleHIDTransportBootloader
InterfaceDisabled
hid-merge-personality
4
%-20s | %-60s | %-20s
AHTDevice
Supports Memory Dump
Failed to allocate NSData for the property
-
bInterfaceNumber
Time (ms)
Failed to create power assertion for polling data: 0x%x
AHTDevice: beginDrainPollingFifo failed: 0x%x
AHTDevice: endDrainPollingFifo failed: 0x%x
AHTDevice: drainInputReportLoggingBuffer failed: 0x%x
AHTDevice: initial pollData failed with 0x%x, disabling polling
AHTDevice: Received kAHTDeviceNotificationTypePollingReady notification
AHTDevice: Received unknown notification type: %u
AHTDevice: pollDataOnce called but polling is not enabled
```
