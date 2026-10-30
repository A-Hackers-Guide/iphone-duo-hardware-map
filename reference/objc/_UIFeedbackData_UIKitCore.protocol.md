# `_UIFeedbackData` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 16 properties, 16 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) effectiveEventType;
@property (Td,R,N) effectiveDuration;
@property (Td,R,N) effectiveDelay;
@property (T@"_UIFeedbackParameters",R,N) hapticParameters;
@property (T@"_UIFeedbackParameters",R,N) audioParameters;
@property (TQ,R,N) effectiveEnabledFeedbackTypes;
@property (TI,R,N) effectiveSystemSoundID;
@property (T@"NSURL",R,N) fileURL;
@property (TQ,R,N) fileFeedbackType;
@property (T@"CHHapticPattern",R,N) pattern;
@property (T@"BKSHIDHapticFeedbackRequest",R,N) hidRequest;
@property (TB,R,N) isTransientHaptic;
@property (Tf,R,N) intensity;
@property (Tf,R,N) sharpness;
@property (TB,R,N) disableEventUseVolumeEnvelope;
@property (TB,R,N) canReuseCoreHapticsPlayer;
```

## Instance methods

```
-[_UIFeedbackData intensity];
-[_UIFeedbackData pattern];
-[_UIFeedbackData hapticParameters];
-[_UIFeedbackData effectiveSystemSoundID];
-[_UIFeedbackData fileURL];
-[_UIFeedbackData audioParameters];
-[_UIFeedbackData disableEventUseVolumeEnvelope];
-[_UIFeedbackData effectiveDuration];
-[_UIFeedbackData sharpness];
-[_UIFeedbackData effectiveEnabledFeedbackTypes];
-[_UIFeedbackData fileFeedbackType];
-[_UIFeedbackData effectiveEventType];
-[_UIFeedbackData effectiveDelay];
-[_UIFeedbackData isTransientHaptic];
-[_UIFeedbackData canReuseCoreHapticsPlayer];
-[_UIFeedbackData hidRequest];
```
