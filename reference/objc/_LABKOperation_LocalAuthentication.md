# `_LABKOperation`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKOperationDelegate`
- 6 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _isUserPresent;
@"BKOperation" __BKOperation;
@"_LABKDevice" _device;
@"<BKOperationDelegate>" _delegate;
q _state;
```

## Properties

```
@property (T@"BKOperation",R,N,V__BKOperation) _BKOperation;
@property (T@"_LABKDevice",R,N,V_device) device;
@property (T@"<BKOperationDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (Tq,N,V_state) state;
@property (TB,N,V_isUserPresent) isUserPresent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_LABKOperation _wrapperForBKOperation:device:];
```

## Instance methods

```
-[_LABKOperation startWithError:];
-[_LABKOperation setState:];
-[_LABKOperation observeValueForKeyPath:ofObject:change:context:];
-[_LABKOperation device];
-[_LABKOperation operation:finishedWithReason:];
-[_LABKOperation dealloc];
-[_LABKOperation queue];
-[_LABKOperation forwardingTargetForSelector:];
-[_LABKOperation setDelegate:];
-[_LABKOperation delegate];
-[_LABKOperation startWithReply:];
-[_LABKOperation state];
-[_LABKOperation setQueue:];
-[_LABKOperation operation:presenceStateChanged:];
-[_LABKOperation operation:stateChanged:];
-[_LABKOperation dispatchDelegateSelector:block:];
-[_LABKOperation _BKOperation];
-[_LABKOperation _initWithBKOperation:device:];
-[_LABKOperation isUserPresent];
-[_LABKOperation setIsUserPresent:];
-[_LABKOperation shim];
```
