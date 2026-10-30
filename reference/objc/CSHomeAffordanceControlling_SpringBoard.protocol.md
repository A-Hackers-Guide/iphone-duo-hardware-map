# `CSHomeAffordanceControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"UIPanGestureRecognizer",R,N) screenEdgePanGesture;
@property (T@"BSAnimationSettings",R,N) hideHomeAffordanceAnimationSettings;
@property (T@"BSAnimationSettings",R,N) unhideHomeAffordanceAnimationSettings;
@property (T@"<UIViewSpringAnimationBehaviorDescribing>",R,N) settleHomeAffordanceAnimationBehaviorDescription;
```

## Instance methods

```
-[CSHomeAffordanceControlling hideHomeAffordanceAnimationSettings];
-[CSHomeAffordanceControlling keyboardAssertionForGestureWindow:];
-[CSHomeAffordanceControlling registerHomeGestureParticipant:withIdentifier:];
-[CSHomeAffordanceControlling screenEdgePanGesture];
-[CSHomeAffordanceControlling settleHomeAffordanceAnimationBehaviorDescription];
-[CSHomeAffordanceControlling unhideHomeAffordanceAnimationSettings];
-[CSHomeAffordanceControlling unregisterHomeGestureParticipant:withIdentifier:];
```
