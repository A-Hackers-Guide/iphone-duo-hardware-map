# `_TtC23LocalAuthenticationCore24LACAutoLockNetworkSignal`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP23LocalAuthenticationCore33LACAutoLockNetworkMonitorObserver_`
- 9 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
LocalAuthenticationCore.LACAutoLockSignalDelegate ? delegate;
LocalAuthenticationCore.LACAutoLockSignalIdentifier identifier;
LocalAuthenticationCore.LACAtomic Swift.Bool _isEnabled;
_$sSd threshold;
(objc_protocol 0x20683f140) networkMonitor;
LocalAuthenticationCore.LACAutoLockPeriodTracking networkTracker;
_$sl23LocalAuthenticationCore34LACAutoLockSignalEvaluationCaching_px5ValueAaBPRts_XP _$sSbXj cache;
(objc_protocol 0x20683a7b0) timer;
DispatchQueue workQueue;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore24LACAutoLockNetworkSignal networkDidBecomeReachable:];
-[_TtC23LocalAuthenticationCore24LACAutoLockNetworkSignal networkDidBecomeUnreachable:];
```
