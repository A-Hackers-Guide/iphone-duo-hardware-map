# `_UIKBRTRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 17 properties, 68 instance methods, 0 class methods

## Instance variables

```
B _isWaiting;
B _disableHomeRowReturn;
@"<_UIKBRTRecognizerDelegate>" _delegate;
@"<_UIKBRTRecognizerTouchLoggingProtocol>" _touchLogger;
@"<_UIKBRTRecognizerTouchPointTrackingProtocol>" _touchTracker;
@"NSMutableSet" _definitiveRules;
@"NSMutableSet" _averagingRules;
d _maximumNonRestMoveDistance;
@"NSObject<OS_dispatch_queue>" _touchQueue;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSMutableArray" _touchInfos;
@"NSMutableSet" _activeTouches;
@"NSObject<OS_dispatch_queue>" _activeTouchesQueue;
@"NSMutableArray" _ignoredTouches;
@"NSObject<OS_dispatch_queue>" _ignoredTouchesQueue;
Q _numProlongedTouches;
d _touchIntervalAverage;
{CGSize="width"d"height"d} _clusterRestHaloSize;
```

## Properties

```
@property (T{CGSize=dd},N,V_clusterRestHaloSize) clusterRestHaloSize;
@property (Td,N,V_maximumNonRestMoveDistance) maximumNonRestMoveDistance;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_touchQueue) touchQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_delegateQueue) delegateQueue;
@property (T@"NSMutableArray",&,N,V_touchInfos) touchInfos;
@property (T@"NSMutableSet",&,N,V_activeTouches) activeTouches;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_activeTouchesQueue) activeTouchesQueue;
@property (T@"NSMutableArray",&,N,V_ignoredTouches) ignoredTouches;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_ignoredTouchesQueue) ignoredTouchesQueue;
@property (TQ,N,V_numProlongedTouches) numProlongedTouches;
@property (Td,N,V_touchIntervalAverage) touchIntervalAverage;
@property (T@"<_UIKBRTRecognizerTouchLoggingProtocol>",&,N,V_touchLogger) touchLogger;
@property (T@"<_UIKBRTRecognizerTouchPointTrackingProtocol>",&,N,V_touchTracker) touchTracker;
@property (T@"<_UIKBRTRecognizerDelegate>",N,V_delegate) delegate;
@property (T@"NSMutableSet",R,N,V_definitiveRules) definitiveRules;
@property (T@"NSMutableSet",R,N,V_averagingRules) averagingRules;
@property (TB,N,V_disableHomeRowReturn) disableHomeRowReturn;
```

## Instance methods

```
-[_UIKBRTRecognizer setActiveTouches:];
-[_UIKBRTRecognizer init];
-[_UIKBRTRecognizer reset];
-[_UIKBRTRecognizer setDelegate:];
-[_UIKBRTRecognizer setDelegateQueue:];
-[_UIKBRTRecognizer delegate];
-[_UIKBRTRecognizer activeTouches];
-[_UIKBRTRecognizer delegateQueue];
-[_UIKBRTRecognizer definitiveRules];
-[_UIKBRTRecognizer letRulesModifyPendingTouchInfo:];
-[_UIKBRTRecognizer setTouchLogger:];
-[_UIKBRTRecognizer _doCancelledTouchWithTouchInfo:];
-[_UIKBRTRecognizer makeTouchIgnored:force:because:];
-[_UIKBRTRecognizer notifyDelegateOfCancelledTouch:];
-[_UIKBRTRecognizer _doBeginTouchWithTouchInfo:];
-[_UIKBRTRecognizer _doEndedTouchWithTouchInfo:];
-[_UIKBRTRecognizer _doIgnoreTouchWithTouchInfo:];
-[_UIKBRTRecognizer _doMarkTouchProcessedWithTouchInfo:];
-[_UIKBRTRecognizer _doMovedTouchWithTouchInfo:];
-[_UIKBRTRecognizer activeTouchesQueue];
-[_UIKBRTRecognizer addedToActiveTouches:];
-[_UIKBRTRecognizer averagingRules];
-[_UIKBRTRecognizer cancelTouchOnLayoutWithTouchInfo:];
-[_UIKBRTRecognizer clusterRestHaloSize];
-[_UIKBRTRecognizer disableHomeRowReturn];
-[_UIKBRTRecognizer explicitlyIgnoreTouch:withIdentifier:];
-[_UIKBRTRecognizer ignoredTouches];
-[_UIKBRTRecognizer ignoredTouchesQueue];
-[_UIKBRTRecognizer kbStatusMessage:];
-[_UIKBRTRecognizer letRulesModifyNewTouchInfo:];
-[_UIKBRTRecognizer makeTouchActive:];
-[_UIKBRTRecognizer makeTouchIgnored:force:];
-[_UIKBRTRecognizer makeTouchIgnored:force:withMessage:];
-[_UIKBRTRecognizer markTouchProcessed:withIdentifier:];
-[_UIKBRTRecognizer maximumNonRestMoveDistance];
-[_UIKBRTRecognizer notifyDelegateOfIgnoringTouch:];
-[_UIKBRTRecognizer notifyDelegateOfMovedIgnoredTouch:];
-[_UIKBRTRecognizer notifyDelegateOfMovedTouch:];
-[_UIKBRTRecognizer notifyDelegateOfRestingTouch:];
-[_UIKBRTRecognizer notifyDelegateOfSuccessfulTouch:];
-[_UIKBRTRecognizer numProlongedTouches];
-[_UIKBRTRecognizer processTouchInfo:];
-[_UIKBRTRecognizer queryDelegateOfIgnoringTouch:forOtherTouch:];
-[_UIKBRTRecognizer queryDelegateOfRestingTouch:];
-[_UIKBRTRecognizer queryDelegateToBeginTouch:forBeginState:restartIfNecessary:];
-[_UIKBRTRecognizer removedFromActiveTouches:];
-[_UIKBRTRecognizer setActiveTouchesQueue:];
-[_UIKBRTRecognizer setClusterRestHaloSize:];
-[_UIKBRTRecognizer setDisableHomeRowReturn:];
-[_UIKBRTRecognizer setIgnoredTouches:];
-[_UIKBRTRecognizer setIgnoredTouchesQueue:];
-[_UIKBRTRecognizer setMaximumNonRestMoveDistance:];
-[_UIKBRTRecognizer setNumProlongedTouches:];
-[_UIKBRTRecognizer setStandardKeyPixelSize:];
-[_UIKBRTRecognizer setTouchInfos:];
-[_UIKBRTRecognizer setTouchIntervalAverage:];
-[_UIKBRTRecognizer setTouchQueue:];
-[_UIKBRTRecognizer setTouchTracker:];
-[_UIKBRTRecognizer touchCancelled:withIdentifier:];
-[_UIKBRTRecognizer touchDown:withIdentifier:canLogTouch:];
-[_UIKBRTRecognizer touchDragged:withIdentifier:];
-[_UIKBRTRecognizer touchInfos];
-[_UIKBRTRecognizer touchIntervalAverage];
-[_UIKBRTRecognizer touchLogger];
-[_UIKBRTRecognizer touchQueue];
-[_UIKBRTRecognizer touchTracker];
-[_UIKBRTRecognizer touchUp:withIdentifier:];
-[_UIKBRTRecognizer updateIgnoredTouchesForTouchInfo:whenTouchInfo:changesStateTo:];
```
