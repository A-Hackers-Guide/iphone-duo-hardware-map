# `SSRVTUITrainingManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSVTUITrainingSessionDelegate`, `CSVTUIAudioSessionDelegate`, `CSVTUIEndpointAnalyzerDelegate`, `SSRVTUITrainingServiceDelegate`, `SSRVTUITrainingService`
- 32 instance variables, 12 properties, 71 instance methods, 3 class methods

## Instance variables

```
B _performRMS;
@"NSString" _locale;
@"NSString" _vtAssetConfigVersion;
@"<CSVTUIAudioSession>" _audioSession;
@"CSVTUIEndpointAnalyzer" _audioAnalyzer;
@"<_TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_>" _keywordDetector;
@"NSMutableArray" _trainingSessions;
@"CSVTUITrainingSession" _currentTrainingSession;
q _sessionNumber;
B _suspendAudio;
@"NSObject<OS_dispatch_queue>" _queue;
@? _cleanupCompletion;
@"SFSpeechRecognizer" _speechRecognizer;
@"CSAsset" _currentAsset;
@"SecureAsset" _currentSecureAsset;
@"SSRVoiceProfile" _profile;
@"CSDispatchGroup" _didStopWaitingGroup;
@"NSUUID" _mhUUID;
@"CSAudioZeroCounter" _audioZeroCounter;
B _shouldTrainViaXPC;
@"SSRVTUITrainingServiceClient" _trainingServiceClient;
@"AVAudioPlayer" _audioPlayer;
@"NSMutableDictionary" _pageAttemptMap;
q _lastAttemptedUtterance;
@"<CSAudioProviderSelecting>" _audioProviderSelector;
Q _audioStartRecordingHostTime;
B _shouldUseRecordingStartHostTime;
B _speechRecognizerAvailable;
B _snrCheckEnabled;
f _rms;
@"<SSRVTUITrainingManagerDelegate>" _delegate;
@"CSPlainAudioFileWriter" _audioFileWriter;
```

## Properties

```
@property (T@"CSPlainAudioFileWriter",&,N,V_audioFileWriter) audioFileWriter;
@property (T@"SSRVoiceProfile",R) voiceProfile;
@property (Tf,V_rms) rms;
@property (T@"<SSRVTUITrainingManagerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,V_speechRecognizerAvailable) speechRecognizerAvailable;
@property (TQ,R) audioSource;
@property (TB) suspendAudio;
@property (TB,N,V_snrCheckEnabled) snrCheckEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SSRVTUITrainingManager trainingManagerWithLocaleID:withAppDomain:withSiriSharedUserId:];
+[SSRVTUITrainingManager sharedtrainingSessionQueue];
+[SSRVTUITrainingManager trainingManagerWithLocaleID:withAppDomain:];
```

## Instance methods

```
-[SSRVTUITrainingManager audioFileWriter];
-[SSRVTUITrainingManager setLocaleIdentifier:];
-[SSRVTUITrainingManager setAudioFileWriter:];
-[SSRVTUITrainingManager reset];
-[SSRVTUITrainingManager setDelegate:];
-[SSRVTUITrainingManager delegate];
-[SSRVTUITrainingManager prepareWithCompletion:];
-[SSRVTUITrainingManager audioSource];
-[SSRVTUITrainingManager setSuspendAudio:];
-[SSRVTUITrainingManager _stopAudioSession];
-[SSRVTUITrainingManager rms];
-[SSRVTUITrainingManager CSVTUITrainingSessionStopListen];
-[SSRVTUITrainingManager CSVTUIRemoteDetectedPartialTranscriptionResult:];
-[SSRVTUITrainingManager CSVTUITrainingSession:hasTrainUtterance:languageCode:payload:];
-[SSRVTUITrainingManager setRms:];
-[SSRVTUITrainingManager snrCheckEnabled];
-[SSRVTUITrainingManager stopRMS];
-[SSRVTUITrainingManager CSVTUIDetectedPartialTranscriptionResult:];
-[SSRVTUITrainingManager CSVTUIRemoteTrainingSessionRMSAvailable:];
-[SSRVTUITrainingManager CSVTUITrainingSessionRMSAvailable:];
-[SSRVTUITrainingManager _audioSource];
-[SSRVTUITrainingManager _beginOfSpeechDetected];
-[SSRVTUITrainingManager _createAudioAnalyzer];
-[SSRVTUITrainingManager _createAudioSessionRecorderWithAudioProviderSelector:];
-[SSRVTUITrainingManager _destroyAudioSession];
-[SSRVTUITrainingManager _endOfSpeechDetected];
-[SSRVTUITrainingManager _fetchCurrentAsset];
-[SSRVTUITrainingManager _fetchPreInstalledSecureAsset];
-[SSRVTUITrainingManager _getAudioToneFileName:];
-[SSRVTUITrainingManager _logSessionSummary];
-[SSRVTUITrainingManager _otaAssetsAvailable];
-[SSRVTUITrainingManager _playSoundsEffect:];
-[SSRVTUITrainingManager _resetAudioAnalyzer];
-[SSRVTUITrainingManager _secureAssetWithAssetResourcePathURL:assetFileName:];
-[SSRVTUITrainingManager _setupAudioSession];
-[SSRVTUITrainingManager _shouldShowHeadsetDisconnectionMessage];
-[SSRVTUITrainingManager _startAudioSession];
-[SSRVTUITrainingManager _trainUtteranceLocally:shouldUseASR:mhUUID:referenceString:completionWithResult:];
-[SSRVTUITrainingManager _updateAttemptForPageNumber:];
-[SSRVTUITrainingManager _validateRecordingStartHostTime:];
-[SSRVTUITrainingManager audioSessionDidStartRecording:error:];
-[SSRVTUITrainingManager audioSessionDidStopRecording:];
-[SSRVTUITrainingManager audioSessionErrorDidOccur:];
-[SSRVTUITrainingManager audioSessionRecordBufferAvailable:];
-[SSRVTUITrainingManager audioSessionUnsupportedAudioRoute];
-[SSRVTUITrainingManager cancelTrainingForID:];
-[SSRVTUITrainingManager cleanupWithCompletion:];
-[SSRVTUITrainingManager closeSessionBeforeStartWithStatus:successfully:completionWithResult:];
-[SSRVTUITrainingManager closeSessionBeforeStartWithStatus:successfully:withCompletion:];
-[SSRVTUITrainingManager createKeywordDetector];
-[SSRVTUITrainingManager createSpeechRecognizer];
-[SSRVTUITrainingManager destroySpeakerTrainer];
-[SSRVTUITrainingManager didDetectForceEndPoint];
-[SSRVTUITrainingManager endpointer:didDetectHardEndpointAtTime:];
-[SSRVTUITrainingManager endpointer:didDetectStartpointAtTime:];
-[SSRVTUITrainingManager getAudioSessionID:];
-[SSRVTUITrainingManager initWithLocaleIdentifier:withAppDomain:];
-[SSRVTUITrainingManager initWithLocaleIdentifier:withAppDomain:withSiriSharedUserId:withAudioProviderSelector:shouldTrainViaXPC:];
-[SSRVTUITrainingManager playSoundEffectWithAudioTone:];
-[SSRVTUITrainingManager playSoundsEffect:];
-[SSRVTUITrainingManager setRecordingStartHostTime:];
-[SSRVTUITrainingManager setSnrCheckEnabled:];
-[SSRVTUITrainingManager shouldPerformRMS];
-[SSRVTUITrainingManager speechRecognizerAvailable];
-[SSRVTUITrainingManager startRMS];
-[SSRVTUITrainingManager suspendAudio];
-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:];
-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:];
-[SSRVTUITrainingManager trainUtteranceWithReferenceString:completionWithResult:];
-[SSRVTUITrainingManager updateTrainingManagerForDevice:trainingDeviceUUIDList:];
-[SSRVTUITrainingManager voiceProfile];
```
