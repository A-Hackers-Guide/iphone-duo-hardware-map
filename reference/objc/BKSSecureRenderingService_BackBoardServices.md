# `BKSSecureRenderingService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSSecureRenderingClientInterface`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"BSServiceQueue" _delegateQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_registeredDisplayUUIDs;
@"<BKSSecureRenderingServiceDelegate>" _delegate;
```

## Properties

```
@property (T@"<BKSSecureRenderingServiceDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSSecureRenderingService init];
-[BKSSecureRenderingService setDelegate:];
-[BKSSecureRenderingService delegate];
-[BKSSecureRenderingService activateSecureRenderingControlForDisplayUUID:];
-[BKSSecureRenderingService isSecureRenderingEnabledForDisplayUUID:];
-[BKSSecureRenderingService secureRenderingViolationsOccurred:];
-[BKSSecureRenderingService setSecureRenderingEnabled:forDisplayUUID:];
```
