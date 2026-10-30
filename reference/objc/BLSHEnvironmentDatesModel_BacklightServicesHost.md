# `BLSHEnvironmentDatesModel`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _specifiers;
@"NSDateInterval" _dateInterval;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHBacklightSceneHostEnvironment>" _environment;
```

## Properties

```
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,W,N,V_environment) environment;
@property (T@"NSDateInterval",R,N) dateInterval;
@property (T@"NSArray",R,C,N) specifiers;
@property (Tq,R,N) count;
```

## Instance methods

```
-[BLSHEnvironmentDatesModel dateInterval];
-[BLSHEnvironmentDatesModel initWithEnvironment:];
-[BLSHEnvironmentDatesModel count];
-[BLSHEnvironmentDatesModel environment];
-[BLSHEnvironmentDatesModel specifiers];
-[BLSHEnvironmentDatesModel missingIntervalForDateInterval:];
-[BLSHEnvironmentDatesModel clearAllSpecifiers];
-[BLSHEnvironmentDatesModel purgeSpecifiersBefore:];
-[BLSHEnvironmentDatesModel registerSpecifiers:forDateInterval:];
-[BLSHEnvironmentDatesModel specifierForDate:];
```
