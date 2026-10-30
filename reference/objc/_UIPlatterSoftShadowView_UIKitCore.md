# `_UIPlatterSoftShadowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _needsPunchOut;
@"UIBezierPath" _shadowPath;
@"UIView" _backgroundView;
@"_UIPlatterShadowView" _diffuseShadowView;
@"_UIPlatterShadowView" _rimShadowView;
```

## Properties

```
@property (T@"UIView",R,N,V_backgroundView) backgroundView;
@property (T@"_UIPlatterShadowView",R,N,V_diffuseShadowView) diffuseShadowView;
@property (T@"_UIPlatterShadowView",R,N,V_rimShadowView) rimShadowView;
@property (T@"UIBezierPath",C,N,V_shadowPath) shadowPath;
@property (TB,N,V_needsPunchOut) needsPunchOut;
```

## Instance methods

```
-[_UIPlatterSoftShadowView setShadowPath:];
-[_UIPlatterSoftShadowView diffuseShadowView];
-[_UIPlatterSoftShadowView rimShadowView];
-[_UIPlatterSoftShadowView setNeedsPunchOut:];
-[_UIPlatterSoftShadowView shadowPath];
-[_UIPlatterSoftShadowView _updateForShadowPath];
-[_UIPlatterSoftShadowView initWithFrame:shadowPath:];
-[_UIPlatterSoftShadowView backgroundView];
-[_UIPlatterSoftShadowView needsPunchOut];
```
