# `PKStrokeSelectionImageConfig`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _invertedColors;
B _rotated;
B _sixChannel;
B _transparentBlending;
B _highlighted;
B _extendedDynamicRange;
d _scale;
{CGSize="width"d"height"d} _imageSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _strokeBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _imageViewBounds;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_strokeBounds) strokeBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_imageViewBounds) imageViewBounds;
@property (Td,R,N,V_scale) scale;
@property (T{CGSize=dd},R,N,V_imageSize) imageSize;
@property (TB,R,N,V_invertedColors) invertedColors;
@property (TB,R,N,V_rotated) rotated;
@property (TB,R,N,V_sixChannel) sixChannel;
@property (TB,R,N,V_transparentBlending) transparentBlending;
@property (TB,R,N,V_highlighted) highlighted;
@property (TB,R,N,V_extendedDynamicRange) extendedDynamicRange;
```

## Instance methods

```
-[PKStrokeSelectionImageConfig imageSize];
-[PKStrokeSelectionImageConfig highlighted];
-[PKStrokeSelectionImageConfig scale];
-[PKStrokeSelectionImageConfig hash];
-[PKStrokeSelectionImageConfig rotated];
-[PKStrokeSelectionImageConfig copyWithZone:];
-[PKStrokeSelectionImageConfig isEqual:];
-[PKStrokeSelectionImageConfig imageViewBounds];
-[PKStrokeSelectionImageConfig extendedDynamicRange];
-[PKStrokeSelectionImageConfig initWithStrokeBounds:imageViewBounds:scale:imageSize:invertedColors:rotated:sixChannel:transparentBlending:highlighted:extendedDynamicRange:];
-[PKStrokeSelectionImageConfig invertedColors];
-[PKStrokeSelectionImageConfig sixChannel];
-[PKStrokeSelectionImageConfig strokeBounds];
-[PKStrokeSelectionImageConfig transparentBlending];
```
