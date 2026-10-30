# `UISVectorGlyphDrawing`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISDrawing`
- 5 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{CGImage=} _image;
^{CGColor=} _tintColor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _imageFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _alignmentRect;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) alignmentRect;
@property (T{CGSize=dd},R,N) drawingSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISVectorGlyphDrawing dealloc];
-[UISVectorGlyphDrawing alignmentRect];
-[UISVectorGlyphDrawing drawInContext:atPoint:];
-[UISVectorGlyphDrawing drawingSize];
-[UISVectorGlyphDrawing initWithVectorGlyph:tintColor:];
```
