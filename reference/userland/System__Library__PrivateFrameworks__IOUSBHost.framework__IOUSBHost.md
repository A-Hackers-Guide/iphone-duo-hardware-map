# `/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`

iOS 27.2 dyld shared cache image. Version `1617.40.10.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`

## Objective-C: 13 classes, 0 protocols, 289 methods, 91 properties

### Class pages

Every class and protocol, with its methods: [`IOBufferMutableData`](../objc/IOBufferMutableData_IOUSBHost.md), [`IOUSBHostCIControllerStateMachine`](../objc/IOUSBHostCIControllerStateMachine_IOUSBHost.md), [`IOUSBHostCIDeviceStateMachine`](../objc/IOUSBHostCIDeviceStateMachine_IOUSBHost.md), [`IOUSBHostCIEndpointStateMachine`](../objc/IOUSBHostCIEndpointStateMachine_IOUSBHost.md), [`IOUSBHostCIPortStateMachine`](../objc/IOUSBHostCIPortStateMachine_IOUSBHost.md), [`IOUSBHostControllerInterface`](../objc/IOUSBHostControllerInterface_IOUSBHost.md), [`IOUSBHostDevice`](../objc/IOUSBHostDevice_IOUSBHost.md), [`IOUSBHostIOSource`](../objc/IOUSBHostIOSource_IOUSBHost.md), [`IOUSBHostInterestNotifier`](../objc/IOUSBHostInterestNotifier_IOUSBHost.md), [`IOUSBHostInterface`](../objc/IOUSBHostInterface_IOUSBHost.md), [`IOUSBHostObject`](../objc/IOUSBHostObject_IOUSBHost.md), [`IOUSBHostPipe`](../objc/IOUSBHostPipe_IOUSBHost.md), [`IOUSBHostStream`](../objc/IOUSBHostStream_IOUSBHost.md)

### Classes

`IOBufferMutableData`, `IOUSBHostCIControllerStateMachine`, `IOUSBHostCIDeviceStateMachine`, `IOUSBHostCIEndpointStateMachine`, `IOUSBHostCIPortStateMachine`, `IOUSBHostControllerInterface`, `IOUSBHostDevice`, `IOUSBHostIOSource`, `IOUSBHostInterestNotifier`, `IOUSBHostInterface`, `IOUSBHostObject`, `IOUSBHostPipe`, `IOUSBHostStream`

### Properties

```
@property (T@?,C,V_deallocator) deallocator;
@property (Ti,N,V_controllerState) controllerState;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (TQ,N,V_lastFrameNumber) lastFrameNumber;
@property (TQ,N,V_lastFrameTimestamp) lastFrameTimestamp;
@property (Ti,N,V_deviceState) deviceState;
@property (TQ,N,V_completeRoute) completeRoute;
@property (TQ,N,V_deviceAddress) deviceAddress;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (Ti,N,V_endpointState) endpointState;
@property (TQ,N,V_deviceAddress) deviceAddress;
@property (TQ,N,V_endpointAddress) endpointAddress;
@property (Tr^{IOUSBHostCIMessage=IIQ},N,V_currentTransferMessage) currentTransferMessage;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (Ti,N,V_endpointType) endpointType;
@property (TQ,N,V_portNumber) portNumber;
@property (Ti,N,V_portState) portState;
@property (TI,N,V_portStatus) portStatus;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (TB,N,V_powered) powered;
@property (TB,N,V_connected) connected;
@property (TB,N,V_overcurrent) overcurrent;
@property (Ti,R,N,V_linkState) linkState;
@property (Ti,R,N,V_speed) speed;
@property (T@"IOUSBHostCIControllerStateMachine",&,N,V_controllerStateMachine) controllerStateMachine;
@property (Tr^{IOUSBHostCIMessage=IIQ},N,V_capabilities) capabilities;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (TI,N,V_ioConnect) ioConnect;
@property (TQ,N,V_ioConnectAsyncPending) ioConnectAsyncPending;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{IONotificationPort=},N,V_notificationPortRef) notificationPortRef;
@property (T@?,C,N,V_commandHandler) commandHandler;
@property (T@?,C,N,V_doorbellHandler) doorbellHandler;
@property (T^?,N,V_interestHandler) interestHandler;
@property (T@"IOUSBHostInterestNotifier",&,N,V_interestNotifier) interestNotifier;
@property (T{IOUSBHostCIMessage=IIQ},V_command) command;
@property (T@"NSMutableData",&,N,V_doorbells) doorbells;
@property (T@"NSMutableData",&,N,V_interrupts) interrupts;
@property (T@"NSRecursiveLock",&,N,V_interruptLock) interruptLock;
@property (TQ,V_interruptProducerIndex) interruptProducerIndex;
@property (TQ,V_interruptConsumerIndex) interruptConsumerIndex;
@property (TB,V_interruptDeliveryPending) interruptDeliveryPending;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_interruptQueue) interruptQueue;
@property (TQ,V_nextInterruptTime) nextInterruptTime;
@property (TB,R,D) destroyed;
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (TQ,N,V_interruptRateHz) interruptRateHz;
@property (TQ,V_lastKnownConfiguration) lastKnownConfiguration;
@property (Tr^{IOUSBConfigurationDescriptor=CCSCCCCC},R) configurationDescriptor;
@property (TI,V_debugLoggingMask) debugLoggingMask;
@property (T@"IOUSBHostInterface",&,V_hostInterface) hostInterface;
@property (TQ,V_deviceAddress) deviceAddress;
@property (TQ,V_endpointAddress) endpointAddress;
@property (TI,R) ioConnection;
@property (T^{IONotificationPort=},R) ioNotificationPortRef;
@property (T@"NSObject",W,N,V_owner) owner;
@property (TB,N,V_destroyed) destroyed;
@property (T@"NSRecursiveLock",&,N,V_lock) lock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{IONotificationPort=},N,V_notificationPortRef) notificationPortRef;
@property (T^?,N,V_callback) callback;
@property (TI,N,V_service) service;
@property (TI,N,V_notifier) notifier;
@property (TI,N,V_matchingIterator) matchingIterator;
@property (Tr^{IOUSBConfigurationDescriptor=CCSCCCCC},V_configurationDescriptor) configurationDescriptor;
@property (TQ,V_interfaceNumber) interfaceNumber;
@property (TQ,V_lastKnownAlternateSetting) lastKnownAlternateSetting;
@property (Td,R) idleTimeout;
@property (Tr^{IOUSBInterfaceDescriptor=CCCCCCCCC},R) interfaceDescriptor;
@property (TQ,V_debugLoggingMask) debugLoggingMask;
@property (TI,V_ioService) ioService;
@property (TI,V_ioConnection) ioConnection;
@property (T^{IONotificationPort=},V_ioNotificationPortRef) ioNotificationPortRef;
@property (T@"IOUSBHostInterestNotifier",&,N,V_interestNotifier) interestNotifier;
@property (T@?,C,V_interestHandler) interestHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSMutableSet",&,V_invalidDescriptorCache) invalidDescriptorCache;
@property (T@"NSMutableDictionary",&,V_descriptorCache) descriptorCache;
@property (Tr^{IOUSBDeviceDescriptor=CCSCCCCSSSCCCC},V_deviceDescriptor) deviceDescriptor;
@property (T@"NSArray",&,V_supportedStringLanguages) supportedStringLanguages;
@property (Tr^{IOUSBBOSDescriptor=CCSC},R) capabilityDescriptors;
@property (TQ,R) deviceAddress;
@property (T@"NSData",&,V_originalDescriptorsCache) originalDescriptorsCache;
@property (T@"NSData",&,V_currentDescriptorsCache) currentDescriptorsCache;
@property (T@"NSMutableSet",&,V_invalidDescriptorCache) invalidDescriptorCache;
@property (TB,V_streamsEnabled) streamsEnabled;
@property (Tr^{IOUSBHostIOSourceDescriptors=S{IOUSBEndpointDescriptor=CCCCSC}{IOUSBSuperSpeedEndpointCompanionDescriptor=CCCCS}{IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor=CCSI}},R) originalDescriptors;
@property (Tr^{IOUSBHostIOSourceDescriptors=S{IOUSBEndpointDescriptor=CCCCSC}{IOUSBSuperSpeedEndpointCompanionDescriptor=CCCCS}{IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor=CCSI}},R) descriptors;
@property (Td,R) idleTimeout;
@property (T@"IOUSBHostPipe",&,V_hostPipe) hostPipe;
@property (TQ,V_streamID) streamID;
```

## Strings (309)

```
IOUSBHostInterestNotifier: Failed to allocate lock\n
dealloc IOUSBHostControllerInterface with UUID %@ without first calling destroy
destroyed IOUSBHostControllerInterface with UUID %@
interrupt %s
IOUSBHostInterestNotifier: Failed to register for interest\n
IOUSBHostInterfaceNotifier: adding interest for %d\n
IOUSBHostInterestNotifier: Failed to allocate queue\n
Notification message 0x%08x argument 0x%016lx
created IOUSBHostControllerInterface with UUID %@
destroying IOUSBHostControllerInterface with UUID %@
command %s
doorbell Device %d Endpoint 0x%02x\n
Fatal error: %s
IOUSBHostInterestNotifier: Failed to create notification port\n
IOUSBHostInterestNotifier: Failed to create matching notification\n
Failed to create notifier\n
Error: %@ with reason: %@
/Library/Caches/com.apple.xbs/98EF6CB8-8FA6-45DA-A384-BB62F362A246/TemporaryDirectory.ioYslQ/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostObject.m
IOUSBHostCIMessageTypeEndpointReset
IOUSBHostCIMessageStatusTransactionError
SuperPlusBy2
Command does not target this state machine instance.
bDeviceClass
Unable to abort IO.
IOUSBHostCIExceptionTypeCommandWriteFailed
IOUSBHostCIExceptionTypeInterruptOverflow
Halted
idVendor
IOUSBHostControllerInterfaceUUID
IOServiceFirstMatch
IOUSBHostCIMessageTypePortSuspend
IOUSBHostCIMessageTypeEndpointPause
Command response was not sent.
 Overcurrent Change
Command is not handled by the device state machine.
Unable to enqueue IO.
 Link Change
Unable to set configuration.
Unable to obtain interface number.
Unable to disable streams.
IOUSBHostDispatchQueue
-[IOUSBHostObject closeWithOptions:]
IOUSBHostCIMessageTypeEndpointDestroy
IOUSBHostCIExceptionTypeDoorbellOverflow
kUSBCurrentConfiguration
: Invalid
Select a valid endpoint address
Unable to obtain device descriptor.
-[IOUSBHostInterface idleTimeout]
Not enough space for interrupts.
Unable to allocate dispatch queue.
Unable to open io_service_t object and create user client.
U2
U3
Capabilities structure was rejected.
 Port Route 0x%08x
YES
Unable to send device request.
Failed to abort device requests.
IOUSBHostCIMessageTypeEndpointCreate
IOUSBHostCIMessageStatusStallError
idProductMask
 Link
Unable to adjust pipe.
ID can not be modified for ioData buffer
The current transfer cannot generate a transfer completion.
...
IOUSBHostCIMessageTypePortEvent
Powered
Unable to allocate memory.
 (
 Root Port %u
StreamID out of bounds.
IOUSBHostCIExceptionTypeDoorbellReadCollision
Found a link to an invalid transfer structure address.
bAlternateSetting
 Request 0x%02x %02x %04x %04x %04x
-[IOUSBHostObject openWithOptions:error:]
Failed to get descriptor.
-[IOUSBHostObject deviceAddress]
IOUSBHostCIMessageTypeControllerFrameNumber
SuperPlus
Frame update was not sent.
IOUSBHostCIMessageTypeDeviceStart
AppleUSBUserHCIResources
Failed to retrieve current microframe
IOUSBHostCIMessageStatusBadArgument
IOUSBHostCIExceptionTypeFrameUpdateError
IOServiceOpen failed.
!
IOUSBHostCIMessageTypeControllerStart
U0
Port number is too high.
Unable to select alternate setting.
High
Port is not powered.
IOUSBHostCIMessageTypeEndpointSetNextTransfer
Reset
Full
Unable to send IO with stream.
The frame number or timestamp cannot regress.
Unable to set an idle timeout.
Select a valid streamID.
Unable to create IONotificationPort port.
IOUSBHostCIMessageTypePortCapabilities
Low
IOUSBHostCIExceptionTypeInterruptInvalid
Link state cannot be updated.
Capabilities are not valid.
IOUSBHostCIMessageTypeSetupTransfer
Resume
Active
 Device Speed %s
Unable to allocate memory for doorbells.
Enable streams before disabling streams.
Transfer completion message was not sent.
[Line %d of %s] %sconnect call failed with 0x%x
Unable to create interest notifier.
IOUSBHostCIMessageTypePortDisable
IOUSBHostCIMessageTypeDeviceDestroy
IOUSBHostCIMessageStatusNotPermitted
Failed to create IOUSBHostObject.
IOUSBHostCIMessageTypeControllerPowerOn
IOUSBHostCIMessageTypeDeviceUpdate
IOUSBHostCIExceptionTypeCommandReadCollision
Failed to create IOUSBHostCIPortStateMachine.
 Link State %s
IOUSBHostErrorDomain
bDeviceProtocol
0x
Recovery
The current endpoint state %s cannot generate transfer completions.
Exclusive open of usb object failed.
IOUSBHostCIMessageTypePortReset
IOUSBHostCIMessageStatusNoResources
U1
Failed to read command from kernel.
0x%08x %08x %016llx
IOUSBHostCIExceptionTypeTerminated
Command is not handled by the endpoint state machine.
Failed to create IOUSBHostCIControllerStateMachine.
Failed to create IOUSBHostCIDeviceStateMachine.
Failed to allocate interruptData.
v8@?0
Port number is out of range.
 Device %d Endpoint 0x%02x
IOGeneralInterest
IOUSBHostCIMessageTypeControllerPowerOff
IOUSBHostCIMessageTypeDevicePause
Unable to reset device
Controller %@ State %s
Unable to connect to the kernel.
Unable to create notification port.
 Status %s
 Device %u Endpoint 0x%02lx Length %u Status %s Transfer Structure 0x%016llx
Unable to enqueue device request.
RxDetect
Command cannot be processed successfully.
Failed to read doorbells from kernel.
ConfigurationValue of 0 is invalid
kUSBVendorString
 Connect
IOUSBHostCIMessageStatusError
bInterfaceSubClass
)
IOUSBHostCIMessageStatusEndpointStopped
 Clear State %s
-[IOUSBHostPipe idleTimeout]
IOUSBHostCIMessageTypeControllerCapabilities
IOUSBHostCIMessageTypePortStatus
Disabled
Off
 
[Line %d of %s] %sservice is already opened
v24@?0^v8Q16
IOUSBHostCIMessageTypeLink
IOUSBHostCIMessageStatusOffline
IOUSBHostCIMessageStatusOverrunError
Command is not handled by the port state machine.
/Library/Caches/com.apple.xbs/98EF6CB8-8FA6-45DA-A384-BB62F362A246/TemporaryDirectory.ioYslQ/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostPipe.m
The length is less than descriptor's wTotalLength.
IOUSBHostCIMessageTypeDeviceCreate
 Overcurrent
Rejected doorbell.
Failed to create IOUSBHostInterface.
Unable to send control request.
Unable to copy stream.
Paused
Link state is not compatible with speed.
 Powered
 Connected
Endpoint address not found.
IOUSBHostPipe init failed.
Failed to get configuration descriptor.
IOUSBHostCIMessageTypeEndpointUpdate
1
Command cannot be processed in the current state.
0x%08x does not target this endpoint.
Unable to obtain configuration descriptor.
 Descriptor 0x%016llx
Failed to retrieve reference microframe.
: 
The wLength field of the request must be less than or equal to the data's length.
The specified message %p does not match the current transfer %p.
bInterfaceNumber
Unable to create IOUSBHostInterestNotifier
IOUSBHostCIMessageTypePortResume
IOUSBHostCIMessageStatusSuccess
Failed [super init]
kUSBSerialNumberString
IOUSBHostCIMessageTypeControllerPause
IOUSBHostCIMessageTypeStatusTransfer
IOUSBHostCIExceptionTypeCapabilitiesInvalid
Unable to allocate bus current
Failed to create IOUSBHostControllerInterface.
/Library/Caches/com.apple.xbs/98EF6CB8-8FA6-45DA-A384-BB62F362A246/TemporaryDirectory.ioYslQ/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostInterface.m
Command is not handled by the controller state machine.
 Device Address %u
NO
 Transfer Structure 0x%016llx
IOService
Unable to allocate NSMutableDictionary.
Compliance
Failed to allocate interruptLock.
Unable to clear stall.
Unable to enqueue IO with stream.
Failed to create UUID.
Unable to get configuration descriptor.
Unable to allocate IOData Buffer.
IOUSBHostCIMessageTypeFrameNumberUpdate
IOUSBHostCIMessageStatusTimeout
Super
Failed to create IOUSBHostCIEndpointStateMachine.
Unable to enqueue control request.
IOUSBHostCIMessageTypeTransferComplete
IOUSBHostCIExceptionTypeProtocolError
%@.%@
Unknown
init failed.
Failed to allocate interruptQueue.
Failed to retrieve port state machine.
Data buffer is smaller than request wLength.
Test
IOUSBHostCIExceptionTypeCommandTimeout
 Connect Change
 Clear Change Bits:
Unable to enable streams.
Unable to get device speed.
IOUSBHostCIMessageStatusReserved
Suspended
Destroyed
Unable to send IO.
ioDataSetLengthException
IOUSBHostCIMessageTypePortPowerOff
IOUSBHostCIMessageTypeNormalTransfer
IOUSBHostCIExceptionTypeCommandFailure
 Length 0x%x Buffer 0x%016llx\n
IOUSBHostStream init failed.
Unable to allocateNSMutableSet.
[Line %d of %s] %sservice is not opened
Length can not be modified for ioData buffer
Unable to set UUID property.
Unable to enqueue asynchronous operation.
IOUSBHostCIMessageTypePortPowerOn
None
Failed to send interrupts.
 Device Address %llu Status %s
Unable to find configuration descriptor with specified value
ioDataSetIDException
2
Unable to copy pipe.
bInterfaceProtocol
locationID
!5
IOUSBHostCIMessageTypeIsochronousTransfer
IOUSBHostCIMessageStatusProtocolError
IOUSBHostCIMessageStatusMissedServiceError
Command failed common validation checks.
IOPropertyMatch
Enable streams before copying a stream.
The wLength field of the request must be less than or equal to the data's length
Requested descriptor likely does not exist.
IOUSBHostCIMessageTypeFrameTimestampUpdate
 )
bcdDevice
Failed to send interrupts to kernel.\n
Inactive
Port %d State %s Status 0x%08x
A
bConfigurationValue
bDeviceSubClass
kUSBContainerID
: %s
Another client likely has exclusive access.
Device %d State %s
Unable to set idle timeout.
Streams were never enabled.
Polling
Device %d Endpoint 0x%02x State %s Current Transfer %p ( %@ )
idProduct
com.apple.iokit.usb.framework.IOUSBHost
IOUserClient
A successful IOUSBHostCIMessageTypePortReset requires a U0 link state.
idProductArray
%s%02x
Unable to abort stream.
Frame updates are not meaningful in the current state.
bInterfaceClass
USBSpeed
```
