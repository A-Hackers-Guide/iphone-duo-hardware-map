# `VTAnalyzerNDAPI`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 53 instance methods, 0 class methods

## Instance variables

```
^v _novDetect;
@"NSDictionary" _decodedInfo;
```

## Instance methods

```
-[VTAnalyzerNDAPI dealloc];
-[VTAnalyzerNDAPI reset];
-[VTAnalyzerNDAPI getSuperVectorWithEndPoint:];
-[VTAnalyzerNDAPI initWithConfigPath:resourcePath:];
-[VTAnalyzerNDAPI resetBest];
-[VTAnalyzerNDAPI getThresholdSAT];
-[VTAnalyzerNDAPI _decodeJson:];
-[VTAnalyzerNDAPI _getBooleanValueFromConfigurationName:defaultTo:];
-[VTAnalyzerNDAPI _getFloatValueFromConfigurationName:defaultTo:];
-[VTAnalyzerNDAPI _getIntValueFromConfigurationName:defaultTo:];
-[VTAnalyzerNDAPI _getNumberForKey:category:default:];
-[VTAnalyzerNDAPI _getOptionValueFromConfigurationName:];
-[VTAnalyzerNDAPI _getStringValueFromConfigurationName:defaultTo:];
-[VTAnalyzerNDAPI analyzeSAT:size:];
-[VTAnalyzerNDAPI analyzeWavData:length:];
-[VTAnalyzerNDAPI deleteVectorIndex:];
-[VTAnalyzerNDAPI getAnalyzedResult];
-[VTAnalyzerNDAPI getAnalyzedResult:];
-[VTAnalyzerNDAPI getCombinedLoggingThreshold];
-[VTAnalyzerNDAPI getCombinedSecondChanceThreshold];
-[VTAnalyzerNDAPI getCombinedTriggerThreshold];
-[VTAnalyzerNDAPI getDoSAT];
-[VTAnalyzerNDAPI getDoSupervectorSecondaryTest];
-[VTAnalyzerNDAPI getExtraSamplesAtStart];
-[VTAnalyzerNDAPI getMaximumSpeakerVectors];
-[VTAnalyzerNDAPI getNDAPILoggingThreshold];
-[VTAnalyzerNDAPI getNDAPISecondChanceThreshold];
-[VTAnalyzerNDAPI getNDAPITriggerThreshold];
-[VTAnalyzerNDAPI getPayloadUtteranceLifeTimeInDays];
-[VTAnalyzerNDAPI getRecognizerConfig];
-[VTAnalyzerNDAPI getRecognizerScoreScaleFactor];
-[VTAnalyzerNDAPI getRecognizerThresholdOffset];
-[VTAnalyzerNDAPI getRecognizerWaitTime];
-[VTAnalyzerNDAPI getRetrainExplicitUttThresholdSAT];
-[VTAnalyzerNDAPI getRetrainExplicitUttThresholdTDSR];
-[VTAnalyzerNDAPI getRetrainNumExplicitUtt];
-[VTAnalyzerNDAPI getRetrainNumImplicitUtt];
-[VTAnalyzerNDAPI getRetrainSamplingPolicy];
-[VTAnalyzerNDAPI getRetrainThresholdSAT];
-[VTAnalyzerNDAPI getRetrainThresholdTDSR];
-[VTAnalyzerNDAPI getRetrainThresholdTrigger];
-[VTAnalyzerNDAPI getSATVectorCount];
-[VTAnalyzerNDAPI getScoreSuperVector:size:];
-[VTAnalyzerNDAPI getSecondPassTrailingTime];
-[VTAnalyzerNDAPI getThresholdPresuperVector];
-[VTAnalyzerNDAPI getTriggerTokens];
-[VTAnalyzerNDAPI getUseFallbackThresholdUponTimeout];
-[VTAnalyzerNDAPI getUseKeywordSpotting];
-[VTAnalyzerNDAPI getUseRecognizer];
-[VTAnalyzerNDAPI getVoiceProfilePruningCookie];
-[VTAnalyzerNDAPI getVoiceProfilePruningNumRetentionUtterances];
-[VTAnalyzerNDAPI initializeSAT:];
-[VTAnalyzerNDAPI updateSAT];
```
