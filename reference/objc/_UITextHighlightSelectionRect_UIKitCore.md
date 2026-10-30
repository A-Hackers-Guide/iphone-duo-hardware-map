# `_UITextHighlightSelectionRect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextSelectionRect`
- 3 instance variables, 3 properties, 6 instance methods, 3 class methods

## Instance variables

```
B _containsStart;
B _containsEnd;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (TB,N,V_containsStart) containsStart;
@property (TB,N,V_containsEnd) containsEnd;
```

## Class methods

```
+[_UITextHighlightSelectionRect endingSelectionRectWithRect:];
+[_UITextHighlightSelectionRect selectionRectWithRect:];
+[_UITextHighlightSelectionRect startingSelectionRectWithRect:];
```

## Instance methods

```
-[_UITextHighlightSelectionRect setContainsStart:];
-[_UITextHighlightSelectionRect setContainsEnd:];
-[_UITextHighlightSelectionRect rect];
-[_UITextHighlightSelectionRect containsStart];
-[_UITextHighlightSelectionRect setRect:];
-[_UITextHighlightSelectionRect containsEnd];
```
