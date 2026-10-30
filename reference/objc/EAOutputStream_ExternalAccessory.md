# `EAOutputStream`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOutputStream`
- 16 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@ _delegate;
i _sock;
@"EAAccessory" _accessory;
@"EASession" _session;
@"NSRecursiveLock" _statusLock;
@"NSRecursiveLock" _runloopLock;
B _useSocket;
^{__CFSocket=} _cfSocket;
B _isOpenCompletedEventSent;
B _hasSpaceAvailableEventSent;
B _hasSpaceAvailable;
B _isAtEndEventSent;
Q _streamStatus;
^{__CFRunLoop=} _runLoop;
^{__CFRunLoopSource=} _runLoopSource;
^{__CFRunLoopSource=} _socketRunLoopSource;
```

## Instance methods

```
-[EAOutputStream propertyForKey:];
-[EAOutputStream open];
-[EAOutputStream setProperty:forKey:];
-[EAOutputStream close];
-[EAOutputStream streamError];
-[EAOutputStream dealloc];
-[EAOutputStream removeFromRunLoop:forMode:];
-[EAOutputStream setDelegate:];
-[EAOutputStream delegate];
-[EAOutputStream scheduleInRunLoop:forMode:];
-[EAOutputStream streamStatus];
-[EAOutputStream hasSpaceAvailable];
-[EAOutputStream write:maxLength:];
-[EAOutputStream _scheduleCallback];
-[EAOutputStream _streamEventTrigger];
-[EAOutputStream _performAtEndOfStreamValidation];
-[EAOutputStream _accessoryDidDisconnect:];
-[EAOutputStream _streamWriteable];
-[EAOutputStream endStream];
-[EAOutputStream initWithAccessory:forSession:socket:];
-[EAOutputStream initWithAccessoryWithoutSocket:forSession:];
-[EAOutputStream openCompleted];
```
