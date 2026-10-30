# `UIAccessibilityHUDView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 1 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"UIAccessibilityHUDItem" _item;
@"UIView" _transformContainer;
@"UIVisualEffectView" _effectView;
@"UIBlurEffect" _blurEffect;
@"UIVisualEffectView" _itemEffectView;
@"UIImageView" _imageView;
@"UILabel" _titleLabel;
@"UIView" _customView;
```

## Properties

```
@property (T@"UIAccessibilityHUDItem",C,N,V_item) item;
```

## Class methods

```
+[UIAccessibilityHUDView preferredHUDSize];
```

## Instance methods

```
-[UIAccessibilityHUDView customView];
-[UIAccessibilityHUDView titleLabel];
-[UIAccessibilityHUDView layoutManager];
-[UIAccessibilityHUDView setItem:];
-[UIAccessibilityHUDView dismissAnimated:completion:];
-[UIAccessibilityHUDView layoutSubviews];
-[UIAccessibilityHUDView item];
-[UIAccessibilityHUDView sizeThatFits:];
-[UIAccessibilityHUDView imageView];
-[UIAccessibilityHUDView _contentEffectsForItem:];
-[UIAccessibilityHUDView _show:animated:completion:];
-[UIAccessibilityHUDView _updateLabelForItem];
-[UIAccessibilityHUDView containerViewForLayout];
-[UIAccessibilityHUDView imageInsetsForLayout];
-[UIAccessibilityHUDView initWithHUDItem:];
-[UIAccessibilityHUDView itemContainerViewForLayout];
-[UIAccessibilityHUDView showAnimated:completion:];
```
