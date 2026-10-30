# `AVAnnotationTextRepresentation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAnnotationRepresentation`
- 8 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSString" _text;
@"NSString" _font;
^{CGColor=} _backgroundColor;
^{CGColor=} _foregroundColor;
@"NSString" _link;
B _hasShadow;
B _hasUnderline;
q _writingMode;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (T@"NSString",C,N,V_font) font;
@property (T^{CGColor=},N) backgroundColor;
@property (T^{CGColor=},N) foregroundColor;
@property (T@"NSString",C,N,V_link) link;
@property (TB,N,V_hasShadow) hasShadow;
@property (TB,N,V_hasUnderline) hasUnderline;
@property (Tq,N,V_writingMode) writingMode;
```

## Instance methods

```
-[AVAnnotationTextRepresentation hasShadow];
-[AVAnnotationTextRepresentation setForegroundColor:];
-[AVAnnotationTextRepresentation text];
-[AVAnnotationTextRepresentation dealloc];
-[AVAnnotationTextRepresentation setBackgroundColor:];
-[AVAnnotationTextRepresentation hash];
-[AVAnnotationTextRepresentation backgroundColor];
-[AVAnnotationTextRepresentation description];
-[AVAnnotationTextRepresentation setText:];
-[AVAnnotationTextRepresentation font];
-[AVAnnotationTextRepresentation foregroundColor];
-[AVAnnotationTextRepresentation isEqual:];
-[AVAnnotationTextRepresentation setHasShadow:];
-[AVAnnotationTextRepresentation setFont:];
-[AVAnnotationTextRepresentation link];
-[AVAnnotationTextRepresentation setLink:];
-[AVAnnotationTextRepresentation setWritingMode:];
-[AVAnnotationTextRepresentation _initWithPropertyList:binaryData:];
-[AVAnnotationTextRepresentation _propertyListAndBinaryData:];
-[AVAnnotationTextRepresentation hasUnderline];
-[AVAnnotationTextRepresentation initWithText:font:];
-[AVAnnotationTextRepresentation setHasUnderline:];
-[AVAnnotationTextRepresentation writingMode];
```
