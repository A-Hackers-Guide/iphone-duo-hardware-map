# `CWFXPCProxy`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxy`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _synchronous;
@ _target;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TB,N,GisSynchronous,V_synchronous) synchronous;
@property (T@,&,N,V_target) target;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Instance methods

```
-[CWFXPCProxy setSynchronous:];
-[CWFXPCProxy init];
-[CWFXPCProxy queue];
-[CWFXPCProxy setTarget:];
-[CWFXPCProxy methodSignatureForSelector:];
-[CWFXPCProxy isSynchronous];
-[CWFXPCProxy __copyReplyBlockFromInvocation:];
-[CWFXPCProxy target];
-[CWFXPCProxy forwardInvocation:];
-[CWFXPCProxy setQueue:];
```
