# `AHTDevice`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`](../userland/System__Library__PrivateFrameworks__AppleHIDTransportSupport.framework__AppleHIDTransportSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AHTCommon`
- 11 instance variables, 11 properties, 51 instance methods, 4 class methods

## Instance variables

```
B _pollingEnabled;
I _machPort;
@? _pollingParsedAction;
@? _pollingRawAction;
@"NSObject<OS_dispatch_source>" _dispatchSource;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
^{__CFMachPort=} _cfMachPort;
^{__CFRunLoopSource=} _cfRunLoopSource;
@"NSRunLoop" _runLoop;
@"NSMutableData" _pollingBuffer;
@"NSString" _pollingFifoName;
```

## Properties

```
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
```

## Class methods

```
+[AHTDevice allDevices];
+[AHTDevice withService:];
+[AHTDevice deviceWithParentRegistryId:];
+[AHTDevice withName:];
```

## Instance methods

```
-[AHTDevice dispatchQueue];
-[AHTDevice dealloc];
-[AHTDevice reset];
-[AHTDevice machPort];
-[AHTDevice setDispatchQueue:];
-[AHTDevice runLoop];
-[AHTDevice description];
-[AHTDevice initWithService:];
-[AHTDevice setMachPort:];
-[AHTDevice setPower:];
-[AHTDevice createMachPort];
-[AHTDevice setRunLoop:];
-[AHTDevice stopPolling:];
-[AHTDevice getBootLoader];
-[AHTDevice cfRunLoopSource];
-[AHTDevice reporterResults];
-[AHTDevice cleanupMachPort];
-[AHTDevice pollingFifoName];
-[AHTDevice startWithPolling:runLoop:error:];
-[AHTDevice cfMachPort];
-[AHTDevice cleanupDispatchQueuePolling];
-[AHTDevice cleanupRunLoopPolling];
-[AHTDevice dispatchSource];
-[AHTDevice drainInputReportLoggingBuffer:];
-[AHTDevice enableInputReportLogging:enable:];
-[AHTDevice getInterface:];
-[AHTDevice getInterfaceWithName:];
-[AHTDevice getInterfaces];
-[AHTDevice getPollingData:kernResult:];
-[AHTDevice getPower:];
-[AHTDevice handleMachNotification];
-[AHTDevice parsePollingData:];
-[AHTDevice parsePollingEntryFromBytes:totalLength:offset:];
-[AHTDevice pollData];
-[AHTDevice pollData:];
-[AHTDevice pollDataOnce];
-[AHTDevice pollDataOnce:];
-[AHTDevice pollingBuffer];
-[AHTDevice pollingEnabled];
-[AHTDevice pollingParsedAction];
-[AHTDevice pollingRawAction];
-[AHTDevice setCfMachPort:];
-[AHTDevice setCfRunLoopSource:];
-[AHTDevice setDispatchSource:];
-[AHTDevice setPollingBuffer:];
-[AHTDevice setPollingEnabled:];
-[AHTDevice setPollingFifoName:];
-[AHTDevice setPollingParsedAction:];
-[AHTDevice setPollingRawAction:];
-[AHTDevice startPollingCommon:error:];
-[AHTDevice startWithPolling:queue:error:];
```
