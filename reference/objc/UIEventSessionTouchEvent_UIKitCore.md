# `UIEventSessionTouchEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _touchStatus;
q _touchType;
q _trackpadFingerDownCount;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_touchStatus) touchStatus;
@property (Tq,V_touchType) touchType;
@property (Tq,V_trackpadFingerDownCount) trackpadFingerDownCount;
```

## Instance methods

```
-[UIEventSessionTouchEvent setTouchStatus:];
-[UIEventSessionTouchEvent containsTouchID:];
-[UIEventSessionTouchEvent initWithTouchType:withTrackpadFingerDownCount:];
-[UIEventSessionTouchEvent setTouchType:];
-[UIEventSessionTouchEvent setTrackpadFingerDownCount:];
-[UIEventSessionTouchEvent touchStatus];
-[UIEventSessionTouchEvent touchType];
-[UIEventSessionTouchEvent trackpadFingerDownCount];
```
