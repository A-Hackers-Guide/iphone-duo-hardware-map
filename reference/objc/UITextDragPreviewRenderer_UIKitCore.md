# `UITextDragPreviewRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextPreviewRenderer`
- 11 instance variables, 11 properties, 17 instance methods, 0 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _range;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _firstRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _middleRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentBounds;
{CGPoint="x"d"y"d} _origin;
@"UIImage" _image;
B _calculated;
B _unifyRects;
B _excludeBackground;
@"NSLayoutManager" _layoutManager;
```

## Properties

```
@property (T@"NSLayoutManager",R,N,V_layoutManager) layoutManager;
@property (T@"UIImage",R,N) image;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) firstLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bodyRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) lastLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentBounds;
@property (TB,N,V_excludeBackground) excludeBackground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextDragPreviewRenderer contentBounds];
-[UITextDragPreviewRenderer layoutManager];
-[UITextDragPreviewRenderer image];
-[UITextDragPreviewRenderer _calculate];
-[UITextDragPreviewRenderer _calculateRectsUsingLayoutManager:];
-[UITextDragPreviewRenderer _correctlyOffsetBoundingRect];
-[UITextDragPreviewRenderer _rawBoundingRect];
-[UITextDragPreviewRenderer addRenderingAttributes:];
-[UITextDragPreviewRenderer adjustFirstLineRect:bodyRect:lastLineRect:textOrigin:];
-[UITextDragPreviewRenderer bodyRect];
-[UITextDragPreviewRenderer excludeBackground];
-[UITextDragPreviewRenderer firstLineRect];
-[UITextDragPreviewRenderer initWithLayoutManager:range:];
-[UITextDragPreviewRenderer initWithLayoutManager:range:unifyRects:];
-[UITextDragPreviewRenderer lastLineRect];
-[UITextDragPreviewRenderer removeRenderingAttributes:];
-[UITextDragPreviewRenderer setExcludeBackground:];
```
