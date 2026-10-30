# `SBIdleTimerDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 10 properties, 3 instance methods, 0 class methods

## Properties

```
@property (Td,R,D,N) minimumLockscreenIdleTime;
@property (TB,R,D,N) disableAutoDim;
@property (TB,R,D,N) dontDimOrLockWhileConnectedToPower;
@property (TB,R,D,N) supportLiftToWake;
@property (TB,R,D,N) supportTapToWake;
@property (TB,R,D,N) disableAttentionAwareness;
@property (Td,D,N) notificationVisibleIdleTimer;
@property (Td,D,N) ambientExtendedIdleTimer;
@property (TB,R,D,N) enableDisplayDimTouchSuppressionForAllSurfaces;
@property (TB,R,D,N,GisBacklightLoggingEnabled) backlightLoggingEnabled;
```

## Instance methods

```
-[SBIdleTimerDefaults _bindAndRegisterDefaults];
-[SBIdleTimerDefaults disableAutoDim];
-[SBIdleTimerDefaults disableAutoDimExists];
```
