# `BKUIOrientationStateHandler`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
i _rawOrientationToken;
i _orientationLockToken;
i _rotationLockNotificationToken;
i _orientationNotificationToken;
q _lastKownOrientation;
```

## Properties

```
@property (Ti,N,V_rawOrientationToken) rawOrientationToken;
@property (Ti,N,V_orientationLockToken) orientationLockToken;
@property (Ti,N,V_rotationLockNotificationToken) rotationLockNotificationToken;
@property (Ti,N,V_orientationNotificationToken) orientationNotificationToken;
@property (Tq,N,V_lastKownOrientation) lastKownOrientation;
```

## Class methods

```
+[BKUIOrientationStateHandler bkui_getState:];
```

## Instance methods

```
-[BKUIOrientationStateHandler init];
-[BKUIOrientationStateHandler dealloc];
-[BKUIOrientationStateHandler rawDeviceOrientationIgnoringOrientationLocks];
-[BKUIOrientationStateHandler _invalidateTokenIfNeeded:];
-[BKUIOrientationStateHandler lastKownOrientation];
-[BKUIOrientationStateHandler orientationLockToken];
-[BKUIOrientationStateHandler orientationNotificationToken];
-[BKUIOrientationStateHandler rawOrientationToken];
-[BKUIOrientationStateHandler registerRotationLockObserver:];
-[BKUIOrientationStateHandler registerRotationObserver:];
-[BKUIOrientationStateHandler rotationLockNotificationToken];
-[BKUIOrientationStateHandler rotationLockStatusIsLocked];
-[BKUIOrientationStateHandler setLastKownOrientation:];
-[BKUIOrientationStateHandler setOrientationLockToken:];
-[BKUIOrientationStateHandler setOrientationNotificationToken:];
-[BKUIOrientationStateHandler setRawOrientationToken:];
-[BKUIOrientationStateHandler setRotationLockNotificationToken:];
```
