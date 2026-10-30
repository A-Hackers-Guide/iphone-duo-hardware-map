# `BKUIPearlPillView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 27 instance variables, 28 properties, 68 instance methods, 0 class methods

## Instance variables

```
d _radius;
Q _state;
d _ringHeight;
d _numberOfPills;
d _pillInitialHeight;
d _pillCompletedHeight;
d _pillCornerRadius;
@"CADisplayLink" _displayLink;
@"CAShapeLayer" _shapeLayer;
@"NSTimer" _stateDelayTimer;
@"NSDate" _stateAnimationStart;
d _stateAnimationDuration;
@? _stateAnimationCompletion;
d _arc;
d _startArc;
d _targetArc;
d _height;
d _startHeight;
d _targetHeight;
d _cornerRadius;
d _startCornerRadius;
d _targetCornerRadius;
@"NSDate" _radiusAnimationStart;
d _radiusAnimationDuration;
@? _radiusAnimationCompletion;
d _startRadius;
d _targetRadius;
```

## Properties

```
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"CAShapeLayer",&,N,V_shapeLayer) shapeLayer;
@property (T@"NSTimer",&,N,V_stateDelayTimer) stateDelayTimer;
@property (T@"NSDate",&,N,V_stateAnimationStart) stateAnimationStart;
@property (Td,N,V_stateAnimationDuration) stateAnimationDuration;
@property (T@?,C,N,V_stateAnimationCompletion) stateAnimationCompletion;
@property (Td,N,V_arc) arc;
@property (Td,N,V_startArc) startArc;
@property (Td,N,V_targetArc) targetArc;
@property (Td,N,V_height) height;
@property (Td,N,V_startHeight) startHeight;
@property (Td,N,V_targetHeight) targetHeight;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Td,N,V_startCornerRadius) startCornerRadius;
@property (Td,N,V_targetCornerRadius) targetCornerRadius;
@property (T@"NSDate",&,N,V_radiusAnimationStart) radiusAnimationStart;
@property (Td,N,V_radiusAnimationDuration) radiusAnimationDuration;
@property (T@?,C,N,V_radiusAnimationCompletion) radiusAnimationCompletion;
@property (Td,N,V_startRadius) startRadius;
@property (Td,N,V_targetRadius) targetRadius;
@property (Td,N,V_radius) radius;
@property (TQ,N,V_state) state;
@property (TB,R,N,GisCompleted) completed;
@property (Td,N,V_ringHeight) ringHeight;
@property (Td,N,V_numberOfPills) numberOfPills;
@property (Td,N,V_pillInitialHeight) pillInitialHeight;
@property (Td,N,V_pillCompletedHeight) pillCompletedHeight;
@property (Td,N,V_pillCornerRadius) pillCornerRadius;
```

## Instance methods

```
-[BKUIPearlPillView displayLink];
-[BKUIPearlPillView setState:];
-[BKUIPearlPillView setState:animated:];
-[BKUIPearlPillView shapeLayer];
-[BKUIPearlPillView init];
-[BKUIPearlPillView isCompleted];
-[BKUIPearlPillView setShapeLayer:];
-[BKUIPearlPillView dealloc];
-[BKUIPearlPillView layoutSubviews];
-[BKUIPearlPillView setCornerRadius:];
-[BKUIPearlPillView setRadius:];
-[BKUIPearlPillView setDisplayLink:];
-[BKUIPearlPillView setHeight:];
-[BKUIPearlPillView radius];
-[BKUIPearlPillView cornerRadius];
-[BKUIPearlPillView pillCornerRadius];
-[BKUIPearlPillView height];
-[BKUIPearlPillView state];
-[BKUIPearlPillView setStartHeight:];
-[BKUIPearlPillView setTargetHeight:];
-[BKUIPearlPillView startHeight];
-[BKUIPearlPillView targetHeight];
-[BKUIPearlPillView pillInitialHeight];
-[BKUIPearlPillView ringHeight];
-[BKUIPearlPillView setNumberOfPills:];
-[BKUIPearlPillView setPillCompletedHeight:];
-[BKUIPearlPillView setPillCornerRadius:];
-[BKUIPearlPillView setPillInitialHeight:];
-[BKUIPearlPillView setRadius:animationDuration:completion:];
-[BKUIPearlPillView setRingHeight:];
-[BKUIPearlPillView setState:animated:animationDelay:completion:failure:];
-[BKUIPearlPillView tearDownPillView];
-[BKUIPearlPillView targetCornerRadius];
-[BKUIPearlPillView arc];
-[BKUIPearlPillView setArc:];
-[BKUIPearlPillView setStartRadius:];
-[BKUIPearlPillView stateDelayTimer];
-[BKUIPearlPillView displayTick];
-[BKUIPearlPillView numberOfPills];
-[BKUIPearlPillView pillCompletedHeight];
-[BKUIPearlPillView pillMaxLength];
-[BKUIPearlPillView pillPath];
-[BKUIPearlPillView radiusAnimationCompletion];
-[BKUIPearlPillView radiusAnimationDuration];
-[BKUIPearlPillView radiusAnimationStart];
-[BKUIPearlPillView ringArcLength];
-[BKUIPearlPillView setRadiusAnimationCompletion:];
-[BKUIPearlPillView setRadiusAnimationDuration:];
-[BKUIPearlPillView setRadiusAnimationStart:];
-[BKUIPearlPillView setStartArc:];
-[BKUIPearlPillView setStartCornerRadius:];
-[BKUIPearlPillView setState:animated:completion:failure:];
-[BKUIPearlPillView setStateAnimationCompletion:];
-[BKUIPearlPillView setStateAnimationDuration:];
-[BKUIPearlPillView setStateAnimationStart:];
-[BKUIPearlPillView setStateDelayTimer:];
-[BKUIPearlPillView setTargetArc:];
-[BKUIPearlPillView setTargetCornerRadius:];
-[BKUIPearlPillView setTargetRadius:];
-[BKUIPearlPillView startAnimationWithDuration:completion:];
-[BKUIPearlPillView startArc];
-[BKUIPearlPillView startCornerRadius];
-[BKUIPearlPillView startRadius];
-[BKUIPearlPillView stateAnimationCompletion];
-[BKUIPearlPillView stateAnimationDuration];
-[BKUIPearlPillView stateAnimationStart];
-[BKUIPearlPillView targetArc];
-[BKUIPearlPillView targetRadius];
```
