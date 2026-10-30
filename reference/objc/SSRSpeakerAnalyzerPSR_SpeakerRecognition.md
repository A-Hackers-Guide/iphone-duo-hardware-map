# `SSRSpeakerAnalyzerPSR`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EARSyncPSRAudioProcessorDelegate`
- 10 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _triggerPhraseDetectedOnTap;
Q _numSamplesProecssed;
@"<SSRSpeakerAnalyzerPSRDelegate>" _delegate;
@"EARSyncPSRAudioProcessor" _psrAudioProcessor;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"SSRSpeakerRecognitionContext" _context;
@"NSDictionary" _voiceProfilesModelFilePaths;
@"NSDictionary" _voiceProfilesExpModelFilePaths;
@"NSArray" _psrScorers;
```

## Properties

```
@property (T@"<SSRSpeakerAnalyzerPSRDelegate>",W,N,V_delegate) delegate;
@property (T@"EARSyncPSRAudioProcessor",&,N,V_psrAudioProcessor) psrAudioProcessor;
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"SSRSpeakerRecognitionContext",&,N,V_context) context;
@property (T@"NSDictionary",&,N,V_voiceProfilesModelFilePaths) voiceProfilesModelFilePaths;
@property (T@"NSDictionary",&,N,V_voiceProfilesExpModelFilePaths) voiceProfilesExpModelFilePaths;
@property (T@"NSArray",&,N,V_psrScorers) psrScorers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerAnalyzerPSR dealloc];
-[SSRSpeakerAnalyzerPSR setDelegate:];
-[SSRSpeakerAnalyzerPSR setContext:];
-[SSRSpeakerAnalyzerPSR delegate];
-[SSRSpeakerAnalyzerPSR context];
-[SSRSpeakerAnalyzerPSR endAudio];
-[SSRSpeakerAnalyzerPSR psrAudioProcessor:finishedWithFinalSpeakerVector:speakerVectorSize:processedAudioDurationMs:];
-[SSRSpeakerAnalyzerPSR psrAudioProcessor:hasSpeakerVector:speakerVectorSize:processedAudioDurationMs:];
-[SSRSpeakerAnalyzerPSR resetForNewRequest];
-[SSRSpeakerAnalyzerPSR psrAudioProcessor];
-[SSRSpeakerAnalyzerPSR setPsrAudioProcessor:];
-[SSRSpeakerAnalyzerPSR setVoiceProfilesModelFilePaths:];
-[SSRSpeakerAnalyzerPSR _isSpeakerVectorValid:speakerVectorSize:fromPsrAudioProcessor:];
-[SSRSpeakerAnalyzerPSR _processSpeakerVector:withSize:processedAudioDurationMs:];
-[SSRSpeakerAnalyzerPSR configFilePath];
-[SSRSpeakerAnalyzerPSR getEARSyncPSRAudioProcessorProcessingTime];
-[SSRSpeakerAnalyzerPSR getVoiceRecognizerResults];
-[SSRSpeakerAnalyzerPSR initWithVoiceRecognitionContext:delegate:];
-[SSRSpeakerAnalyzerPSR processAudioData:];
-[SSRSpeakerAnalyzerPSR psrScorers];
-[SSRSpeakerAnalyzerPSR resourceFilePath];
-[SSRSpeakerAnalyzerPSR setConfigFilePath:];
-[SSRSpeakerAnalyzerPSR setPsrScorers:];
-[SSRSpeakerAnalyzerPSR setResourceFilePath:];
-[SSRSpeakerAnalyzerPSR setVoiceProfilesExpModelFilePaths:];
-[SSRSpeakerAnalyzerPSR voiceProfilesExpModelFilePaths];
-[SSRSpeakerAnalyzerPSR voiceProfilesModelFilePaths];
```
