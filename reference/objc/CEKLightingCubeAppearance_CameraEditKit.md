# `CEKLightingCubeAppearance`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 13 instance variables, 13 properties, 17 instance methods, 1 class methods

## Instance variables

```
^{CGGradient=} _background;
^{CGColor=} _topFill;
^{CGGradient=} _topGlow;
^{CGGradient=} _topMask;
^{CGColor=} _bottomFill;
^{CGGradient=} _bottomInnerGlow;
^{CGGradient=} _bottomOuterGlow;
^{CGGradient=} _bottomMask;
^{CGColor=} _verticalFillColor;
d _verticalFillFrontIntensity;
d _verticalFillBackIntensity;
^{CGGradient=} _topOver;
^{CGColor=} _stroke;
```

## Properties

```
@property (T^{CGGradient=},R,N,V_background) background;
@property (T^{CGColor=},R,N,V_topFill) topFill;
@property (T^{CGGradient=},R,N,V_topGlow) topGlow;
@property (T^{CGGradient=},R,N,V_topMask) topMask;
@property (T^{CGColor=},R,N,V_bottomFill) bottomFill;
@property (T^{CGGradient=},R,N,V_bottomInnerGlow) bottomInnerGlow;
@property (T^{CGGradient=},R,N,V_bottomOuterGlow) bottomOuterGlow;
@property (T^{CGGradient=},R,N,V_bottomMask) bottomMask;
@property (T^{CGColor=},R,N,V_verticalFillColor) verticalFillColor;
@property (Td,R,N,V_verticalFillBackIntensity) verticalFillBackIntensity;
@property (Td,R,N,V_verticalFillFrontIntensity) verticalFillFrontIntensity;
@property (T^{CGGradient=},R,N,V_topOver) topOver;
@property (T^{CGColor=},R,N,V_stroke) stroke;
```

## Class methods

```
+[CEKLightingCubeAppearance appearanceFrom:to:progress:];
```

## Instance methods

```
-[CEKLightingCubeAppearance mutableCopyWithZone:];
-[CEKLightingCubeAppearance bottomMask];
-[CEKLightingCubeAppearance dealloc];
-[CEKLightingCubeAppearance background];
-[CEKLightingCubeAppearance copyWithZone:];
-[CEKLightingCubeAppearance topMask];
-[CEKLightingCubeAppearance stroke];
-[CEKLightingCubeAppearance bottomOuterGlow];
-[CEKLightingCubeAppearance topFill];
-[CEKLightingCubeAppearance bottomInnerGlow];
-[CEKLightingCubeAppearance initWithStroke:];
-[CEKLightingCubeAppearance topGlow];
-[CEKLightingCubeAppearance topOver];
-[CEKLightingCubeAppearance bottomFill];
-[CEKLightingCubeAppearance verticalFillBackIntensity];
-[CEKLightingCubeAppearance verticalFillColor];
-[CEKLightingCubeAppearance verticalFillFrontIntensity];
```
