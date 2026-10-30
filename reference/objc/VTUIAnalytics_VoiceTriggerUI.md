# `VTUIAnalytics`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
i _introViewShown;
i _aboutViewShown;
i _skippedFromIntroAOP;
i _skippedFromIntroNonAOP;
i _turnOnSiriNonAOP;
i _voiceTrainingCancelled;
i _voiceTrainingCancelledStep;
i _voiceTrainingCompleted;
i _voiceTrainingStarted;
i _asrError;
i _vtError;
@"NSString" _languageCode;
@"NSString" _setupMode;
```

## Properties

```
@property (Ti,N,V_introViewShown) introViewShown;
@property (Ti,N,V_aboutViewShown) aboutViewShown;
@property (Ti,N,V_skippedFromIntroAOP) skippedFromIntroAOP;
@property (Ti,N,V_skippedFromIntroNonAOP) skippedFromIntroNonAOP;
@property (Ti,N,V_turnOnSiriNonAOP) turnOnSiriNonAOP;
@property (Ti,N,V_voiceTrainingCancelled) voiceTrainingCancelled;
@property (Ti,N,V_voiceTrainingCancelledStep) voiceTrainingCancelledStep;
@property (Ti,N,V_voiceTrainingCompleted) voiceTrainingCompleted;
@property (Ti,N,V_voiceTrainingStarted) voiceTrainingStarted;
@property (Ti,N,V_asrError) asrError;
@property (Ti,N,V_vtError) vtError;
@property (T@"NSString",&,N,V_languageCode) languageCode;
@property (T@"NSString",&,N,V_setupMode) setupMode;
```

## Instance methods

```
-[VTUIAnalytics languageCode];
-[VTUIAnalytics logEvent];
-[VTUIAnalytics setLanguageCode:];
-[VTUIAnalytics setSetupMode:];
-[VTUIAnalytics setupMode];
-[VTUIAnalytics vtError];
-[VTUIAnalytics aboutViewShown];
-[VTUIAnalytics asrError];
-[VTUIAnalytics introViewShown];
-[VTUIAnalytics setAboutViewShown:];
-[VTUIAnalytics setAsrError:];
-[VTUIAnalytics setIntroViewShown:];
-[VTUIAnalytics setSkippedFromIntroAOP:];
-[VTUIAnalytics setSkippedFromIntroNonAOP:];
-[VTUIAnalytics setTurnOnSiriNonAOP:];
-[VTUIAnalytics setVoiceTrainingCancelled:];
-[VTUIAnalytics setVoiceTrainingCancelledStep:];
-[VTUIAnalytics setVoiceTrainingCompleted:];
-[VTUIAnalytics setVoiceTrainingStarted:];
-[VTUIAnalytics setVtError:];
-[VTUIAnalytics skippedFromIntroAOP];
-[VTUIAnalytics skippedFromIntroNonAOP];
-[VTUIAnalytics turnOnSiriNonAOP];
-[VTUIAnalytics voiceTrainingCancelled];
-[VTUIAnalytics voiceTrainingCancelledStep];
-[VTUIAnalytics voiceTrainingCompleted];
-[VTUIAnalytics voiceTrainingStarted];
```
