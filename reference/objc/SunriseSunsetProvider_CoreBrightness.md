# `SunriseSunsetProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
B _cancelled;
@"_CDClientContext" _duetContextStore;
@"_CDContextualKeyPath" _duetKeyPath;
@"_CDContextualChangeRegistration" _duetRegistration;
@"NSObject<OS_dispatch_semaphore>" _duetDispatchSemaphore;
B _sunriseSunsetNotificationEnabled;
@? _callbackBlock;
@? _duetCallback;
@"_CDContextualPredicate" _predicate;
```

## Instance methods

```
-[SunriseSunsetProvider dealloc];
-[SunriseSunsetProvider cancel];
-[SunriseSunsetProvider initWithCallback:];
-[SunriseSunsetProvider registerBlock:];
-[SunriseSunsetProvider unregisterBlock];
-[SunriseSunsetProvider copySunriseSunsetInfo:];
-[SunriseSunsetProvider copySunsetSunriseInfoFromContext];
-[SunriseSunsetProvider unregisterNotification];
-[SunriseSunsetProvider updateSunriseSunsetInfo];
```
