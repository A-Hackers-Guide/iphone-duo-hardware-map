# `LACUIKeyboardLayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- 4 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
cancellables;
keyboardLayoutHeightLC;
keyboardGeometry;
keyboardGeometryUpdateSubject;
```

## Properties

```
@property (T@"NSDictionary",N,R) fallbackKeyboardInfo;
@property (Tq,N,R) currentOrientation;
@property (Td,N,R) defaultHeightConstant;
```

## Instance methods

```
-[LACUIKeyboardLayoutGuide updateLayoutIfNeeded];
-[LACUIKeyboardLayoutGuide currentOrientation];
-[LACUIKeyboardLayoutGuide init];
-[LACUIKeyboardLayoutGuide initWithView:];
-[LACUIKeyboardLayoutGuide viewWillTransitionToSize:withTransitionCoordinator:];
-[LACUIKeyboardLayoutGuide initWithCoder:];
-[LACUIKeyboardLayoutGuide animateLayoutWith:animated:];
-[LACUIKeyboardLayoutGuide calculateKeyboardConstantFrom:];
-[LACUIKeyboardLayoutGuide defaultHeightConstant];
-[LACUIKeyboardLayoutGuide fallbackKeyboardInfo];
-[LACUIKeyboardLayoutGuide setupKeyboardDebouncing];
-[LACUIKeyboardLayoutGuide setupKeyboardObservers];
-[LACUIKeyboardLayoutGuide updateLayoutGuideWithUserInfo:isHide:animated:];
```
