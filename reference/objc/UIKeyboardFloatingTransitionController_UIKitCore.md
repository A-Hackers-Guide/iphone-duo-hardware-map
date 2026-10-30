# `UIKeyboardFloatingTransitionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 23 instance variables, 26 properties, 73 instance methods, 4 class methods

## Instance variables

```
B _initWithStateBasedAnimations;
B _isTransitioning;
B _startedFromFloating;
B _withinDockingRegion;
B _expandedForDocking;
@"<UIKeyboardFloatingTransitionControllerDelegate>" _delegate;
@"UIKeyboardFloatingPinchGestureRecognizer" _pinchGestureRecognizer;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UIInputWindowController" _inputWindowController;
@"UIKeyboardFloatingTransitionState" _startState;
@"UIKeyboardFloatingTransitionState" _endState;
@"NSArray" _commonVisibleKeys;
@"UIView" _platterView;
@"UIView" _platterCornerRadiusView;
@"_UIPopoverStandardChromeView" _platterPopoverBackgroundView;
@"UIKBInputBackdropView" _platterVisualEffectView;
@"_UIKBLightEffectsBackground" _lightEffectsTransitionBackdrop;
@"UIView" _pillView;
d _progress;
d _gestureBeginTime;
@"UIViewSpringAnimationBehavior" _animationBehavior;
@"NSMapTable" _activeKeyboardLayoutGuideTransitionAssertions;
{CGPoint="x"d"y"d} _lastGestureCenter;
```

## Properties

```
@property (T@"UIKeyboardFloatingPinchGestureRecognizer",&,N,V_pinchGestureRecognizer) pinchGestureRecognizer;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (TB,N,V_isTransitioning) isTransitioning;
@property (T@"UIInputWindowController",W,N,V_inputWindowController) inputWindowController;
@property (T@"UIKeyboardFloatingTransitionState",&,N,V_startState) startState;
@property (T@"UIKeyboardFloatingTransitionState",&,N,V_endState) endState;
@property (TB,N,V_startedFromFloating) startedFromFloating;
@property (T@"NSArray",&,N,V_commonVisibleKeys) commonVisibleKeys;
@property (T@"UIView",&,N,V_platterView) platterView;
@property (T@"UIView",&,N,V_platterCornerRadiusView) platterCornerRadiusView;
@property (T@"_UIPopoverStandardChromeView",&,N,V_platterPopoverBackgroundView) platterPopoverBackgroundView;
@property (T@"UIKBInputBackdropView",&,N,V_platterVisualEffectView) platterVisualEffectView;
@property (T@"_UIKBLightEffectsBackground",&,N,V_lightEffectsTransitionBackdrop) lightEffectsTransitionBackdrop;
@property (T@"UIView",&,N,V_pillView) pillView;
@property (Td,N,V_progress) progress;
@property (Td,N,V_gestureBeginTime) gestureBeginTime;
@property (T{CGPoint=dd},N,V_lastGestureCenter) lastGestureCenter;
@property (TB,N,V_withinDockingRegion) withinDockingRegion;
@property (TB,N,V_expandedForDocking) expandedForDocking;
@property (T@"UIViewSpringAnimationBehavior",&,V_animationBehavior) animationBehavior;
@property (T@"NSMapTable",&,N,V_activeKeyboardLayoutGuideTransitionAssertions) activeKeyboardLayoutGuideTransitionAssertions;
@property (T@"<UIKeyboardFloatingTransitionControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardFloatingTransitionController dockingRegion];
+[UIKeyboardFloatingTransitionController isPointWithinDockingRegion:];
+[UIKeyboardFloatingTransitionController magneticEdgeMargin];
+[UIKeyboardFloatingTransitionController snapshotOfKeyplaneView:];
```

## Instance methods

```
-[UIKeyboardFloatingTransitionController platterView];
-[UIKeyboardFloatingTransitionController panGestureRecognizer];
-[UIKeyboardFloatingTransitionController pillView];
-[UIKeyboardFloatingTransitionController setPillView:];
-[UIKeyboardFloatingTransitionController setPanGestureRecognizer:];
-[UIKeyboardFloatingTransitionController setPlatterView:];
-[UIKeyboardFloatingTransitionController setProgress:];
-[UIKeyboardFloatingTransitionController startState];
-[UIKeyboardFloatingTransitionController isTransitioning];
-[UIKeyboardFloatingTransitionController animationBehavior];
-[UIKeyboardFloatingTransitionController progress];
-[UIKeyboardFloatingTransitionController setDelegate:];
-[UIKeyboardFloatingTransitionController gestureRecognizerShouldBegin:];
-[UIKeyboardFloatingTransitionController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIKeyboardFloatingTransitionController delegate];
-[UIKeyboardFloatingTransitionController setIsTransitioning:];
-[UIKeyboardFloatingTransitionController inputWindowController];
-[UIKeyboardFloatingTransitionController pinchGestureRecognizer];
-[UIKeyboardFloatingTransitionController setPinchGestureRecognizer:];
-[UIKeyboardFloatingTransitionController endTransitionAtPoint:withScale:];
-[UIKeyboardFloatingTransitionController restoreAccessoryViewConstraints];
-[UIKeyboardFloatingTransitionController activeKeyboardLayoutGuideTransitionAssertions];
-[UIKeyboardFloatingTransitionController addGestureRecognizersToView:];
-[UIKeyboardFloatingTransitionController beginPanGesture:];
-[UIKeyboardFloatingTransitionController beginPinchGesture:];
-[UIKeyboardFloatingTransitionController beginTransitionAtPoint:withScale:recognizer:];
-[UIKeyboardFloatingTransitionController beginTransitionFromPanGestureRecognizer:];
-[UIKeyboardFloatingTransitionController captureStateForStart:];
-[UIKeyboardFloatingTransitionController commonVisibleKeys];
-[UIKeyboardFloatingTransitionController constrainAccessoryViewToBottom];
-[UIKeyboardFloatingTransitionController endPanGesture:];
-[UIKeyboardFloatingTransitionController endPinchGesture:];
-[UIKeyboardFloatingTransitionController endState];
-[UIKeyboardFloatingTransitionController expandedForDocking];
-[UIKeyboardFloatingTransitionController finalizeTransition];
-[UIKeyboardFloatingTransitionController gestureBeginTime];
-[UIKeyboardFloatingTransitionController handlePanGestureRecognizerAction:];
-[UIKeyboardFloatingTransitionController handlePinchGestureRecognizerAction:];
-[UIKeyboardFloatingTransitionController initializeContextAtPoint:recognizer:];
-[UIKeyboardFloatingTransitionController inputViewSnapshot:withPlatterInsets:];
-[UIKeyboardFloatingTransitionController lastGestureCenter];
-[UIKeyboardFloatingTransitionController lightEffectsTransitionBackdrop];
-[UIKeyboardFloatingTransitionController platterCornerRadiusView];
-[UIKeyboardFloatingTransitionController platterPopoverBackgroundView];
-[UIKeyboardFloatingTransitionController platterVisualEffectView];
-[UIKeyboardFloatingTransitionController removeGestureRecognizers];
-[UIKeyboardFloatingTransitionController setActiveKeyboardLayoutGuideTransitionAssertions:];
-[UIKeyboardFloatingTransitionController setAnimationBehavior:];
-[UIKeyboardFloatingTransitionController setCommonVisibleKeys:];
-[UIKeyboardFloatingTransitionController setEndState:];
-[UIKeyboardFloatingTransitionController setExpandedForDocking:];
-[UIKeyboardFloatingTransitionController setGestureBeginTime:];
-[UIKeyboardFloatingTransitionController setInputWindowController:];
-[UIKeyboardFloatingTransitionController setKeyboardLayoutGuideInTransition:forWindow:];
-[UIKeyboardFloatingTransitionController setLastGestureCenter:];
-[UIKeyboardFloatingTransitionController setLightEffectsTransitionBackdrop:];
-[UIKeyboardFloatingTransitionController setPlatterCornerRadiusView:];
-[UIKeyboardFloatingTransitionController setPlatterPopoverBackgroundView:];
-[UIKeyboardFloatingTransitionController setPlatterVisualEffectView:];
-[UIKeyboardFloatingTransitionController setStartState:];
-[UIKeyboardFloatingTransitionController setStartedFromFloating:];
-[UIKeyboardFloatingTransitionController setWithinDockingRegion:];
-[UIKeyboardFloatingTransitionController startedFromFloating];
-[UIKeyboardFloatingTransitionController updateAnimationAtScale:];
-[UIKeyboardFloatingTransitionController updateHysteresisForCurrentFloatingState];
-[UIKeyboardFloatingTransitionController updateLayoutGuideForTransitionStart:];
-[UIKeyboardFloatingTransitionController updateLayoutGuideFromFrame:];
-[UIKeyboardFloatingTransitionController updateOffsetForProgressToFull:isFloating:duringInteraction:];
-[UIKeyboardFloatingTransitionController updatePanGesture:];
-[UIKeyboardFloatingTransitionController updatePinchGesture:];
-[UIKeyboardFloatingTransitionController updateTransitionAtPoint:withScale:interactive:];
-[UIKeyboardFloatingTransitionController useStateBasedAnimations];
-[UIKeyboardFloatingTransitionController withinDockingRegion];
```
