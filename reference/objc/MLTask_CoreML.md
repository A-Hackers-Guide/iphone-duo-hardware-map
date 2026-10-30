# `MLTask`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _taskIdentifier;
q _state;
@"NSError" _error;
@"NSObject<OS_dispatch_queue>" _syncQueue;
```

## Properties

```
@property (Tq,V_state) state;
@property (T@"NSError",C,V_error) error;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_syncQueue) syncQueue;
@property (T@"NSString",R,C,N,V_taskIdentifier) taskIdentifier;
```

## Instance methods

```
-[MLTask taskIdentifier];
-[MLTask syncQueue];
-[MLTask setError:];
-[MLTask setState:];
-[MLTask initWithState:];
-[MLTask error];
-[MLTask cancel];
-[MLTask resume];
-[MLTask state];
-[MLTask _canCancel];
-[MLTask _canComplete];
-[MLTask _canFail];
-[MLTask _canResume];
-[MLTask _canSuspend];
-[MLTask _resumeWithTaskContext:];
-[MLTask completeWithTaskContext:];
-[MLTask failWithError:taskContext:];
-[MLTask resumeWithTaskContext:];
-[MLTask suspendWithTaskContext:];
-[MLTask taskStatesToString:];
```
