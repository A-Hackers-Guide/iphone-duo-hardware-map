# `_UIInteractiveHighlightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"UIVisualEffectView" _effectView;
@"_UIInteractiveHighlightEnvironment" _environment;
@"UIView" _superview;
@"_UIPortalView" _portalView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _preferredContentInsets;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UIVisualEffectView",W,N,V_effectView) effectView;
@property (T@"_UIInteractiveHighlightEnvironment",&,N,V_environment) environment;
@property (T@"UIView",W,N,V_superview) superview;
@property (T@"_UIPortalView",W,N,V_portalView) portalView;
@property (T{UIEdgeInsets=dddd},N,V_preferredContentInsets) preferredContentInsets;
```

## Instance methods

```
-[_UIInteractiveHighlightEffect portalView];
-[_UIInteractiveHighlightEffect setEnvironment:];
-[_UIInteractiveHighlightEffect setPortalView:];
-[_UIInteractiveHighlightEffect setEffectView:];
-[_UIInteractiveHighlightEffect dealloc];
-[_UIInteractiveHighlightEffect setView:];
-[_UIInteractiveHighlightEffect view];
-[_UIInteractiveHighlightEffect effectView];
-[_UIInteractiveHighlightEffect environment];
-[_UIInteractiveHighlightEffect applyBackgroundEffectWithMagnitude:interactive:completion:];
-[_UIInteractiveHighlightEffect finalizeEffect];
-[_UIInteractiveHighlightEffect preferredContentInsets];
-[_UIInteractiveHighlightEffect setPreferredContentInsets:];
-[_UIInteractiveHighlightEffect setSuperview:];
-[_UIInteractiveHighlightEffect superview];
```
