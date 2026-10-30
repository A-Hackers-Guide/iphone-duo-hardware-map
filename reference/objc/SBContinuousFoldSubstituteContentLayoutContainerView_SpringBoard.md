# `SBContinuousFoldSubstituteContentLayoutContainerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentView;
{CGSize="width"d"height"d} _contentSize;
@"UIView" _leftEdgeExtension;
@"UIView" _rightEdgeExtension;
@"UIView" _topEdgeExtension;
@"UIView" _bottomEdgeExtension;
@"UIView" _fillView;
B _debugBordersEnabled;
B _fillsFreeAxis;
q _fillMode;
@"UIColor" _fillColor;
@"UIColor" _debugBorderColor;
d _contentRotation;
```

## Properties

```
@property (Tq,N,V_fillMode) fillMode;
@property (T@"UIColor",&,N,V_fillColor) fillColor;
@property (TB,N,GisDebugBordersEnabled,V_debugBordersEnabled) debugBordersEnabled;
@property (T@"UIColor",&,N,V_debugBorderColor) debugBorderColor;
@property (TB,N,V_fillsFreeAxis) fillsFreeAxis;
@property (Td,N,V_contentRotation) contentRotation;
```

## Instance methods

```
-[SBContinuousFoldSubstituteContentLayoutContainerView fillMode];
-[SBContinuousFoldSubstituteContentLayoutContainerView setFillMode:];
-[SBContinuousFoldSubstituteContentLayoutContainerView setContentMode:];
-[SBContinuousFoldSubstituteContentLayoutContainerView setFillColor:];
-[SBContinuousFoldSubstituteContentLayoutContainerView fillColor];
-[SBContinuousFoldSubstituteContentLayoutContainerView layoutSubviews];
-[SBContinuousFoldSubstituteContentLayoutContainerView debugBorderColor];
-[SBContinuousFoldSubstituteContentLayoutContainerView _updateDebugBorders];
-[SBContinuousFoldSubstituteContentLayoutContainerView _ensureFillView];
-[SBContinuousFoldSubstituteContentLayoutContainerView contentRotation];
-[SBContinuousFoldSubstituteContentLayoutContainerView _makeEdgeExtensionForEdge:];
-[SBContinuousFoldSubstituteContentLayoutContainerView _positionEdgeExtension:sampleRect:targetRect:edge:];
-[SBContinuousFoldSubstituteContentLayoutContainerView _teardownEdgeExtensions];
-[SBContinuousFoldSubstituteContentLayoutContainerView _teardownFillView];
-[SBContinuousFoldSubstituteContentLayoutContainerView _updateEdgeExtensionsForRenderedContentRect:scaleX:scaleY:];
-[SBContinuousFoldSubstituteContentLayoutContainerView _updateFillForRenderedContentRect:scaleX:scaleY:];
-[SBContinuousFoldSubstituteContentLayoutContainerView _updateStaticColorFill];
-[SBContinuousFoldSubstituteContentLayoutContainerView fillsFreeAxis];
-[SBContinuousFoldSubstituteContentLayoutContainerView initWithContentView:contentSize:];
-[SBContinuousFoldSubstituteContentLayoutContainerView isDebugBordersEnabled];
-[SBContinuousFoldSubstituteContentLayoutContainerView setContentRotation:];
-[SBContinuousFoldSubstituteContentLayoutContainerView setDebugBorderColor:];
-[SBContinuousFoldSubstituteContentLayoutContainerView setDebugBordersEnabled:];
-[SBContinuousFoldSubstituteContentLayoutContainerView setFillsFreeAxis:];
```
