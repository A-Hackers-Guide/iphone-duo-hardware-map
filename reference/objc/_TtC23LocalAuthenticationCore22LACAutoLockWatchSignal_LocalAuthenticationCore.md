# `_TtC23LocalAuthenticationCore22LACAutoLockWatchSignal`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP23LocalAuthenticationCore31LACAutoLockWatchMonitorObserver_`
- 10 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
LocalAuthenticationCore.LACAutoLockSignalDelegate ? delegate;
LocalAuthenticationCore.LACAutoLockSignalIdentifier identifier;
LocalAuthenticationCore.LACAtomic Swift.Bool _isEnabled;
_$sSd threshold;
(objc_protocol 0x20683c848) watchMonitor;
LocalAuthenticationCore.LACAutoLockPeriodTracking watchTracker;
_$sl23LocalAuthenticationCore34LACAutoLockSignalEvaluationCaching_px5ValueAaBPRts_XP _$sSbXj cache;
(objc_protocol 0x20683a7b0) timer;
DispatchQueue workQueue;
LocalAuthenticationCore.LACAtomic _$sSbSg _isDisconnected;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore22LACAutoLockWatchSignal watchDidBecomeReachable:];
-[_TtC23LocalAuthenticationCore22LACAutoLockWatchSignal watchDidBecomeUnreachable:];
```
