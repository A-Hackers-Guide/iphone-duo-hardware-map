# `SBControlCenterSystemAgent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCUIControlCenterSystemAgent`
- 2 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBWindowScene" _sbWindowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_sbWindowScene) sbWindowScene;
@property (T@"UIWindowScene",R,W,N) windowScene;
@property (TQ,R,N) screenType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBControlCenterSystemAgent isRestoring];
-[SBControlCenterSystemAgent screenType];
-[SBControlCenterSystemAgent initWithWindowScene:applicationController:];
-[SBControlCenterSystemAgent isRingerMuted];
-[SBControlCenterSystemAgent isUILocked];
-[SBControlCenterSystemAgent windowScene];
-[SBControlCenterSystemAgent isOrientationLocked];
-[SBControlCenterSystemAgent isPasscodeLocked];
-[SBControlCenterSystemAgent hasApplicationForDisplayID:];
-[SBControlCenterSystemAgent hasApplicationPlaceholderForDisplayID:];
-[SBControlCenterSystemAgent reasonToDisallowEditing];
-[SBControlCenterSystemAgent lockOrientation];
-[SBControlCenterSystemAgent observeRingerMutedWithBlock:];
-[SBControlCenterSystemAgent sbWindowScene];
-[SBControlCenterSystemAgent setRingerMuted:reason:];
-[SBControlCenterSystemAgent setSbWindowScene:];
-[SBControlCenterSystemAgent unlockOrientation];
```
