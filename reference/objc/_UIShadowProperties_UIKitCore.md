# `_UIShadowProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
d _opacity;
@"UIColor" _color;
d _radius;
{CGSize="width"d"height"d} _offset;
```

## Properties

```
@property (Td,N,V_opacity) opacity;
@property (T@"UIColor",&,N,V_color) color;
@property (T{CGSize=dd},N,V_offset) offset;
@property (Td,N,V_radius) radius;
```

## Class methods

```
+[_UIShadowProperties propertiesFromView:];
```

## Instance methods

```
-[_UIShadowProperties setColor:];
-[_UIShadowProperties applyToView:];
-[_UIShadowProperties init];
-[_UIShadowProperties scaleBy:];
-[_UIShadowProperties opacity];
-[_UIShadowProperties updatedShadowWithIntensity:];
-[_UIShadowProperties setRadius:];
-[_UIShadowProperties setOpacity:];
-[_UIShadowProperties color];
-[_UIShadowProperties radius];
-[_UIShadowProperties setOffset:];
-[_UIShadowProperties copyWithZone:];
-[_UIShadowProperties offset];
```
