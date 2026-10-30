# `UISTextLineDrawing`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISDrawing`
- 5 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{__CTLine=} _line;
{CGSize="width"d"height"d} _size;
{CGVector="dx"d"dy"d} _offset;
d _baseline;
B _hasLineBreak;
```

## Properties

```
@property (TB,R,N,V_hasLineBreak) hasLineBreak;
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISTextLineDrawing dealloc];
-[UISTextLineDrawing alignmentRect];
-[UISTextLineDrawing drawInContext:atPoint:];
-[UISTextLineDrawing drawingSize];
-[UISTextLineDrawing hasLineBreak];
-[UISTextLineDrawing initWithAttributedString:lineBreakMode:textAlignment:width:scale:];
-[UISTextLineDrawing initWithNonretainedLine:lineBreakMode:textAlignment:width:scale:];
-[UISTextLineDrawing initWithString:attributes:lineBreakMode:textAlignment:width:scale:];
```
