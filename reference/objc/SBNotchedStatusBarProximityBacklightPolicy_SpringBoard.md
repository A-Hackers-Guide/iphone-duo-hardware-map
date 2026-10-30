# `SBNotchedStatusBarProximityBacklightPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDefaultProximityBacklightPolicy`
- Protocols: `SBNotchedStatusBarProximityBacklightPolicyEnablementConditionDelegate`, `_SBProximityTouchHandlingDelegate`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBProximityTouchHandlingController" _proxTouchHandlingController;
@"SBNotchedStatusBarProximityBacklightPolicyEnablementCondition" _enablementCondition;
Q _timesEnabledWithObjectInProximity;
Q _touchesReceivedWithObjectInProximity;
B _objectInProximity;
@"SBProximitySettings" _proximitySettings;
```

## Properties

```
@property (T@"SBProximitySettings",&,N,G_proximitySettings,S_setProximitySettings:,V_proximitySettings) proximitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNotchedStatusBarProximityBacklightPolicy dealloc];
-[SBNotchedStatusBarProximityBacklightPolicy initWithConfiguration:];
-[SBNotchedStatusBarProximityBacklightPolicy windowSceneDidConnect:];
-[SBNotchedStatusBarProximityBacklightPolicy _absorbTouchesBelowStatusBarHeight];
-[SBNotchedStatusBarProximityBacklightPolicy _absorbTouchesFullScreen];
-[SBNotchedStatusBarProximityBacklightPolicy _createNewEnablementCondition];
-[SBNotchedStatusBarProximityBacklightPolicy _debounceDurationForNumberOfTouchesReceivedWithObjectInProximity:];
-[SBNotchedStatusBarProximityBacklightPolicy _proximitySettings];
-[SBNotchedStatusBarProximityBacklightPolicy _scheduleBacklightFactorToZeroAfterDebounceDuration:];
-[SBNotchedStatusBarProximityBacklightPolicy _setProximitySettings:];
-[SBNotchedStatusBarProximityBacklightPolicy _stopAbsorbingTouches];
-[SBNotchedStatusBarProximityBacklightPolicy condition:enablementDidChange:];
-[SBNotchedStatusBarProximityBacklightPolicy didHitAllowedRegion:];
-[SBNotchedStatusBarProximityBacklightPolicy initWithConfiguration:touchHandlingController:];
-[SBNotchedStatusBarProximityBacklightPolicy proximitySensorManager:objectWithinProximityDidChange:];
```
