# `_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACKeyBagObserver`, `_TtP23LocalAuthenticationCore27LACAutoLockKeybagMonitoring_`
- 5 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
DispatchQueue workQueue;
(objc_protocol 0x20683c160) keybag;
_$sSo11NSHashTableC (objc_protocol 0x20683c100) observers;
LocalAuthenticationCore.LACAtomic Swift.Bool _isKeybagUnlocked;
Swift.Bool isMonitoring;
```

## Properties

```
@property (TB,N,R) isUnlocked;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor startMonitoring];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor removeObserver:];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor init];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor stopMonitoring];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor addObserver:];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor isUnlocked];
-[_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor keybagStateDidChange:];
```
