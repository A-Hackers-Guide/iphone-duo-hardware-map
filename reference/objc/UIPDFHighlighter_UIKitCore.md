# `UIPDFHighlighter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CALayerDelegate`
- 8 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _highLightLayers;
^{CGColor=} _highlightColor;
^{CGColor=} _borderColor;
^{CGColor=} _whiteColor;
^{CGPDFPage=} _page;
d _enlargeFactor;
d _pdfToViewScale;
d inset;
```

## Properties

```
@property (Td,N,Vinset) inset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFHighlighter setNeedsDisplay];
-[UIPDFHighlighter clear];
-[UIPDFHighlighter init];
-[UIPDFHighlighter dealloc];
-[UIPDFHighlighter drawLayer:inContext:];
-[UIPDFHighlighter unhide];
-[UIPDFHighlighter addAnimation:];
-[UIPDFHighlighter addHighlightFor:to:animated:];
-[UIPDFHighlighter addHighlightLayerFor:atIndex:to:animated:];
-[UIPDFHighlighter addRectPath:toView:layer:rectangle:upright:];
-[UIPDFHighlighter inset];
-[UIPDFHighlighter makeTheBorderPath:layer:rectangle:upright:];
-[UIPDFHighlighter makeTheClipPath:layer:rectangle:upright:];
-[UIPDFHighlighter setInset:];
```
