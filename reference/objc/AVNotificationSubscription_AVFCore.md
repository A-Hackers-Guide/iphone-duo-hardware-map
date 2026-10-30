# `AVNotificationSubscription`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCancellable`
- 4 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject" _object;
@ _observerToken;
@? _callback;
^{OpaqueFigSimpleMutex=} _cancelMutex;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVNotificationSubscription dealloc];
-[AVNotificationSubscription description];
-[AVNotificationSubscription cancel];
-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:];
```
