# `NWURLSessionOutputStream`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOutputStream`
- 12 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
B _opened;
B _writing;
B _pendingClose;
S _writeWaiters;
@"NSURLSessionStreamTask" _streamTask;
@"<NSStreamDelegate>" _streamDelegate;
@"NSRunLoop" _runLoop;
@"NSMutableArray" _runLoopModes;
@"NSObject<OS_dispatch_semaphore>" _writeSemaphore;
@"NSObject<OS_dispatch_data>" _pendingData;
@"NSError" _error;
```

## Instance methods

```
-[NWURLSessionOutputStream propertyForKey:];
-[NWURLSessionOutputStream open];
-[NWURLSessionOutputStream setProperty:forKey:];
-[NWURLSessionOutputStream close];
-[NWURLSessionOutputStream streamError];
-[NWURLSessionOutputStream removeFromRunLoop:forMode:];
-[NWURLSessionOutputStream setDelegate:];
-[NWURLSessionOutputStream delegate];
-[NWURLSessionOutputStream scheduleInRunLoop:forMode:];
-[NWURLSessionOutputStream streamStatus];
-[NWURLSessionOutputStream hasSpaceAvailable];
-[NWURLSessionOutputStream write:maxLength:];
```
