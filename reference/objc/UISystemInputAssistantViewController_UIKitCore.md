# `UISystemInputAssistantViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewController`
- Protocols: `UIPopoverPresentationControllerDelegate`, `UIKeyboardAutocorrectionObserver`, `TUISystemInputAssistantViewDelegate`, `TUIEmojiSearchInputViewControllerDelegate`
- 34 instance variables, 33 properties, 163 instance methods, 6 class methods

## Instance variables

```
@"<UIKeyInput>" _pendingResponderForChangedNotification;
@"NSTimer" _pendingResponderChangedTimer;
B _postedSwitchFromEmojiNotification;
B _isInputAssistantItemEmpty;
B _isButtonBarItemsInlineVisible;
B _containsWritingToolsItem;
@"CAShapeLayer" _cornerMaskLayer;
B _showsRemoteInputDashViewController;
B _assistantEnabledPreference;
B _assistantOniPhonePreference;
B _hasCheckedPreferences;
B _currentlyCheckingPreferences;
B _assistantViewCanAnimate;
@"UIViewController<UIPredictiveViewController>" _centerViewController;
q _assistantBarStyle;
@"UIView" _popoverSourceView;
@"UITextInputAssistantItem" _observedInputAssistantItem;
@"NSMutableDictionary" _cachedPredictiveViewControllers;
@"TUISystemInputAssistantLayoutStandard" _standardAssistantViewLayout;
@"TUISystemInputAssistantLayoutSplit" _splitAssistantViewLayout;
@"TUISystemInputAssistantLayout" _floatAssistantViewLayout;
@"TUISystemInputAssistantLayout" _compactAssistantViewLayout;
@"TUISystemInputAssistantStyleStandard" _standardStyle;
@"TUISystemInputAssistantStyleFloat" _floatStyle;
@"TUISystemInputAssistantStyleCompact" _compactStyle;
@"UITextInputAssistantItem" _remoteAssistantItem;
d _remoteCenterViewPreferredWidth;
@"TUIEmojiSearchInputViewController" _emojiSearchViewController;
@"UIViewController<UIPredictiveViewController>" _predictiveViewController;
@"UIViewController" _expandedItemsController;
@"NSValue" _currentInputDelegatePointerValue;
@"_UILayerHostView" _remoteAssistantView;
@"UIView" _remoteAssistantContainerView;
@"UIRemoteInputViewInfo" _remoteAssistantViewInfo;
```

## Properties

```
@property (T@"UIView",W,N,V_popoverSourceView) popoverSourceView;
@property (T@"UITextInputAssistantItem",W,N,V_observedInputAssistantItem) observedInputAssistantItem;
@property (T@"NSMutableDictionary",&,N,V_cachedPredictiveViewControllers) cachedPredictiveViewControllers;
@property (T@"TUISystemInputAssistantLayoutStandard",&,N,V_standardAssistantViewLayout) standardAssistantViewLayout;
@property (T@"TUISystemInputAssistantLayoutSplit",&,N,V_splitAssistantViewLayout) splitAssistantViewLayout;
@property (T@"TUISystemInputAssistantLayout",&,N,V_floatAssistantViewLayout) floatAssistantViewLayout;
@property (T@"TUISystemInputAssistantLayout",&,N,V_compactAssistantViewLayout) compactAssistantViewLayout;
@property (T@"TUISystemInputAssistantStyleStandard",&,N,V_standardStyle) standardStyle;
@property (T@"TUISystemInputAssistantStyleFloat",&,N,V_floatStyle) floatStyle;
@property (T@"TUISystemInputAssistantStyleCompact",&,N,V_compactStyle) compactStyle;
@property (T@"UITextInputAssistantItem",&,N,V_remoteAssistantItem) remoteAssistantItem;
@property (TB,N,V_showsRemoteInputDashViewController) showsRemoteInputDashViewController;
@property (Td,N,V_remoteCenterViewPreferredWidth) remoteCenterViewPreferredWidth;
@property (T@"TUIEmojiSearchInputViewController",&,N,V_emojiSearchViewController) emojiSearchViewController;
@property (T@"UIViewController<UIPredictiveViewController>",&,N,V_predictiveViewController) predictiveViewController;
@property (T@"UIViewController",W,N,V_expandedItemsController) expandedItemsController;
@property (TB,V_assistantEnabledPreference) assistantEnabledPreference;
@property (TB,V_assistantOniPhonePreference) assistantOniPhonePreference;
@property (TB,V_hasCheckedPreferences) hasCheckedPreferences;
@property (TB,V_currentlyCheckingPreferences) currentlyCheckingPreferences;
@property (TB,N,V_assistantViewCanAnimate) assistantViewCanAnimate;
@property (Tq,N,V_assistantBarStyle) assistantBarStyle;
@property (T@"NSValue",&,N,V_currentInputDelegatePointerValue) currentInputDelegatePointerValue;
@property (T@"_UILayerHostView",&,N,V_remoteAssistantView) remoteAssistantView;
@property (T@"UIView",&,N,V_remoteAssistantContainerView) remoteAssistantContainerView;
@property (T@"UIRemoteInputViewInfo",&,N,V_remoteAssistantViewInfo) remoteAssistantViewInfo;
@property (T@"UIViewController<UIPredictiveViewController>",&,N,V_centerViewController) centerViewController;
@property (TB,R,N) supportsCompactStyle;
@property (T@"TUISystemInputAssistantView",R,N) systemInputAssistantView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISystemInputAssistantViewController _requiresProxyInterface];
+[UISystemInputAssistantViewController shouldShowSystemInputAssistantItems];
+[UISystemInputAssistantViewController floatingAssistantBottomPadding];
+[UISystemInputAssistantViewController keyboardOrientation];
+[UISystemInputAssistantViewController _defaultPreferredHeightForTraitCollection:interfaceOrientation:];
+[UISystemInputAssistantViewController _defaultPreferredHeightForTraitCollection:];
```

## Instance methods

```
-[UISystemInputAssistantViewController autocorrectionControllerDidClearAutocorrections:];
-[UISystemInputAssistantViewController adaptivePresentationStyleForPresentationController:];
-[UISystemInputAssistantViewController _hidesCenterViewForActiveWindowingMode];
-[UISystemInputAssistantViewController updateFloatingAssistantRectEdge:position:];
-[UISystemInputAssistantViewController setAssistantViewCanAnimate:];
-[UISystemInputAssistantViewController _applicationDidBecomeActiveNotification:];
-[UISystemInputAssistantViewController isEmojiSearchResultsVisible];
-[UISystemInputAssistantViewController emojiSearchTextFieldDidBecomeInactive:];
-[UISystemInputAssistantViewController expandedItemsController];
-[UISystemInputAssistantViewController setRemoteCenterViewPreferredWidth:];
-[UISystemInputAssistantViewController setCurrentlyCheckingPreferences:];
-[UISystemInputAssistantViewController setSplitAssistantViewLayout:];
-[UISystemInputAssistantViewController observedInputAssistantItem];
-[UISystemInputAssistantViewController _usesCustomBackground];
-[UISystemInputAssistantViewController _updateSystemInputAssistantViewStylingForInputAssistantItem:];
-[UISystemInputAssistantViewController compactAssistantViewLayout];
-[UISystemInputAssistantViewController emojiSearchTextFieldDidBecomeActive:];
-[UISystemInputAssistantViewController emojiSearchTextFieldWillBecomeInactive:];
-[UISystemInputAssistantViewController compatibilityViewController];
-[UISystemInputAssistantViewController _registerForAssistantViewNotifications];
-[UISystemInputAssistantViewController observeValueForKeyPath:ofObject:change:context:];
-[UISystemInputAssistantViewController preferencesControllerChanged:];
-[UISystemInputAssistantViewController splitAssistantViewLayout];
-[UISystemInputAssistantViewController setEmojiSearchViewController:];
-[UISystemInputAssistantViewController emojiSearchTextFieldWillBecomeActive:];
-[UISystemInputAssistantViewController _writingDirectionChanged:];
-[UISystemInputAssistantViewController layoutHasBuiltinAssistantView];
-[UISystemInputAssistantViewController _shouldCollapseEmojiSearchView];
-[UISystemInputAssistantViewController setCenterViewController:];
-[UISystemInputAssistantViewController _willShowKeyboardSwitcher];
-[UISystemInputAssistantViewController dismissEmojiSearch];
-[UISystemInputAssistantViewController setPopoverSourceView:];
-[UISystemInputAssistantViewController init];
-[UISystemInputAssistantViewController systemInputAssistantView:wantsToShowCollapsedItemGroup:fromView:];
-[UISystemInputAssistantViewController setStandardAssistantViewLayout:];
-[UISystemInputAssistantViewController _updateLanguageIndicatorPointerInteractionAndImage];
-[UISystemInputAssistantViewController _defaultTintColor];
-[UISystemInputAssistantViewController updateContainsWritingToolsItem:];
-[UISystemInputAssistantViewController automaticallySetCenterViewControllerBasedOnInputDelegate:];
-[UISystemInputAssistantViewController hasCheckedPreferences];
-[UISystemInputAssistantViewController setCompactAssistantViewLayout:];
-[UISystemInputAssistantViewController remoteAssistantViewInfo];
-[UISystemInputAssistantViewController shouldBeShownForInputDelegate:inputViews:];
-[UISystemInputAssistantViewController dealloc];
-[UISystemInputAssistantViewController _willChangeTextEffectsRotationNotification:];
-[UISystemInputAssistantViewController setFloatAssistantViewLayout:];
-[UISystemInputAssistantViewController prepareForPopoverPresentation:];
-[UISystemInputAssistantViewController floatStyle];
-[UISystemInputAssistantViewController setHasCheckedPreferences:];
-[UISystemInputAssistantViewController standardAssistantViewLayout];
-[UISystemInputAssistantViewController placeholderItemOfWidth:];
-[UISystemInputAssistantViewController assistantEnabledPreference];
-[UISystemInputAssistantViewController prepareForFloating:];
-[UISystemInputAssistantViewController viewDidLoad];
-[UISystemInputAssistantViewController updateAssistantBarStyle:];
-[UISystemInputAssistantViewController updateRemoteAssistantViewHidden];
-[UISystemInputAssistantViewController _updateCenterViewWidthAndRenderConfig];
-[UISystemInputAssistantViewController isInputAssistantItemEmpty];
-[UISystemInputAssistantViewController _allowedToShowBarButtonItemsInline:];
-[UISystemInputAssistantViewController dismissLanguageIndicatorMenuIfNeeded];
-[UISystemInputAssistantViewController floatAssistantViewLayout];
-[UISystemInputAssistantViewController systemInputAssistantView];
-[UISystemInputAssistantViewController showEmojiSearch:];
-[UISystemInputAssistantViewController setInputAssistantButtonItemsForResponder:];
-[UISystemInputAssistantViewController candidateViewController];
-[UISystemInputAssistantViewController _popoverViewControllerForBarButtonItemGroup:];
-[UISystemInputAssistantViewController setStandardStyle:];
-[UISystemInputAssistantViewController _currentInputDelegate];
-[UISystemInputAssistantViewController _inputDelegateAsResponder:];
-[UISystemInputAssistantViewController setAssistantBarStyle:];
-[UISystemInputAssistantViewController remoteAssistantItem];
-[UISystemInputAssistantViewController cachedPredictiveViewControllers];
-[UISystemInputAssistantViewController autocorrectionController:didUpdateAutocorrectionList:];
-[UISystemInputAssistantViewController viewWillAppear:];
-[UISystemInputAssistantViewController emojiSearchWillInsertEmoji:forSearchQuery:];
-[UISystemInputAssistantViewController setRemoteAssistantView:];
-[UISystemInputAssistantViewController _responderChangedNotification:];
-[UISystemInputAssistantViewController _textDidChange];
-[UISystemInputAssistantViewController _emojiSearchField];
-[UISystemInputAssistantViewController _canShowWhileLocked];
-[UISystemInputAssistantViewController shouldShowEmojiSearchViewControllerForInputDelegate:];
-[UISystemInputAssistantViewController isVisibleWhenMinimized];
-[UISystemInputAssistantViewController _expandBarItems];
-[UISystemInputAssistantViewController _buttonBarWidthForTraitCollection:interfaceOrientation:];
-[UISystemInputAssistantViewController maskInputAssistantView];
-[UISystemInputAssistantViewController _shouldShowExpandableButtonBarItemsForResponder:];
-[UISystemInputAssistantViewController keyboardDidChange];
-[UISystemInputAssistantViewController _centerViewWidthForTraitCollection:interfaceOrientation:];
-[UISystemInputAssistantViewController setCurrentInputDelegatePointerValue:];
-[UISystemInputAssistantViewController loadView];
-[UISystemInputAssistantViewController _centerViewWidthForTraitCollection:];
-[UISystemInputAssistantViewController barFrame];
-[UISystemInputAssistantViewController setOverrideSafeAreaInsets];
-[UISystemInputAssistantViewController _beginObservingInputAssistantItemForRelevantItemChanges:];
-[UISystemInputAssistantViewController setAssistantOniPhonePreference:];
-[UISystemInputAssistantViewController _canShowCenterBarButtonItem];
-[UISystemInputAssistantViewController predictionViewController];
-[UISystemInputAssistantViewController setShowsRemoteInputDashViewController:];
-[UISystemInputAssistantViewController dismissDictationMenuIfNeeded];
-[UISystemInputAssistantViewController applyRemoteAssistantItem:];
-[UISystemInputAssistantViewController setObservedInputAssistantItem:];
-[UISystemInputAssistantViewController supportsCompactStyle];
-[UISystemInputAssistantViewController _customCenterBarButtonItem:];
-[UISystemInputAssistantViewController assistantBarStyle];
-[UISystemInputAssistantViewController _assistantItemsVisibleForResponder:];
-[UISystemInputAssistantViewController dismissKeyboardItemIfNeeded];
-[UISystemInputAssistantViewController _hasCustomCenterViewControllerWidth];
-[UISystemInputAssistantViewController _isAssistantPreferenceEnabled];
-[UISystemInputAssistantViewController assistantOniPhonePreference];
-[UISystemInputAssistantViewController _shouldCheckItemsVisibility];
-[UISystemInputAssistantViewController _centerPredictionViewVisibleForInputDelegate:inputViews:];
-[UISystemInputAssistantViewController styleFromAssistantBarStyle:];
-[UISystemInputAssistantViewController _responderCapabilitiesChangedNotification:];
-[UISystemInputAssistantViewController currentInputDelegatePointerValue];
-[UISystemInputAssistantViewController showsRemoteInputDashViewController];
-[UISystemInputAssistantViewController shouldUseCustomBackground:];
-[UISystemInputAssistantViewController remoteAssistantContainerView];
-[UISystemInputAssistantViewController setNeedsValidation];
-[UISystemInputAssistantViewController setCachedPredictiveViewControllers:];
-[UISystemInputAssistantViewController _didChangePlacementOrInputSourceNotification:];
-[UISystemInputAssistantViewController setFloatStyle:];
-[UISystemInputAssistantViewController _isEmojiInputMode];
-[UISystemInputAssistantViewController _updateViewsForAssistantBarStyle:];
-[UISystemInputAssistantViewController standardStyle];
-[UISystemInputAssistantViewController setPredictiveViewController:];
-[UISystemInputAssistantViewController setAssistantEnabledPreference:];
-[UISystemInputAssistantViewController preferredHeightForTraitCollection:];
-[UISystemInputAssistantViewController _updateCenterViewWidthForInterfaceOrientation:];
-[UISystemInputAssistantViewController _showCandidates];
-[UISystemInputAssistantViewController prepareTransition:animated:];
-[UISystemInputAssistantViewController remoteAssistantView];
-[UISystemInputAssistantViewController containsWritingToolsButton];
-[UISystemInputAssistantViewController UIAssistantItemForRTIAssistantItem:];
-[UISystemInputAssistantViewController animatableElement];
-[UISystemInputAssistantViewController compactStyle];
-[UISystemInputAssistantViewController preferredHeightForTraitCollection:orientation:];
-[UISystemInputAssistantViewController _collapseBarItems];
-[UISystemInputAssistantViewController popoverPresentationControllerDidDismissPopover:];
-[UISystemInputAssistantViewController _candidatesChanged];
-[UISystemInputAssistantViewController setCompactStyle:];
-[UISystemInputAssistantViewController setExpandedItemsController:];
-[UISystemInputAssistantViewController currentlyCheckingPreferences];
-[UISystemInputAssistantViewController inputWindowController];
-[UISystemInputAssistantViewController remoteCenterViewPreferredWidth];
-[UISystemInputAssistantViewController updateAssistantPreferences];
-[UISystemInputAssistantViewController setRemoteAssistantViewInfo:];
-[UISystemInputAssistantViewController updateCenterViewVisibilityStateForInputDelegate:];
-[UISystemInputAssistantViewController layoutFromAssistantBarStyle:];
-[UISystemInputAssistantViewController _customCenterViewController:];
-[UISystemInputAssistantViewController setRemoteAssistantContainerView:];
-[UISystemInputAssistantViewController predictiveViewController];
-[UISystemInputAssistantViewController setRemoteAssistantItem:];
-[UISystemInputAssistantViewController _didChangeTextEffectsRotationNotification:];
-[UISystemInputAssistantViewController popoverSourceView];
-[UISystemInputAssistantViewController _dismissEmojiSearch];
-[UISystemInputAssistantViewController assistantViewCanAnimate];
-[UISystemInputAssistantViewController UIGroupsForRTIGroups:];
-[UISystemInputAssistantViewController _willChangePlacementNotification:];
-[UISystemInputAssistantViewController _inputModeChanged:];
-[UISystemInputAssistantViewController emojiSearchViewController];
-[UISystemInputAssistantViewController _queueResponderChangedForNewResponder:];
-[UISystemInputAssistantViewController centerViewController];
-[UISystemInputAssistantViewController _keyboardDictationAvailabilityDidChangeNotification:];
```
