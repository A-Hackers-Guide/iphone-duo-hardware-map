# `_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP23LocalAuthenticationCore27LACAutoLockSnatchMonitoring_`
- 8 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
_$sSd gForceThreshold;
_$sSd cooldownSeconds;
(objc_protocol 0x206838f30) accelerometerProvider;
DispatchQueue workQueue;
_$sSo11NSHashTableC 8 observers;
Swift.Bool isMonitoringActive;
Swift.Bool isCoolingDown;
_$sSu monitoringGeneration;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor startMonitoring];
-[_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor removeObserver:];
-[_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor stopMonitoring];
-[_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor addObserver:];
```
