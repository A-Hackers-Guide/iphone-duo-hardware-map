# `_UISheetPresentationControllerDetentResolutionContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UISheetPresentationControllerDetentResolutionContext`
- 0 instance variables, 9 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _containerBounds;
@property (T{UIEdgeInsets=dddd},R,N) _containerSafeAreaInsets;
@property (T@"UITraitCollection",R,N) _containerTraitCollection;
@property (TB,R,N,G_isEdgeAttached) _edgeAttached;
@property (TB,R,N,G_isInverted) _inverted;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _effectiveKeyboardFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _fullHeightPresentedViewFrame;
@property (Td,R,N) _maximumDetentValue;
@property (T{CGSize=dd},R,N) _minimumSize;
```

## Instance methods

```
-[_UISheetPresentationControllerDetentResolutionContext _containerTraitCollection];
-[_UISheetPresentationControllerDetentResolutionContext _effectiveKeyboardFrame];
-[_UISheetPresentationControllerDetentResolutionContext _fullHeightPresentedViewFrame];
-[_UISheetPresentationControllerDetentResolutionContext _maximumDetentValue];
-[_UISheetPresentationControllerDetentResolutionContext _minimumSize];
-[_UISheetPresentationControllerDetentResolutionContext _isInverted];
-[_UISheetPresentationControllerDetentResolutionContext _containerBounds];
-[_UISheetPresentationControllerDetentResolutionContext _isEdgeAttached];
-[_UISheetPresentationControllerDetentResolutionContext _containerSafeAreaInsets];
```
