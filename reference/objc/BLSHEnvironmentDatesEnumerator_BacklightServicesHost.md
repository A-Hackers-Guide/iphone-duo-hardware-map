# `BLSHEnvironmentDatesEnumerator`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BLSAlwaysOnDateSpecifier" _specifier;
@"NSEnumerator" _enumerator;
@"NSDateInterval" _dateInterval;
@"<BLSHBacklightSceneHostEnvironment>" _environment;
@"BLSHEnvironmentDatesModel" _sourceModel;
```

## Properties

```
@property (T@"BLSAlwaysOnDateSpecifier",&,N,V_specifier) specifier;
@property (T@"NSEnumerator",R,N,V_enumerator) enumerator;
@property (T@"NSDateInterval",R,N,V_dateInterval) dateInterval;
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,N,V_environment) environment;
@property (T@"BLSHEnvironmentDatesModel",R,N,V_sourceModel) sourceModel;
```

## Class methods

```
+[BLSHEnvironmentDatesEnumerator createWithInitialSpecifier:enumerator:dateInterval:environment:sourceModel:];
```

## Instance methods

```
-[BLSHEnvironmentDatesEnumerator dateInterval];
-[BLSHEnvironmentDatesEnumerator specifier];
-[BLSHEnvironmentDatesEnumerator setSpecifier:];
-[BLSHEnvironmentDatesEnumerator enumerator];
-[BLSHEnvironmentDatesEnumerator description];
-[BLSHEnvironmentDatesEnumerator environment];
-[BLSHEnvironmentDatesEnumerator sourceModel];
```
