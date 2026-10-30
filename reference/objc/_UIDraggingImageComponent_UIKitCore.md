# `_UIDraggingImageComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _ignoresAccessibilityFilters;
B _hidesImage;
@"UIView" _view;
@"UIImage" _image;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"UIView",R,N,V_view) view;
@property (T@"UIImage",R,N,V_image) image;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (TB,R,N,V_ignoresAccessibilityFilters) ignoresAccessibilityFilters;
@property (TB,R,N,V_hidesImage) hidesImage;
```

## Instance methods

```
-[_UIDraggingImageComponent initWithView:];
-[_UIDraggingImageComponent view];
-[_UIDraggingImageComponent description];
-[_UIDraggingImageComponent image];
-[_UIDraggingImageComponent copyWithZone:];
-[_UIDraggingImageComponent hidesImage];
-[_UIDraggingImageComponent frame];
-[_UIDraggingImageComponent _initWithNoImageAndFrame:];
-[_UIDraggingImageComponent ignoresAccessibilityFilters];
-[_UIDraggingImageComponent initHidingDragImage];
-[_UIDraggingImageComponent initWithImage:frame:ignoreAccessibilityFilters:];
```
