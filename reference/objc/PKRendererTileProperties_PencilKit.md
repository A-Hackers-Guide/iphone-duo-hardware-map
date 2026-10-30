# `PKRendererTileProperties`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _sixChannelMode;
B _extendedDynamicRange;
B _transparentBlending;
q _level;
{CGPoint="x"d"y"d} _offset;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _drawingTransform;
```

## Properties

```
@property (Tq,R,N,V_level) level;
@property (T{CGPoint=dd},R,N,V_offset) offset;
@property (TB,R,N,V_sixChannelMode) sixChannelMode;
@property (TB,R,N,V_extendedDynamicRange) extendedDynamicRange;
@property (TB,R,N,V_transparentBlending) transparentBlending;
@property (T{CGAffineTransform=dddddd},R,N,V_drawingTransform) drawingTransform;
```

## Instance methods

```
-[PKRendererTileProperties level];
-[PKRendererTileProperties hash];
-[PKRendererTileProperties copyWithZone:];
-[PKRendererTileProperties isEqual:];
-[PKRendererTileProperties offset];
-[PKRendererTileProperties drawingTransform];
-[PKRendererTileProperties extendedDynamicRange];
-[PKRendererTileProperties initWithLevel:offset:drawingTransform:sixChannelMode:transparentBlending:extendedDynamicRange:];
-[PKRendererTileProperties sixChannelMode];
-[PKRendererTileProperties transparentBlending];
```
