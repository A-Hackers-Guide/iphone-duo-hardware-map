# `SBInteractiveScreenshotGestureCropsView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 32 instance variables, 11 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"UIView" _bottomLeftCornerHorizontalView;
@"UIView" _bottomLeftCornerVerticalView;
@"UIView" _bottomRightCornerHorizontalView;
@"UIView" _bottomRightCornerVerticalView;
@"UIView" _topLeftCornerHorizontalView;
@"UIView" _topLeftCornerVerticalView;
@"UIView" _topRightCornerHorizontalView;
@"UIView" _topRightCornerVerticalView;
@"UIView" _bottomLineView;
@"UIView" _bottomLineGrabberView;
@"UIView" _leftLineView;
@"UIView" _leftLineGrabberView;
@"UIView" _rightLineView;
@"UIView" _rightLineGrabberView;
@"UIView" _topLineView;
@"UIView" _topLineGrabberView;
@"NSArray" _cornerViews;
@"NSArray" _lineViews;
@"NSArray" _lineGrabberViews;
@"NSObject<OS_dispatch_queue>" _accessQueue;
d _queue_displayScale;
d _cornerAlpha;
d _cornerEdgeLength;
@"UIColor" _cornerColor;
d _lineGrabberAlpha;
d _lineGrabberEdgeLength;
@"UIColor" _lineGrabberColor;
d _grabberLineWidth;
d _lineAlpha;
d _lineWidth;
@"UIColor" _lineColor;
@ _cropsCompositingFilter;
```

## Properties

```
@property (Td,N,V_cornerAlpha) cornerAlpha;
@property (Td,N,V_cornerEdgeLength) cornerEdgeLength;
@property (T@"UIColor",&,N,V_cornerColor) cornerColor;
@property (Td,N,V_lineGrabberAlpha) lineGrabberAlpha;
@property (Td,N,V_lineGrabberEdgeLength) lineGrabberEdgeLength;
@property (T@"UIColor",&,N,V_lineGrabberColor) lineGrabberColor;
@property (Td,N,V_grabberLineWidth) grabberLineWidth;
@property (Td,N,V_lineAlpha) lineAlpha;
@property (Td,N,V_lineWidth) lineWidth;
@property (T@"UIColor",&,N,V_lineColor) lineColor;
@property (T@,&,N,V_cropsCompositingFilter) cropsCompositingFilter;
```

## Instance methods

```
-[SBInteractiveScreenshotGestureCropsView lineWidth];
-[SBInteractiveScreenshotGestureCropsView setLineWidth:];
-[SBInteractiveScreenshotGestureCropsView _setPresentationValue:forKey:];
-[SBInteractiveScreenshotGestureCropsView layoutSubviews];
-[SBInteractiveScreenshotGestureCropsView setBounds:];
-[SBInteractiveScreenshotGestureCropsView setFrame:];
-[SBInteractiveScreenshotGestureCropsView traitCollectionDidChange:];
-[SBInteractiveScreenshotGestureCropsView initWithFrame:];
-[SBInteractiveScreenshotGestureCropsView lineColor];
-[SBInteractiveScreenshotGestureCropsView setLineColor:];
-[SBInteractiveScreenshotGestureCropsView _setupUI];
-[SBInteractiveScreenshotGestureCropsView lineAlpha];
-[SBInteractiveScreenshotGestureCropsView setLineAlpha:];
-[SBInteractiveScreenshotGestureCropsView setCornerColor:];
-[SBInteractiveScreenshotGestureCropsView setCornerAlpha:];
-[SBInteractiveScreenshotGestureCropsView _didSetCompositingFilter];
-[SBInteractiveScreenshotGestureCropsView _didSetCornerAlpha];
-[SBInteractiveScreenshotGestureCropsView _didSetCornerColor];
-[SBInteractiveScreenshotGestureCropsView _didSetGrabberLineWidth];
-[SBInteractiveScreenshotGestureCropsView _updateGeometryForBounds:shouldUsePresentationValues:];
-[SBInteractiveScreenshotGestureCropsView _updateGeometryOrDeferLayoutUsingModelBounds];
-[SBInteractiveScreenshotGestureCropsView cornerAlpha];
-[SBInteractiveScreenshotGestureCropsView cornerColor];
-[SBInteractiveScreenshotGestureCropsView cornerEdgeLength];
-[SBInteractiveScreenshotGestureCropsView cropsCompositingFilter];
-[SBInteractiveScreenshotGestureCropsView grabberLineWidth];
-[SBInteractiveScreenshotGestureCropsView lineGrabberAlpha];
-[SBInteractiveScreenshotGestureCropsView lineGrabberColor];
-[SBInteractiveScreenshotGestureCropsView lineGrabberEdgeLength];
-[SBInteractiveScreenshotGestureCropsView setCornerEdgeLength:];
-[SBInteractiveScreenshotGestureCropsView setCropsCompositingFilter:];
-[SBInteractiveScreenshotGestureCropsView setGrabberLineWidth:];
-[SBInteractiveScreenshotGestureCropsView setLineGrabberAlpha:];
-[SBInteractiveScreenshotGestureCropsView setLineGrabberColor:];
-[SBInteractiveScreenshotGestureCropsView setLineGrabberEdgeLength:];
```
