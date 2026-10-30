# `UISTextParagraphDrawing`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISDrawing`
- 6 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{__CFAttributedString=} _textString;
^{__CTFrame=} _frame;
{CGSize="width"d"height"d} _frameSize;
d _drawingHeight;
d _scale;
C _lineCount;
```

## Properties

```
@property (TC,R,N,V_lineCount) lineCount;
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISTextParagraphDrawing dealloc];
-[UISTextParagraphDrawing alignmentRect];
-[UISTextParagraphDrawing lineCount];
-[UISTextParagraphDrawing drawInContext:atPoint:];
-[UISTextParagraphDrawing drawingSize];
-[UISTextParagraphDrawing initWithString:attributes:size:numberOfLines:scale:];
```
