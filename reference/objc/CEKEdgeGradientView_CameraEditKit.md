# `CEKEdgeGradientView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
q _edgeGradientStyle;
@"UIColor" _customEdgeGradientColor;
q _gradientDirection;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
{?="startFadeInset"d"startFadeLength"d"endFadeLength"d"endFadeInset"d} _gradientDimensions;
```

## Properties

```
@property (Tq,R,N,V_edgeGradientStyle) edgeGradientStyle;
@property (T@"UIColor",R,N,V_customEdgeGradientColor) customEdgeGradientColor;
@property (Tq,N,V_gradientDirection) gradientDirection;
@property (T{UIEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (Td,N) outerColorLength;
@property (Td,N) innerFadeLength;
@property (T{?=dddd},N,V_gradientDimensions) gradientDimensions;
```

## Instance methods

```
-[CEKEdgeGradientView setContentInsets:];
-[CEKEdgeGradientView edgeGradientStyle];
-[CEKEdgeGradientView drawRect:];
-[CEKEdgeGradientView isOpaque];
-[CEKEdgeGradientView setEdgeGradientStyleMask];
-[CEKEdgeGradientView setEdgeGradientStyleBlack];
-[CEKEdgeGradientView customEdgeGradientColor];
-[CEKEdgeGradientView outerColorLength];
-[CEKEdgeGradientView setGradientDirection:];
-[CEKEdgeGradientView setOuterColorLength:];
-[CEKEdgeGradientView setInnerFadeLength:];
-[CEKEdgeGradientView contentInsets];
-[CEKEdgeGradientView gradientDimensions];
-[CEKEdgeGradientView setCustomEdgeGradientStyleWithColor:];
-[CEKEdgeGradientView gradientDirection];
-[CEKEdgeGradientView setGradientDimensions:];
-[CEKEdgeGradientView initWithFrame:];
-[CEKEdgeGradientView innerFadeLength];
```
