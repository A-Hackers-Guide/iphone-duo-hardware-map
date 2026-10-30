# `UIKeyboardHiddenViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIViewControllerTransitioningDelegate`, `UIInputViewControllerNeedSceneSize`
- 3 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"_SFPasswordViewController" _autofillVC;
B _presentedAutofill;
B _processingSceneDidChange;
```

## Properties

```
@property (T@"_SFPasswordViewController",&,N,V_autofillVC) autofillVC;
@property (TB,N,V_presentedAutofill) presentedAutofill;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardHiddenViewController presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[UIKeyboardHiddenViewController viewWillDisappear:];
-[UIKeyboardHiddenViewController dealloc];
-[UIKeyboardHiddenViewController presentViewController:];
-[UIKeyboardHiddenViewController initWithNibName:bundle:];
-[UIKeyboardHiddenViewController viewWillAppear:];
-[UIKeyboardHiddenViewController _canShowWhileLocked];
-[UIKeyboardHiddenViewController _deviceWillLock:];
-[UIKeyboardHiddenViewController sizeForChildContentContainer:withParentContainerSize:];
-[UIKeyboardHiddenViewController _localAuthenticationUIDismissed];
-[UIKeyboardHiddenViewController _sceneDidChange];
-[UIKeyboardHiddenViewController _localAuthenticationUIPresented];
-[UIKeyboardHiddenViewController presentAutofillVCWithAnimation:];
-[UIKeyboardHiddenViewController _formSheetObeysContentContainerSize];
-[UIKeyboardHiddenViewController autofillVC];
-[UIKeyboardHiddenViewController passwordViewControllerDidFinish:];
-[UIKeyboardHiddenViewController presentSelfWithAnimation:];
-[UIKeyboardHiddenViewController presentedAutofill];
-[UIKeyboardHiddenViewController setAutofillVC:];
-[UIKeyboardHiddenViewController setPresentedAutofill:];
-[UIKeyboardHiddenViewController shouldPresentAsPopover];
```
