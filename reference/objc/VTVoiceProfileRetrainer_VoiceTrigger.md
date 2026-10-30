# `VTVoiceProfileRetrainer`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTTextDependentSpeakerRecognizerDelegate`
- 14 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
d _retrainThresholdTrigger;
d _retrainExplicitUttThresholdSAT;
d _retrainExplicitUttThresholdTDSR;
d _retrainThresholdSAT;
d _retrainThresholdTDSR;
d _retrainTDSRScore;
Q _numRetentionUtterances;
@"VTAnalyzerNDAPI" _analyzer;
@"NSString" _languageCode;
Q _modelType;
@"NSString" _configPath;
@"NSString" _resourcePath;
@"VTTextDependentSpeakerRecognizer" _satRetrainingTdSr;
@"NSObject<OS_dispatch_semaphore>" _satRetrainingTdSrSemaphore;
```

## Properties

```
@property (T@"VTAnalyzerNDAPI",&,N,V_analyzer) analyzer;
@property (T@"NSString",&,N,V_languageCode) languageCode;
@property (TQ,N,V_modelType) modelType;
@property (T@"NSString",&,N,V_configPath) configPath;
@property (T@"NSString",&,N,V_resourcePath) resourcePath;
@property (T@"VTTextDependentSpeakerRecognizer",&,N,V_satRetrainingTdSr) satRetrainingTdSr;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_satRetrainingTdSrSemaphore) satRetrainingTdSrSemaphore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTVoiceProfileRetrainer dealloc];
-[VTVoiceProfileRetrainer setAnalyzer:];
-[VTVoiceProfileRetrainer languageCode];
-[VTVoiceProfileRetrainer resourcePath];
-[VTVoiceProfileRetrainer modelType];
-[VTVoiceProfileRetrainer setResourcePath:];
-[VTVoiceProfileRetrainer analyzer];
-[VTVoiceProfileRetrainer setModelType:];
-[VTVoiceProfileRetrainer setLanguageCode:];
-[VTVoiceProfileRetrainer configPath];
-[VTVoiceProfileRetrainer setConfigPath:];
-[VTVoiceProfileRetrainer _analyzeEnrollmentUtts:thresholdTrigger:thresholdSAT:thresholdTDSR:isUpdatingModel:extraUtts:discardUtts:psrTimeout:];
-[VTVoiceProfileRetrainer _computeSamplingMSEForUtts:withBeforeScores:];
-[VTVoiceProfileRetrainer _deleteUtterances:];
-[VTVoiceProfileRetrainer _getLastPruningCookie];
-[VTVoiceProfileRetrainer _updatePruningCookie:];
-[VTVoiceProfileRetrainer initWithAnalyzer:languageCode:modelType:configPath:resourcePath:];
-[VTVoiceProfileRetrainer pruneVoiceProfileIfNecessary];
-[VTVoiceProfileRetrainer retrainSATModelWithCompletion:];
-[VTVoiceProfileRetrainer satRetrainingTdSr];
-[VTVoiceProfileRetrainer satRetrainingTdSrSemaphore];
-[VTVoiceProfileRetrainer setSatRetrainingTdSr:];
-[VTVoiceProfileRetrainer setSatRetrainingTdSrSemaphore:];
-[VTVoiceProfileRetrainer textDependentSpeakerRecognizer:failedWithError:];
-[VTVoiceProfileRetrainer textDependentSpeakerRecognizer:hasSatScore:];
```
