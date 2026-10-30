# `LACCompanionAuthenticationSessionMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCompanionAuthenticationSessionMonitoring`
- 7 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
q companion;
@ observers;
@"OS_dispatch_queue" replyQueue;
_sessionProvider;
$__lazy_storage_$_mockedSessionProvider;
sessionSubscription;
B isUnderlyingSessionActive;
```

## Properties

```
@property (Tq,N,R,Vcompanion) companion;
@property (T@,N,&,Vobservers) observers;
@property (T@"OS_dispatch_queue",N,R,VreplyQueue) replyQueue;
@property (TB,N,VisUnderlyingSessionActive) isUnderlyingSessionActive;
@property (T@"NSString",N,R) description;
@property (TB,N,R) isAvailable;
@property (TB,N,R) isMonitoring;
@property (TB,N,R) isSessionActive;
```

## Instance methods

```
-[LACCompanionAuthenticationSessionMonitor startMonitoring];
-[LACCompanionAuthenticationSessionMonitor isAvailable];
-[LACCompanionAuthenticationSessionMonitor isMonitoring];
-[LACCompanionAuthenticationSessionMonitor companion];
-[LACCompanionAuthenticationSessionMonitor isSessionActive];
-[LACCompanionAuthenticationSessionMonitor removeObserver:];
-[LACCompanionAuthenticationSessionMonitor init];
-[LACCompanionAuthenticationSessionMonitor initForCompanion:environmentProvider:replyQueue:];
-[LACCompanionAuthenticationSessionMonitor stopMonitoring];
-[LACCompanionAuthenticationSessionMonitor addObserver:];
-[LACCompanionAuthenticationSessionMonitor refreshWithCompletion:];
-[LACCompanionAuthenticationSessionMonitor description];
-[LACCompanionAuthenticationSessionMonitor setObservers:];
-[LACCompanionAuthenticationSessionMonitor isUnderlyingSessionActive];
-[LACCompanionAuthenticationSessionMonitor replyQueue];
-[LACCompanionAuthenticationSessionMonitor observers];
-[LACCompanionAuthenticationSessionMonitor setIsUnderlyingSessionActive:];
```
