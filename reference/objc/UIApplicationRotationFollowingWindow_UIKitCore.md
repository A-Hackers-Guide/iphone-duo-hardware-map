# `UIApplicationRotationFollowingWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- 2 instance variables, 2 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _limitToWindowLevel;
q _priorityLevel;
```

## Properties

```
@property (Tq,N,V_priorityLevel) priorityLevel;
@property (TB,N,V_limitToWindowLevel) limitToWindowLevel;
```

## Class methods

```
+[UIApplicationRotationFollowingWindow _isSystemWindow];
```

## Instance methods

```
-[UIApplicationRotationFollowingWindow init];
-[UIApplicationRotationFollowingWindow initWithWindowScene:];
-[UIApplicationRotationFollowingWindow _shouldAutorotateToInterfaceOrientation:];
-[UIApplicationRotationFollowingWindow _shouldControlAutorotation];
-[UIApplicationRotationFollowingWindow isInterfaceAutorotationDisabled];
-[UIApplicationRotationFollowingWindow __autorotationSanityCheckObjectFromSource:selector:];
-[UIApplicationRotationFollowingWindow _commonApplicationRotationFollowingWindowInit];
-[UIApplicationRotationFollowingWindow _handleStatusBarOrientationChange:];
-[UIApplicationRotationFollowingWindow _initWithFrame:attached:];
-[UIApplicationRotationFollowingWindow _initWithFrame:debugName:attached:];
-[UIApplicationRotationFollowingWindow _initWithFrame:debugName:displayConfiguration:];
-[UIApplicationRotationFollowingWindow _initWithFrame:debugName:scene:attached:];
-[UIApplicationRotationFollowingWindow _initWithFrame:debugName:windowScene:];
-[UIApplicationRotationFollowingWindow _topMostWindow];
-[UIApplicationRotationFollowingWindow applicationWindow:didRotateWithOrientation:duration:];
-[UIApplicationRotationFollowingWindow limitToWindowLevel];
-[UIApplicationRotationFollowingWindow priorityLevel];
-[UIApplicationRotationFollowingWindow setLimitToWindowLevel:];
-[UIApplicationRotationFollowingWindow setPriorityLevel:];
```
