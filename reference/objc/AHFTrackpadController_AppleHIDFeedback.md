# `AHFTrackpadController`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`](../userland/System__Library__PrivateFrameworks__AppleHIDFeedback.framework__AppleHIDFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
Q _prevTimestampUs;
@"HIDEventSystemClient" _trackpadClient;
@"NSMutableDictionary" _availableTrackpads;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_prevTimestampUs) prevTimestampUs;
@property (T@"HIDEventSystemClient",&,N,V_trackpadClient) trackpadClient;
@property (T@"NSMutableDictionary",&,N,V_availableTrackpads) availableTrackpads;
```

## Instance methods

```
-[AHFTrackpadController init];
-[AHFTrackpadController dealloc];
-[AHFTrackpadController queue];
-[AHFTrackpadController setQueue:];
-[AHFTrackpadController prevTimestampUs];
-[AHFTrackpadController allPatterns];
-[AHFTrackpadController availableTrackpads];
-[AHFTrackpadController getActuationIdForPattern:];
-[AHFTrackpadController initializeTrackpadSystem];
-[AHFTrackpadController playFeedback:accessoryID:timestamp:error:];
-[AHFTrackpadController playFeedback:senderID:timestamp:error:];
-[AHFTrackpadController playFeedbackGated:client:timestamp:error:];
-[AHFTrackpadController setAvailableTrackpads:];
-[AHFTrackpadController setPrevTimestampUs:];
-[AHFTrackpadController setTrackpadClient:];
-[AHFTrackpadController trackpadClient];
```
