# `UISnapshotView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 10 properties, 32 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _contentSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentBeyondBounds;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _edgePadding;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _edgeInsets;
{CGPoint="x"d"y"d} _contentOffset;
@"UIColor" _edgePaddingColor;
@"UIView" _imageView;
@"NSMutableArray" _edgePaddingViews;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _snapshotRect;
@"UIImageView" _shadowView;
b1 _disableEdgeAntialiasing;
b1 _disableVerticalStretch;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,V_edgePadding) edgePadding;
@property (T@"UIColor",&,N,V_edgePaddingColor) edgePaddingColor;
@property (T@"UIView",R,N,G_snapshotView,V_imageView) snapshotView;
@property (T{CGSize=dd},R,N,G_contentSize,V_contentSize) contentSize;
@property (T{CGPoint=dd},N,G_contentOffset,S_setContentOffset:,V_contentOffset) contentOffset;
@property (T{UIEdgeInsets=dddd},N,V_edgeInsets) edgeInsets;
@property (TB,N,GisVerticalStretchEnabled) verticalStretchEnabled;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,G_snapshotRect,S_setSnapshotRect:) snapshotRect;
@property (T@"UIView",&,N,V_shadowView) shadowView;
@property (TB,N,GisEdgeAntialiasingEnabled) edgeAntialiasingEnabled;
```

## Instance methods

```
-[UISnapshotView _setContentOffset:];
-[UISnapshotView setEdgeAntialiasingEnabled:];
-[UISnapshotView setVerticalStretchEnabled:];
-[UISnapshotView dealloc];
-[UISnapshotView _updateContentsRect];
-[UISnapshotView _snapshotView];
-[UISnapshotView setEdgeInsets:];
-[UISnapshotView captureSnapshotRect:fromView:withSnapshotType:];
-[UISnapshotView layoutSubviews];
-[UISnapshotView captureSnapshotOfView:withSnapshotType:];
-[UISnapshotView setBounds:];
-[UISnapshotView setEdgePaddingColor:];
-[UISnapshotView _contentOffset];
-[UISnapshotView _positionImageView];
-[UISnapshotView _setSnapshotRect:];
-[UISnapshotView shadowView];
-[UISnapshotView _contentSize];
-[UISnapshotView setFrame:];
-[UISnapshotView edgeInsets];
-[UISnapshotView setShadowView:];
-[UISnapshotView setEdgePadding:];
-[UISnapshotView _edgePadding];
-[UISnapshotView isEdgeAntialiasingEnabled];
-[UISnapshotView edgePaddingColor];
-[UISnapshotView _snapshotRect];
-[UISnapshotView edgePadding];
-[UISnapshotView _drawEdges:withContentSize:];
-[UISnapshotView initWithFrame:];
-[UISnapshotView _contentsCenterForEdgePadding:withContentSize:];
-[UISnapshotView _addEdgePaddingViewInRect:];
-[UISnapshotView setContentStretch:];
-[UISnapshotView isVerticalStretchEnabled];
```
