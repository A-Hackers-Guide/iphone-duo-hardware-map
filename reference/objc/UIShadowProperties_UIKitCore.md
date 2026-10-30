# `UIShadowProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `NSCoding`
- 1 instance variables, 12 properties, 29 instance methods, 1 class methods

## Instance variables

```
_backingProperties;
```

## Properties

```
@property (T@"UIColor",N,&) color;
@property (T@"UIColor",N,&) _color;
@property (Td,N) opacity;
@property (Td,N) _opacity;
@property (Td,N) radius;
@property (Td,N) _radius;
@property (T{CGSize=dd},N) offset;
@property (T{CGSize=dd},N) _offset;
@property (T@"UIBezierPath",N,&) path;
@property (T@"UIBezierPath",N,&) _path;
@property (Tq,N) _backgroundConfigurationShadowType;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIShadowProperties supportsSecureCoding];
```

## Instance methods

```
-[UIShadowProperties _color];
-[UIShadowProperties setColor:];
-[UIShadowProperties init];
-[UIShadowProperties _path];
-[UIShadowProperties opacity];
-[UIShadowProperties setRadius:];
-[UIShadowProperties setOpacity:];
-[UIShadowProperties color];
-[UIShadowProperties radius];
-[UIShadowProperties set_color:];
-[UIShadowProperties encodeWithCoder:];
-[UIShadowProperties description];
-[UIShadowProperties initWithCoder:];
-[UIShadowProperties set_path:];
-[UIShadowProperties setOffset:];
-[UIShadowProperties setPath:];
-[UIShadowProperties copyWithZone:];
-[UIShadowProperties isEqual:];
-[UIShadowProperties offset];
-[UIShadowProperties path];
-[UIShadowProperties _radius];
-[UIShadowProperties _offset];
-[UIShadowProperties _applyPropertiesFromDefaultProperties:];
-[UIShadowProperties _backgroundConfigurationShadowType];
-[UIShadowProperties _opacity];
-[UIShadowProperties set_backgroundConfigurationShadowType:];
-[UIShadowProperties set_offset:];
-[UIShadowProperties set_opacity:];
-[UIShadowProperties set_radius:];
```
