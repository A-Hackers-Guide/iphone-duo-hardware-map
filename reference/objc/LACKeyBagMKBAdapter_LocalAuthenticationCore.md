# `LACKeyBagMKBAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenterObserver`, `LACKeyBag`
- 6 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
q _state;
@"LACKeyBagStateProviderMKBAdapter" _keyBagStateProvider;
@"LACKeyBagObserverCollection" _observers;
@"LACDarwinNotificationCenter" _notificationCenter;
I _userId;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
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
-[LACKeyBagMKBAdapter removeObserver:];
-[LACKeyBagMKBAdapter dealloc];
-[LACKeyBagMKBAdapter addObserver:];
-[LACKeyBagMKBAdapter userId];
-[LACKeyBagMKBAdapter state];
-[LACKeyBagMKBAdapter initWithUserId:];
-[LACKeyBagMKBAdapter _addKeybagStatusObserver];
-[LACKeyBagMKBAdapter _removeKeybagStatusObserver];
-[LACKeyBagMKBAdapter _updateKeybagState];
-[LACKeyBagMKBAdapter initWithKeyBagStateProvider:notificationCenter:userId:];
-[LACKeyBagMKBAdapter notificationCenter:didReceiveNotification:];
```
