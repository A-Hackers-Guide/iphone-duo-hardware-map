# `AHFPencilController`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`](../userland/System__Library__PrivateFrameworks__AppleHIDFeedback.framework__AppleHIDFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
I _availablePencilHaptics;
@"AHFPencilPatternLibrary" _patternsLibrary;
@"NSObject<OS_dispatch_queue>" _queue;
Q _prevTimestampUs;
@"HIDEventSystemClient" _digitizerStylusClient;
@"NSMutableSet" _availableDigitizerStylus;
@"HIDEventSystemClient" _opaqueTouchClient;
@"NSMutableSet" _availableOpaqueTouch;
@"HIDEventSystemClient" _pencilHapticsClient;
```

## Properties

```
@property (T@"AHFPencilPatternLibrary",&,N,V_patternsLibrary) patternsLibrary;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_prevTimestampUs) prevTimestampUs;
@property (T@"HIDEventSystemClient",&,N,V_digitizerStylusClient) digitizerStylusClient;
@property (T@"NSMutableSet",&,N,V_availableDigitizerStylus) availableDigitizerStylus;
@property (T@"HIDEventSystemClient",&,N,V_opaqueTouchClient) opaqueTouchClient;
@property (T@"NSMutableSet",&,N,V_availableOpaqueTouch) availableOpaqueTouch;
@property (T@"HIDEventSystemClient",&,N,V_pencilHapticsClient) pencilHapticsClient;
@property (TI,N,V_availablePencilHaptics) availablePencilHaptics;
```

## Instance methods

```
-[AHFPencilController init];
-[AHFPencilController dealloc];
-[AHFPencilController queue];
-[AHFPencilController setQueue:];
-[AHFPencilController patternsLibrary];
-[AHFPencilController initializeDigitizerStylusSystem];
-[AHFPencilController prevTimestampUs];
-[AHFPencilController availableDigitizerStylus];
-[AHFPencilController availableOpaqueTouch];
-[AHFPencilController availablePencilHaptics];
-[AHFPencilController digitizerStylusClient];
-[AHFPencilController initializeOpaqueTouchSystem];
-[AHFPencilController initializePencilHapticsSystem];
-[AHFPencilController opaqueTouchClient];
-[AHFPencilController pencilHapticsClient];
-[AHFPencilController playFeedback:accessoryID:timestamp:error:];
-[AHFPencilController playFeedback:senderID:timestamp:error:];
-[AHFPencilController playFeedbackGated:haptics:timestamp:error:];
-[AHFPencilController setAvailableDigitizerStylus:];
-[AHFPencilController setAvailableOpaqueTouch:];
-[AHFPencilController setAvailablePencilHaptics:];
-[AHFPencilController setDigitizerStylusClient:];
-[AHFPencilController setOpaqueTouchClient:];
-[AHFPencilController setPatternsLibrary:];
-[AHFPencilController setPencilHapticsClient:];
-[AHFPencilController setPrevTimestampUs:];
```
