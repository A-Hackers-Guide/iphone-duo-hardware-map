# `CASDFShadowEffect`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CASDFEffect`
- 5 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
B _punchout;
B _invert;
^{CGColor=} _color;
d _radius;
{CGSize="width"d"height"d} _offset;
```

## Properties

```
@property (T^{CGColor=},&,N,V_color) color;
@property (Td,N,V_radius) radius;
@property (T{CGSize=dd},N,V_offset) offset;
@property (TB,N,V_punchout) punchout;
@property (TB,N,V_invert) invert;
```

## Class methods

```
+[CASDFShadowEffect defaultValues];
+[CASDFShadowEffect name];
```

## Instance methods

```
-[CASDFShadowEffect setColor:];
-[CASDFShadowEffect punchout];
-[CASDFShadowEffect dealloc];
-[CASDFShadowEffect invert];
-[CASDFShadowEffect configureLayer:transaction:];
-[CASDFShadowEffect setRadius:];
-[CASDFShadowEffect color];
-[CASDFShadowEffect setInvert:];
-[CASDFShadowEffect radius];
-[CASDFShadowEffect setPunchout:];
-[CASDFShadowEffect setOffset:];
-[CASDFShadowEffect copyWithZone:];
-[CASDFShadowEffect offset];
```
