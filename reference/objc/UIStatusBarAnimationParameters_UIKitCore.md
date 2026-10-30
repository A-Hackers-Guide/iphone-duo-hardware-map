# `UIStatusBarAnimationParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 17 instance methods, 4 class methods

## Instance variables

```
d _duration;
d _delay;
q _curve;
@"<_UIBasicAnimationFactory>" _animationFactory;
B _skipFencing;
d _startTime;
```

## Properties

```
@property (Td,N,V_duration) duration;
@property (Td,N,V_delay) delay;
@property (Tq,N,V_curve) curve;
@property (T@"<_UIBasicAnimationFactory>",&,N,V_animationFactory) animationFactory;
@property (TB,N,V_skipFencing) skipFencing;
@property (Td,N,V_startTime) startTime;
@property (T@"BSAnimationSettings",R,N) bsAnimationSettings;
```

## Class methods

```
+[UIStatusBarAnimationParameters animateWithParameters:fromCurrentState:animations:completion:];
+[UIStatusBarAnimationParameters animateWithParameters:fromCurrentState:frameInterval:animations:completion:];
+[UIStatusBarAnimationParameters fencingAnimation];
+[UIStatusBarAnimationParameters animateWithParameters:animations:completion:];
```

## Instance methods

```
-[UIStatusBarAnimationParameters setAnimationFactory:];
-[UIStatusBarAnimationParameters animationFactory];
-[UIStatusBarAnimationParameters init];
-[UIStatusBarAnimationParameters startTime];
-[UIStatusBarAnimationParameters shouldAnimate];
-[UIStatusBarAnimationParameters initWithDefaultParameters];
-[UIStatusBarAnimationParameters duration];
-[UIStatusBarAnimationParameters delay];
-[UIStatusBarAnimationParameters setStartTime:];
-[UIStatusBarAnimationParameters bsAnimationSettings];
-[UIStatusBarAnimationParameters setDelay:];
-[UIStatusBarAnimationParameters setSkipFencing:];
-[UIStatusBarAnimationParameters skipFencing];
-[UIStatusBarAnimationParameters setDuration:];
-[UIStatusBarAnimationParameters curve];
-[UIStatusBarAnimationParameters setCurve:];
-[UIStatusBarAnimationParameters initWithEmptyParameters];
```
