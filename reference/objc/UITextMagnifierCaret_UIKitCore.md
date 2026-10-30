# `UITextMagnifierCaret`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextMagnifier`
- 2 instance variables, 1 properties, 13 instance methods, 3 class methods

## Instance variables

```
d _yOffset;
{CGPoint="x"d"y"d} _offset;
```

## Properties

```
@property (T{CGPoint=dd},N,V_offset) offset;
```

## Class methods

```
+[UITextMagnifierCaret activeCaretMagnifier];
+[UITextMagnifierCaret renderClass];
+[UITextMagnifierCaret sharedCaretMagnifier];
```

## Instance methods

```
-[UITextMagnifierCaret remove];
-[UITextMagnifierCaret setOffset:];
-[UITextMagnifierCaret offset];
-[UITextMagnifierCaret isHorizontal];
-[UITextMagnifierCaret zoomUpAnimation];
-[UITextMagnifierCaret animationPoint];
-[UITextMagnifierCaret beginMagnifyingTarget:text:magnificationPoint:offset:animated:];
-[UITextMagnifierCaret initWithFrame];
-[UITextMagnifierCaret offsetFromMagnificationPoint];
-[UITextMagnifierCaret setAnimationPoint:];
-[UITextMagnifierCaret terminalPointPlacedCarefully];
-[UITextMagnifierCaret updateFrameAndOffset];
-[UITextMagnifierCaret zoomDownAnimation];
```
