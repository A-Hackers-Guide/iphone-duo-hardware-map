# `SSRTriggerPhraseDetectorNDAPIResult`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isEarlyWarning;
B _isRescoring;
f _bestScore;
Q _phId;
Q _samplesFed;
Q _bestPhrase;
Q _bestStart;
Q _bestEnd;
```

## Properties

```
@property (TQ,N,V_phId) phId;
@property (TQ,N,V_samplesFed) samplesFed;
@property (TQ,N,V_bestPhrase) bestPhrase;
@property (TQ,N,V_bestStart) bestStart;
@property (TQ,N,V_bestEnd) bestEnd;
@property (Tf,N,V_bestScore) bestScore;
@property (TB,N,V_isEarlyWarning) isEarlyWarning;
@property (TB,N,V_isRescoring) isRescoring;
```

## Instance methods

```
-[SSRTriggerPhraseDetectorNDAPIResult bestScore];
-[SSRTriggerPhraseDetectorNDAPIResult setBestScore:];
-[SSRTriggerPhraseDetectorNDAPIResult bestEnd];
-[SSRTriggerPhraseDetectorNDAPIResult setIsRescoring:];
-[SSRTriggerPhraseDetectorNDAPIResult bestPhrase];
-[SSRTriggerPhraseDetectorNDAPIResult bestStart];
-[SSRTriggerPhraseDetectorNDAPIResult isEarlyWarning];
-[SSRTriggerPhraseDetectorNDAPIResult isRescoring];
-[SSRTriggerPhraseDetectorNDAPIResult phId];
-[SSRTriggerPhraseDetectorNDAPIResult samplesFed];
-[SSRTriggerPhraseDetectorNDAPIResult setBestEnd:];
-[SSRTriggerPhraseDetectorNDAPIResult setBestPhrase:];
-[SSRTriggerPhraseDetectorNDAPIResult setBestStart:];
-[SSRTriggerPhraseDetectorNDAPIResult setIsEarlyWarning:];
-[SSRTriggerPhraseDetectorNDAPIResult setPhId:];
-[SSRTriggerPhraseDetectorNDAPIResult setSamplesFed:];
```
