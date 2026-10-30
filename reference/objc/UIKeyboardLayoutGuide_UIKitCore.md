# `UIKeyboardLayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITrackingLayoutGuide`
- Protocols: `_UIAssertionControllerSubject`
- 20 instance variables, 24 properties, 77 instance methods, 0 class methods

## Instance variables

```
B _docked;
B _windowGuide;
B _transitioning;
B _addsHeightWhenUndocked;
B _followsUndockedKeyboard;
B _usesBottomSafeArea;
B _ignoresSafeArea;
B _ignoreKeyboardChanges;
@"_UIAssertionController" _assertionController;
d _keyboardDismissPadding;
@"NSLayoutConstraint" _viewBottomConstraint;
q _followTypes;
@"_UIKBLightEffectsBackground" _lightEffectsBackdrop;
@"NSArray" _backdropConstraints;
@"NSLayoutConstraint" _assistantHeightConstraint;
q _currentKeyboardVisualState;
{UIOffset="horizontal"d"vertical"d} _previousOffset;
{CGSize="width"d"height"d} _previousSize;
{UIOffset="horizontal"d"vertical"d} _interactionResetOffset;
{CGSize="width"d"height"d} _interactionResetSize;
```

## Properties

```
@property (T{UIOffset=dd},N,V_previousOffset) previousOffset;
@property (T{CGSize=dd},N,V_previousSize) previousSize;
@property (T@"NSLayoutConstraint",&,N,V_viewBottomConstraint) viewBottomConstraint;
@property (TB,N,V_ignoresSafeArea) ignoresSafeArea;
@property (TB,N,V_ignoreKeyboardChanges) ignoreKeyboardChanges;
@property (Tq,N,V_followTypes) followTypes;
@property (T@"_UIKBLightEffectsBackground",&,N,V_lightEffectsBackdrop) lightEffectsBackdrop;
@property (T@"NSArray",&,N,V_backdropConstraints) backdropConstraints;
@property (T@"NSLayoutConstraint",&,N,V_assistantHeightConstraint) assistantHeightConstraint;
@property (T{UIOffset=dd},N,V_interactionResetOffset) interactionResetOffset;
@property (T{CGSize=dd},N,V_interactionResetSize) interactionResetSize;
@property (T@"_UIAssertionController",R,N,V_assertionController) _assertionController;
@property (TB,N,GisDocked,V_docked) docked;
@property (Tq,N,V_currentKeyboardVisualState) currentKeyboardVisualState;
@property (TB,N,GisWindowGuide,V_windowGuide) windowGuide;
@property (TB,R,N,GisTransitioning,V_transitioning) transitioning;
@property (TB,N,V_addsHeightWhenUndocked) addsHeightWhenUndocked;
@property (TB,N,V_followsUndockedKeyboard) followsUndockedKeyboard;
@property (TB,N,V_usesBottomSafeArea) usesBottomSafeArea;
@property (Td,N,V_keyboardDismissPadding) keyboardDismissPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardLayoutGuide isDocked];
-[UIKeyboardLayoutGuide _commonInit];
-[UIKeyboardLayoutGuide assertionActivationStateForType:];
-[UIKeyboardLayoutGuide setKeyboardTrackingState:];
-[UIKeyboardLayoutGuide setPreviousSize:];
-[UIKeyboardLayoutGuide validatedOverlappingEdges:];
-[UIKeyboardLayoutGuide setAssistantHeightConstraint:];
-[UIKeyboardLayoutGuide changeSizingConstants:];
-[UIKeyboardLayoutGuide changeOffsetConstants:];
-[UIKeyboardLayoutGuide _changeOffsetConstants:force:];
-[UIKeyboardLayoutGuide setAddsHeightWhenUndocked:];
-[UIKeyboardLayoutGuide setPreviousOffset:];
-[UIKeyboardLayoutGuide constrainToReference:];
-[UIKeyboardLayoutGuide updateBottomConstraint];
-[UIKeyboardLayoutGuide backdropConstraints];
-[UIKeyboardLayoutGuide currentStateIsDocked];
-[UIKeyboardLayoutGuide inheritOptionsFromGuide:];
-[UIKeyboardLayoutGuide init];
-[UIKeyboardLayoutGuide lightEffectsBackdrop];
-[UIKeyboardLayoutGuide removeLightEffectsView];
-[UIKeyboardLayoutGuide _assertionController];
-[UIKeyboardLayoutGuide setFollowsUndockedKeyboard:];
-[UIKeyboardLayoutGuide isTransitioning];
-[UIKeyboardLayoutGuide _obtainTransitionAssertionForReason:];
-[UIKeyboardLayoutGuide usesBottomSafeArea];
-[UIKeyboardLayoutGuide setViewBottomConstraint:];
-[UIKeyboardLayoutGuide useLightEffectsBackgroundBelowView:];
-[UIKeyboardLayoutGuide setLightEffectsBackdrop:];
-[UIKeyboardLayoutGuide prepareForTestingWithState:];
-[UIKeyboardLayoutGuide guideBackdropMatchLayer];
-[UIKeyboardLayoutGuide ignoreKeyboardChanges];
-[UIKeyboardLayoutGuide isWindowGuide];
-[UIKeyboardLayoutGuide setFollowTypes:];
-[UIKeyboardLayoutGuide setKeyboardDismissPadding:];
-[UIKeyboardLayoutGuide setIgnoresSafeArea:];
-[UIKeyboardLayoutGuide interactionResetSize];
-[UIKeyboardLayoutGuide followTypes];
-[UIKeyboardLayoutGuide previousSize];
-[UIKeyboardLayoutGuide assistantHeightConstraint];
-[UIKeyboardLayoutGuide addsHeightWhenUndocked];
-[UIKeyboardLayoutGuide updateSizeForInputMode:orientation:showsAssistantBar:animated:];
-[UIKeyboardLayoutGuide _detachGuideFromKeyboard:];
-[UIKeyboardLayoutGuide hideLightEffectsView:];
-[UIKeyboardLayoutGuide forceResizeGuideForInputMode:orientation:showsAssistantBar:animated:];
-[UIKeyboardLayoutGuide moveGuideOffscreenAtEdge:];
-[UIKeyboardLayoutGuide interactionResetOffset];
-[UIKeyboardLayoutGuide encodeWithCoder:];
-[UIKeyboardLayoutGuide ignoresSafeArea];
-[UIKeyboardLayoutGuide followsUndockedKeyboard];
-[UIKeyboardLayoutGuide resetGuideForCancelledDismissInteraction];
-[UIKeyboardLayoutGuide viewBottomConstraint];
-[UIKeyboardLayoutGuide forceDismissGuideAnimated:];
-[UIKeyboardLayoutGuide disableSynchronizingWithKeyboard];
-[UIKeyboardLayoutGuide keyboardDismissPadding];
-[UIKeyboardLayoutGuide assertionActivationStateChangedToState:forType:];
-[UIKeyboardLayoutGuide _changeSizingConstants:force:];
-[UIKeyboardLayoutGuide initWithCoder:];
-[UIKeyboardLayoutGuide updateLightEffectsRenderConfig:animated:];
-[UIKeyboardLayoutGuide currentKeyboardVisualState];
-[UIKeyboardLayoutGuide setUsesBottomSafeArea:];
-[UIKeyboardLayoutGuide reenableSynchronizingWithKeyboard];
-[UIKeyboardLayoutGuide setIgnoreKeyboardChanges:];
-[UIKeyboardLayoutGuide shouldFollowCurrentKeyboard];
-[UIKeyboardLayoutGuide forceResizeGuideForOrientation:showsAssistantBar:animated:];
-[UIKeyboardLayoutGuide keyboardStateIsDocked:];
-[UIKeyboardLayoutGuide setBackdropConstraints:];
-[UIKeyboardLayoutGuide followUndockedKeyboardOfTypes:];
-[UIKeyboardLayoutGuide setInteractionResetOffset:];
-[UIKeyboardLayoutGuide setCurrentKeyboardVisualState:];
-[UIKeyboardLayoutGuide defaultKeyboardSizeForInputMode:orientation:addingAssistant:];
-[UIKeyboardLayoutGuide _setTransitioning:];
-[UIKeyboardLayoutGuide previousOffset];
-[UIKeyboardLayoutGuide setDocked:];
-[UIKeyboardLayoutGuide setWindowGuide:];
-[UIKeyboardLayoutGuide setInteractionResetSize:];
-[UIKeyboardLayoutGuide _moveGuideOffscreenAtEdge:force:];
-[UIKeyboardLayoutGuide transitionBackdropForAnimationStart:];
```
