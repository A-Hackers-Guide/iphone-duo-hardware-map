# `SBHomeGrabberView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyPathObserver`, `SBAssistantSceneControllingObserver`, `SBAttentionAwarenessClientDelegate`, `MTLumaDodgePillBackgroundLuminanceObserver`, `SBFSystemPointerInteractionDelegate`, `SBMousePointerHardwareConnectionObserver`, `SBFHomeAffordanceInteractionDelegate`
- 34 instance variables, 16 properties, 86 instance methods, 2 class methods

## Instance variables

```
@"SBFHomeGrabberSettings" _settings;
@"MTLumaDodgePillSettings" _pillSettings;
@"SBFHomeAffordanceView" _homeAffordanceView;
@"MTLumaDodgePillView" _pillView;
@"UIView" _hitTestRectVisualizationView;
@"UIView" _touchHitTestBlockingView;
B _touchHitTestBlockingViewBlocksTouches;
@"UIView" _pointerHitTestBlockingView;
q _outstandingHintAnimationCount;
@"SBAttentionAwarenessClient" _idleTouchAwarenessClient;
q _touchState;
Q _lastActivatingToken;
Q _lastInitialHideToken;
B _autoHides;
B _edgeProtectEnabled;
B _shouldEnableGestures;
@"NSMutableSet" _hiddenOverrides;
q _luma;
q _presence;
q _style;
Q _lastVisibilityTransitionToken;
@"NSMutableSet" _outstandingVisibilityTransitionTokens;
B _isSystemPointerInteractionEnabled;
@"NSHashTable" _observers;
@"<SBFHomeAffordanceInteraction>" _homeAffordanceInteraction;
@"SBSystemPointerInteractionManager" _systemPointerInteractionManager;
@"<SBAssistantSceneControlling>" _assistantController;
B _homeAffordanceInteractionEnabled;
B _ignoresLuminance;
B _suppressesBounce;
@"<SBHomeGrabberDelegate>" _delegate;
q _colorBias;
q _behavior;
@"<SBHomeGrabberPointerClickDelegate>" _pointerClickDelegate;
```

## Properties

```
@property (T@"<SBHomeGrabberDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N,V_pointerClickDelegate) pointerClickDelegate;
@property (TB,N) autoHides;
@property (TB,N,GisEdgeProtectEnabled,V_edgeProtectEnabled) edgeProtectEnabled;
@property (Tq,N,V_colorBias) colorBias;
@property (TB,N,V_ignoresLuminance) ignoresLuminance;
@property (TB,N,GisHomeAffordanceInteractionEnabled,V_homeAffordanceInteractionEnabled) homeAffordanceInteractionEnabled;
@property (TB,N,V_suppressesBounce) suppressesBounce;
@property (Tq,N,V_behavior) behavior;
@property (Td,R,N) suggestedEdgeSpacing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) grabberFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) grabberHitTestRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBHomeGrabberView defaultBehavior];
+[SBHomeGrabberView wantsAutoHideAlwaysEnabled];
```

## Instance methods

```
-[SBHomeGrabberView clientDidResetForUserAttention:withEvent:];
-[SBHomeGrabberView homeAffordanceInteractionDidRecognizeSingleClick:];
-[SBHomeGrabberView suggestedSizeForContentWidth:];
-[SBHomeGrabberView _updateHomeAffordanceInteraction];
-[SBHomeGrabberView _animationSettingsForTransitionFromStyle:toStyle:fromPresence:toPresence:];
-[SBHomeGrabberView homeAffordanceInteractionDidFailToRecognizeDoubleTap:];
-[SBHomeGrabberView _calculatePresence];
-[SBHomeGrabberView _effectiveLumaDodgePillSettings];
-[SBHomeGrabberView _edgeProtectEffectivelyEnabled];
-[SBHomeGrabberView homeAffordanceInteractionDidRecognizeDoubleTap:];
-[SBHomeGrabberView _newHomeAffordanceView];
-[SBHomeGrabberView didMoveToWindow];
-[SBHomeGrabberView isHomeAffordanceInteractionEnabled];
-[SBHomeGrabberView homeAffordanceInteractionAllowsUserInteraction:];
-[SBHomeGrabberView suggestedEdgeSpacing];
-[SBHomeGrabberView styleForRegion:forView:];
-[SBHomeGrabberView regionAtLocation:forView:];
-[SBHomeGrabberView homeAffordanceInteractionDidRecognizeSingleTap:];
-[SBHomeGrabberView setPointerClickDelegate:];
-[SBHomeGrabberView setHomeAffordanceInteractionEnabled:];
-[SBHomeGrabberView colorBias];
-[SBHomeGrabberView client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBHomeGrabberView suppressesBounce];
-[SBHomeGrabberView homeAffordanceFrameForHomeAffordanceInteraction:];
-[SBHomeGrabberView setColorBias:];
-[SBHomeGrabberView assistantDidChangeHomeAffordanceDoubleTapGestureEnablement:];
-[SBHomeGrabberView setHidden:];
-[SBHomeGrabberView setIgnoresLuminance:];
-[SBHomeGrabberView removeObserver:];
-[SBHomeGrabberView _autohideEffectivelyEnabled];
-[SBHomeGrabberView _setSystemPointerInteractionEnabled:];
-[SBHomeGrabberView _updatePresence:style:withAnimationSettings:];
-[SBHomeGrabberView autoHides];
-[SBHomeGrabberView _updateIdleTouchAwarenessClient];
-[SBHomeGrabberView homeAffordanceInteraction:didRecognizeTouchThatShouldUnhideViewImmediately:];
-[SBHomeGrabberView initWithFrame:settings:shouldEnableGestures:];
-[SBHomeGrabberView _effectiveHomeAffordanceViewFrame];
-[SBHomeGrabberView resetAutoHideWithInitialDelay:];
-[SBHomeGrabberView _screenForPillViewGeometry];
-[SBHomeGrabberView pointerClickDelegate];
-[SBHomeGrabberView dealloc];
-[SBHomeGrabberView turnOffAutoHideWithDelay:];
-[SBHomeGrabberView updateStyleWithAnimationSettings:];
-[SBHomeGrabberView layoutSubviews];
-[SBHomeGrabberView _updateHitTestRectVisualizationView];
-[SBHomeGrabberView hitTest:withEvent:];
-[SBHomeGrabberView grabberFrame];
-[SBHomeGrabberView resetAutoHide];
-[SBHomeGrabberView homeAffordanceInteractionHomeAffordanceHitTestRectDidChange:];
-[SBHomeGrabberView ignoresLuminance];
-[SBHomeGrabberView shouldBeginPointerInteractionRequest:atLocation:forView:];
-[SBHomeGrabberView _hasOutstandingAnimations];
-[SBHomeGrabberView _hintStyleForWindowScene:];
-[SBHomeGrabberView grabberFrameForBounds:];
-[SBHomeGrabberView addObserver:];
-[SBHomeGrabberView lumaDodgePillDidDetectBackgroundLuminanceChange:];
-[SBHomeGrabberView setDelegate:];
-[SBHomeGrabberView setBehavior:];
-[SBHomeGrabberView behavior];
-[SBHomeGrabberView isHidden];
-[SBHomeGrabberView willMoveToWindow:];
-[SBHomeGrabberView mousePointerManager:hardwarePointingDeviceAttachedDidChange:];
-[SBHomeGrabberView grabberHitTestRect];
-[SBHomeGrabberView forgetBackgroundLuminance];
-[SBHomeGrabberView delegate];
-[SBHomeGrabberView standardHomeAffordanceHitTestRectOutsetsForHomeAffordanceInteraction:];
-[SBHomeGrabberView initWithFrame:shouldEnableGestures:];
-[SBHomeGrabberView isEdgeProtectEnabled];
-[SBHomeGrabberView _outstandingAnimationCount];
-[SBHomeGrabberView initWithCoder:];
-[SBHomeGrabberView _calculateStyle];
-[SBHomeGrabberView updateStyle];
-[SBHomeGrabberView _newPillView];
-[SBHomeGrabberView _pointerInteractionHitTestRect];
-[SBHomeGrabberView _updateTouchHitTestBlockingView];
-[SBHomeGrabberView setAutoHides:];
-[SBHomeGrabberView _notifyObserversOfDidUpdateHidden];
-[SBHomeGrabberView _calculateLumaStyle];
-[SBHomeGrabberView setSuppressesBounce:];
-[SBHomeGrabberView turnOnAutoHideWithInitialDelay:];
-[SBHomeGrabberView pointerWillExitRegion];
-[SBHomeGrabberView initWithFrame:];
-[SBHomeGrabberView _animateToStyle:disallowAdditive:withAnimationSettings:];
-[SBHomeGrabberView settings:changedValueForKeyPath:];
-[SBHomeGrabberView setEdgeProtectEnabled:];
-[SBHomeGrabberView setHidden:forReason:withAnimationSettings:];
```
