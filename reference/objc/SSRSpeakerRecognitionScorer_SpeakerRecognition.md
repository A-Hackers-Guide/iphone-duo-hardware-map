# `SSRSpeakerRecognitionScorer`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 37 instance methods, 1 class methods

## Instance variables

```
^v _novDetect;
Q _offsetsType;
B _satModelAvailable;
@"NSString" _profileID;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"NSURL" _modelFilePath;
```

## Properties

```
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSURL",&,N,V_modelFilePath) modelFilePath;
@property (T@"NSString",R,N,V_profileID) profileID;
@property (T@"NSString",R,N) sysConfigRoot;
@property (T@"NSString",R,N) psrConfigFilePath;
@property (T@"NSString",R,N) psrConfigRoot;
@property (TB,R,N,V_satModelAvailable) satModelAvailable;
```

## Class methods

```
+[SSRSpeakerRecognitionScorer createVoiceScorersWithVoiceProfiles:withConfigFile:withResourceFile:withOffsetsType:forRetraining:];
```

## Instance methods

```
-[SSRSpeakerRecognitionScorer dealloc];
-[SSRSpeakerRecognitionScorer profileID];
-[SSRSpeakerRecognitionScorer modelFilePath];
-[SSRSpeakerRecognitionScorer setModelFilePath:];
-[SSRSpeakerRecognitionScorer resetForNewRequest];
-[SSRSpeakerRecognitionScorer _getFloatValueForNDAPIConfigOption:defaultValue:];
-[SSRSpeakerRecognitionScorer _getFloatValueFromConfigurationName:defaultTo:];
-[SSRSpeakerRecognitionScorer _getIntValueFromConfigurationName:defaultTo:];
-[SSRSpeakerRecognitionScorer _getOptionValueFromConfigurationName:];
-[SSRSpeakerRecognitionScorer _getStringValueFromConfigurationName:defaultTo:];
-[SSRSpeakerRecognitionScorer _getValueForNDAPIConfigOption:];
-[SSRSpeakerRecognitionScorer deleteVectorAtIndex:];
-[SSRSpeakerRecognitionScorer getSATVectorCount];
-[SSRSpeakerRecognitionScorer updateSAT];
-[SSRSpeakerRecognitionScorer _satLogitCeilScore];
-[SSRSpeakerRecognitionScorer _satLogitFloorScore];
-[SSRSpeakerRecognitionScorer _satScoreNonVTOffset];
-[SSRSpeakerRecognitionScorer _satScoreNonVTScale];
-[SSRSpeakerRecognitionScorer _satScoreVTOffset];
-[SSRSpeakerRecognitionScorer _satScoreVTScale];
-[SSRSpeakerRecognitionScorer analyzeSpeakerVector:withDimensions:withThresholdType:];
-[SSRSpeakerRecognitionScorer analyzeSuperVector:withDimensions:withThresholdType:];
-[SSRSpeakerRecognitionScorer configFilePath];
-[SSRSpeakerRecognitionScorer getInSpeakerConfusionScores];
-[SSRSpeakerRecognitionScorer getSpeakerVectorAtIndex:];
-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:config:memoryIndex:withOffsetsType:forRetraining:];
-[SSRSpeakerRecognitionScorer initWithProfileID:withModelFile:withConfigFile:withResourceFile:withOffsetsType:forRetraining:];
-[SSRSpeakerRecognitionScorer normalizedScoreFromRawScore:forScoreType:];
-[SSRSpeakerRecognitionScorer psrConfigFilePath];
-[SSRSpeakerRecognitionScorer psrConfigRoot];
-[SSRSpeakerRecognitionScorer resetScorerWithModelFilePath:];
-[SSRSpeakerRecognitionScorer resourceFilePath];
-[SSRSpeakerRecognitionScorer satModelAvailable];
-[SSRSpeakerRecognitionScorer scoreSpeakerVector:withDimensions:withThresholdType:];
-[SSRSpeakerRecognitionScorer setConfigFilePath:];
-[SSRSpeakerRecognitionScorer setResourceFilePath:];
-[SSRSpeakerRecognitionScorer sysConfigRoot];
```
