# `BKOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BiometricKitXPCClientDelegate`, `BiometricKitDelegateXpcProtocol`
- 7 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"BiometricKitXPCClient" _xpcClient;
B _startPending;
B _cancelPending;
@"BKDevice" _device;
@"<BKOperationDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
q _state;
```

## Properties

```
@property (T@"BKDevice",R,N,V_device) device;
@property (T@"<BKOperationDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (Tq,R,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKOperation isDelegate];
-[BKOperation startWithError:];
-[BKOperation statusMessage:client:];
-[BKOperation dispatchQueue];
-[BKOperation initWithDevice:];
-[BKOperation homeButtonPressed:];
-[BKOperation connectionInterrupted];
-[BKOperation statusMessage:details:client:];
-[BKOperation device];
-[BKOperation enrollUpdate:client:];
-[BKOperation dealloc];
-[BKOperation queue];
-[BKOperation startBioOperation:reply:];
-[BKOperation enrollResult:details:client:];
-[BKOperation setDelegate:];
-[BKOperation templateUpdate:details:client:];
-[BKOperation taskResumeStatus:client:];
-[BKOperation delegate];
-[BKOperation changeState:];
-[BKOperation touchIDButtonPressed:client:];
-[BKOperation cancel];
-[BKOperation enrollFeedback:client:];
-[BKOperation startWithReply:];
-[BKOperation state];
-[BKOperation setQueue:];
-[BKOperation matchResult:details:client:];
-[BKOperation operationEndsWithReason:];
-[BKOperation operationInterrupted];
-[BKOperation optionsDictionaryWithError:];
-[BKOperation startOperation:reply:];
-[BKOperation userPresentWithError:];
```
