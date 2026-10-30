# `PKTextAttachmentResizeView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 12 properties, 28 instance methods, 1 class methods

## Instance variables

```
B _top;
B _highlighted;
B _enabled;
@"PKDrawingAdjustmentKnob" _knobView;
@"UIView" _separatorView;
@"UIView" _separatorHighlightedView;
@"<PKTextAttachmentResizeViewDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originalDrawingBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originalViewBounds;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _originalContentInset;
```

## Properties

```
@property (T@"PKDrawingAdjustmentKnob",&,N,V_knobView) knobView;
@property (T@"UIView",&,N,V_separatorView) separatorView;
@property (T@"UIView",&,N,V_separatorHighlightedView) separatorHighlightedView;
@property (T@"<PKTextAttachmentResizeViewDelegate>",W,N,V_delegate) delegate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_originalDrawingBounds) originalDrawingBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_originalViewBounds) originalViewBounds;
@property (T{UIEdgeInsets=dddd},N,V_originalContentInset) originalContentInset;
@property (TB,R,N,V_top) top;
@property (TB,N,V_highlighted) highlighted;
@property (TB,N,V_enabled) enabled;
@property (TB,R,N) shown;
@property (Td,R,N) resizeContentInset;
```

## Class methods

```
+[PKTextAttachmentResizeView resizeHitSize];
```

## Instance methods

```
-[PKTextAttachmentResizeView handleGesture:];
-[PKTextAttachmentResizeView didMoveToWindow];
-[PKTextAttachmentResizeView separatorHighlightedView];
-[PKTextAttachmentResizeView resizeContentInset];
-[PKTextAttachmentResizeView enabled];
-[PKTextAttachmentResizeView setOriginalDrawingBounds:];
-[PKTextAttachmentResizeView originalContentInset];
-[PKTextAttachmentResizeView setOriginalContentInset:];
-[PKTextAttachmentResizeView layoutSubviews];
-[PKTextAttachmentResizeView highlighted];
-[PKTextAttachmentResizeView top];
-[PKTextAttachmentResizeView show:enabled:animated:];
-[PKTextAttachmentResizeView setSeparatorHighlightedView:];
-[PKTextAttachmentResizeView setSeparatorView:];
-[PKTextAttachmentResizeView originalDrawingBounds];
-[PKTextAttachmentResizeView setDelegate:];
-[PKTextAttachmentResizeView setHighlighted:];
-[PKTextAttachmentResizeView knobView];
-[PKTextAttachmentResizeView setKnobView:];
-[PKTextAttachmentResizeView setEnabled:];
-[PKTextAttachmentResizeView layoutInsideSuperview];
-[PKTextAttachmentResizeView initAtTop:delegate:];
-[PKTextAttachmentResizeView delegate];
-[PKTextAttachmentResizeView drawingScrollViewDidScroll:];
-[PKTextAttachmentResizeView separatorView];
-[PKTextAttachmentResizeView shown];
-[PKTextAttachmentResizeView setOriginalViewBounds:];
-[PKTextAttachmentResizeView originalViewBounds];
```
