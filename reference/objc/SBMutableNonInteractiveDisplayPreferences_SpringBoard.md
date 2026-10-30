# `SBMutableNonInteractiveDisplayPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBNonInteractiveDisplayPreferences`
- 0 instance variables, 10 properties, 2 instance methods, 0 class methods

## Properties

```
@property (TB,D,N,GisActive) active;
@property (T@"SSKContentMode",&,D,N) contentMode;
@property (T@"SSKPowerReasons",&,D,N) powerReasons;
@property (T@"SSKCloningMode",&,D,N) cloningMode;
@property (Tq,D,N) pointScale;
@property (T{CGSize=dd},D,N) resolution;
@property (T{CGSize=dd},D,N) logicalScale;
@property (T@"SSKRefreshRateCriteria",&,D,N) refreshRateCriteria;
@property (T@"SSKOverscanCompensation",&,D,N) overscanCompensation;
@property (T@"SSKHDRMode",&,D,N) hdrMode;
```

## Instance methods

```
-[SBMutableNonInteractiveDisplayPreferences updateForWantsControlOfDisplay:];
-[SBMutableNonInteractiveDisplayPreferences updateForDisplayConfigurationRequest:];
```
