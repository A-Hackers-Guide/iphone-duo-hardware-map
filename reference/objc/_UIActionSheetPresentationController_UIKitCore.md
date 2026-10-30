# `_UIActionSheetPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPopoverPresentationController`
- Protocols: `_UIActionSheetCompactPresentationControllerDelegate`
- 6 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _dismissActionUsesShorterHeightWhenCompactVertically;
B __shouldUseCompactPresentationControllerWhenPresentedInSheet;
B _avoidsKeyboardDisabled;
@"NSString" _dismissActionTitle;
@"<UIActionSheetPresentationControllerDelegate>" _actionSheetDelegate;
@"_UIActionSheetCompactPresentationController" _compactPresentationController;
```

## Properties

```
@property (T@"_UIActionSheetCompactPresentationController",&,N,V_compactPresentationController) compactPresentationController;
@property (TB,N,V_avoidsKeyboardDisabled) avoidsKeyboardDisabled;
@property (T@"NSString",C,N,V_dismissActionTitle) dismissActionTitle;
@property (TB,N,V_dismissActionUsesShorterHeightWhenCompactVertically) dismissActionUsesShorterHeightWhenCompactVertically;
@property (TB,N,S_setShouldUseCompactPresentationControllerWhenPresentedInSheet:,V__shouldUseCompactPresentationControllerWhenPresentedInSheet) _shouldUseCompactPresentationControllerWhenPresentedInSheet;
@property (T@"<UIActionSheetPresentationControllerDelegate>",W,N,V_actionSheetDelegate) actionSheetDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIActionSheetPresentationController _compactPresentationController];
-[_UIActionSheetPresentationController dimmingViewWasTapped:withDismissCompletion:];
-[_UIActionSheetPresentationController _presentationControllerForTraitCollection:];
-[_UIActionSheetPresentationController dealloc];
-[_UIActionSheetPresentationController _exceptionStringForNilSourceViewOrBarButtonItem];
-[_UIActionSheetPresentationController _shouldPresentedViewControllerControlStatusBarAppearance];
-[_UIActionSheetPresentationController _visualStyleForTraitCollection:];
-[_UIActionSheetPresentationController _setShouldUseCompactPresentationControllerWhenPresentedInSheet:];
-[_UIActionSheetPresentationController _presentationContextForViewController:];
-[_UIActionSheetPresentationController _shouldUseCompactPresentationControllerWhenPresentedInSheet];
-[_UIActionSheetPresentationController actionSheetCompactPresentationControllerDidDismiss:];
-[_UIActionSheetPresentationController actionSheetCompactPresentationControllerShouldPresentInCurrentContext:];
-[_UIActionSheetPresentationController actionSheetDelegate];
-[_UIActionSheetPresentationController avoidsKeyboardDisabled];
-[_UIActionSheetPresentationController beginPseudoAlertPresentationMode];
-[_UIActionSheetPresentationController compactPresentationController];
-[_UIActionSheetPresentationController dismissActionTitle];
-[_UIActionSheetPresentationController dismissActionUsesShorterHeightWhenCompactVertically];
-[_UIActionSheetPresentationController endPseudoAlertPresentationMode];
-[_UIActionSheetPresentationController setActionSheetDelegate:];
-[_UIActionSheetPresentationController setAvoidsKeyboardDisabled:];
-[_UIActionSheetPresentationController setCompactPresentationController:];
-[_UIActionSheetPresentationController setDismissActionTitle:];
-[_UIActionSheetPresentationController setDismissActionUsesShorterHeightWhenCompactVertically:];
```
