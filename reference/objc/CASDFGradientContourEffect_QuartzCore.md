# `CASDFGradientContourEffect`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CASDFEffect`
- 9 instance variables, 9 properties, 21 instance methods, 2 class methods

## Instance variables

```
^{CGColor=} _startColor;
^{CGColor=} _endColor;
d _angle;
d _radius;
d _shadowEffectOffset;
d _shadowGradientStart;
d _shadowGradientEnd;
d _shadowAlpha;
d _gradientOffset;
```

## Properties

```
@property (T^{CGColor=},&,N,V_startColor) startColor;
@property (T^{CGColor=},&,N,V_endColor) endColor;
@property (Td,N,V_angle) angle;
@property (Td,N,V_radius) radius;
@property (Td,N,V_shadowEffectOffset) shadowEffectOffset;
@property (Td,N,V_shadowGradientStart) shadowGradientStart;
@property (Td,N,V_shadowGradientEnd) shadowGradientEnd;
@property (Td,N,V_shadowAlpha) shadowAlpha;
@property (Td,N,V_gradientOffset) gradientOffset;
```

## Class methods

```
+[CASDFGradientContourEffect defaultValues];
+[CASDFGradientContourEffect name];
```

## Instance methods

```
-[CASDFGradientContourEffect setAngle:];
-[CASDFGradientContourEffect angle];
-[CASDFGradientContourEffect setShadowAlpha:];
-[CASDFGradientContourEffect shadowAlpha];
-[CASDFGradientContourEffect startColor];
-[CASDFGradientContourEffect shadowGradientStart];
-[CASDFGradientContourEffect shadowEffectOffset];
-[CASDFGradientContourEffect setShadowGradientEnd:];
-[CASDFGradientContourEffect setShadowEffectOffset:];
-[CASDFGradientContourEffect dealloc];
-[CASDFGradientContourEffect shadowGradientEnd];
-[CASDFGradientContourEffect configureLayer:transaction:];
-[CASDFGradientContourEffect setGradientOffset:];
-[CASDFGradientContourEffect setRadius:];
-[CASDFGradientContourEffect radius];
-[CASDFGradientContourEffect setEndColor:];
-[CASDFGradientContourEffect endColor];
-[CASDFGradientContourEffect setStartColor:];
-[CASDFGradientContourEffect setShadowGradientStart:];
-[CASDFGradientContourEffect gradientOffset];
-[CASDFGradientContourEffect copyWithZone:];
```
