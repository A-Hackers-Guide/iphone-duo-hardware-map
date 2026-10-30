# `UIInputViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UITextDocumentInterfaceDelegate`, `UITextInputDelegate`
- 9 instance variables, 18 properties, 50 instance methods, 4 class methods

## Instance variables

```
B _commitInputModeOnTouchEnd;
B _inputModeListIsShown;
B _viewConformsToRemotePlaceholder;
d _touchBegan;
B _alignsToContentViewController;
B _autosizeToCurrentKeyboard;
B _hasDictationKey;
@"<UITextDocumentProxy>" _textDocumentProxy;
@"NSString" _primaryLanguage;
```

## Properties

```
@property (T@"UIKeyboard",R,N) _keyboard;
@property (TB,R,N) _isPlaceholder;
@property (TB,N,V_alignsToContentViewController) _alignsToContentViewController;
@property (TB,N,S_setAutosizeToCurrentKeyboard:,V_autosizeToCurrentKeyboard) _autosizeToCurrentKeyboard;
@property (T@"UIKeyboard",R,N) _keyboard;
@property (TB,R,N) _isPlaceholder;
@property (TB,N) _alignsToContentViewController;
@property (TB,N,S_setAutosizeToCurrentKeyboard:) _autosizeToCurrentKeyboard;
@property (T@"UIInputView",&,N) inputView;
@property (T@"<UITextDocumentProxy>",R,N,V_textDocumentProxy) textDocumentProxy;
@property (T@"NSString",C,N,V_primaryLanguage) primaryLanguage;
@property (TB,N,V_hasDictationKey) hasDictationKey;
@property (TB,R,N) hasFullAccess;
@property (TB,R,N) needsInputModeSwitchKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInputViewController _requiresProxyInterface];
+[UIInputViewController _autoFillContextForAutomaticStrongPasswords];
+[UIInputViewController prepareForNextKeyResponderFromCurrentWindowSceneResponder:];
+[UIInputViewController presentDialogForAddingKeyboard];
```

## Instance methods

```
-[UIInputViewController _keyboard];
-[UIInputViewController handleInputModeListFromView:withEvent:];
-[UIInputViewController _canBecomeFirstResponder];
-[UIInputViewController _usesCustomBackground];
-[UIInputViewController set_autosizeToCurrentKeyboard:];
-[UIInputViewController primaryLanguage];
-[UIInputViewController _proxyInterface];
-[UIInputViewController _shouldForwardSystemLayoutFittingSizeChanges];
-[UIInputViewController set_alignsToContentViewController:];
-[UIInputViewController _autosizeToCurrentKeyboard];
-[UIInputViewController _systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[UIInputViewController textDocumentProxy];
-[UIInputViewController textDidChange:];
-[UIInputViewController dealloc];
-[UIInputViewController selectionWillChange:];
-[UIInputViewController _textDocumentInterface];
-[UIInputViewController viewDidLoad];
-[UIInputViewController setView:];
-[UIInputViewController _didResetDocumentState];
-[UIInputViewController _isPlaceholder];
-[UIInputViewController initWithNibName:bundle:];
-[UIInputViewController hasFullAccess];
-[UIInputViewController inputView];
-[UIInputViewController viewDidAppear:];
-[UIInputViewController _alignsToContentViewController];
-[UIInputViewController _setExtensionContextUUID:];
-[UIInputViewController _setTextDocumentProxy:];
-[UIInputViewController loadView];
-[UIInputViewController _setAutosizeToCurrentKeyboard:];
-[UIInputViewController textWillChange:];
-[UIInputViewController needsInputModeSwitchKey];
-[UIInputViewController didReceiveMemoryWarning];
-[UIInputViewController _updateConformanceCache];
-[UIInputViewController selectionDidChange:];
-[UIInputViewController setHasDictationKey:];
-[UIInputViewController initWithCoder:];
-[UIInputViewController setInputView:];
-[UIInputViewController _canResignIfContainsFirstResponder];
-[UIInputViewController requestSupplementaryLexiconWithCompletion:];
-[UIInputViewController setPrimaryLanguage:];
-[UIInputViewController _setupInputController];
-[UIInputViewController animatableElement];
-[UIInputViewController hasDictationKey];
-[UIInputViewController returnToPreviousInputMode];
-[UIInputViewController _extensionContext];
-[UIInputViewController dismissKeyboard];
-[UIInputViewController advanceToNextInputMode];
-[UIInputViewController _willResetDocumentState];
-[UIInputViewController proceedShouldReturnIfPossibleForASP];
-[UIInputViewController _compatibilityController];
```
