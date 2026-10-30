# `UIPreviewTarget`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
{CAPoint3D="x"d"y"d"z"d} _center3D;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _transform3D;
d _contentScale;
@"UIView" _container;
```

## Properties

```
@property (T{CATransform3D=dddddddddddddddd},R,N) _transform3D;
@property (Td,N,G_contentScale,S_setContentScale:,V_contentScale) _contentScale;
@property (T@"UIView",R,N,V_container) container;
@property (T{CGPoint=dd},R,D,N) center;
@property (T{CGAffineTransform=dddddd},R,D,N) transform;
```

## Class methods

```
+[UIPreviewTarget new];
+[UIPreviewTarget _targetWithContainer:center:transform3D:];
```

## Instance methods

```
-[UIPreviewTarget _transform3D];
-[UIPreviewTarget _contentScale];
-[UIPreviewTarget init];
-[UIPreviewTarget initWithContainer:center:];
-[UIPreviewTarget transform];
-[UIPreviewTarget initWithContainer:center:transform:];
-[UIPreviewTarget center];
-[UIPreviewTarget _setContentScale:];
-[UIPreviewTarget _transform3DRelativeToWindow:];
-[UIPreviewTarget description];
-[UIPreviewTarget copyWithZone:];
-[UIPreviewTarget isEqual:];
-[UIPreviewTarget container];
```
