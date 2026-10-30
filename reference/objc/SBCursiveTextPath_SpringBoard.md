# `SBCursiveTextPath`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _initialWeight;
d _finalWeight;
d _rampTime;
d _length;
d _duration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBoxOfPath;
d _unitsPerM;
d _ascender;
d _descender;
{vector<std::vector<BezierCurve>, std::allocator<std::vector<BezierCurve>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _bezierArrays;
q _resolution;
```

## Instance methods

```
-[SBCursiveTextPath duration];
-[SBCursiveTextPath initWithURL:];
-[SBCursiveTextPath initWithURL:resolution:];
-[SBCursiveTextPath pathForFraction:calculateLength:];
-[SBCursiveTextPath pathForTime:];
-[SBCursiveTextPath transformForRect:pointSize:flipped:];
```
