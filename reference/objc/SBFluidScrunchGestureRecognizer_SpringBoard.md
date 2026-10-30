# `SBFluidScrunchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTouchTemplateGestureRecognizer`
- Protocols: `SBGestureRecognizerTouchHistoryProviding`, `SBGestureRecognizerPanGestureProviding`
- 8 instance variables, 13 properties, 46 instance methods, 3 class methods

## Instance variables

```
d _absoluteScale;
q _recognizedTouchType;
d _lastPerimeter;
@"SBTouchHistory" _touchHistory;
@"FBSDisplayConfiguration" _displayConfiguration;
{CGPoint="x"d"y"d} _initialCentroid;
{CGPoint="x"d"y"d} _absoluteTranslation;
{CGPoint="x"d"y"d} _additionalTranslationDueToChangingAnchorPoints;
```

## Properties

```
@property (T{CGPoint=dd},N,V_absoluteTranslation) absoluteTranslation;
@property (Td,N,V_absoluteScale) absoluteScale;
@property (T{CGPoint=dd},N,V_additionalTranslationDueToChangingAnchorPoints) additionalTranslationDueToChangingAnchorPoints;
@property (Td,N,V_lastPerimeter) lastPerimeter;
@property (T{CGPoint=dd},N,V_initialCentroid) initialCentroid;
@property (T@"SBTouchHistory",&,N,V_touchHistory) touchHistory;
@property (T@"FBSDisplayConfiguration",&,N,V_displayConfiguration) displayConfiguration;
@property (T{CGPoint=dd},R,N) centroid;
@property (Tq,R,N,V_recognizedTouchType) recognizedTouchType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFluidScrunchGestureRecognizer _panTemplatesForTouchType:displayConfiguration:];
+[SBFluidScrunchGestureRecognizer _rotateTemplates:forDisplayConfiguration:];
+[SBFluidScrunchGestureRecognizer _scrunchTemplatesForTouchType:displayConfiguration:];
```

## Instance methods

```
-[SBFluidScrunchGestureRecognizer translationInView:];
-[SBFluidScrunchGestureRecognizer _gestureView];
-[SBFluidScrunchGestureRecognizer setTouchHistory:];
-[SBFluidScrunchGestureRecognizer averageTouchPathAngleOverTimeDuration:];
-[SBFluidScrunchGestureRecognizer _hysteresis];
-[SBFluidScrunchGestureRecognizer centroid];
-[SBFluidScrunchGestureRecognizer logCategory];
-[SBFluidScrunchGestureRecognizer touchesEnded:withEvent:];
-[SBFluidScrunchGestureRecognizer _computeGestureMotionWithTouches:polygon:];
-[SBFluidScrunchGestureRecognizer setAbsoluteScale:];
-[SBFluidScrunchGestureRecognizer conformsToSBGestureRecognizerTouchHistoryProviding];
-[SBFluidScrunchGestureRecognizer velocityInView:];
-[SBFluidScrunchGestureRecognizer peakSpeed];
-[SBFluidScrunchGestureRecognizer setAllowedTouchTypes:];
-[SBFluidScrunchGestureRecognizer touchHistory];
-[SBFluidScrunchGestureRecognizer timeWithinRadius:];
-[SBFluidScrunchGestureRecognizer setState:];
-[SBFluidScrunchGestureRecognizer touchesCancelled:withEvent:];
-[SBFluidScrunchGestureRecognizer displayConfiguration];
-[SBFluidScrunchGestureRecognizer recognizedTouchType];
-[SBFluidScrunchGestureRecognizer additionalTranslationDueToChangingAnchorPoints];
-[SBFluidScrunchGestureRecognizer initWithTarget:action:displayConfiguration:];
-[SBFluidScrunchGestureRecognizer absoluteScale];
-[SBFluidScrunchGestureRecognizer setAdditionalTranslationDueToChangingAnchorPoints:];
-[SBFluidScrunchGestureRecognizer reset];
-[SBFluidScrunchGestureRecognizer touchesBegan:withEvent:];
-[SBFluidScrunchGestureRecognizer touchesMoved:withEvent:];
-[SBFluidScrunchGestureRecognizer setDisplayConfiguration:];
-[SBFluidScrunchGestureRecognizer initWithTarget:action:];
-[SBFluidScrunchGestureRecognizer setAbsoluteTranslation:];
-[SBFluidScrunchGestureRecognizer locationInView:];
-[SBFluidScrunchGestureRecognizer lastPerimeter];
-[SBFluidScrunchGestureRecognizer _setMatchedPolygon:];
-[SBFluidScrunchGestureRecognizer setLastPerimeter:];
-[SBFluidScrunchGestureRecognizer setInitialCentroid:];
-[SBFluidScrunchGestureRecognizer _updateRecognizedTouchTypeIfNecessaryWithTouches:];
-[SBFluidScrunchGestureRecognizer averageTouchVelocityOverTimeDuration:];
-[SBFluidScrunchGestureRecognizer _shouldAddNewTouchesAfterGestureRecognition];
-[SBFluidScrunchGestureRecognizer absoluteTranslation];
-[SBFluidScrunchGestureRecognizer _installTemplatesForDisplayConfiguration:];
-[SBFluidScrunchGestureRecognizer _centroidInGestureViewForPolygon:];
-[SBFluidScrunchGestureRecognizer translationWithoutConsideringScaleInView:];
-[SBFluidScrunchGestureRecognizer animationDistance];
-[SBFluidScrunchGestureRecognizer incrementalGestureMotionForCandidate:withTransformAnalyzerInfo:];
-[SBFluidScrunchGestureRecognizer _isMatchedTemplateScrunchTemplate];
-[SBFluidScrunchGestureRecognizer initialCentroid];
```
