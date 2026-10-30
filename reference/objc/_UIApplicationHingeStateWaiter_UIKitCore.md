# `_UIApplicationHingeStateWaiter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
{?="orientation"c"magicPoseDeviceOrientation"c"magicPoseHingeState"c"magicPoseTabletopPose"c} _previousState;
@? _callbackBlock;
```

## Properties

```
@property (T@?,R,C,V_callbackBlock) callbackBlock;
```

## Instance methods

```
-[_UIApplicationHingeStateWaiter dealloc];
-[_UIApplicationHingeStateWaiter initWithBlock:];
-[_UIApplicationHingeStateWaiter _checkForHingePoseStateChange];
-[_UIApplicationHingeStateWaiter callbackBlock];
```
