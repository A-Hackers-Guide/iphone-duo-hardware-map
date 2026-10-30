# `_UIGestureStudyInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 6 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<_UIGestureStudyInteractionDelegate>" _delegate;
@"_UIGestureStudyClickInteraction" _forceClickInteraction;
@"_UIGestureStudyClickInteraction" _longPressClickInteraction;
@"_UIGestureStudyMetricsGestureRecognizer" _metricsGestureRecognizer;
@"NSMutableDictionary" _eventMetadata;
```

## Properties

```
@property (T@"<_UIGestureStudyInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"_UIGestureStudyClickInteraction",&,N,V_forceClickInteraction) forceClickInteraction;
@property (T@"_UIGestureStudyClickInteraction",&,N,V_longPressClickInteraction) longPressClickInteraction;
@property (T@"_UIGestureStudyMetricsGestureRecognizer",&,N,V_metricsGestureRecognizer) metricsGestureRecognizer;
@property (T@"NSMutableDictionary",&,N,V_eventMetadata) eventMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIGestureStudyInteraction locationInCoordinateSpace:];
-[_UIGestureStudyInteraction initWithDelegate:];
-[_UIGestureStudyInteraction eventMetadata];
-[_UIGestureStudyInteraction setEventMetadata:];
-[_UIGestureStudyInteraction view];
-[_UIGestureStudyInteraction setDelegate:];
-[_UIGestureStudyInteraction willMoveToView:];
-[_UIGestureStudyInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIGestureStudyInteraction delegate];
-[_UIGestureStudyInteraction didMoveToView:];
-[_UIGestureStudyInteraction _baseMetadataForTriggeredParticipant:];
-[_UIGestureStudyInteraction _handleMetricsEvent:];
-[_UIGestureStudyInteraction _interactionDidTrigger:];
-[_UIGestureStudyInteraction _numberOfActiveTouches];
-[_UIGestureStudyInteraction _reportEventForTriggeredParticipant:];
-[_UIGestureStudyInteraction _viewRegionForTriggeredParticipant:];
-[_UIGestureStudyInteraction forceClickInteraction];
-[_UIGestureStudyInteraction longPressClickInteraction];
-[_UIGestureStudyInteraction metricsGestureRecognizer];
-[_UIGestureStudyInteraction setForceClickInteraction:];
-[_UIGestureStudyInteraction setLongPressClickInteraction:];
-[_UIGestureStudyInteraction setMetricsGestureRecognizer:];
```
