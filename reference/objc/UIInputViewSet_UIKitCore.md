# `UIInputViewSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 39 properties, 95 instance methods, 9 class methods

## Instance variables

```
B _isSplit;
d _splitHeightDelta;
@"UIResponder" _restorableResponder;
@"UIKBRenderConfig" _restorableRenderConfig;
@"UIResponder" _accessoryViewNextResponder;
@"UIResponder" _accessoryControllerNextResponder;
B _restoreUsingBecomeFirstResponder;
@"UIView" _inputView;
@"UIView" _inputAccessoryView;
@"UIView" _inputAssistantView;
@"UIInputViewController" _inputViewController;
@"UIInputViewController" _accessoryViewController;
@"UIInputViewController" _assistantViewController;
B _isNullInputView;
B _isCustomInputView;
B _shouldShowDockView;
B _isRemoteKeyboard;
B _shouldShowInputSwitcherView;
@"UIResponder" _accessorControllerNextResponder;
@"UIView" _inputSwitcherView;
@"UIView" _hostedCustomInputView;
d _bottomPaddingForPortrait;
d _bottomPaddingForLandscape;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputAssistantViewBounds;
```

## Properties

```
@property (Td,N,V_bottomPaddingForPortrait) bottomPaddingForPortrait;
@property (Td,N,V_bottomPaddingForLandscape) bottomPaddingForLandscape;
@property (T@"UIView",&,N,V_inputView) inputView;
@property (T@"UIView",&,N,V_hostedCustomInputView) hostedCustomInputView;
@property (T@"UIView",&,N,V_inputAssistantView) inputAssistantView;
@property (T@"UIView",&,N,V_inputAccessoryView) inputAccessoryView;
@property (T@"UIInputViewController",&,N,V_inputViewController) inputViewController;
@property (T@"UIInputViewController",&,N,V_assistantViewController) assistantViewController;
@property (T@"UIInputViewController",&,N,V_accessoryViewController) accessoryViewController;
@property (T@"UIView",R,N) layeringView;
@property (TB,R,N) visible;
@property (TB,R,N) usesKeyClicks;
@property (T@"UIKeyboard",R,N) keyboard;
@property (T@"UIView",R,N,V_inputSwitcherView) inputSwitcherView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) inputAccessoryViewBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_inputAssistantViewBounds) inputAssistantViewBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) inputViewBounds;
@property (TB,R,N,GisEmpty) empty;
@property (TB,R,N) hasNonPlaceholderViews;
@property (TB,R,N) supportsSplit;
@property (TB,R,N,V_isSplit) isSplit;
@property (TB,R,N) inputViewKeyboardCanSplit;
@property (T@"UIResponder",W,N,V_restorableResponder) restorableResponder;
@property (T@"UIKBRenderConfig",&,N,V_restorableRenderConfig) restorableRenderConfig;
@property (T@"UIResponder",W,N,V_accessoryViewNextResponder) accessoryViewNextResponder;
@property (T@"UIResponder",W,N,V_accessorControllerNextResponder) accessoryControllerNextResponder;
@property (TB,R,N) isInputViewPlaceholder;
@property (TB,R,N) isInputAssistantViewPlaceholder;
@property (TB,R,N) isInputAccessoryViewPlaceholder;
@property (TB,R,N) _inputViewIsSplit;
@property (Td,N,V_splitHeightDelta) splitHeightDelta;
@property (T@"UIView",R,N) splitExemptSubview;
@property (TB,N) restoreUsingBecomeFirstResponder;
@property (TB,N,V_isCustomInputView) isCustomInputView;
@property (TB,N,V_shouldShowDockView) shouldShowDockView;
@property (TB,N,V_isRemoteKeyboard) isRemoteKeyboard;
@property (TB,R,N,V_isNullInputView) isNullInputView;
@property (TB,R,N) isLocalMinimumHeightInputView;
@property (TB,N,V_shouldShowInputSwitcherView) shouldShowInputSwitcherView;
```

## Class methods

```
+[UIInputViewSet inputSetWithKeyboardAndAccessoryView:assistantView:];
+[UIInputViewSet inputSetWithOriginalInputSet:duplicateInputView:duplicateInputAccessoryView:duplicateInputAssistantView:];
+[UIInputViewSet inputSetWithPlaceholderAndAccessoryView:];
+[UIInputViewSet inputSetWithPlaceholderAndAccessoryView:assistantView:];
+[UIInputViewSet emptyInputSet];
+[UIInputViewSet inputSetWithInputView:accessoryView:];
+[UIInputViewSet inputSetWithPlaceholderAndCustomInputView:accessoryView:assistantView:];
+[UIInputViewSet inputSetWithKeyboardAndAccessoryView:];
+[UIInputViewSet inputSetWithInputView:accessoryView:assistantView:];
```

## Instance methods

```
-[UIInputViewSet isSplit];
-[UIInputViewSet inputViewController];
-[UIInputViewSet inputAssistantView];
-[UIInputViewSet supportsSplit];
-[UIInputViewSet setInputAssistantView:];
-[UIInputViewSet setAccessoryControllerNextResponder:];
-[UIInputViewSet restorableRenderConfig];
-[UIInputViewSet _rightInputViewSetFrame];
-[UIInputViewSet setInputAccessoryView:];
-[UIInputViewSet inputAccessoryView];
-[UIInputViewSet keyboard];
-[UIInputViewSet setShouldShowInputSwitcherView:];
-[UIInputViewSet visible];
-[UIInputViewSet inputSwitcherView];
-[UIInputViewSet isInputAssistantViewPlaceholder];
-[UIInputViewSet _setSplitProgress:];
-[UIInputViewSet inputViewBounds];
-[UIInputViewSet _setRenderConfig:];
-[UIInputViewSet _leftInputViewSetFrame];
-[UIInputViewSet refreshPresentation];
-[UIInputViewSet isLocalMinimumHeightInputView];
-[UIInputViewSet hostedCustomInputView];
-[UIInputViewSet dealloc];
-[UIInputViewSet accessoryControllerNextResponder];
-[UIInputViewSet initWithInputView:customInputView:accessoryView:assistantView:isKeyboard:];
-[UIInputViewSet bottomPaddingForLandscape];
-[UIInputViewSet setBottomPaddingForPortrait:];
-[UIInputViewSet setIsRemoteKeyboard:];
-[UIInputViewSet inputSetWithInputAccessoryViewFromInputSet:];
-[UIInputViewSet setIsCustomInputView:];
-[UIInputViewSet setRestoreUsingBecomeFirstResponder:];
-[UIInputViewSet _beginSplitTransitionIfNeeded];
-[UIInputViewSet layeringView];
-[UIInputViewSet _inputViewIsSplit];
-[UIInputViewSet setShouldShowDockView:];
-[UIInputViewSet restorableResponder];
-[UIInputViewSet inputViewSplitHeight];
-[UIInputViewSet accessoryViewController];
-[UIInputViewSet keyboardOrientation:];
-[UIInputViewSet inputView];
-[UIInputViewSet _inputViewIsVisible];
-[UIInputViewSet initWithInputView:accessoryView:assistantView:isKeyboard:];
-[UIInputViewSet isStrictSupersetOfViewSet:];
-[UIInputViewSet canAnimateToInputViewSet:];
-[UIInputViewSet accessoryViewNextResponder];
-[UIInputViewSet inputAssistantViewBounds];
-[UIInputViewSet setAccessoryViewVisible:delay:];
-[UIInputViewSet isInputAccessoryViewPlaceholder];
-[UIInputViewSet isEmpty];
-[UIInputViewSet _inputViewSetSupportsSplit];
-[UIInputViewSet setSplitHeightDelta:];
-[UIInputViewSet inputSetWithInputAccessoryViewOnly];
-[UIInputViewSet containsView:];
-[UIInputViewSet containsResponder:];
-[UIInputViewSet _themableInputAccessoryView];
-[UIInputViewSet _actLikeInputAccessoryViewSupportsSplit];
-[UIInputViewSet setAccessoryViewController:];
-[UIInputViewSet setBottomPaddingForLandscape:];
-[UIInputViewSet normalizePlaceholders];
-[UIInputViewSet restoreUsingBecomeFirstResponder];
-[UIInputViewSet shouldShowDockView];
-[UIInputViewSet _inputAccessoryViewSupportsSplit];
-[UIInputViewSet description];
-[UIInputViewSet setAccessoryViewNextResponder:];
-[UIInputViewSet _splittableInputAccessoryView];
-[UIInputViewSet isRemoteKeyboard];
-[UIInputViewSet setInputView:];
-[UIInputViewSet hasNonPlaceholderViews];
-[UIInputViewSet setRestorableRenderConfig:];
-[UIInputViewSet setHostedCustomInputView:];
-[UIInputViewSet isCustomInputView];
-[UIInputViewSet isNullInputView];
-[UIInputViewSet splitHeightDelta];
-[UIInputViewSet _inputViewSupportsSplit];
-[UIInputViewSet _forceRestoreUsingBecomeFirstResponder:];
-[UIInputViewSet usesKeyClicks];
-[UIInputViewSet inheritNullState:];
-[UIInputViewSet shouldShowInputSwitcherView];
-[UIInputViewSet inputAccessoryViewBounds];
-[UIInputViewSet isEqual:];
-[UIInputViewSet assistantViewController];
-[UIInputViewSet __isCKAccessoryView];
-[UIInputViewSet onscreenSizeOfViewsInSetIncludingIAV:];
-[UIInputViewSet inputViewKeyboardCanSplit];
-[UIInputViewSet splitExemptSubview];
-[UIInputViewSet _endSplitTransitionIfNeeded];
-[UIInputViewSet setAssistantViewController:];
-[UIInputViewSet setInputViewController:];
-[UIInputViewSet isInputViewPlaceholder];
-[UIInputViewSet setKeyboardAssistantBar:];
-[UIInputViewSet hierarchyContainsView:];
-[UIInputViewSet setRestorableResponder:];
-[UIInputViewSet bottomPaddingForPortrait];
-[UIInputViewSet _isFullscreen];
-[UIInputViewSet _isKeyboard];
```
