# `CBRingLight`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
f _currentMinNits;
Q _pendingState;
@"<CBRampManagerI>" _rampManager;
B _overriddenByUser;
@"NSNumber" _lastUserSetBrightness;
Q _state;
```

## Properties

```
@property (TQ,V_state) state;
@property (Tf,R) currentMinNits;
@property (TB,R) isEnabled;
@property (TB,R) isActive;
```

## Class methods

```
+[CBRingLight stateToString:];
```

## Instance methods

```
-[CBRingLight setState:];
-[CBRingLight dealloc];
-[CBRingLight setRampManager:];
-[CBRingLight isEnabled];
-[CBRingLight isActive];
-[CBRingLight initWithDisplayID:];
-[CBRingLight state];
-[CBRingLight currentMinNits];
-[CBRingLight handleDisablementWithPeriod:];
-[CBRingLight handleEnablementWithMinNits:andPeriod:];
-[CBRingLight handleMinNitsChange:andPeriod:];
-[CBRingLight handleMinNitsChangeInternalFor:andPeriod:];
-[CBRingLight handleUserBrightnessChange];
-[CBRingLight handleUserBrightnessCommitForNits:];
-[CBRingLight resetUserAdjustmentState];
-[CBRingLight statusInfo];
-[CBRingLight transitionToDisabledState];
```
