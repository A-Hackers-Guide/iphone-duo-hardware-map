# `_TtC23LocalAuthenticationCore23LACAutoLockKeybagSignal`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP23LocalAuthenticationCore25LACAutoLockKeybagObserver_`
- 10 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
LocalAuthenticationCore.LACAutoLockSignalDelegate ? delegate;
LocalAuthenticationCore.LACAutoLockKeybagSignalDelegate ? keybagDelegate;
LocalAuthenticationCore.LACAutoLockSignalIdentifier identifier;
LocalAuthenticationCore.LACAtomic Swift.Bool _isEnabled;
_$sSd threshold;
(objc_protocol 0x20683c508) keybagMonitor;
LocalAuthenticationCore.LACAutoLockPeriodTracking keybagTracker;
_$sl23LocalAuthenticationCore34LACAutoLockSignalEvaluationCaching_px5ValueAaBPRts_XP _$sSbXj cache;
(objc_protocol 0x20683a7b0) timer;
DispatchQueue workQueue;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore23LACAutoLockKeybagSignal keybagMonitorDidLock:];
-[_TtC23LocalAuthenticationCore23LACAutoLockKeybagSignal keybagMonitorDidUnlock:];
```
