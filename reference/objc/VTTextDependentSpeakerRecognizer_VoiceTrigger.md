# `VTTextDependentSpeakerRecognizer`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EARPSRAudioProcessorDelegate`
- 15 instance variables, 19 properties, 44 instance methods, 3 class methods

## Instance variables

```
^v _novDetect;
B _isTdPsrAbleToProcess;
f _lastRequestSatScore;
@"NSString" _tdSATModelFilePath;
@"EARPSRAudioProcessor" _speakerVectorGenerator;
@"<VTTextDependentSpeakerRecognizerDelegate>" _delegate;
@"NSString" _resourcePath;
@"NSString" _satDirectory;
@"NSString" _tdSATModelDirPath;
@"NSString" _assetHash;
@"NSData" _speakerVector;
Q _numSamplesProecssed;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _stateSerialQueue;
@"NSMutableData" _psrAudioDataForLogging;
```

## Properties

```
@property (T@"EARPSRAudioProcessor",&,N,V_speakerVectorGenerator) speakerVectorGenerator;
@property (T@"<VTTextDependentSpeakerRecognizerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_resourcePath) resourcePath;
@property (T@"NSString",&,N,V_satDirectory) satDirectory;
@property (T@"NSString",&,N,V_tdSATModelDirPath) tdSATModelDirPath;
@property (T@"NSString",&,N,V_assetHash) assetHash;
@property (T@"NSString",&,N,V_tdSATModelFilePath) tdSATModelFilePath;
@property (TB,N,V_isTdPsrAbleToProcess) tdPsrCanProcessRequest;
@property (Tf,N,V_lastRequestSatScore) lastRequestSatScore;
@property (T@"NSData",&,N,V_speakerVector) speakerVector;
@property (TQ,N,V_numSamplesProecssed) numSamplesProecssed;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_stateSerialQueue) stateSerialQueue;
@property (T@"NSMutableData",&,N,V_psrAudioDataForLogging) psrAudioDataForLogging;
@property (Tq,R,N) getSATVectorCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTTextDependentSpeakerRecognizer errorWithCode:message:];
+[VTTextDependentSpeakerRecognizer _createDirectoryIfDoesNotExist:];
+[VTTextDependentSpeakerRecognizer psrTdAssetExistsAtResourcePath:];
```

## Instance methods

```
-[VTTextDependentSpeakerRecognizer dealloc];
-[VTTextDependentSpeakerRecognizer queue];
-[VTTextDependentSpeakerRecognizer setDelegate:];
-[VTTextDependentSpeakerRecognizer resourcePath];
-[VTTextDependentSpeakerRecognizer delegate];
-[VTTextDependentSpeakerRecognizer setResourcePath:];
-[VTTextDependentSpeakerRecognizer setQueue:];
-[VTTextDependentSpeakerRecognizer assetHash];
-[VTTextDependentSpeakerRecognizer endAudio];
-[VTTextDependentSpeakerRecognizer psrAudioProcessor:hasResult:numElements:];
-[VTTextDependentSpeakerRecognizer resetForNewRequest];
-[VTTextDependentSpeakerRecognizer getThresholdSAT];
-[VTTextDependentSpeakerRecognizer _getFloatValueForNDAPIConfigOption:defaultValue:];
-[VTTextDependentSpeakerRecognizer _getSATVectorCount];
-[VTTextDependentSpeakerRecognizer _getValueForNDAPIConfigOption:];
-[VTTextDependentSpeakerRecognizer deleteExistingSATModel];
-[VTTextDependentSpeakerRecognizer deleteVectorAtIndex:];
-[VTTextDependentSpeakerRecognizer getCombinationWeight];
-[VTTextDependentSpeakerRecognizer getSATVectorCount];
-[VTTextDependentSpeakerRecognizer initWithResourcePath:satDirectory:assetHash:shouldCreateModelDir:delegate:];
-[VTTextDependentSpeakerRecognizer lastRequestSatScore];
-[VTTextDependentSpeakerRecognizer logWithAudioFilepath:];
-[VTTextDependentSpeakerRecognizer numSamplesProecssed];
-[VTTextDependentSpeakerRecognizer processAudio:numSamples:];
-[VTTextDependentSpeakerRecognizer psrAudioDataForLogging];
-[VTTextDependentSpeakerRecognizer satDirectory];
-[VTTextDependentSpeakerRecognizer setAssetHash:];
-[VTTextDependentSpeakerRecognizer setLastRequestSatScore:];
-[VTTextDependentSpeakerRecognizer setNumSamplesProecssed:];
-[VTTextDependentSpeakerRecognizer setPsrAudioDataForLogging:];
-[VTTextDependentSpeakerRecognizer setSatDirectory:];
-[VTTextDependentSpeakerRecognizer setSpeakerVector:];
-[VTTextDependentSpeakerRecognizer setSpeakerVectorGenerator:];
-[VTTextDependentSpeakerRecognizer setStateSerialQueue:];
-[VTTextDependentSpeakerRecognizer setTdPsrCanProcessRequest:];
-[VTTextDependentSpeakerRecognizer setTdSATModelDirPath:];
-[VTTextDependentSpeakerRecognizer setTdSATModelFilePath:];
-[VTTextDependentSpeakerRecognizer speakerVector];
-[VTTextDependentSpeakerRecognizer speakerVectorGenerator];
-[VTTextDependentSpeakerRecognizer stateSerialQueue];
-[VTTextDependentSpeakerRecognizer tdPsrCanProcessRequest];
-[VTTextDependentSpeakerRecognizer tdSATModelDirPath];
-[VTTextDependentSpeakerRecognizer tdSATModelFilePath];
-[VTTextDependentSpeakerRecognizer updateSAT];
```
