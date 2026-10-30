# `_UIKeyboardFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _scalingForSpeedEnabled;
@"NSDictionary" _feedbacks;
d _slowTypingTime;
d _fastTypingTime;
d _fastTypingVolumeMultiplier;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_feedbacks) feedbacks;
@property (Td,N,V_slowTypingTime) slowTypingTime;
@property (Td,N,V_fastTypingTime) fastTypingTime;
@property (Td,N,V_fastTypingVolumeMultiplier) fastTypingVolumeMultiplier;
@property (TB,N,V_scalingForSpeedEnabled) scalingForSpeedEnabled;
```

## Class methods

```
+[_UIKeyboardFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIKeyboardFeedbackGeneratorConfiguration feedbacks];
-[_UIKeyboardFeedbackGeneratorConfiguration setFeedbacks:];
-[_UIKeyboardFeedbackGeneratorConfiguration fastTypingVolumeMultiplier];
-[_UIKeyboardFeedbackGeneratorConfiguration setFastTypingVolumeMultiplier:];
-[_UIKeyboardFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIKeyboardFeedbackGeneratorConfiguration scalingForSpeedEnabled];
-[_UIKeyboardFeedbackGeneratorConfiguration setFastTypingTime:];
-[_UIKeyboardFeedbackGeneratorConfiguration defaultEnabled];
-[_UIKeyboardFeedbackGeneratorConfiguration setSlowTypingTime:];
-[_UIKeyboardFeedbackGeneratorConfiguration slowTypingTime];
-[_UIKeyboardFeedbackGeneratorConfiguration setScalingForSpeedEnabled:];
-[_UIKeyboardFeedbackGeneratorConfiguration fastTypingTime];
```
