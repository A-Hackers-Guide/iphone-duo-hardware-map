# `UIPopoverBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPopoverBackgroundViewMethods`
- 3 instance variables, 6 properties, 28 instance methods, 6 class methods

## Instance variables

```
B __chromeHidden;
@"UIPopoverPresentationController" _presentationController;
q __backgroundBlurEffectStyle;
```

## Properties

```
@property (TB,N,S_setChromeHidden:,V__chromeHidden) _chromeHidden;
@property (Tq,N,S_setBackgroundBlurEffectStyle:,V__backgroundBlurEffectStyle) _backgroundBlurEffectStyle;
@property (T@"UITraitCollection",R,N) _traitCollectionForGlassContent;
@property (T@"UIPopoverPresentationController",W,N,S_setPresentationController:,V_presentationController) _presentationController;
@property (Td,N) arrowOffset;
@property (TQ,N) arrowDirection;
```

## Class methods

```
+[UIPopoverBackgroundView arrowBase];
+[UIPopoverBackgroundView cornerRadius];
+[UIPopoverBackgroundView arrowHeight];
+[UIPopoverBackgroundView _contentViewCornerRadiusForArrowDirection:];
+[UIPopoverBackgroundView contentViewInsets];
+[UIPopoverBackgroundView wantsDefaultContentAppearance];
```

## Instance methods

```
-[UIPopoverBackgroundView _shadowRadius];
-[UIPopoverBackgroundView actionForLayer:forKey:];
-[UIPopoverBackgroundView _contentViewFrame];
-[UIPopoverBackgroundView _shadowOpacity];
-[UIPopoverBackgroundView setArrowDirection:];
-[UIPopoverBackgroundView layoutSubviews];
-[UIPopoverBackgroundView _updateShadow];
-[UIPopoverBackgroundView backgroundStyle];
-[UIPopoverBackgroundView setArrowOffset:];
-[UIPopoverBackgroundView arrowDirection];
-[UIPopoverBackgroundView _shouldAnimatePropertyWithKey:];
-[UIPopoverBackgroundView initWithFrame:];
-[UIPopoverBackgroundView arrowOffset];
-[UIPopoverBackgroundView _traitCollectionForGlassContent];
-[UIPopoverBackgroundView _backgroundBlurEffectStyle];
-[UIPopoverBackgroundView _backgroundContentViewFrame];
-[UIPopoverBackgroundView _chromeHidden];
-[UIPopoverBackgroundView _contentViewInsets];
-[UIPopoverBackgroundView _contentViewInsetsForArrowDirection:];
-[UIPopoverBackgroundView _presentationController];
-[UIPopoverBackgroundView _setBackgroundBlurEffectStyle:];
-[UIPopoverBackgroundView _setChromeHidden:];
-[UIPopoverBackgroundView _setPresentationController:];
-[UIPopoverBackgroundView _shadowInsets];
-[UIPopoverBackgroundView _shadowOffset];
-[UIPopoverBackgroundView _shadowPath];
-[UIPopoverBackgroundView _shadowPathForRect:arrowDirection:];
-[UIPopoverBackgroundView _updateChrome];
```
