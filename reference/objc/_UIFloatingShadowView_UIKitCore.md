# `_UIFloatingShadowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 10 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"UIView" _shadowView;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _shadowTransform;
B _shadowEnabled;
B __disableOutsetShadowPath;
d _shadowRadius;
d _shadowOpacity;
d _shadowVerticalOffset;
d _shadowExpansion;
@"UIImage" _shadowImage;
d _cornerRadius;
{CGSize="width"d"height"d} _shadowSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _shadowContentsCenter;
```

## Properties

```
@property (TB,N,GisShadowEnabled,V_shadowEnabled) shadowEnabled;
@property (T{CGSize=dd},N,V_shadowSize) shadowSize;
@property (Td,N,V_shadowRadius) shadowRadius;
@property (Td,N,V_shadowOpacity) shadowOpacity;
@property (Td,N,V_shadowVerticalOffset) shadowVerticalOffset;
@property (Td,N,V_shadowExpansion) shadowExpansion;
@property (T@"UIImage",&,N,V_shadowImage) shadowImage;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_shadowContentsCenter) shadowContentsCenter;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TB,N,V__disableOutsetShadowPath) _disableOutsetShadowPath;
```

## Class methods

```
+[_UIFloatingShadowView layerClass];
```

## Instance methods

```
-[_UIFloatingShadowView setShadowRadius:];
-[_UIFloatingShadowView shadowImage];
-[_UIFloatingShadowView layoutSubviews];
-[_UIFloatingShadowView setCornerRadius:];
-[_UIFloatingShadowView setShadowImage:];
-[_UIFloatingShadowView cornerRadius];
-[_UIFloatingShadowView isShadowEnabled];
-[_UIFloatingShadowView shadowOpacity];
-[_UIFloatingShadowView _layoutShadow];
-[_UIFloatingShadowView setShadowEnabled:];
-[_UIFloatingShadowView initWithFrame:];
-[_UIFloatingShadowView shadowRadius];
-[_UIFloatingShadowView setShadowOpacity:];
-[_UIFloatingShadowView shadowExpansion];
-[_UIFloatingShadowView _disableOutsetShadowPath];
-[_UIFloatingShadowView _setShadowImageIfNeeded];
-[_UIFloatingShadowView _shadowPathForSize:radius:];
-[_UIFloatingShadowView _updateShadowLayer];
-[_UIFloatingShadowView setShadowContentsCenter:];
-[_UIFloatingShadowView setShadowExpansion:];
-[_UIFloatingShadowView setShadowSize:];
-[_UIFloatingShadowView setShadowVerticalOffset:];
-[_UIFloatingShadowView set_disableOutsetShadowPath:];
-[_UIFloatingShadowView shadowContentsCenter];
-[_UIFloatingShadowView shadowSize];
-[_UIFloatingShadowView shadowVerticalOffset];
```
