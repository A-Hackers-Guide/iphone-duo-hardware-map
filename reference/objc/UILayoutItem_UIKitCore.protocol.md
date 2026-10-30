# `UILayoutItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITraitEnvironment`
- 0 instance variables, 17 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _ui_bounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) _ui_frame;
@property (T@"UIView",R,N) _ui_superview;
@property (T@"UIView",R,N) _ui_view;
@property (TB,N) _ui_usesManualLayout;
@property (T@"NSLayoutXAxisAnchor",R,N) leadingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) trailingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) leftAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) rightAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) topAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) bottomAnchor;
@property (T@"NSLayoutDimension",R,N) widthAnchor;
@property (T@"NSLayoutDimension",R,N) heightAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) centerXAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) centerYAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) firstBaselineAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) lastBaselineAnchor;
```

## Instance methods

```
-[UILayoutItem lastBaselineAnchor];
-[UILayoutItem firstBaselineAnchor];
-[UILayoutItem _ui_addSubLayoutItem:];
-[UILayoutItem _ui_bounds];
-[UILayoutItem _ui_frame];
-[UILayoutItem _ui_insertSubLayoutItem:atIndex:];
-[UILayoutItem _ui_removeFromParentLayoutItem];
-[UILayoutItem _ui_superview];
-[UILayoutItem _ui_usesManualLayout];
-[UILayoutItem _ui_view];
-[UILayoutItem bottomAnchor];
-[UILayoutItem centerXAnchor];
-[UILayoutItem centerYAnchor];
-[UILayoutItem heightAnchor];
-[UILayoutItem leadingAnchor];
-[UILayoutItem leftAnchor];
-[UILayoutItem rightAnchor];
-[UILayoutItem set_ui_frame:];
-[UILayoutItem set_ui_usesManualLayout:];
-[UILayoutItem topAnchor];
-[UILayoutItem trailingAnchor];
-[UILayoutItem widthAnchor];
```
