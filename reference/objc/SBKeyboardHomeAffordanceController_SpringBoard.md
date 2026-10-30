# `SBKeyboardHomeAffordanceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHomeGrabberDelegate`, `SBSceneHandleObserver`, `SBUIActiveOrientationObserver`, `SBMedusaHostedKeyboardWindowControllerObserver`
- 5 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _assertions;
@"SBHomeGrabberRotationView" _homeGrabberView;
B _isHomeGrabberContainingViewAlwaysPortrait;
B _isKeyboardDocked;
@"SBKeyboardHomeAffordanceAssertion" _topMostAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardHomeAffordanceController sharedInstance];
```

## Instance methods

```
-[SBKeyboardHomeAffordanceController activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBKeyboardHomeAffordanceController _keyboardWillChangeFrame:];
-[SBKeyboardHomeAffordanceController init];
-[SBKeyboardHomeAffordanceController dealloc];
-[SBKeyboardHomeAffordanceController activeInterfaceOrientationWillChangeToOrientation:];
-[SBKeyboardHomeAffordanceController shouldAllowThinStyleForHomeGrabberView:];
-[SBKeyboardHomeAffordanceController additionalEdgeSpacingForHomeGrabberView:];
-[SBKeyboardHomeAffordanceController shouldAllowAutoHideForHomeGrabberView:];
-[SBKeyboardHomeAffordanceController unregisterAssertion:];
-[SBKeyboardHomeAffordanceController _updateHomeAffordance];
-[SBKeyboardHomeAffordanceController _didChangeAdditionalEdgeMarginForAssertion:];
-[SBKeyboardHomeAffordanceController _getHomeGrabberContainingView:isAlwaysPortrait:];
-[SBKeyboardHomeAffordanceController _updateTopMostAssertion];
-[SBKeyboardHomeAffordanceController registerAssertion:];
-[SBKeyboardHomeAffordanceController usingMedusaHostedKeyboardWindowDidChange];
```
