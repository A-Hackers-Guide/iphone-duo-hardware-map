# `UIInputLayoutHostingItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputWindowControllerHostingItem`
- Protocols: `UIGestureRecognizerDelegate`, `UIInputViewSetPlacementOwner`
- 34 instance variables, 46 properties, 141 instance methods, 1 class methods

## Instance variables

```
B _isOnScreen;
B _isFloating;
@"UIKBInputBackdropView" _inputAccessoryBackdropView;
@"NSLayoutConstraint" _assistantTopConstraint;
@"NSLayoutConstraint" _assistantSpacingConstraint;
@"NSLayoutConstraint" _bottomMostGuideConstraint;
@"NSLayoutConstraint" _leftConstraint;
@"NSLayoutConstraint" _rightConstraint;
@"NSLayoutConstraint" _keyplaneWidthConstraint;
@"NSLayoutConstraint" _accessoryViewHeightConstraint;
@"NSLayoutConstraint" _accessoryToGuideConstraint;
@"NSArray" _accessoryEmbedConstraints;
@"NSArray" _accessoryBackdropConstraints;
@"NSArray" _assistantViewEmbedConstraints;
@"NSLayoutConstraint" _assistantHeight;
@"NSArray" _inputViewEmbedConstraints;
@"NSArray" _backgroundConstraints;
@"NSLayoutConstraint" _inputViewHeight;
@"NSArray" _dockViewEmbedConstraints;
@"NSLayoutConstraint" _dockHeight;
@"UIKeyboardItemContainerView" _containerView;
@"UIView" _inputLayoutView;
@"UIView" _inputLayoutAssistantView;
@"UIKBBackdropView" _backdropView;
@"TUIInputAssistantHostView" _inputAssistantHostView;
@"NSArray" _assistantHostViewConstraints;
@"UIInputViewSet" _inputViewSet;
@"UIInputWindowControllerHosting" _hosting;
@"TUIKeyboardState" _currentState;
@"UIKBInputBackdropView" _standardBackgroundView;
@"UIView" _platterView;
@"UIView" _pillView;
@"UIPinchGestureRecognizer" _pinchGesture;
{CGPoint="x"d"y"d} _persistentOffset;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_assistantTopConstraint) assistantTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_assistantSpacingConstraint) assistantSpacingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_bottomMostGuideConstraint) bottomMostGuideConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leftConstraint) leftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_rightConstraint) rightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_keyplaneWidthConstraint) keyplaneWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_accessoryViewHeightConstraint) accessoryViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_accessoryToGuideConstraint) accessoryToGuideConstraint;
@property (T@"NSArray",&,N,V_accessoryEmbedConstraints) accessoryEmbedConstraints;
@property (T@"NSArray",&,N,V_accessoryBackdropConstraints) accessoryBackdropConstraints;
@property (T@"NSArray",&,N,V_assistantViewEmbedConstraints) assistantViewEmbedConstraints;
@property (T@"NSLayoutConstraint",&,N,V_assistantHeight) assistantHeight;
@property (T@"NSArray",&,N,V_inputViewEmbedConstraints) inputViewEmbedConstraints;
@property (T@"NSArray",&,N,V_backgroundConstraints) backgroundConstraints;
@property (T@"NSLayoutConstraint",&,N,V_inputViewHeight) inputViewHeight;
@property (T@"NSArray",&,N,V_dockViewEmbedConstraints) dockViewEmbedConstraints;
@property (T@"NSLayoutConstraint",&,N,V_dockHeight) dockHeight;
@property (T@"UIKeyboardItemContainerView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_inputLayoutView) inputLayoutView;
@property (T@"UIView",&,N,V_inputLayoutAssistantView) inputLayoutAssistantView;
@property (T@"UIKBBackdropView",&,N,V_backdropView) backdropView;
@property (T@"TUIInputAssistantHostView",&,N,V_inputAssistantHostView) inputAssistantHostView;
@property (T@"NSArray",&,N,V_assistantHostViewConstraints) assistantHostViewConstraints;
@property (T@"UIKBInputBackdropView",&,N,SsetInputAccessoryBackdropView:,V_inputAccessoryBackdropView) _inputAccessoryBackdropView;
@property (T@"UIInputViewSet",&,N,V_inputViewSet) inputViewSet;
@property (T@"UIInputWindowControllerHosting",W,N,V_hosting) hosting;
@property (TB,N,V_isOnScreen) isOnScreen;
@property (TB,N,V_isFloating) isFloating;
@property (T@"TUIKeyboardState",&,N,V_currentState) currentState;
@property (T{CGPoint=dd},N,V_persistentOffset) persistentOffset;
@property (T@"UIKBInputBackdropView",&,N,V_standardBackgroundView) standardBackgroundView;
@property (T@"UIView",&,N,V_platterView) platterView;
@property (T@"UIView",&,N,V_pillView) pillView;
@property (T@"UIPinchGestureRecognizer",&,N,V_pinchGesture) pinchGesture;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R) keyboardController;
@property (T@"UIInputViewSetPlacement",R) placement;
@property (T@"<UIInputViewSetPlacementApplicator>",R,N) applicator;
@property (T{UIEdgeInsets=dddd},R) inputViewPadding;
@property (T@"UIView",R) hostView;
@property (TB) hideInputViewBackdrops;
@property (Tq,R) inputViewBackdropStyle;
@property (TB) hideInputView;
```

## Class methods

```
+[UIInputLayoutHostingItem requiresConstraintBasedLayout];
```

## Instance methods

```
-[UIInputLayoutHostingItem completeTransition:withInfo:];
-[UIInputLayoutHostingItem platterView];
-[UIInputLayoutHostingItem draggableView];
-[UIInputLayoutHostingItem setBackdropView:];
-[UIInputLayoutHostingItem _updateBackdropViews];
-[UIInputLayoutHostingItem inputViewController];
-[UIInputLayoutHostingItem pillView];
-[UIInputLayoutHostingItem clearInputViewEdgeConstraints];
-[UIInputLayoutHostingItem animatingTransitionFromState:toState:animationType:totalDuration:];
-[UIInputLayoutHostingItem updateTransition:withInfo:];
-[UIInputLayoutHostingItem clearInputAssistantViewEdgeConstraints];
-[UIInputLayoutHostingItem updateKeyboardDockViewVisibility];
-[UIInputLayoutHostingItem inputAssistantView];
-[UIInputLayoutHostingItem setInputViewSet:];
-[UIInputLayoutHostingItem removeInputAssistantHostView];
-[UIInputLayoutHostingItem disableViewSizingConstraints:forNewView:];
-[UIInputLayoutHostingItem dockHeight];
-[UIInputLayoutHostingItem sizeForVisualState:];
-[UIInputLayoutHostingItem unloadForPlacement];
-[UIInputLayoutHostingItem prepareForTransitionToState:animationType:interactiveTransition:];
-[UIInputLayoutHostingItem setInputAssistantView:];
-[UIInputLayoutHostingItem setPersistentOffset:];
-[UIInputLayoutHostingItem transitioningToState:animationType:completionPercentage:];
-[UIInputLayoutHostingItem hostView];
-[UIInputLayoutHostingItem setPillView:];
-[UIInputLayoutHostingItem finishedTransitionToState:animationType:interactiveTransition:];
-[UIInputLayoutHostingItem constrainGuidesIfNeeded];
-[UIInputLayoutHostingItem updateVisibilityConstraintsForPlacement:];
-[UIInputLayoutHostingItem updateEmptyHeightConstraint];
-[UIInputLayoutHostingItem backdropView];
-[UIInputLayoutHostingItem notificationsFrame];
-[UIInputLayoutHostingItem stateChangeRequiresBottomConstraintChange:];
-[UIInputLayoutHostingItem hosting];
-[UIInputLayoutHostingItem updateViewSizingConstraints];
-[UIInputLayoutHostingItem accessoryViewHeightConstraint];
-[UIInputLayoutHostingItem persistentOffset];
-[UIInputLayoutHostingItem resetInputViewVisibility];
-[UIInputLayoutHostingItem inputViewSet];
-[UIInputLayoutHostingItem setAccessoryViewHeightConstraint:];
-[UIInputLayoutHostingItem updateConstraintInsets];
-[UIInputLayoutHostingItem setContainerView:];
-[UIInputLayoutHostingItem setIsFloating:];
-[UIInputLayoutHostingItem setInputAccessoryView:];
-[UIInputLayoutHostingItem inputAccessoryView];
-[UIInputLayoutHostingItem setAssistantHostViewConstraints:];
-[UIInputLayoutHostingItem isFloating];
-[UIInputLayoutHostingItem setAssistantTopConstraint:];
-[UIInputLayoutHostingItem refreshApplicator];
-[UIInputLayoutHostingItem updateViewConstraints];
-[UIInputLayoutHostingItem setIsOnScreen:];
-[UIInputLayoutHostingItem visibleFrame];
-[UIInputLayoutHostingItem createHostForAssistantIfNeeded];
-[UIInputLayoutHostingItem setAssistantViewEmbedConstraints:];
-[UIInputLayoutHostingItem setBackgroundConstraints:];
-[UIInputLayoutHostingItem setPlatterView:];
-[UIInputLayoutHostingItem willBeginTranslationFromPlacement:to:];
-[UIInputLayoutHostingItem prepareAssistantHostIfNeededForCompact:];
-[UIInputLayoutHostingItem trackPinch:];
-[UIInputLayoutHostingItem clearVisibilityConstraints];
-[UIInputLayoutHostingItem initWithInputViewSet:container:];
-[UIInputLayoutHostingItem setRightConstraint:];
-[UIInputLayoutHostingItem setAssistantSpacingConstraint:];
-[UIInputLayoutHostingItem positionConstraintConstant];
-[UIInputLayoutHostingItem prepareTranslationFromPlacement:to:];
-[UIInputLayoutHostingItem inputAssistantViewHeight];
-[UIInputLayoutHostingItem setInputLayoutView:];
-[UIInputLayoutHostingItem createItemHostView];
-[UIInputLayoutHostingItem updateInputBackdropViewVisibility];
-[UIInputLayoutHostingItem assistantViewEmbedConstraints];
-[UIInputLayoutHostingItem inputViewEmbedConstraints];
-[UIInputLayoutHostingItem animationTransformForState:];
-[UIInputLayoutHostingItem updateInputBackdropView];
-[UIInputLayoutHostingItem setDockViewEmbedConstraints:];
-[UIInputLayoutHostingItem _inputAccessoryBackdropView];
-[UIInputLayoutHostingItem inputAccessoryViewController];
-[UIInputLayoutHostingItem addManualHeightForInputView:];
-[UIInputLayoutHostingItem constraintsForView:embeddedInGuide:insets:identifier:];
-[UIInputLayoutHostingItem setKeyplaneWidthConstraint:];
-[UIInputLayoutHostingItem changeConstraintsForState:animated:];
-[UIInputLayoutHostingItem isOnScreen];
-[UIInputLayoutHostingItem bottomMostGuideConstraint];
-[UIInputLayoutHostingItem standardBackgroundView];
-[UIInputLayoutHostingItem updateViewSizingConstraints:];
-[UIInputLayoutHostingItem trackingCoordinatorFrame];
-[UIInputLayoutHostingItem hideBackdrop:];
-[UIInputLayoutHostingItem buildContainerConstraintsIfNeeded];
-[UIInputLayoutHostingItem setLeftConstraint:];
-[UIInputLayoutHostingItem initWithContainer:];
-[UIInputLayoutHostingItem setStandardBackgroundView:];
-[UIInputLayoutHostingItem setAccessoryToGuideConstraint:];
-[UIInputLayoutHostingItem containerView];
-[UIInputLayoutHostingItem animatedAssistantView];
-[UIInputLayoutHostingItem updateInputViewSet:];
-[UIInputLayoutHostingItem rightConstraint];
-[UIInputLayoutHostingItem accessoryEmbedConstraints];
-[UIInputLayoutHostingItem inputView];
-[UIInputLayoutHostingItem setHideInputViewBackdrops:];
-[UIInputLayoutHostingItem keyplaneWidthConstraint];
-[UIInputLayoutHostingItem usesKeyboardState];
-[UIInputLayoutHostingItem setInputViewEmbedConstraints:];
-[UIInputLayoutHostingItem setCurrentState:];
-[UIInputLayoutHostingItem setInputLayoutAssistantView:];
-[UIInputLayoutHostingItem setBottomMostGuideConstraint:];
-[UIInputLayoutHostingItem inputLayoutAssistantView];
-[UIInputLayoutHostingItem setAccessoryViewVisible:delay:];
-[UIInputLayoutHostingItem clearInputAccessoryViewEdgeConstraints];
-[UIInputLayoutHostingItem setInputAssistantHostView:];
-[UIInputLayoutHostingItem leftConstraint];
-[UIInputLayoutHostingItem setAccessoryBackdropConstraints:];
-[UIInputLayoutHostingItem reloadForPlacement];
-[UIInputLayoutHostingItem setAccessoryEmbedConstraints:];
-[UIInputLayoutHostingItem inputLayoutView];
-[UIInputLayoutHostingItem inputViewHeight];
-[UIInputLayoutHostingItem updateHeightForAccessory:];
-[UIInputLayoutHostingItem assistantHeight];
-[UIInputLayoutHostingItem setDockHeight:];
-[UIInputLayoutHostingItem needsAssistantHost];
-[UIInputLayoutHostingItem dockViewEmbedConstraints];
-[UIInputLayoutHostingItem setInputAccessoryBackdropView:];
-[UIInputLayoutHostingItem setInputView:];
-[UIInputLayoutHostingItem setAssistantHeight:];
-[UIInputLayoutHostingItem setHosting:];
-[UIInputLayoutHostingItem inputAssistantHostView];
-[UIInputLayoutHostingItem accessoryBackdropConstraints];
-[UIInputLayoutHostingItem createBackdropViewIfNeeded];
-[UIInputLayoutHostingItem assistantTopConstraint];
-[UIInputLayoutHostingItem didFinishTranslationFromPlacement:to:];
-[UIInputLayoutHostingItem assistantHostViewConstraints];
-[UIInputLayoutHostingItem addManualHeightForAssistant:];
-[UIInputLayoutHostingItem backgroundConstraints];
-[UIInputLayoutHostingItem accessoryToGuideConstraint];
-[UIInputLayoutHostingItem assistantSpacingConstraint];
-[UIInputLayoutHostingItem setInputViewHeight:];
-[UIInputLayoutHostingItem animatedInputView];
-[UIInputLayoutHostingItem pinchGesture];
-[UIInputLayoutHostingItem inputAssistantViewController];
-[UIInputLayoutHostingItem currentState];
-[UIInputLayoutHostingItem setHideInputView:];
-[UIInputLayoutHostingItem constraintsForView:embeddedInView:insets:];
-[UIInputLayoutHostingItem setPinchGesture:];
-[UIInputLayoutHostingItem updateInputAccessoryBackdropView];
```
