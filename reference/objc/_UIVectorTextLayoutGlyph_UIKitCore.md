# `_UIVectorTextLayoutGlyph`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVectorTextLayoutGlyph`
- 4 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
S _glyph;
@"UIBezierPath" _path;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _pathTransform;
```

## Properties

```
@property (TS,N,V_glyph) glyph;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (T@"UIBezierPath",&,N,V_path) path;
@property (T{CGAffineTransform=dddddd},N,V_pathTransform) pathTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVectorTextLayoutGlyph setGlyph:];
-[_UIVectorTextLayoutGlyph glyph];
-[_UIVectorTextLayoutGlyph rect];
-[_UIVectorTextLayoutGlyph setRect:];
-[_UIVectorTextLayoutGlyph setPath:];
-[_UIVectorTextLayoutGlyph path];
-[_UIVectorTextLayoutGlyph pathTransform];
-[_UIVectorTextLayoutGlyph setPathTransform:];
```
