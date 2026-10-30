# `BKUIPearlPositioningGuideView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 28 instance variables, 28 properties, 76 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _displayLink;
B _startMaskFromCenter;
B _inSheet;
@"CAShapeLayer" _roundedRectMaskLayer;
d _lineWidth;
d _edgeDistance;
d _cornerRadius;
d _postCornerLength;
d _lineAlpha;
d _ringRadius;
@"NSDate" _animationStart;
d _animationDuration;
q _animationCurve;
@? _animationCompletion;
d _startLineWidth;
d _startEdgeDistance;
d _startCornerRadius;
d _startPostCornerLength;
d _startLineAlpha;
d _targetLineWidth;
d _targetEdgeDistance;
d _targetCornerRadius;
d _targetPostCornerLength;
d _targetLineAlpha;
d _lastAnimationTickProgres;
{CGPoint="x"d"y"d} _portalCenter;
{CGPoint="x"d"y"d} _startPortalCenter;
{CGPoint="x"d"y"d} _targetPortalCenter;
```

## Properties

```
@property (Td,N,V_startLineWidth) startLineWidth;
@property (Td,N,V_startEdgeDistance) startEdgeDistance;
@property (Td,N,V_startCornerRadius) startCornerRadius;
@property (Td,N,V_startPostCornerLength) startPostCornerLength;
@property (Td,N,V_startLineAlpha) startLineAlpha;
@property (T{CGPoint=dd},N,V_startPortalCenter) startPortalCenter;
@property (Td,N,V_targetLineWidth) targetLineWidth;
@property (Td,N,V_targetEdgeDistance) targetEdgeDistance;
@property (Td,N,V_targetCornerRadius) targetCornerRadius;
@property (Td,N,V_targetPostCornerLength) targetPostCornerLength;
@property (Td,N,V_targetLineAlpha) targetLineAlpha;
@property (T{CGPoint=dd},N,V_targetPortalCenter) targetPortalCenter;
@property (Td,N,V_lastAnimationTickProgres) lastAnimationTickProgres;
@property (T@"CAShapeLayer",&,N,V_roundedRectMaskLayer) roundedRectMaskLayer;
@property (Td,N,V_lineWidth) lineWidth;
@property (Td,N,V_edgeDistance) edgeDistance;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Td,N,V_postCornerLength) postCornerLength;
@property (Td,N,V_lineAlpha) lineAlpha;
@property (Td,N,V_ringRadius) ringRadius;
@property (T{CGPoint=dd},N,V_portalCenter) portalCenter;
@property (T@"NSDate",&,N,V_animationStart) animationStart;
@property (Td,N,V_animationDuration) animationDuration;
@property (Tq,N,V_animationCurve) animationCurve;
@property (T@?,C,N,V_animationCompletion) animationCompletion;
@property (Td,R,N) minimumMaskLayerDistanceFromCenter;
@property (Td,R,N) maximumMaskLayerDistanceFromCenter;
@property (TB,N,V_inSheet) inSheet;
```

## Instance methods

```
-[BKUIPearlPositioningGuideView lineWidth];
-[BKUIPearlPositioningGuideView setLineWidth:];
-[BKUIPearlPositioningGuideView setAnimationDuration:];
-[BKUIPearlPositioningGuideView animationDuration];
-[BKUIPearlPositioningGuideView setHidden:];
-[BKUIPearlPositioningGuideView setAnimationCompletion:];
-[BKUIPearlPositioningGuideView animationCurve];
-[BKUIPearlPositioningGuideView drawRect:];
-[BKUIPearlPositioningGuideView setCornerRadius:];
-[BKUIPearlPositioningGuideView setAnimationCurve:];
-[BKUIPearlPositioningGuideView cornerRadius];
-[BKUIPearlPositioningGuideView initWithFrame:];
-[BKUIPearlPositioningGuideView animationCompletion];
-[BKUIPearlPositioningGuideView ringRadius];
-[BKUIPearlPositioningGuideView setRingRadius:];
-[BKUIPearlPositioningGuideView lineAlpha];
-[BKUIPearlPositioningGuideView setLineAlpha:];
-[BKUIPearlPositioningGuideView targetCornerRadius];
-[BKUIPearlPositioningGuideView breathe];
-[BKUIPearlPositioningGuideView inSheet];
-[BKUIPearlPositioningGuideView targetLineAlpha];
-[BKUIPearlPositioningGuideView targetLineWidth];
-[BKUIPearlPositioningGuideView _displayTick];
-[BKUIPearlPositioningGuideView _maxDistance];
-[BKUIPearlPositioningGuideView _minDistance];
-[BKUIPearlPositioningGuideView _roundedRectMaskForMaskDistance:portalCenter:cornerRadius:];
-[BKUIPearlPositioningGuideView _startAnimationWithDuration:completion:];
-[BKUIPearlPositioningGuideView _startDisplay];
-[BKUIPearlPositioningGuideView _stopDisplay];
-[BKUIPearlPositioningGuideView _updateChildrenValuesForDisplayTickProgress:];
-[BKUIPearlPositioningGuideView _updateTargetValuesForAnimation:animationCurve:];
-[BKUIPearlPositioningGuideView _updatedFloatWithTarget:current:start:progress:];
-[BKUIPearlPositioningGuideView animateToBreatheOutValuesOverDuration:completion:];
-[BKUIPearlPositioningGuideView animateToFinishedValuesOverDuration:center:completion:];
-[BKUIPearlPositioningGuideView animateToOpenValuesOverDuration:curve:completion:];
-[BKUIPearlPositioningGuideView animateToPopOutValuesOverDuration:completion:];
-[BKUIPearlPositioningGuideView animationStart];
-[BKUIPearlPositioningGuideView edgeDistance];
-[BKUIPearlPositioningGuideView lastAnimationTickProgres];
-[BKUIPearlPositioningGuideView maximumMaskLayerDistanceFromCenter];
-[BKUIPearlPositioningGuideView minimumMaskLayerDistanceFromCenter];
-[BKUIPearlPositioningGuideView needsMaskedNeedsPositionStyleEnrollment];
-[BKUIPearlPositioningGuideView portalCenter];
-[BKUIPearlPositioningGuideView postCornerLength];
-[BKUIPearlPositioningGuideView prepareMaskLayerForReducedMotionOpenTransition];
-[BKUIPearlPositioningGuideView prepareMaskLayerForStartToOpenTransition];
-[BKUIPearlPositioningGuideView resetValuesToStart];
-[BKUIPearlPositioningGuideView roundedRectMaskLayer];
-[BKUIPearlPositioningGuideView setAnimationStart:];
-[BKUIPearlPositioningGuideView setEdgeDistance:];
-[BKUIPearlPositioningGuideView setInSheet:];
-[BKUIPearlPositioningGuideView setLastAnimationTickProgres:];
-[BKUIPearlPositioningGuideView setPortalCenter:];
-[BKUIPearlPositioningGuideView setPostCornerLength:];
-[BKUIPearlPositioningGuideView setRoundedRectMaskLayer:];
-[BKUIPearlPositioningGuideView setStartCornerRadius:];
-[BKUIPearlPositioningGuideView setStartEdgeDistance:];
-[BKUIPearlPositioningGuideView setStartLineAlpha:];
-[BKUIPearlPositioningGuideView setStartLineWidth:];
-[BKUIPearlPositioningGuideView setStartPortalCenter:];
-[BKUIPearlPositioningGuideView setStartPostCornerLength:];
-[BKUIPearlPositioningGuideView setTargetCornerRadius:];
-[BKUIPearlPositioningGuideView setTargetEdgeDistance:];
-[BKUIPearlPositioningGuideView setTargetLineAlpha:];
-[BKUIPearlPositioningGuideView setTargetLineWidth:];
-[BKUIPearlPositioningGuideView setTargetPortalCenter:];
-[BKUIPearlPositioningGuideView setTargetPostCornerLength:];
-[BKUIPearlPositioningGuideView startCornerRadius];
-[BKUIPearlPositioningGuideView startEdgeDistance];
-[BKUIPearlPositioningGuideView startLineAlpha];
-[BKUIPearlPositioningGuideView startLineWidth];
-[BKUIPearlPositioningGuideView startPortalCenter];
-[BKUIPearlPositioningGuideView startPostCornerLength];
-[BKUIPearlPositioningGuideView targetEdgeDistance];
-[BKUIPearlPositioningGuideView targetPortalCenter];
-[BKUIPearlPositioningGuideView targetPostCornerLength];
```
