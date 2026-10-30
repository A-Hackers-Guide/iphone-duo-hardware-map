# `BLSHTTRWatchdogConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
B _enabledByDefault;
d _timeout;
d _leeway;
@"NSString" _timerIdentifier;
```

## Properties

```
@property (T@"NSString",&,V_timerIdentifier) timerIdentifier;
@property (T@"NSString",&) identifier;
@property (Td,V_timeout) timeout;
@property (Td,V_leeway) leeway;
@property (TB,V_enabledByDefault) enabledByDefault;
```

## Instance methods

```
-[BLSHTTRWatchdogConfiguration identifier];
-[BLSHTTRWatchdogConfiguration leeway];
-[BLSHTTRWatchdogConfiguration setLeeway:];
-[BLSHTTRWatchdogConfiguration timeout];
-[BLSHTTRWatchdogConfiguration setIdentifier:];
-[BLSHTTRWatchdogConfiguration setTimeout:];
-[BLSHTTRWatchdogConfiguration setEnabledByDefault:];
-[BLSHTTRWatchdogConfiguration enabledByDefault];
-[BLSHTTRWatchdogConfiguration timerIdentifier];
-[BLSHTTRWatchdogConfiguration setTimerIdentifier:];
```
