# `IOUSBHostObject`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 13 properties, 51 instance methods, 0 class methods

## Instance variables

```
AB destroyed;
I _ioService;
I _ioConnection;
@"NSObject<OS_dispatch_queue>" _queue;
r^{IOUSBDeviceDescriptor=CCSCCCCSSSCCCC} _deviceDescriptor;
Q _debugLoggingMask;
^{IONotificationPort=} _ioNotificationPortRef;
@"IOUSBHostInterestNotifier" _interestNotifier;
@? _interestHandler;
@"NSMutableSet" _invalidDescriptorCache;
@"NSMutableDictionary" _descriptorCache;
@"NSArray" _supportedStringLanguages;
```

## Properties

```
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
```

## Instance methods

```
-[IOUSBHostObject destroy];
-[IOUSBHostObject dealloc];
-[IOUSBHostObject queue];
-[IOUSBHostObject setQueue:];
-[IOUSBHostObject deviceAddress];
-[IOUSBHostObject deviceDescriptor];
-[IOUSBHostObject setDeviceDescriptor:];
-[IOUSBHostObject ioService];
-[IOUSBHostObject setIoService:];
-[IOUSBHostObject openWithOptions:error:];
-[IOUSBHostObject dataWithCapacity:options:error:];
-[IOUSBHostObject descriptorCache];
-[IOUSBHostObject interestHandler];
-[IOUSBHostObject abortDeviceRequestsWithError:];
-[IOUSBHostObject abortDeviceRequestsWithOption:error:];
-[IOUSBHostObject capabilityDescriptors];
-[IOUSBHostObject closeWithOptions:];
-[IOUSBHostObject configurationDescriptorWithConfigurationValue:error:];
-[IOUSBHostObject configurationDescriptorWithIndex:error:];
-[IOUSBHostObject currentMicroframeWithTime:error:];
-[IOUSBHostObject debugLoggingMask];
-[IOUSBHostObject descriptorWithType:length:error:];
-[IOUSBHostObject descriptorWithType:length:index:languageID:error:];
-[IOUSBHostObject descriptorWithType:length:index:languageID:requestType:requestRecipient:error:];
-[IOUSBHostObject destroyWithOptions:];
-[IOUSBHostObject enqueueDeviceRequest:data:completionTimeout:error:completionHandler:];
-[IOUSBHostObject enqueueDeviceRequest:data:error:completionHandler:];
-[IOUSBHostObject enqueueDeviceRequest:error:completionHandler:];
-[IOUSBHostObject frameNumberWithTime:];
-[IOUSBHostObject initWithIOService:options:queue:error:interestHandler:];
-[IOUSBHostObject initWithIOService:queue:error:interestHandler:];
-[IOUSBHostObject interestNotifier];
-[IOUSBHostObject invalidDescriptorCache];
-[IOUSBHostObject ioConnection];
-[IOUSBHostObject ioDataWithCapacity:error:];
-[IOUSBHostObject ioNotificationPortRef];
-[IOUSBHostObject referenceMicroframeWithTime:error:];
-[IOUSBHostObject sendDeviceRequest:data:bytesTransferred:completionTimeout:error:];
-[IOUSBHostObject sendDeviceRequest:data:bytesTransferred:error:];
-[IOUSBHostObject sendDeviceRequest:error:];
-[IOUSBHostObject setDebugLoggingMask:];
-[IOUSBHostObject setDescriptorCache:];
-[IOUSBHostObject setInterestHandler:];
-[IOUSBHostObject setInterestNotifier:];
-[IOUSBHostObject setInvalidDescriptorCache:];
-[IOUSBHostObject setIoConnection:];
-[IOUSBHostObject setIoNotificationPortRef:];
-[IOUSBHostObject setSupportedStringLanguages:];
-[IOUSBHostObject stringWithIndex:error:];
-[IOUSBHostObject stringWithIndex:languageID:error:];
-[IOUSBHostObject supportedStringLanguages];
```
