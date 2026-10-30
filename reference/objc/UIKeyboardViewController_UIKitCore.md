# `UIKeyboardViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`
- 7 instance variables, 15 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _shouldUpdateLayoutAutomatically;
@"UIView<UIKeyInput>" _textInputView;
@"UIView" _pathEffectView;
Q _serviceRole;
@"UIKeyboard" _keyboard;
@"UIInputViewController" _inputViewController;
@"UISystemInputAssistantViewController" _systemInputAssistantViewController;
```

## Properties

```
@property (TQ,N,V_serviceRole) serviceRole;
@property (T@"UIKeyboard",&,N,V_keyboard) keyboard;
@property (T@"UIInputViewController",&,N,V_inputViewController) inputViewController;
@property (T@"UISystemInputAssistantViewController",&,N,V_systemInputAssistantViewController) systemInputAssistantViewController;
@property (T@"UIView<UIKeyInput>",&,N,V_textInputView) textInputView;
@property (T@"UIView",R,W,N,V_pathEffectView) pathEffectView;
@property (T@"UIView",R,N) inputAssistantView;
@property (T@"UIViewController",R,N) inputAssistantViewController;
@property (T@"UIKeyboardAutocorrectionController",R,N) autocorrectionController;
@property (TB,N,V_shouldUpdateLayoutAutomatically) shouldUpdateLayoutAutomatically;
@property (TB,N) resizable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardViewController _verifyClient];
```

## Instance methods

```
-[UIKeyboardViewController setServiceRole:];
-[UIKeyboardViewController inputViewController];
-[UIKeyboardViewController inputAssistantView];
-[UIKeyboardViewController serviceRole];
-[UIKeyboardViewController textInputView];
-[UIKeyboardViewController keyboard];
-[UIKeyboardViewController shouldUpdateLayoutAutomatically];
-[UIKeyboardViewController init];
-[UIKeyboardViewController viewWillDisappear:];
-[UIKeyboardViewController viewDidLoad];
-[UIKeyboardViewController viewWillAppear:];
-[UIKeyboardViewController systemInputAssistantViewController];
-[UIKeyboardViewController loadView];
-[UIKeyboardViewController setShouldUpdateLayoutAutomatically:];
-[UIKeyboardViewController inputAssistantViewController];
-[UIKeyboardViewController setInputViewController:];
-[UIKeyboardViewController autocorrectionController];
-[UIKeyboardViewController didSelectPredictiveCandidate:];
-[UIKeyboardViewController initWithServiceRole:];
-[UIKeyboardViewController pathEffectView];
-[UIKeyboardViewController registerProxyKeysWithViews:];
-[UIKeyboardViewController resizable];
-[UIKeyboardViewController setKeyboard:];
-[UIKeyboardViewController setResizable:];
-[UIKeyboardViewController setSystemInputAssistantViewController:];
-[UIKeyboardViewController setTextInputView:];
-[UIKeyboardViewController shouldAcceptAutocorrection];
```
