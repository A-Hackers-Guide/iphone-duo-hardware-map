# `SBTouchTemplateGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 15 instance variables, 16 properties, 57 instance methods, 0 class methods

## Instance variables

```
B _recognitionBegan;
@"NSTimer" _noChangeCancellationTimer;
Q _sequenceNumber;
@"NSMutableDictionary" _templatesForTouchType;
@"NSMapTable" _initialTouchPointMap;
Q _failedRecognitionAttempts;
Q _trackingTouchCount;
d _cumulativeMotion;
d _cumulativeMotionEnvelope;
d _smoothedIncrementalMotion;
d _animationDistance;
q _requiredDirectionality;
@"UIGestureRecognizerTransformAnalyzer" _transformAnalyzer;
@"SBTouchTemplate" _matchedTemplate;
@"SBPolygon" _matchedPolygon;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_templatesForTouchType) templatesForTouchType;
@property (T@"NSMapTable",R,N,G_initialTouchPointMap,V_initialTouchPointMap) initialTouchPointMap;
@property (TQ,N,G_failedRecognitionAttempts,S_setFailedRecognitionAttempts:,V_failedRecognitionAttempts) failedRecognitionAttempts;
@property (TQ,N,G_trackingTouchCount,S_setTrackingTouchCount:,V_trackingTouchCount) trackingTouchCount;
@property (Td,N,G_cumulativeMotion,S_setCumulativeMotion:,V_cumulativeMotion) cumulativeMotion;
@property (Td,N,G_cumulativeMotionEnvelope,S_setCumulativeMotionEnvelope:,V_cumulativeMotionEnvelope) cumulativeMotionEnvelope;
@property (Td,N,G_smoothedIncrementalMotion,S_setSmoothedIncrementalMotion:,V_smoothedIncrementalMotion) smoothedIncrementalMotion;
@property (T@"NSTimer",&,N,S_setNoChangeCancellationTimer:,V_noChangeCancellationTimer) _noChangeCancellationTimer;
@property (Td,N,V_animationDistance) animationDistance;
@property (Tq,N,V_requiredDirectionality) requiredDirectionality;
@property (T@"UIGestureRecognizerTransformAnalyzer",R,N,V_transformAnalyzer) transformAnalyzer;
@property (T@"SBTouchTemplate",&,N,G_matchedTemplate,S_setMatchedTemplate:,V_matchedTemplate) matchedTemplate;
@property (T@"SBPolygon",&,N,G_matchedPolygon,S_setMatchedPolygon:,V_matchedPolygon) matchedPolygon;
@property (T@"<SBTouchTemplateGestureRecognizerDelegate>",W,D,N) delegate;
@property (TQ,R,N,V_sequenceNumber) sequenceNumber;
@property (Td,R,N) cumulativePercentage;
```

## Instance methods

```
-[SBTouchTemplateGestureRecognizer logCategory];
-[SBTouchTemplateGestureRecognizer touchesEnded:withEvent:];
-[SBTouchTemplateGestureRecognizer _computeGestureMotionWithTouches:polygon:];
-[SBTouchTemplateGestureRecognizer _reset];
-[SBTouchTemplateGestureRecognizer setState:];
-[SBTouchTemplateGestureRecognizer touchesCancelled:withEvent:];
-[SBTouchTemplateGestureRecognizer sequenceNumber];
-[SBTouchTemplateGestureRecognizer reset];
-[SBTouchTemplateGestureRecognizer transformAnalyzer];
-[SBTouchTemplateGestureRecognizer touchesBegan:withEvent:];
-[SBTouchTemplateGestureRecognizer touchesMoved:withEvent:];
-[SBTouchTemplateGestureRecognizer initWithTarget:action:];
-[SBTouchTemplateGestureRecognizer _setMatchedPolygon:];
-[SBTouchTemplateGestureRecognizer _shouldAddNewTouchesAfterGestureRecognition];
-[SBTouchTemplateGestureRecognizer log:];
-[SBTouchTemplateGestureRecognizer animationDistance];
-[SBTouchTemplateGestureRecognizer incrementalGestureMotionForCandidate:withTransformAnalyzerInfo:];
-[SBTouchTemplateGestureRecognizer setAnimationDistance:];
-[SBTouchTemplateGestureRecognizer _resetNoChangeCancellationTimer];
-[SBTouchTemplateGestureRecognizer _matchedPolygon];
-[SBTouchTemplateGestureRecognizer _attemptTemplateMatchWithTouches:polygon:];
-[SBTouchTemplateGestureRecognizer _cumulativeMotion];
-[SBTouchTemplateGestureRecognizer _cumulativeMotionEnvelope];
-[SBTouchTemplateGestureRecognizer _directionallyAcceptMotion:];
-[SBTouchTemplateGestureRecognizer _failMeForReason:];
-[SBTouchTemplateGestureRecognizer _failedRecognitionAttempts];
-[SBTouchTemplateGestureRecognizer _initialTouchPointMap];
-[SBTouchTemplateGestureRecognizer _invalidateNoChangeCancellationTimer];
-[SBTouchTemplateGestureRecognizer _log:];
-[SBTouchTemplateGestureRecognizer _matchedTemplate];
-[SBTouchTemplateGestureRecognizer _matchedTemplateForTouches:polygon:];
-[SBTouchTemplateGestureRecognizer _noChangeCancellationTimer];
-[SBTouchTemplateGestureRecognizer _noChangeCancellationTimerFired:];
-[SBTouchTemplateGestureRecognizer _pingNoChangeCancellationTimer];
-[SBTouchTemplateGestureRecognizer _polygonForTouches:];
-[SBTouchTemplateGestureRecognizer _projectedMotionForInterval:];
-[SBTouchTemplateGestureRecognizer _setCumulativeMotion:];
-[SBTouchTemplateGestureRecognizer _setCumulativeMotionEnvelope:];
-[SBTouchTemplateGestureRecognizer _setFailedRecognitionAttempts:];
-[SBTouchTemplateGestureRecognizer _setMatchedTemplate:];
-[SBTouchTemplateGestureRecognizer _setNoChangeCancellationTimer:];
-[SBTouchTemplateGestureRecognizer _setSmoothedIncrementalMotion:];
-[SBTouchTemplateGestureRecognizer _setTrackingTouchCount:];
-[SBTouchTemplateGestureRecognizer _smoothedIncrementalMotion];
-[SBTouchTemplateGestureRecognizer _touchesByFilteringRestingTrackpadTouches:];
-[SBTouchTemplateGestureRecognizer _trackingTouchCount];
-[SBTouchTemplateGestureRecognizer _updateForTouchesBeganOrMoved:];
-[SBTouchTemplateGestureRecognizer _updateForTouchesCancelledOrEnded:state:withEvent:];
-[SBTouchTemplateGestureRecognizer _updateMatchedTemplateForTouchesBeganOrEnded:];
-[SBTouchTemplateGestureRecognizer cumulativePercentage];
-[SBTouchTemplateGestureRecognizer hasSignificantMotionToBegin];
-[SBTouchTemplateGestureRecognizer projectedCompletionTypeForInterval:];
-[SBTouchTemplateGestureRecognizer requiredDirectionality];
-[SBTouchTemplateGestureRecognizer setRequiredDirectionality:];
-[SBTouchTemplateGestureRecognizer setTemplates:forTouchType:];
-[SBTouchTemplateGestureRecognizer templatesForTouchType];
-[SBTouchTemplateGestureRecognizer templatesForTouchType:];
```
