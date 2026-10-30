# `BLSHWatchdogTester`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _testables;
Q _lock_nextTimerID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHWatchdogProvider" _watchdogProvider;
@"<BLSHWatchdogProviderDelegate>" _watchdogProviderDelegate;
```

## Instance methods

```
-[BLSHWatchdogTester _watchdogProvider];
-[BLSHWatchdogTester _triggerTestWatchdog:];
-[BLSHWatchdogTester initWithWatchdogProviderDelegate:testables:];
```
