# `VTPhraseConfig`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 15 instance methods, 0 class methods

## Instance variables

```
f _threshold;
f _secondChanceThreshold;
f _loggingThreshold;
f _ndapiScaleFactor;
f _recognizerScoreOffset;
f _recognizerScoreScaleFactor;
f _twoShotFeedbackDelay;
f _remoraTwoShotFeedbackDelay;
f _keywordRejectLoggingThreshold;
f _speakerRejectLoggingThreshold;
f _preTriggerSilenceOffset;
@"NSString" _name;
@"NSString" _recognizerToken;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (Tf,R,N,V_threshold) threshold;
@property (Tf,R,N,V_secondChanceThreshold) secondChanceThreshold;
@property (Tf,R,N,V_loggingThreshold) loggingThreshold;
@property (Tf,R,N,V_ndapiScaleFactor) ndapiScaleFactor;
@property (Tf,R,N,V_recognizerScoreOffset) recognizerScoreOffset;
@property (Tf,R,N,V_recognizerScoreScaleFactor) recognizerScoreScaleFactor;
@property (T@"NSString",R,N,V_recognizerToken) recognizerToken;
@property (Tf,R,N,V_twoShotFeedbackDelay) twoShotFeedbackDelay;
@property (Tf,R,N,V_remoraTwoShotFeedbackDelay) remoraTwoShotFeedbackDelay;
@property (Tf,R,N,V_keywordRejectLoggingThreshold) keywordRejectLoggingThreshold;
@property (Tf,R,N,V_speakerRejectLoggingThreshold) speakerRejectLoggingThreshold;
@property (Tf,R,N,V_preTriggerSilenceOffset) preTriggerSilenceOffset;
```

## Instance methods

```
-[VTPhraseConfig threshold];
-[VTPhraseConfig loggingThreshold];
-[VTPhraseConfig twoShotFeedbackDelay];
-[VTPhraseConfig name];
-[VTPhraseConfig recognizerToken];
-[VTPhraseConfig copyWithThreshold:secondChanceThreshold:loggingThreshold:ndapiScaleFactor:recognizerScoreOffset:recognizerScoreScaleFactor:keywordRejectLoggingThreshold:];
-[VTPhraseConfig initWithName:threshold:secondChanceThreshold:loggingThreshold:ndapiScaleFactor:recognizerScoreOffset:recognizerScoreScaleFactor:recognizerToken:twoShotFeedbackDelay:remoraTwoShotFeedbackDelay:keywordRejectLoggingThreshold:speakerRejectLoggingThreshold:preTriggerSilenceOffset:];
-[VTPhraseConfig keywordRejectLoggingThreshold];
-[VTPhraseConfig ndapiScaleFactor];
-[VTPhraseConfig preTriggerSilenceOffset];
-[VTPhraseConfig recognizerScoreOffset];
-[VTPhraseConfig recognizerScoreScaleFactor];
-[VTPhraseConfig remoraTwoShotFeedbackDelay];
-[VTPhraseConfig secondChanceThreshold];
-[VTPhraseConfig speakerRejectLoggingThreshold];
```
