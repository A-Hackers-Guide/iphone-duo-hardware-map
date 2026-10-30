# `_UISelectionFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 8 instance variables, 8 properties, 22 instance methods, 5 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _feedback;
d _minimumInterval;
@"NSString" _hidFeedbackPatternName;
d _maxSpeed;
d _slowAudioVolume;
d _fastAudioVolume;
d _slowHapticVolume;
d _fastHapticVolume;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_feedback) feedback;
@property (Td,N,V_minimumInterval) minimumInterval;
@property (T@"NSString",&,N,V_hidFeedbackPatternName) hidFeedbackPatternName;
@property (Td,N,V_maxSpeed) maxSpeed;
@property (Td,N,V_slowAudioVolume) slowAudioVolume;
@property (Td,N,V_fastAudioVolume) fastAudioVolume;
@property (Td,N,V_slowHapticVolume) slowHapticVolume;
@property (Td,N,V_fastHapticVolume) fastHapticVolume;
```

## Class methods

```
+[_UISelectionFeedbackGeneratorConfiguration pickerConfiguration];
+[_UISelectionFeedbackGeneratorConfiguration lightConfiguration];
+[_UISelectionFeedbackGeneratorConfiguration strongConfiguration];
+[_UISelectionFeedbackGeneratorConfiguration defaultConfiguration];
+[_UISelectionFeedbackGeneratorConfiguration pageControlConfiguration];
```

## Instance methods

```
-[_UISelectionFeedbackGeneratorConfiguration feedback];
-[_UISelectionFeedbackGeneratorConfiguration setFeedback:];
-[_UISelectionFeedbackGeneratorConfiguration setFastAudioVolume:];
-[_UISelectionFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UISelectionFeedbackGeneratorConfiguration requiredPeripheralSupportLevel];
-[_UISelectionFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UISelectionFeedbackGeneratorConfiguration slowHapticVolume];
-[_UISelectionFeedbackGeneratorConfiguration setHidFeedbackPatternName:];
-[_UISelectionFeedbackGeneratorConfiguration setMinimumInterval:];
-[_UISelectionFeedbackGeneratorConfiguration fastHapticVolume];
-[_UISelectionFeedbackGeneratorConfiguration setFastHapticVolume:];
-[_UISelectionFeedbackGeneratorConfiguration setMaxSpeed:];
-[_UISelectionFeedbackGeneratorConfiguration slowAudioVolume];
-[_UISelectionFeedbackGeneratorConfiguration maxSpeed];
-[_UISelectionFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UISelectionFeedbackGeneratorConfiguration setSlowAudioVolume:];
-[_UISelectionFeedbackGeneratorConfiguration hidFeedbackPatternName];
-[_UISelectionFeedbackGeneratorConfiguration copyWithZone:];
-[_UISelectionFeedbackGeneratorConfiguration isEqual:];
-[_UISelectionFeedbackGeneratorConfiguration minimumInterval];
-[_UISelectionFeedbackGeneratorConfiguration fastAudioVolume];
-[_UISelectionFeedbackGeneratorConfiguration setSlowHapticVolume:];
```
