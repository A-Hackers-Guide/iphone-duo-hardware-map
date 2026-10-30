# `UIViewPropertyAnimatorTrackingState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _startPaused;
B _scrubsLinearly;
B _userInteractionEnabled;
B _optimizationsEnabled;
B _shouldLayoutSubviews;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TB,N,V_startPaused) startPaused;
@property (TB,N,V_scrubsLinearly) scrubsLinearly;
@property (TB,N,V_userInteractionEnabled) userInteractionEnabled;
@property (TB,N,V_optimizationsEnabled) optimizationsEnabled;
@property (TB,N,V_shouldLayoutSubviews) shouldLayoutSubviews;
```

## Instance methods

```
-[UIViewPropertyAnimatorTrackingState scrubsLinearly];
-[UIViewPropertyAnimatorTrackingState setUserInteractionEnabled:];
-[UIViewPropertyAnimatorTrackingState setScrubsLinearly:];
-[UIViewPropertyAnimatorTrackingState shouldLayoutSubviews];
-[UIViewPropertyAnimatorTrackingState uuid];
-[UIViewPropertyAnimatorTrackingState init];
-[UIViewPropertyAnimatorTrackingState setShouldLayoutSubviews:];
-[UIViewPropertyAnimatorTrackingState startPaused];
-[UIViewPropertyAnimatorTrackingState setStartPaused:];
-[UIViewPropertyAnimatorTrackingState optimizationsEnabled];
-[UIViewPropertyAnimatorTrackingState userInteractionEnabled];
-[UIViewPropertyAnimatorTrackingState setOptimizationsEnabled:];
```
