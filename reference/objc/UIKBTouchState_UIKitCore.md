# `UIKBTouchState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 13 instance methods, 7 class methods

## Instance variables

```
d _timestamp;
q _phase;
@"UIWindow" _window;
d _pathMajorRadius;
Q _pathIndex;
@"NSUUID" _touchUUID;
Q _tapCount;
q _inputSource;
@"UITouch" _uiTouch;
{CGPoint="x"d"y"d} _locationInWindow;
```

## Properties

```
@property (Td,R,N,V_timestamp) timestamp;
@property (Tq,R,N,V_phase) phase;
@property (T@"UIWindow",R,N,V_window) window;
@property (T{CGPoint=dd},R,N,V_locationInWindow) locationInWindow;
@property (Td,R,N,V_pathMajorRadius) pathMajorRadius;
@property (TQ,R,N,V_pathIndex) pathIndex;
@property (T@"NSUUID",R,N,V_touchUUID) touchUUID;
@property (TQ,R,N,V_tapCount) tapCount;
@property (Tq,R,N,V_inputSource) inputSource;
@property (T@"UITouch",R,W,N,V_uiTouch) uiTouch;
```

## Class methods

```
+[UIKBTouchState releaseUUIDForTouch:];
+[UIKBTouchState touchForTouchUUID:];
+[UIKBTouchState touchStateForTouch:];
+[UIKBTouchState touchStateForTouchUUID:withTimestamp:phase:location:pathIndex:inView:];
+[UIKBTouchState touchUUIDForTouch:];
+[UIKBTouchState touchUUIDsForTouches:];
+[UIKBTouchState touchesForTouchUUIDs:];
```

## Instance methods

```
-[UIKBTouchState phase];
-[UIKBTouchState timestamp];
-[UIKBTouchState window];
-[UIKBTouchState locationInView:];
-[UIKBTouchState description];
-[UIKBTouchState copyWithZone:];
-[UIKBTouchState pathIndex];
-[UIKBTouchState locationInWindow];
-[UIKBTouchState touchUUID];
-[UIKBTouchState tapCount];
-[UIKBTouchState pathMajorRadius];
-[UIKBTouchState uiTouch];
-[UIKBTouchState inputSource];
```
