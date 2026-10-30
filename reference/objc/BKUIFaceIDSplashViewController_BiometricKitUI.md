# `BKUIFaceIDSplashViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBWelcomeController`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _inBuddy;
@"OBTrayButton" _skipButton;
@? _endEnrollActionPrimary;
@? _endEnrollActionSecondary;
@"OBTrayButton" _continueButton;
@"BKDevice" _device;
@"OBAnimationController" _animationController;
```

## Properties

```
@property (TB,N,V_inBuddy) inBuddy;
@property (T@"OBTrayButton",&,N,V_skipButton) skipButton;
@property (T@?,C,N,V_endEnrollActionPrimary) endEnrollActionPrimary;
@property (T@?,C,N,V_endEnrollActionSecondary) endEnrollActionSecondary;
@property (T@"OBTrayButton",&,N,V_continueButton) continueButton;
@property (T@"BKDevice",&,N,V_device) device;
@property (T@"OBAnimationController",&,N,V_animationController) animationController;
```

## Instance methods

```
-[BKUIFaceIDSplashViewController animationController];
-[BKUIFaceIDSplashViewController setDevice:];
-[BKUIFaceIDSplashViewController setSkipButton:];
-[BKUIFaceIDSplashViewController device];
-[BKUIFaceIDSplashViewController viewDidLoad];
-[BKUIFaceIDSplashViewController viewDidAppear:];
-[BKUIFaceIDSplashViewController skipButton];
-[BKUIFaceIDSplashViewController setAnimationController:];
-[BKUIFaceIDSplashViewController continueButton];
-[BKUIFaceIDSplashViewController setContinueButton:];
-[BKUIFaceIDSplashViewController inBuddy];
-[BKUIFaceIDSplashViewController setInBuddy:];
-[BKUIFaceIDSplashViewController _didSelectEnroll];
-[BKUIFaceIDSplashViewController _didSelectSkip];
-[BKUIFaceIDSplashViewController endEnrollActionPrimary];
-[BKUIFaceIDSplashViewController endEnrollActionSecondary];
-[BKUIFaceIDSplashViewController initInBuddy:bkDevice:withEndEnrollmentActionPrimary:enrollmentActionSecondary:];
-[BKUIFaceIDSplashViewController initInBuddy:isDemo:bkDevice:withEndEnrollmentActionPrimary:enrollmentActionSecondary:];
-[BKUIFaceIDSplashViewController setEndEnrollActionPrimary:];
-[BKUIFaceIDSplashViewController setEndEnrollActionSecondary:];
```
