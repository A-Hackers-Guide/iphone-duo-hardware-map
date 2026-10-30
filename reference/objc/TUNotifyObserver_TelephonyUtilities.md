# `TUNotifyObserver`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUNotifyObserver`
- 5 instance variables, 11 properties, 16 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
i _token;
@? _callback;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _notificationName;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_lock) lock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSString",C,N,V_notificationName) notificationName;
@property (Ti,N,V_token) token;
@property (T@?,C,N,V_callback) callback;
@property (TQ,R,N) state;
@property (TB,R,N,GisObserving) observing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUNotifyObserver callback];
-[TUNotifyObserver setCallback:];
-[TUNotifyObserver dealloc];
-[TUNotifyObserver queue];
-[TUNotifyObserver isObserving];
-[TUNotifyObserver setNotificationName:];
-[TUNotifyObserver notificationName];
-[TUNotifyObserver token];
-[TUNotifyObserver lock];
-[TUNotifyObserver setToken:];
-[TUNotifyObserver endObserving];
-[TUNotifyObserver state];
-[TUNotifyObserver beginObserving];
-[TUNotifyObserver initWithNotificationName:queue:];
-[TUNotifyObserver _endObserving];
-[TUNotifyObserver initWithNotificationName:queue:callback:];
```
