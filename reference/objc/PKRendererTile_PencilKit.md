# `PKRendererTile`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 24 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
Ad _cachedContentsScale;
Aq _renderCount;
Ad _lastUsedTimestamp;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _drawingTransform;
B _framebufferIsLocked;
B _multiplyFramebufferIsLocked;
B _sixChannelMode;
B _transparentBlending;
B _wantsExtendedDynamicRangeContent;
B _outOfDate;
B _hidden;
@"CALayer" _tileLayer;
@"CALayer" _tileMultiplyLayer;
@"PKMetalFramebuffer" _framebuffer;
@"PKMetalFramebuffer" _multiplyFramebuffer;
@"NSUUID" _identifier;
q _level;
@"NSArray" _renderedStrokes;
q _currentlyRenderingCount;
d _contentsScale;
d _opacity;
{CGPoint="x"d"y"d} _offset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _drawingFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Instance methods

```
-[PKRendererTile debugDescription];
-[PKRendererTile dealloc];
-[PKRendererTile description];
-[PKRendererTile copyWithZone:];
```
