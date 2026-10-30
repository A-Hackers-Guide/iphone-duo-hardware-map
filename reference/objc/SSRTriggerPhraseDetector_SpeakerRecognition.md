# `SSRTriggerPhraseDetector`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _recognizerScoreScaleFactor;
@"SSRTriggerPhraseDetectorNDAPI" _detectorNDAPI;
@"SSRTriggerPhraseDetectorQuasar" _detectorQuasar;
```

## Properties

```
@property (T@"SSRTriggerPhraseDetectorNDAPI",&,N,V_detectorNDAPI) detectorNDAPI;
@property (T@"SSRTriggerPhraseDetectorQuasar",&,N,V_detectorQuasar) detectorQuasar;
@property (Tf,N,V_recognizerScoreScaleFactor) recognizerScoreScaleFactor;
```

## Class methods

```
+[SSRTriggerPhraseDetector filterVTAudioFiles:withLocale:withAsset:];
```

## Instance methods

```
-[SSRTriggerPhraseDetector recognizerScoreScaleFactor];
-[SSRTriggerPhraseDetector computeTriggerConfidenceForAudio:withCompletion:];
-[SSRTriggerPhraseDetector detectorNDAPI];
-[SSRTriggerPhraseDetector detectorQuasar];
-[SSRTriggerPhraseDetector initWithLocale:asset:];
-[SSRTriggerPhraseDetector setDetectorNDAPI:];
-[SSRTriggerPhraseDetector setDetectorQuasar:];
-[SSRTriggerPhraseDetector setRecognizerScoreScaleFactor:];
```
