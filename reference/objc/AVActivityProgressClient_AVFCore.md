# `AVActivityProgressClient`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnection<BSServiceConnectionClient>" _connection;
@ _server;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[AVActivityProgressClient resetConnection];
-[AVActivityProgressClient invalidateConnection];
-[AVActivityProgressClient server];
-[AVActivityProgressClient init];
-[AVActivityProgressClient cancelActivities:];
-[AVActivityProgressClient dealloc];
-[AVActivityProgressClient queue];
-[AVActivityProgressClient activateConnection];
-[AVActivityProgressClient endActivityForTaskID:];
-[AVActivityProgressClient eventResultReceivedForActivity:event:result:];
-[AVActivityProgressClient failActivityForTaskID:];
-[AVActivityProgressClient postActivityEvent:forIdentifier:];
-[AVActivityProgressClient startProgressActivity:taskID:bundleID:name:description:imageUTI:];
-[AVActivityProgressClient unfailActivityForTaskID:];
-[AVActivityProgressClient updateActivityName:description:forTaskID:];
-[AVActivityProgressClient updateProgress:forTaskID:];
```
