# `BKMouseEventAccumulator`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 48 instance variables, 30 properties, 62 instance methods, 0 class methods

## Instance variables

```
Q _eventTypeMask;
Q _interpolateEventTypeMask;
Q _eventSequenceStartTimestamp;
@? _postEventAsyncBlock;
@"NSMutableDictionary" _eventStateBySenderID;
@"NSMutableSet" _doomedSenderIDs;
{XYDeltaDistributorWithAcceleration="_queue"[4{PendingDelta="raw"{CGPoint="x"d"y"d}"compensatedScaled"{CGPoint="x"d"y"d}"ingestTime"Q"scanRate"d"cumulativeElapsed"d"dispatchAll"B}]"_count"i"_lastIngestTime"Q"_previousAccelSpeed"d} _pointerInterpolator;
{CGPoint="x"d"y"d} _pointerUnacceleratedDelta;
{CGPoint="x"d"y"d} _pointerAcceleratedDelta;
{CGPoint="x"d"y"d} _pointerAbsolutePosition;
q _positionType;
{PhasedEventTracker<6U>="_eventSender"@"<BKHIDEventSenderInfo>""_inputPhase"S"_outputPhase"S"_initialTimestamp"Q"_reportBeganPhase"B"_sentTerminalEvent"B} _scrollPhaseTracker;
{XYDeltaDistributorWithAcceleration="_queue"[4{PendingDelta="raw"{CGPoint="x"d"y"d}"compensatedScaled"{CGPoint="x"d"y"d}"ingestTime"Q"scanRate"d"cumulativeElapsed"d"dispatchAll"B}]"_count"i"_lastIngestTime"Q"_previousAccelSpeed"d} _scrollInterpolator;
{CGPoint="x"d"y"d} _scrollUnacceleratedDelta;
{CGPoint="x"d"y"d} _scrollAcceleratedDelta;
q _discreteScrollGeneration;
{PhasedEventTracker<4U>="_eventSender"@"<BKHIDEventSenderInfo>""_inputPhase"S"_outputPhase"S"_initialTimestamp"Q"_reportBeganPhase"B"_sentTerminalEvent"B} _translationPhaseTracker;
{XYDeltaDistributor="_queue"[4{PendingDelta="compensated"{CGPoint="x"d"y"d}"ingestTime"Q"scanRate"d"cumulativeElapsed"d"dispatchAll"B}]"_count"i"_lastIngestTime"Q"_previousSpeed"d} _translationInterpolator;
{CGPoint="x"d"y"d} _translationDelta;
{PhasedEventTracker<7U>="_eventSender"@"<BKHIDEventSenderInfo>""_inputPhase"S"_outputPhase"S"_initialTimestamp"Q"_reportBeganPhase"B"_sentTerminalEvent"B} _scalePhaseTracker;
{ScalarDeltaDistributor="_queue"[4{PendingDelta="compensated"d"ingestTime"Q"scanRate"d"cumulativeElapsed"d"dispatchAll"B}]"_count"i"_lastIngestTime"Q"_previousSpeed"d} _scaleInterpolator;
d _scaleZ;
{PhasedEventTracker<5U>="_eventSender"@"<BKHIDEventSenderInfo>""_inputPhase"S"_outputPhase"S"_initialTimestamp"Q"_reportBeganPhase"B"_sentTerminalEvent"B} _rotationPhaseTracker;
{ScalarDeltaDistributor="_queue"[4{PendingDelta="compensated"d"ingestTime"Q"scanRate"d"cumulativeElapsed"d"dispatchAll"B}]"_count"i"_lastIngestTime"Q"_previousSpeed"d} _rotationInterpolator;
d _rotationZ;
@"NSMutableArray" _digitizerEvents;
^{__IOHIDEvent=} _forceEvent;
I _buttonMask;
@"NSMutableArray" _buttonEvents;
B _touchingPathIndexesDidChange;
B _buttonMaskDidChange;
B _scrollPhaseDidChange;
B _isInvalid;
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq} _interpolationLogFile;
d _frameInterval;
B _forceDidChange;
B _absolutePositionIsValid;
B _shouldScrollNaturally;
B _shouldSwapPrimaryAndSecondaryButtons;
B _shouldUseButtonDownRecenteringBehavior;
B _logInterpolationDetails;
S _scrollPhase;
I _previousButtonMask;
I _stage;
d _force;
@"NSIndexSet" _touchingPathIndexes;
Q _lastRemoteEventTimestamp;
@"<BKHIDEventSenderInfo>" _mostRecentSender;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_digitizerEvents) digitizerEvents;
@property (TQ,R,N,V_eventTypeMask) eventTypeMask;
@property (TI,R,N,V_previousButtonMask) previousButtonMask;
@property (TI,R,N,V_buttonMask) buttonMask;
@property (TB,R,N) buttonMaskDidChange;
@property (Td,R,N,V_force) force;
@property (TI,R,N,V_stage) stage;
@property (TB,R,N,V_forceDidChange) forceDidChange;
@property (T@"NSIndexSet",R,N,V_touchingPathIndexes) touchingPathIndexes;
@property (TB,R,N) touchingPathIndexesDidChange;
@property (TS,R,N,V_scrollPhase) scrollPhase;
@property (TQ,R,N) eventSequenceStartTimestamp;
@property (TQ,R,N,V_lastRemoteEventTimestamp) lastRemoteEventTimestamp;
@property (TB,R,N) scrollPhaseDidChange;
@property (T{CGPoint=dd},R,N) unacceleratedRelativePointerPosition;
@property (T{CGPoint=dd},R,N) acceleratedRelativePointerPosition;
@property (T{CGPoint=dd},R,N,V_pointerAbsolutePosition) pointerAbsolutePosition;
@property (TB,R,N,V_absolutePositionIsValid) absolutePositionIsValid;
@property (Tq,R,N,V_positionType) positionType;
@property (Tq,R,N) hitTestReason;
@property (T@"<BKHIDEventSenderInfo>",R,N,V_mostRecentSender) mostRecentSender;
@property (TB,N,V_shouldScrollNaturally) shouldScrollNaturally;
@property (TB,N,V_shouldSwapPrimaryAndSecondaryButtons) shouldSwapPrimaryAndSecondaryButtons;
@property (TB,N,V_shouldUseButtonDownRecenteringBehavior) shouldUseButtonDownRecenteringBehavior;
@property (TB,N,V_logInterpolationDetails) logInterpolationDetails;
@property (Td,N,V_frameInterval) frameInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKMouseEventAccumulator nextEvent];
-[BKMouseEventAccumulator setFrameInterval:];
-[BKMouseEventAccumulator init];
-[BKMouseEventAccumulator stage];
-[BKMouseEventAccumulator dealloc];
-[BKMouseEventAccumulator invalidate];
-[BKMouseEventAccumulator frameInterval];
-[BKMouseEventAccumulator force];
-[BKMouseEventAccumulator buttonMask];
-[BKMouseEventAccumulator positionType];
-[BKMouseEventAccumulator digitizerEvents];
-[BKMouseEventAccumulator _terminateAllGesturesForSender:];
-[BKMouseEventAccumulator addTranslationEvent:fromSender:];
-[BKMouseEventAccumulator _eventStateForSender:];
-[BKMouseEventAccumulator _shouldHitTestForGestureBegan];
-[BKMouseEventAccumulator _terminateScrollingForSender:];
-[BKMouseEventAccumulator _updateTouchingPathIndexesFromDeviceEventState];
-[BKMouseEventAccumulator absolutePositionIsValid];
-[BKMouseEventAccumulator acceleratedRelativePointerPosition];
-[BKMouseEventAccumulator addButtonEvent:fromSender:];
-[BKMouseEventAccumulator addButtonNumber:down:fromSender:];
-[BKMouseEventAccumulator addDigitizerEvent:fromSender:];
-[BKMouseEventAccumulator addForceEvent:fromSender:];
-[BKMouseEventAccumulator addRotationEvent:fromSender:];
-[BKMouseEventAccumulator addScaleEvent:fromSender:];
-[BKMouseEventAccumulator addScrollEvent:fromSender:];
-[BKMouseEventAccumulator addSyntheticTopLevelEventIfNeeded];
-[BKMouseEventAccumulator addTopLevelEvent:fromSender:];
-[BKMouseEventAccumulator addTopLevelScaleEvent:fromSender:];
-[BKMouseEventAccumulator addTopLevelScrollEvent:fromSender:];
-[BKMouseEventAccumulator appendSubeventsForEventTypeMask:toTopLevelEvent:interfaceOrientation:getEventSummary:];
-[BKMouseEventAccumulator buttonMaskDidChange];
-[BKMouseEventAccumulator deviceServiceDidAppear:];
-[BKMouseEventAccumulator deviceServiceDidTerminate:];
-[BKMouseEventAccumulator eventSequenceStartTimestamp];
-[BKMouseEventAccumulator eventTypeMask];
-[BKMouseEventAccumulator forceDidChange];
-[BKMouseEventAccumulator frameDidEnd];
-[BKMouseEventAccumulator frameWillBegin];
-[BKMouseEventAccumulator hitTestReason];
-[BKMouseEventAccumulator initWithInterpolatedEventTypeMask:postEventsBlock:];
-[BKMouseEventAccumulator invalidateAbsolutePosition];
-[BKMouseEventAccumulator isSenderLocked];
-[BKMouseEventAccumulator lastRemoteEventTimestamp];
-[BKMouseEventAccumulator logInterpolationDetails];
-[BKMouseEventAccumulator mostRecentSender];
-[BKMouseEventAccumulator pointerAbsolutePosition];
-[BKMouseEventAccumulator previousButtonMask];
-[BKMouseEventAccumulator scrollPhase];
-[BKMouseEventAccumulator scrollPhaseDidChange];
-[BKMouseEventAccumulator senderPostsAtHighFrequency:];
-[BKMouseEventAccumulator setDigitizerEvents:];
-[BKMouseEventAccumulator setLogInterpolationDetails:];
-[BKMouseEventAccumulator setShouldScrollNaturally:];
-[BKMouseEventAccumulator setShouldSwapPrimaryAndSecondaryButtons:];
-[BKMouseEventAccumulator setShouldUseButtonDownRecenteringBehavior:];
-[BKMouseEventAccumulator shouldScrollNaturally];
-[BKMouseEventAccumulator shouldSwapPrimaryAndSecondaryButtons];
-[BKMouseEventAccumulator shouldUseButtonDownRecenteringBehavior];
-[BKMouseEventAccumulator touchingPathIndexes];
-[BKMouseEventAccumulator touchingPathIndexesDidChange];
-[BKMouseEventAccumulator unacceleratedRelativePointerPosition];
```
