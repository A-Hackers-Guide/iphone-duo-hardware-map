# `UIKBViewBackedKeyView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBKeyView`
- 3 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIView<UIKBKeyViewContentView>" _contentView;
@"UIView" _touchForwardingView;
@"UIKBBackdropView" _backdropView;
```

## Properties

```
@property (T@"UIKBBackdropView",&,N,V_backdropView) backdropView;
@property (T@"UIView<UIKBKeyViewContentView>",&,N,V_contentView) contentView;
@property (T@"UIView",W,N,V_touchForwardingView) touchForwardingView;
```

## Instance methods

```
-[UIKBViewBackedKeyView setBackdropView:];
-[UIKBViewBackedKeyView setDrawFrame:];
-[UIKBViewBackedKeyView backdropView];
-[UIKBViewBackedKeyView retestSelectedVariantIndexForKey:atPoint:phase:];
-[UIKBViewBackedKeyView setContentView:];
-[UIKBViewBackedKeyView initWithFrame:keyplane:key:];
-[UIKBViewBackedKeyView setRenderConfig:];
-[UIKBViewBackedKeyView updateForKeyplane:key:];
-[UIKBViewBackedKeyView layoutSubviews];
-[UIKBViewBackedKeyView hitTest:withEvent:];
-[UIKBViewBackedKeyView contentView];
-[UIKBViewBackedKeyView pointInside:withEvent:];
-[UIKBViewBackedKeyView renderFlagsForTraits:];
-[UIKBViewBackedKeyView setTouchForwardingView:];
-[UIKBViewBackedKeyView touchForwardingView];
```
