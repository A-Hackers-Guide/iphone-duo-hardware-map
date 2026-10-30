# `CAMClosedViewfinderController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 30 instance methods, 0 class methods

## Instance variables

```
q _wantsViewfinderClosedDueToSessionReasonCount;
@"<CAMClosedViewfinderControllerDelegate>" _delegate;
@"NSMutableSet" __reasonsForClosingViewfinder;
d __referenceTime;
q __referenceTimeEvent;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__reasonsForClosingViewfinder) _reasonsForClosingViewfinder;
@property (Td,N,S_setReferenceTime:,V__referenceTime) _referenceTime;
@property (Tq,N,S_setReferenceTimeEvent:,V__referenceTimeEvent) _referenceTimeEvent;
@property (T@"<CAMClosedViewfinderControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisViewfinderClosed) viewfinderClosed;
```

## Instance methods

```
-[CAMClosedViewfinderController _handleApplicationWillEnterForeground:];
-[CAMClosedViewfinderController _updateReferenceTimeToNowForEvent:];
-[CAMClosedViewfinderController _closedViewfinderReasonIsDueToSession:];
-[CAMClosedViewfinderController _cancelDelayedLoggingForClosedViewfinder];
-[CAMClosedViewfinderController init];
-[CAMClosedViewfinderController _scheduleLogWarningIfViewfinderStillClosedAfterDelay:];
-[CAMClosedViewfinderController hasClosedViewfinderReason:];
-[CAMClosedViewfinderController _handleApplicationDidEnterBackground:];
-[CAMClosedViewfinderController _descriptionForReasons:];
-[CAMClosedViewfinderController descriptionForTimeBetweenReferenceAndNow];
-[CAMClosedViewfinderController dealloc];
-[CAMClosedViewfinderController removeClosedViewfinderReason:];
-[CAMClosedViewfinderController _handleApplicationDidBecomeActive:];
-[CAMClosedViewfinderController _performDelayedRemovalOfReason:];
-[CAMClosedViewfinderController _setReferenceTime:];
-[CAMClosedViewfinderController setDelegate:];
-[CAMClosedViewfinderController _referenceTimeEvent];
-[CAMClosedViewfinderController wantsPreviewDisplayedBySession];
-[CAMClosedViewfinderController _reasonsForClosingViewfinder];
-[CAMClosedViewfinderController delegate];
-[CAMClosedViewfinderController _setReferenceTimeEvent:];
-[CAMClosedViewfinderController _descriptionStringForReason:];
-[CAMClosedViewfinderController isClosedForExactlyOneReason:];
-[CAMClosedViewfinderController addClosedViewfinderReason:];
-[CAMClosedViewfinderController isViewfinderClosed];
-[CAMClosedViewfinderController cancelDelayedRemovalOfReason:];
-[CAMClosedViewfinderController removeClosedViewfinderReason:afterDelay:];
-[CAMClosedViewfinderController _descriptionStringForReferenceTimeEvent:];
-[CAMClosedViewfinderController _referenceTime];
-[CAMClosedViewfinderController _logWarningIfViewfinderStillClosed];
```
