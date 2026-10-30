# `UIPeripheralHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIScrollViewIntersectionDelegate`, `_UIAssertionControllerSubject`, `UIGestureRecognizerDelegate`
- 29 instance variables, 24 properties, 148 instance methods, 20 class methods

## Instance variables

```
@"UIPeripheralHostView" _hostView;
B _automaticAppearanceEnabled;
B _automaticAppearanceEnabledInternal;
i _ignoredReloads;
i _nextAutomaticOrderInDirection;
B _isTranslating;
B _isUndocked;
B _splitLockState;
@"CADisplayLink" _displayLink;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _targetTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _initialTransform;
{CGPoint="x"d"y"d} _velocity;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastKnownIVFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastKnownIAVFrame;
q _disableAnimationsCount;
@"NSMutableArray" _targetStateStack;
@"UIInputViewSet" _inputViewSet;
@"UIResponder" _responder;
B _animationFencingEnabled;
B _interfaceAutorotationDisabled;
d _ambiguousControlCenterActivationMargin;
@"NSMutableDictionary" _deferredTransitionTasks;
@"_UIAssertionController" _keyboardSuppressionAssertionController;
B _suppressingKeyboardForAssertion;
i _currentState;
@"UIKeyboardRotationState" _rotationState;
@"UIInputViewSet" _transientInputViewSet;
@"NSArray" _allVisibleFrames;
@"UITextInputMode" _documentInputMode;
```

## Properties

```
@property (T@"UIView",R,N) view;
@property (TB,N) automaticAppearanceInternalEnabled;
@property (Td,N) ambiguousControlCenterActivationMargin;
@property (T@"UIResponder",R,D,N) responder;
@property (TB,D,N) animationFencingEnabled;
@property (T@"UIInputViewSet",R,N) inputViews;
@property (T@"UIInputViewSet",R,N) loadAwareInputViews;
@property (TB,R,N) keyClicksEnabled;
@property (T@"UIKeyboardRotationState",&,N,V_rotationState) rotationState;
@property (T@"UIPeripheralHostState",&,N) targetState;
@property (T@"UIResponder",&,N,V_responder) responder;
@property (TB,N,V_animationFencingEnabled) animationFencingEnabled;
@property (TB,R,N) animationsEnabled;
@property (T@"UIInputViewSet",&,N,V_inputViewSet) _inputViews;
@property (T@"UIInputViewSet",&,N,V_transientInputViewSet) _transientInputViews;
@property (T@"NSArray",&,N,V_allVisibleFrames) allVisibleFrames;
@property (Ti,N,V_currentState) currentState;
@property (TB,R,N) automaticAppearanceReallyEnabled;
@property (TB,N,V_automaticAppearanceEnabled) automaticAppearanceEnabled;
@property (T@"UITextInputMode",&,N,V_documentInputMode) documentInputMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPeripheralHost sharedInstance];
+[UIPeripheralHost endPlacementForInputViewSet:windowScene:];
+[UIPeripheralHost allVisibleFrames:];
+[UIPeripheralHost _releaseSharedInstance];
+[UIPeripheralHost visibleInputViewFrame];
+[UIPeripheralHost hostViewClass];
+[UIPeripheralHost defaultUndockedOffset];
+[UIPeripheralHost passthroughViews];
+[UIPeripheralHost allVisiblePeripheralFrames];
+[UIPeripheralHost gridViewRubberBandValueForValue:target:timeInterval:velocity:];
+[UIPeripheralHost floatingChromeBuffer];
+[UIPeripheralHost activeInstance];
+[UIPeripheralHost floatingAssistantBarPlacementClassSupportingCompactStyle:];
+[UIPeripheralHost pointIsWithinKeyboardContent:];
+[UIPeripheralHost setKeyboardOnScreenNotifyKey:];
+[UIPeripheralHost visiblePeripheralFrame];
+[UIPeripheralHost setFloating:onCompletion:];
+[UIPeripheralHost adjustedFloatingOffsetForKeyboardSize:];
+[UIPeripheralHost adjustFloatingPersistentOffsetForKeyboardSize:];
+[UIPeripheralHost setAllVisibleFrames:];
```

## Instance methods

```
-[UIPeripheralHost targetState];
-[UIPeripheralHost _updateContainerWindowLevel];
-[UIPeripheralHost containerRootController];
-[UIPeripheralHost forceOrderInAutomaticAnimated:];
-[UIPeripheralHost _clipCornersOfView:];
-[UIPeripheralHost isTranslating];
-[UIPeripheralHost vendKeyboardSuppressionAssertionForReason:];
-[UIPeripheralHost pushAnimationStyle:];
-[UIPeripheralHost _beginDisablingAnimations];
-[UIPeripheralHost maximizeWithAnimation:];
-[UIPeripheralHost animationsEnabled];
-[UIPeripheralHost transitioningView];
-[UIPeripheralHost containerWindow];
-[UIPeripheralHost performMultipleOperations:withAnimationStyle:];
-[UIPeripheralHost automaticAppearanceEnabled];
-[UIPeripheralHost _endDisablingAnimations];
-[UIPeripheralHost documentInputMode];
-[UIPeripheralHost flushDelayedTasks];
-[UIPeripheralHost extendKeyboardBackdropHeight:withDuration:];
-[UIPeripheralHost _isTransitioning];
-[UIPeripheralHost forceOrderOutAutomaticAnimated:];
-[UIPeripheralHost forceOrderOutAutomaticToDirection:withDuration:];
-[UIPeripheralHost setAutomaticAppearanceEnabled:];
-[UIPeripheralHost queueDelayedTask:forKey:delay:];
-[UIPeripheralHost popAnimationStyle];
-[UIPeripheralHost existingContainerRootController];
-[UIPeripheralHost _restoreInputViewsWithId:animated:];
-[UIPeripheralHost forceReloadInputViews];
-[UIPeripheralHost transitioningFrame];
-[UIPeripheralHost automaticAppearanceReallyEnabled];
-[UIPeripheralHost setTargetState:];
-[UIPeripheralHost setTextEffectsWindowLevelForInputView:responder:];
-[UIPeripheralHost inputViews];
-[UIPeripheralHost viewForTransitionScreenSnapshot];
-[UIPeripheralHost setKeyboardFencingEnabled:];
-[UIPeripheralHost _preserveInputViewsWithId:animated:];
-[UIPeripheralHost _clearPreservedInputViewsWithId:clearKeyboard:];
-[UIPeripheralHost disableInterfaceAutorotation:];
-[UIPeripheralHost _inheritedRenderConfig];
-[UIPeripheralHost _restoreInputAccessoryViewOverrideWithId:];
-[UIPeripheralHost peripheralHostWillResume:];
-[UIPeripheralHost _preserveInputViewsWithId:];
-[UIPeripheralHost shouldUseHideNotificationForGeometry:];
-[UIPeripheralHost _inputViewRectToAvoid];
-[UIPeripheralHost assertionActivationStateForType:];
-[UIPeripheralHost isUndocked];
-[UIPeripheralHost totalPeripheralSizeForOrientation:];
-[UIPeripheralHost forceOrderInAutomaticFromDirection:withDuration:];
-[UIPeripheralHost updateToPlacement:withNormalAnimationsAndNotifications:];
-[UIPeripheralHost setAutomaticAppearanceInternalEnabled:];
-[UIPeripheralHost queueDelayedTask:];
-[UIPeripheralHost _preserveInputViewsWithId:animated:reset:];
-[UIPeripheralHost automaticAppearanceInternalEnabled];
-[UIPeripheralHost setInputViewsHidden:];
-[UIPeripheralHost hasDictationKeyboard];
-[UIPeripheralHost allVisibleFrames];
-[UIPeripheralHost finishRotation];
-[UIPeripheralHost orderInAutomaticSkippingAnimation];
-[UIPeripheralHost manualKeyboardWillBeOrderedIn:];
-[UIPeripheralHost performWithoutDeactivation:];
-[UIPeripheralHost minimize];
-[UIPeripheralHost minimumOffsetForBuffer:];
-[UIPeripheralHost maximize];
-[UIPeripheralHost setDeactivatedKeyboard:forScene:forSuppressionAssertion:updatePlacement:];
-[UIPeripheralHost adjustedPersistentOffset];
-[UIPeripheralHost rotationState];
-[UIPeripheralHost _isSuppressedByManualKeyboard];
-[UIPeripheralHost visiblePeripheralFrame:];
-[UIPeripheralHost orderOutAutomaticToDirection:withDuration:];
-[UIPeripheralHost init];
-[UIPeripheralHost loadAwareInputViews];
-[UIPeripheralHost isOffScreen];
-[UIPeripheralHost sizeOfInputViewForInputViewSet:withInterfaceOrientation:];
-[UIPeripheralHost forceOrderInAutomatic];
-[UIPeripheralHost lastUsedInputModeForCurrentContext];
-[UIPeripheralHost manualKeyboardWillBeOrderedOut:];
-[UIPeripheralHost moveToPersistentOffset];
-[UIPeripheralHost dealloc];
-[UIPeripheralHost _screenForFirstResponder:];
-[UIPeripheralHost updatePlacementForDeactivatedKeyboard:forSuppressionAssertion:wantsAssistant:keepAccessories:animationStyle:];
-[UIPeripheralHost _renderConfigForCurrentResponder];
-[UIPeripheralHost logGeometryDescriptionFromUserInfo:];
-[UIPeripheralHost _currentInputView];
-[UIPeripheralHost isOnScreen];
-[UIPeripheralHost animationFencingEnabled];
-[UIPeripheralHost responder];
-[UIPeripheralHost manualKeyboardWasOrderedOut:];
-[UIPeripheralHost hasCustomInputView];
-[UIPeripheralHost scrollView:didPanWithGesture:];
-[UIPeripheralHost setResponder:];
-[UIPeripheralHost getVerticalOverlapForView:usingKeyboardInfo:];
-[UIPeripheralHost view];
-[UIPeripheralHost finishRotationOfKeyboard:];
-[UIPeripheralHost setCurrentState:];
-[UIPeripheralHost postWillShowNotificationForGeometry:duration:];
-[UIPeripheralHost keyClicksEnabled];
-[UIPeripheralHost setDeactivatedKeyboard:forScene:];
-[UIPeripheralHost setDeactivatedKeyboard:forScene:forSuppressionAssertion:];
-[UIPeripheralHost setRotationState:];
-[UIPeripheralHost enableKeyboardTyping];
-[UIPeripheralHost _isCoordinatingWithSystemGestures];
-[UIPeripheralHost removePreservedInputViewSetForInputView:];
-[UIPeripheralHost setAnimationFencingEnabled:];
-[UIPeripheralHost textEffectsWindowDidRotate:];
-[UIPeripheralHost isRotating];
-[UIPeripheralHost rotateToOrientation:];
-[UIPeripheralHost postDidShowNotificationForGeometry:];
-[UIPeripheralHost contentView];
-[UIPeripheralHost scrollView:didFinishPanGesture:];
-[UIPeripheralHost prepareForRotationToOrientation:];
-[UIPeripheralHost _isKeyboardDeactivated];
-[UIPeripheralHost queueDelayedTask:forKey:];
-[UIPeripheralHost forceOrderOutAutomatic];
-[UIPeripheralHost hasDelayedTasksForKey:];
-[UIPeripheralHost assertionActivationStateChangedToState:forType:];
-[UIPeripheralHost ambiguousControlCenterActivationMargin];
-[UIPeripheralHost userInfoContainsActualGeometryChange:];
-[UIPeripheralHost userInfoFromGeometry:duration:forWill:forShow:];
-[UIPeripheralHost containerTextEffectsWindow];
-[UIPeripheralHost screenRectFromBounds:atCenter:applyingSourceHeightDelta:];
-[UIPeripheralHost offHostPointForPoint:];
-[UIPeripheralHost orderInAutomatic];
-[UIPeripheralHost _clearPreservedInputViewsWithRestorableResponder:];
-[UIPeripheralHost setKeyboardOnScreenNotifyKey:];
-[UIPeripheralHost _inputViews];
-[UIPeripheralHost set_inputViews:];
-[UIPeripheralHost set_transientInputViews:];
-[UIPeripheralHost updateInputAccessoryViewVisibility:withDuration:];
-[UIPeripheralHost _sceneForFirstResponder:];
-[UIPeripheralHost orderOutAutomatic];
-[UIPeripheralHost rotateKeyboard:toOrientation:];
-[UIPeripheralHost _renderConfigForResponder:];
-[UIPeripheralHost orderOutAutomaticSkippingAnimation];
-[UIPeripheralHost setDocumentInputMode:];
-[UIPeripheralHost prepareForRotationOfKeyboard:toOrientation:];
-[UIPeripheralHost containerTextEffectsWindowAboveStatusBar];
-[UIPeripheralHost orderInAutomaticFromDirection:withDuration:];
-[UIPeripheralHost setDeactivatedKeyboard:forScene:forSuppressionAssertion:updatePlacement:wantsAssistant:keepAccessories:];
-[UIPeripheralHost setUndockedWithOffset:animated:];
-[UIPeripheralHost currentState];
-[UIPeripheralHost _transientInputViews];
-[UIPeripheralHost setAmbiguousControlCenterActivationMargin:];
-[UIPeripheralHost transformedContainerView];
-[UIPeripheralHost setAllVisibleFrames:];
-[UIPeripheralHost _shouldDelayRotationForWindow:];
-[UIPeripheralHost manualKeyboardWasOrderedIn:];
-[UIPeripheralHost flushDelayedTasksForKey:];
-[UIPeripheralHost postKeyboardFrameChangeNotification:withInfo:];
```
