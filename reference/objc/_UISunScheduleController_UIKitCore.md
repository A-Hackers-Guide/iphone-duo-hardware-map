# `_UISunScheduleController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 8 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _observers;
@"GEOAlmanac" _almanac;
B _hasTimeZoneLocation;
{?="latitude"d"longitude"d} _timeZoneLocation;
B _inScheduleTime;
@"NSTimer" _nextEventTimer;
d _sunsetAbsolute;
d _sunriseAbsolute;
```

## Properties

```
@property (TB,R,N,GisInScheduleTime) inScheduleTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISunScheduleController _updateStatus];
-[_UISunScheduleController debugDescription];
-[_UISunScheduleController _significantTimeChange];
-[_UISunScheduleController succinctDescriptionBuilder];
-[_UISunScheduleController removeObserver:];
-[_UISunScheduleController init];
-[_UISunScheduleController dealloc];
-[_UISunScheduleController forceUpdate];
-[_UISunScheduleController descriptionWithMultilinePrefix:];
-[_UISunScheduleController succinctDescription];
-[_UISunScheduleController description];
-[_UISunScheduleController descriptionBuilderWithMultilinePrefix:];
-[_UISunScheduleController nextTransition:];
-[_UISunScheduleController _timeZoneChange];
-[_UISunScheduleController _invalidateNextEventTimer];
-[_UISunScheduleController _notifyChange];
-[_UISunScheduleController _setNextEventTimerToAbsoluteTime:];
-[_UISunScheduleController _updateGeoCity];
-[_UISunScheduleController _updateInScheduleTime:];
-[_UISunScheduleController _updateStatusWithAbsoluteTime:];
-[_UISunScheduleController _updateSunriseSunsetTimesRelativeTo:];
-[_UISunScheduleController addObserver:changeHandler:];
-[_UISunScheduleController isInScheduleTime];
```
