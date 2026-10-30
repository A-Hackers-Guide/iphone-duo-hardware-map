# `EAInputStream`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSInputStream`
- 19 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@ _delegate;
@"EAAccessory" _accessory;
@"EASession" _session;
i _sock;
B _useSocket;
@"NSMutableData" _inputFromAccData;
@"NSCondition" _inputFromAccCondition;
@"NSRecursiveLock" _statusLock;
@"NSRecursiveLock" _runloopLock;
@"NSObject<OS_dispatch_queue>" _inputFromAccQueue;
@"NSObject<OS_dispatch_source>" _sockListenSource;
* _inputFromAccBuffer;
B _isOpenCompletedEventSent;
B _hasNewBytesAvailable;
B _isAtEndEventSent;
Q _streamStatus;
^{__CFRunLoop=} _runLoop;
^{__CFRunLoopSource=} _runLoopSource;
i _zeroBytesReadCount;
```

## Properties

```
@property (Ti,V_zeroBytesReadCount) zeroBytesReadCount;
```

## Instance methods

```
-[EAInputStream propertyForKey:];
-[EAInputStream open];
-[EAInputStream setProperty:forKey:];
-[EAInputStream close];
-[EAInputStream streamError];
-[EAInputStream dealloc];
-[EAInputStream getBuffer:length:];
-[EAInputStream removeFromRunLoop:forMode:];
-[EAInputStream setDelegate:];
-[EAInputStream hasBytesAvailable];
-[EAInputStream delegate];
-[EAInputStream scheduleInRunLoop:forMode:];
-[EAInputStream read:maxLength:];
-[EAInputStream streamStatus];
-[EAInputStream _scheduleCallback];
-[EAInputStream _streamEventTrigger];
-[EAInputStream _performAtEndOfStreamValidation];
-[EAInputStream _accessoryDidDisconnect:];
-[EAInputStream endStream];
-[EAInputStream initWithAccessory:forSession:socket:];
-[EAInputStream initWithAccessoryWithoutSocket:forSession:];
-[EAInputStream openCompleted];
-[EAInputStream processIncomingAccessoryData:];
-[EAInputStream setZeroBytesReadCount:];
-[EAInputStream zeroBytesReadCount];
```
