# `_UIPopoverPresentationMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _shouldHideArrow;
B _shouldUseVisualStyleAnimationControllerForDismissal;
B _shouldUseVisualStyleAnimationControllerForPresentation;
d _cornerRadius;
```

## Properties

```
@property (TB,N,V_shouldHideArrow) shouldHideArrow;
@property (TB,N,V_shouldUseVisualStyleAnimationControllerForDismissal) shouldUseVisualStyleAnimationControllerForDismissal;
@property (TB,N,V_shouldUseVisualStyleAnimationControllerForPresentation) shouldUseVisualStyleAnimationControllerForPresentation;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T{CGSize=dd},R,N) defaultPreferredSmallContentSize;
@property (T{CGSize=dd},R,N) defaultPreferredLargeContentSize;
```

## Class methods

```
+[_UIPopoverPresentationMetrics defaultPopoverMetrics];
```

## Instance methods

```
-[_UIPopoverPresentationMetrics setCornerRadius:];
-[_UIPopoverPresentationMetrics cornerRadius];
-[_UIPopoverPresentationMetrics shouldHideArrow];
-[_UIPopoverPresentationMetrics defaultPreferredLargeContentSize];
-[_UIPopoverPresentationMetrics defaultPreferredSmallContentSize];
-[_UIPopoverPresentationMetrics setShouldHideArrow:];
-[_UIPopoverPresentationMetrics setShouldUseVisualStyleAnimationControllerForDismissal:];
-[_UIPopoverPresentationMetrics setShouldUseVisualStyleAnimationControllerForPresentation:];
-[_UIPopoverPresentationMetrics shouldUseVisualStyleAnimationControllerForDismissal];
-[_UIPopoverPresentationMetrics shouldUseVisualStyleAnimationControllerForPresentation];
```
