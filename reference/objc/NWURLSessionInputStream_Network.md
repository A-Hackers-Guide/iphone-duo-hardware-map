# `NWURLSessionInputStream`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSInputStream`
- 14 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
B _opened;
B _reading;
B _receivedEOF;
B _signaledEOF;
S _readWaiters;
@"NSURLSessionStreamTask" _streamTask;
@"<NSStreamDelegate>" _streamDelegate;
@"NSRunLoop" _runLoop;
@"NSMutableArray" _runLoopModes;
@"NSObject<OS_dispatch_semaphore>" _readSemaphore;
Q _readSize;
@"NSObject<OS_dispatch_data>" _pendingData;
@"NSError" _error;
```

## Instance methods

```
-[NWURLSessionInputStream propertyForKey:];
-[NWURLSessionInputStream open];
-[NWURLSessionInputStream setProperty:forKey:];
-[NWURLSessionInputStream close];
-[NWURLSessionInputStream streamError];
-[NWURLSessionInputStream getBuffer:length:];
-[NWURLSessionInputStream removeFromRunLoop:forMode:];
-[NWURLSessionInputStream setDelegate:];
-[NWURLSessionInputStream hasBytesAvailable];
-[NWURLSessionInputStream delegate];
-[NWURLSessionInputStream scheduleInRunLoop:forMode:];
-[NWURLSessionInputStream read:maxLength:];
-[NWURLSessionInputStream streamStatus];
```
