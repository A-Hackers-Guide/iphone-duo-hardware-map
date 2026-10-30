# `SBNonInteractiveDisplayPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 10 instance variables, 14 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _active;
@"SSKContentMode" _contentMode;
@"SSKPowerReasons" _powerReasons;
@"SSKCloningMode" _cloningMode;
q _pointScale;
{CGSize="width"d"height"d} _resolution;
{CGSize="width"d"height"d} _logicalScale;
@"SSKRefreshRateCriteria" _refreshRateCriteria;
@"SSKOverscanCompensation" _overscanCompensation;
@"SSKHDRMode" _hdrMode;
```

## Properties

```
@property (TB,R,N,GisActive,V_active) active;
@property (T@"SSKContentMode",R,N,V_contentMode) contentMode;
@property (T@"SSKPowerReasons",R,N,V_powerReasons) powerReasons;
@property (T@"SSKCloningMode",R,N,V_cloningMode) cloningMode;
@property (Tq,R,N,V_pointScale) pointScale;
@property (T{CGSize=dd},R,N,V_resolution) resolution;
@property (T{CGSize=dd},R,N,V_logicalScale) logicalScale;
@property (T@"SSKRefreshRateCriteria",R,N,V_refreshRateCriteria) refreshRateCriteria;
@property (T@"SSKOverscanCompensation",R,N,V_overscanCompensation) overscanCompensation;
@property (T@"SSKHDRMode",R,N,V_hdrMode) hdrMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBNonInteractiveDisplayPreferences uncontrolledDisplayPreferences];
```

## Instance methods

```
-[SBNonInteractiveDisplayPreferences hdrMode];
-[SBNonInteractiveDisplayPreferences mutableCopyWithZone:];
-[SBNonInteractiveDisplayPreferences contentMode];
-[SBNonInteractiveDisplayPreferences pointScale];
-[SBNonInteractiveDisplayPreferences logicalScale];
-[SBNonInteractiveDisplayPreferences resolution];
-[SBNonInteractiveDisplayPreferences hash];
-[SBNonInteractiveDisplayPreferences description];
-[SBNonInteractiveDisplayPreferences appendDescriptionToStream:];
-[SBNonInteractiveDisplayPreferences isActive];
-[SBNonInteractiveDisplayPreferences copyWithZone:];
-[SBNonInteractiveDisplayPreferences isEqual:];
-[SBNonInteractiveDisplayPreferences overscanCompensation];
-[SBNonInteractiveDisplayPreferences applyToSSKDisplayPreferences:];
-[SBNonInteractiveDisplayPreferences cloningMode];
-[SBNonInteractiveDisplayPreferences powerReasons];
-[SBNonInteractiveDisplayPreferences refreshRateCriteria];
```
