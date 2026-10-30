# `PLAccessibilityAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 14 instance variables, 14 properties, 31 instance methods, 19 class methods

## Instance variables

```
@"PLCFNotificationOperatorComposition" _notificationReduceMotionChanged;
@"PLCFNotificationOperatorComposition" _notificationBackgroundContrastChanged;
@"PLCFNotificationOperatorComposition" _notificationBackTapChanged;
@"PLCFNotificationOperatorComposition" _notificationEyeTrackingChanged;
@"PLCFNotificationOperatorComposition" _notificationFacetimeCaptioningChanged;
@"PLCFNotificationOperatorComposition" _notificationMotionCuesStart;
@"PLCFNotificationOperatorComposition" _notificationMotionCuesStop;
@"PLCFNotificationOperatorComposition" _notificationSpeakSelectionChanged;
@"PLCFNotificationOperatorComposition" _notificationSpeakScreenChanged;
@"PLCFNotificationOperatorComposition" _notificationSoundRecognitionDisabled;
@"PLCFNotificationOperatorComposition" _notificationSoundRecognitionRunning;
@"PLCFNotificationOperatorComposition" _notificationSystemCaptioningChanged;
@"PLCFNotificationOperatorComposition" _notificationVoiceControlChanged;
@"PLCFNotificationOperatorComposition" _notificationZoomChanged;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationReduceMotionChanged) notificationReduceMotionChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationBackgroundContrastChanged) notificationBackgroundContrastChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationBackTapChanged) notificationBackTapChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationEyeTrackingChanged) notificationEyeTrackingChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationFacetimeCaptioningChanged) notificationFacetimeCaptioningChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationMotionCuesStart) notificationMotionCuesStart;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationMotionCuesStop) notificationMotionCuesStop;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSpeakSelectionChanged) notificationSpeakSelectionChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSpeakScreenChanged) notificationSpeakScreenChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSoundRecognitionDisabled) notificationSoundRecognitionDisabled;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSoundRecognitionRunning) notificationSoundRecognitionRunning;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSystemCaptioningChanged) notificationSystemCaptioningChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationVoiceControlChanged) notificationVoiceControlChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationZoomChanged) notificationZoomChanged;
```

## Class methods

```
+[PLAccessibilityAgent entryEventIntervalDefinitions];
+[PLAccessibilityAgent entryEventPointDefinitions];
+[PLAccessibilityAgent entryEventForwardDefinitions];
+[PLAccessibilityAgent entryEventBackwardDefinitions];
+[PLAccessibilityAgent entryEventNoneDefinitions];
+[PLAccessibilityAgent load];
+[PLAccessibilityAgent entryEventForwardNameSpeakSelection];
+[PLAccessibilityAgent entryEventForwardNameHandGestures];
+[PLAccessibilityAgent entryEventForwardNameSystemCaptioning];
+[PLAccessibilityAgent entryEventForwardNameSoundRecognition];
+[PLAccessibilityAgent entryEventForwardNameRecognition];
+[PLAccessibilityAgent entryEventForwardNameSpeakScreen];
+[PLAccessibilityAgent entryEventForwardNameReduceMotion];
+[PLAccessibilityAgent entryEventForwardNameVoiceControl];
+[PLAccessibilityAgent entryEventForwardNameBackTap];
+[PLAccessibilityAgent entryEventForwardNameFacetimeCaptioning];
+[PLAccessibilityAgent entryEventForwardNameAssistiveTouch];
+[PLAccessibilityAgent entryEventForwardNameBackgroundContrast];
+[PLAccessibilityAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLAccessibilityAgent notificationSystemCaptioningChanged];
-[PLAccessibilityAgent logEventForwardVoiceControl];
-[PLAccessibilityAgent logEventForwardMotionCues:];
-[PLAccessibilityAgent logEventForwardEyeTracking];
-[PLAccessibilityAgent logEventForwardSystemCaptioning];
-[PLAccessibilityAgent init];
-[PLAccessibilityAgent logEventForwardSpeakScreen];
-[PLAccessibilityAgent logEventForwardSpeakSelection];
-[PLAccessibilityAgent notificationMotionCuesStart];
-[PLAccessibilityAgent initOperatorDependancies];
-[PLAccessibilityAgent logEventForwardSoundRecognition:];
-[PLAccessibilityAgent logEventForwardNameRecognition:];
-[PLAccessibilityAgent notificationZoomChanged];
-[PLAccessibilityAgent logEventForwardBackgroundContrast];
-[PLAccessibilityAgent notificationEyeTrackingChanged];
-[PLAccessibilityAgent notificationFacetimeCaptioningChanged];
-[PLAccessibilityAgent logEventForwardZoom];
-[PLAccessibilityAgent notificationReduceMotionChanged];
-[PLAccessibilityAgent logEventForwardFacetimeCaptioning];
-[PLAccessibilityAgent notificationSoundRecognitionRunning];
-[PLAccessibilityAgent notificationBackTapChanged];
-[PLAccessibilityAgent logEventForwardBackTap];
-[PLAccessibilityAgent initTaskOperatorDependancies];
-[PLAccessibilityAgent logEventForwardReduceMotion];
-[PLAccessibilityAgent notificationSpeakScreenChanged];
-[PLAccessibilityAgent notificationMotionCuesStop];
-[PLAccessibilityAgent log];
-[PLAccessibilityAgent notificationSpeakSelectionChanged];
-[PLAccessibilityAgent notificationVoiceControlChanged];
-[PLAccessibilityAgent notificationBackgroundContrastChanged];
-[PLAccessibilityAgent notificationSoundRecognitionDisabled];
```
