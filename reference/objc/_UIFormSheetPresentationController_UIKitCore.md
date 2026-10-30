# `_UIFormSheetPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISheetPresentationController`
- 2 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _layoutStateShouldAvoidKeyboard;
d _keyboardYOrigin;
```

## Class methods

```
+[_UIFormSheetPresentationController _initialMode];
```

## Instance methods

```
-[_UIFormSheetPresentationController _keyboardWillShow:];
-[_UIFormSheetPresentationController _keyboardWillHide:];
-[_UIFormSheetPresentationController _defaultPresentationStyleForTraitCollection:];
-[_UIFormSheetPresentationController _shouldHideBottomCorner];
-[_UIFormSheetPresentationController frameOfPresentedViewInContainerView];
-[_UIFormSheetPresentationController _changeLayoutModeToAvoidKeyboard:withOrigin:];
-[_UIFormSheetPresentationController shouldSubscribeToKeyboardNotifications];
-[_UIFormSheetPresentationController _presentationPotentiallyUnderlapsStatusBar];
-[_UIFormSheetPresentationController _shouldPresentedViewControllerControlStatusBarAppearance];
-[_UIFormSheetPresentationController dismissalTransitionWillBegin];
-[_UIFormSheetPresentationController sizeForChildContentContainer:withParentContainerSize:];
-[_UIFormSheetPresentationController presentationTransitionWillBegin];
```
