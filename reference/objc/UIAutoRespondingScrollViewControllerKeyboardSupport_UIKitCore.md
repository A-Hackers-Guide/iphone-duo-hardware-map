# `UIAutoRespondingScrollViewControllerKeyboardSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIViewController<_UIKeyboardAutoRespondingScrollViewController>" _viewController;
d _adjustmentForKeyboard;
b1 _viewIsDisappearing;
b1 _registeredForNotifications;
```

## Properties

```
@property (Td,N,V_adjustmentForKeyboard) adjustmentForKeyboard;
@property (TB,N) viewIsDisappearing;
@property (TB,N) registeredForNotifications;
```

## Instance methods

```
-[UIAutoRespondingScrollViewControllerKeyboardSupport _keyboardWillShow:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport initWithViewController:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport _keyboardDidHide:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport registeredForNotifications];
-[UIAutoRespondingScrollViewControllerKeyboardSupport _keyboardWillHide:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport viewIsDisappearing];
-[UIAutoRespondingScrollViewControllerKeyboardSupport setAdjustmentForKeyboard:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport setRegisteredForNotifications:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport _adjustScrollViewForKeyboardInfo:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport _keyboardDidShow:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport _keyboardDidChangeFrame:];
-[UIAutoRespondingScrollViewControllerKeyboardSupport adjustmentForKeyboard];
-[UIAutoRespondingScrollViewControllerKeyboardSupport setViewIsDisappearing:];
```
