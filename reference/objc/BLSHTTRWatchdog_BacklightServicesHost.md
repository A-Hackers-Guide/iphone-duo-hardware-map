# `BLSHTTRWatchdog`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<BSTimerScheduleQuerying><BSInvalidatable>" _timer;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@? _detailProviderBlock;
@"BLSHTTRWatchdogConfiguration" _configuration;
B _test_forceShowTTRLater;
```

## Instance methods

```
-[BLSHTTRWatchdog startWatchdog];
-[BLSHTTRWatchdog dealloc];
-[BLSHTTRWatchdog stopWatchdog];
-[BLSHTTRWatchdog _watchdogFired:];
-[BLSHTTRWatchdog _setupUserDefaults];
-[BLSHTTRWatchdog _shouldRunWatchdog];
-[BLSHTTRWatchdog _test_enabledViaDefaults];
-[BLSHTTRWatchdog _test_forceShowTTRLater:];
-[BLSHTTRWatchdog _test_forceTryAgainNow];
-[BLSHTTRWatchdog _test_tryAgainState];
-[BLSHTTRWatchdog initWithOSProvider:configurationProvider:detailProvider:];
```
