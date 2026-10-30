# `UISystemInputViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIRecentsInputViewControllerDelegate`
- 38 instance variables, 36 properties, 130 instance methods, 8 class methods

## Instance variables

```
@"NSMutableDictionary" _accessoryViewControllers;
@"NSMutableDictionary" _accessoryConstraints;
B _needsSetupAgain;
B _isVisible;
B _requiresLinearStyleForActiveInputModes;
@"UIResponder<UITraitEnvironment>" _containingResponder;
@"NSUUID" _remoteInputSessionIdentifier;
@"<UIInteraction>" _activeSystemInputInteraction;
B _supportsTouchInput;
B _supportsRecentInputsIntegration;
B _isAutomaticResponderTransition;
B _notifyKeyboardOnScreenOnFocusOnly;
B _willPresentFullscreen;
B _willUpdateBackgroundEffectOnInputModeChange;
B _didDisplayRecents;
@"<UISystemInputViewControllerDelegate>" _systemInputViewControllerDelegate;
@"UIResponder<UITextInput>" _persistentDelegate;
@"UIKeyboard" _keyboard;
@"NSArray" _keyboardConstraints;
@"NSArray" _keyboardBackdropConstraints;
@"UICompatibilityInputViewController" _keyboardVC;
@"NSArray" _editorConstraints;
@"UIKBSystemLayoutViewController" _editorVC;
@"UIButton" _doneButton;
@"UIViewController" _inputVC;
@"UIRecentsInputViewController" _recentsVC;
@"NSArray" _verticalAlignments;
@"NSArray" _horizontalAlignments;
@"UIResponder<UITextInput>" _nextInputDelegate;
@"UITextInputTraits" _textInputTraits;
@"UILexicon" _cachedRecents;
@"UILabel" _promptLabel;
q _resolvedKeyboardStyle;
Q _requestedInteractionModel;
@"UIView" _containingView;
@"UIView" _contentLayoutView;
q _blurEffectStyle;
@"UIKBInputBackdropView" _backdropView;
```

## Properties

```
@property (TB,N,V_supportsTouchInput) supportsTouchInput;
@property (Tq,N,V_resolvedKeyboardStyle) resolvedKeyboardStyle;
@property (TB,N,V_isAutomaticResponderTransition) isAutomaticResponderTransition;
@property (TB,N,V_willPresentFullscreen) willPresentFullscreen;
@property (TB,N,V_willUpdateBackgroundEffectOnInputModeChange) willUpdateBackgroundEffectOnInputModeChange;
@property (TB,N,V_didDisplayRecents) didDisplayRecents;
@property (T@"UIView",&,N,V_containingView) containingView;
@property (T@"UIView",&,N,V_contentLayoutView) contentLayoutView;
@property (Tq,N,V_blurEffectStyle) blurEffectStyle;
@property (T@"UIKeyboard",&,N,V_keyboard) keyboard;
@property (T@"NSArray",&,N,V_keyboardConstraints) keyboardConstraints;
@property (T@"UICompatibilityInputViewController",&,N,V_keyboardVC) keyboardVC;
@property (T@"NSArray",&,N,V_keyboardBackdropConstraints) keyboardBackdropConstraints;
@property (T@"UIKBInputBackdropView",&,N,V_backdropView) backdropView;
@property (T@"NSArray",&,N,V_editorConstraints) editorConstraints;
@property (T@"UIKBSystemLayoutViewController",&,N,V_editorVC) editorVC;
@property (T@"UIButton",&,N,V_doneButton) doneButton;
@property (T@"UIViewController",&,N,V_inputVC) inputVC;
@property (T@"UIRecentsInputViewController",&,N,V_recentsVC) recentsVC;
@property (T@"NSArray",&,N,V_verticalAlignments) verticalAlignments;
@property (T@"NSArray",&,N,V_horizontalAlignments) horizontalAlignments;
@property (T@"UIResponder<UITextInput>",&,N,V_nextInputDelegate) nextInputDelegate;
@property (T@"UITextInputTraits",&,N,V_textInputTraits) textInputTraits;
@property (T@"UILexicon",&,N,V_cachedRecents) cachedRecents;
@property (T@"UILabel",&,N,V_promptLabel) _promptLabel;
@property (TB,N) keyboardCanBecomeFocusedWithZeroAlpha;
@property (T@"UIResponder<UITextInput>",&,N,V_persistentDelegate) persistentDelegate;
@property (T{UIEdgeInsets=dddd},N) unfocusedFocusGuideOutsets;
@property (TB,N,V_supportsRecentInputsIntegration) supportsRecentInputsIntegration;
@property (T@"<UISystemInputViewControllerDelegate>",N,V_systemInputViewControllerDelegate) systemInputViewControllerDelegate;
@property (TQ,N,V_requestedInteractionModel) requestedInteractionModel;
@property (TB,N,V_notifyKeyboardOnScreenOnFocusOnly) notifyKeyboardOnScreenOnFocusOnly;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISystemInputViewController _canonicalTraitsForResponder:];
+[UISystemInputViewController _carPlay_systemInputViewControllerForResponder:editorView:containingResponder:traitCollection:];
+[UISystemInputViewController _iOS_systemInputViewControllerForResponder:editorView:containingResponder:traitCollection:];
+[UISystemInputViewController _tvOS_systemInputViewControllerForResponder:editorView:containingResponder:traitCollection:];
+[UISystemInputViewController canUseSystemInputViewControllerForResponder:];
+[UISystemInputViewController setKeyboardInteractionModel:];
+[UISystemInputViewController systemInputViewControllerForResponder:editorView:];
+[UISystemInputViewController systemInputViewControllerForResponder:editorView:containingResponder:];
```

## Instance methods

```
-[UISystemInputViewController setBackdropView:];
-[UISystemInputViewController textInputTraits];
-[UISystemInputViewController backdropView];
-[UISystemInputViewController setTextInputTraits:];
-[UISystemInputViewController keyboard];
-[UISystemInputViewController inputModeDidChange:];
-[UISystemInputViewController updateViewConstraints];
-[UISystemInputViewController setRequestedInteractionModel:];
-[UISystemInputViewController blurEffectStyle];
-[UISystemInputViewController setDoneButton:];
-[UISystemInputViewController traitCollection];
-[UISystemInputViewController doneButton];
-[UISystemInputViewController _disableAutomaticKeyboardBehavior];
-[UISystemInputViewController viewWillDisappear:];
-[UISystemInputViewController didUpdateFocusInContext:withAnimationCoordinator:];
-[UISystemInputViewController pressesCancelled:withEvent:];
-[UISystemInputViewController pressesEnded:withEvent:];
-[UISystemInputViewController dealloc];
-[UISystemInputViewController requestedInteractionModel];
-[UISystemInputViewController viewDidLayoutSubviews];
-[UISystemInputViewController initWithNibName:bundle:];
-[UISystemInputViewController pressesBegan:withEvent:];
-[UISystemInputViewController viewWillAppear:];
-[UISystemInputViewController setDelegate:];
-[UISystemInputViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[UISystemInputViewController viewDidAppear:];
-[UISystemInputViewController viewWillLayoutSubviews];
-[UISystemInputViewController preferredFocusEnvironments];
-[UISystemInputViewController traitCollectionDidChange:];
-[UISystemInputViewController _removeAccessoryViewController:];
-[UISystemInputViewController _updateRemoteTextEditingSession];
-[UISystemInputViewController inputVC];
-[UISystemInputViewController _windowDidBecomeApplicationKey:];
-[UISystemInputViewController accessoryViewControllerForEdge:];
-[UISystemInputViewController setAlignmentConstraint:forAxis:];
-[UISystemInputViewController setKeyboardBackdropConstraints:];
-[UISystemInputViewController supportsRecentInputsIntegration];
-[UISystemInputViewController _accessoryViewControllerForEdge:];
-[UISystemInputViewController _addAccessoryViewController:];
-[UISystemInputViewController _addChildInputViewController];
-[UISystemInputViewController _clearCursorLocationIfNotFirstResponder];
-[UISystemInputViewController _createKeyboardIfNecessary];
-[UISystemInputViewController _didSuspend:];
-[UISystemInputViewController _dismissSystemInputViewController];
-[UISystemInputViewController _horizontalLayoutTypeForEdge:];
-[UISystemInputViewController _promptLabel];
-[UISystemInputViewController _remoteInputSessionIdentifier];
-[UISystemInputViewController _resetDelegate];
-[UISystemInputViewController _responderIsReloaded];
-[UISystemInputViewController _restoreKeyboardIfNecessary];
-[UISystemInputViewController _returnButtonPressed];
-[UISystemInputViewController _setNonInputViewVisibility:];
-[UISystemInputViewController _setSystemInputInteractionActive:];
-[UISystemInputViewController _traitCollectionForUserInterfaceStyle];
-[UISystemInputViewController _verticalLayoutTypeForEdge:];
-[UISystemInputViewController _willResume:];
-[UISystemInputViewController _windowWillBecomeApplicationKey:];
-[UISystemInputViewController alignmentConstraintArrayForAxis:];
-[UISystemInputViewController alignmentConstraintForAxis:];
-[UISystemInputViewController cachedRecents];
-[UISystemInputViewController configureRecentsVCIfNecessary];
-[UISystemInputViewController constraintFromView:attribute:toView:attribute:];
-[UISystemInputViewController constraintsForEdge:];
-[UISystemInputViewController containingView];
-[UISystemInputViewController contentLayoutView];
-[UISystemInputViewController didDisplayRecents];
-[UISystemInputViewController didSelectRecentInput];
-[UISystemInputViewController doneButtonStringForCurrentInputDelegate];
-[UISystemInputViewController editorConstraints];
-[UISystemInputViewController editorVC];
-[UISystemInputViewController findNextInputDelegate];
-[UISystemInputViewController horizontalAlignments];
-[UISystemInputViewController isAutomaticResponderTransition];
-[UISystemInputViewController keyboardBackdropConstraints];
-[UISystemInputViewController keyboardCanBecomeFocusedWithZeroAlpha];
-[UISystemInputViewController keyboardConstraints];
-[UISystemInputViewController keyboardVC];
-[UISystemInputViewController nextInputDelegate];
-[UISystemInputViewController notifyDelegateWithAccessoryVisibility:];
-[UISystemInputViewController notifyKeyboardOnScreenOnFocusOnly];
-[UISystemInputViewController persistentDelegate];
-[UISystemInputViewController populateCoreHierarchy];
-[UISystemInputViewController prepareForRelease];
-[UISystemInputViewController recentsVC];
-[UISystemInputViewController reloadInputViewsForPersistentDelegate];
-[UISystemInputViewController resetContainingResponder];
-[UISystemInputViewController resolvedKeyboardStyle];
-[UISystemInputViewController setAccessoryViewController:forEdge:];
-[UISystemInputViewController setAlignmentConstraintArray:forAxis:];
-[UISystemInputViewController setBlurEffectStyle:];
-[UISystemInputViewController setCachedRecents:];
-[UISystemInputViewController setConstraints:forEdge:];
-[UISystemInputViewController setContainingView:];
-[UISystemInputViewController setContentLayoutView:];
-[UISystemInputViewController setDidDisplayRecents:];
-[UISystemInputViewController setEditorConstraints:];
-[UISystemInputViewController setEditorVC:];
-[UISystemInputViewController setHorizontalAlignments:];
-[UISystemInputViewController setInputVC:];
-[UISystemInputViewController setIsAutomaticResponderTransition:];
-[UISystemInputViewController setKeyboard:];
-[UISystemInputViewController setKeyboardCanBecomeFocusedWithZeroAlpha:];
-[UISystemInputViewController setKeyboardConstraints:];
-[UISystemInputViewController setKeyboardVC:];
-[UISystemInputViewController setNextInputDelegate:];
-[UISystemInputViewController setNotifyKeyboardOnScreenOnFocusOnly:];
-[UISystemInputViewController setPersistentDelegate:];
-[UISystemInputViewController setRecentsVC:];
-[UISystemInputViewController setResolvedKeyboardStyle:];
-[UISystemInputViewController setSupportsRecentInputsIntegration:];
-[UISystemInputViewController setSupportsTouchInput:];
-[UISystemInputViewController setSystemInputViewControllerDelegate:];
-[UISystemInputViewController setUnfocusedFocusGuideOutsets:];
-[UISystemInputViewController setVerticalAlignments:];
-[UISystemInputViewController setWillPresentFullscreen:];
-[UISystemInputViewController setWillUpdateBackgroundEffectOnInputModeChange:];
-[UISystemInputViewController set_promptLabel:];
-[UISystemInputViewController setupKeyboard];
-[UISystemInputViewController shouldUseSecureRecentInputsForIdiom:];
-[UISystemInputViewController supportsTouchInput];
-[UISystemInputViewController switchToKeyboard];
-[UISystemInputViewController systemInputViewControllerDelegate];
-[UISystemInputViewController unfocusedFocusGuideOutsets];
-[UISystemInputViewController updateAlignmentConstraints];
-[UISystemInputViewController updateBackdropForCarPlay];
-[UISystemInputViewController verticalAlignments];
-[UISystemInputViewController viewForFocusHeading:fromView:];
-[UISystemInputViewController willPresentFullscreen];
-[UISystemInputViewController willShowRecentsList];
-[UISystemInputViewController willUpdateBackgroundEffectOnInputModeChange];
```
