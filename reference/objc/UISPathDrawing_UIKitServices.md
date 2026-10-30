# `UISPathDrawing`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISDrawing`
- 4 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _type;
^{CGPath=} _path;
{CGSize="width"d"height"d} _size;
^{CGColor=} _fillColor;
```

## Properties

```
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISPathDrawing dealloc];
-[UISPathDrawing alignmentRect];
-[UISPathDrawing initWithRectSize:fillColor:];
-[UISPathDrawing drawInContext:atPoint:];
-[UISPathDrawing drawingSize];
-[UISPathDrawing initWithEllipseSize:fillColor:];
-[UISPathDrawing initWithPath:size:fillColor:];
-[UISPathDrawing initWithRoundedRectSize:cornerRadii:fillColor:];
-[UISPathDrawing initWithType:path:size:fillColor:];
```
