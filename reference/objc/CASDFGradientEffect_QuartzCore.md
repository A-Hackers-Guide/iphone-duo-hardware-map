# `CASDFGradientEffect`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CASDFEffect`
- 4 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _premultiplied;
@"NSArray" _colors;
@"NSArray" _distances;
@"NSArray" _interpolations;
```

## Properties

```
@property (T@"NSArray",C,V_colors) colors;
@property (T@"NSArray",C,V_distances) distances;
@property (T@"NSArray",C,V_interpolations) interpolations;
@property (TB,V_premultiplied) premultiplied;
```

## Class methods

```
+[CASDFGradientEffect defaultValues];
+[CASDFGradientEffect name];
```

## Instance methods

```
-[CASDFGradientEffect setColors:];
-[CASDFGradientEffect colors];
-[CASDFGradientEffect interpolations];
-[CASDFGradientEffect dealloc];
-[CASDFGradientEffect configureLayer:transaction:];
-[CASDFGradientEffect distances];
-[CASDFGradientEffect setPremultiplied:];
-[CASDFGradientEffect setInterpolations:];
-[CASDFGradientEffect copyWithZone:];
-[CASDFGradientEffect setDistances:];
-[CASDFGradientEffect premultiplied];
```
