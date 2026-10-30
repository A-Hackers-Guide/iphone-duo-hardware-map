# `CCUIControlCenterSystemAgent` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"UIWindowScene",R,W,N) windowScene;
@property (TQ,R,N) screenType;
```

## Instance methods

```
-[CCUIControlCenterSystemAgent isRestoring];
-[CCUIControlCenterSystemAgent screenType];
-[CCUIControlCenterSystemAgent isRingerMuted];
-[CCUIControlCenterSystemAgent isUILocked];
-[CCUIControlCenterSystemAgent windowScene];
-[CCUIControlCenterSystemAgent isOrientationLocked];
-[CCUIControlCenterSystemAgent isPasscodeLocked];
-[CCUIControlCenterSystemAgent hasApplicationForDisplayID:];
-[CCUIControlCenterSystemAgent hasApplicationPlaceholderForDisplayID:];
-[CCUIControlCenterSystemAgent reasonToDisallowEditing];
-[CCUIControlCenterSystemAgent lockOrientation];
-[CCUIControlCenterSystemAgent observeRingerMutedWithBlock:];
-[CCUIControlCenterSystemAgent setRingerMuted:reason:];
-[CCUIControlCenterSystemAgent unlockOrientation];
```
