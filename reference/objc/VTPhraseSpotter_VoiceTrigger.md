# `VTPhraseSpotter`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTTextDependentSpeakerRecognizerDelegate`, `VTAssetMonitorDelegate`, `VTLanguageCodeUpdateMonitorDelegate`
- 126 instance variables, 15 properties, 88 instance methods, 2 class methods

## Instance variables

```
d _hardwareSampleRate;
@"VTAnalyzerNDAPI" _analyzer;
@"NSArray" _triggerPhrases;
@? _readyCompletion;
@? _readyForAnalyze;
i _firstUnlockAfterRebootNotificationToken;
B _isMaximized;
i _numFramesFromPreTrigger;
d _ndapiThreshold;
d _ndapiThresholdSecondChance;
d _ndapiThresholdLogNearMisses;
d _combinedThreshold;
d _combinedThresholdSecondChance;
d _combinedThresholdLogNearMisses;
d _threshold;
d _thresholdSecondChance;
d _effectiveThreshold;
B _audioLoggingEnabled;
d _thresholdLogNearMisses;
@"NSString" _audioFileDir;
B _secondPassAudioLoggingEnabled;
B _audioCaptureRequested;
@"NSString" _languageCode;
@"NSString" _configPath;
@"NSString" _configData;
@"NSString" _configLanguageCode;
@"NSString" _configVersion;
@"NSString" _resourcePath;
d _triggerThreshold;
I _extraSamplesAtStart;
d _secondPassTrailingTime;
B _isRunningSATEnrollment;
B _isRunningSATDetection;
d _thresholdSAT;
B _implicitlyTrained;
@"NSString" _lastImplicitlyTrainedAudioFile;
Q _retrainNumExplicitUtt;
Q _retrainNumImplicitUtt;
@"NSString" _retrainSamplingPolicy;
d _retrainThresholdTrigger;
d _retrainThresholdSAT;
@"VTAudioCircularBuffer" _audioBuffer;
@"NSDateFormatter" _formatter;
B _doSuperVectorSecondaryTest;
d _thresholdPreSuperVector;
B _isSuperVectorNeeded;
I _samplecount;
I _samplecountAtLastTriggerStart;
I _samplecountAtLastTriggerEnd;
I _samplecountAtRealTriggerStart;
I _sampleCountAtFirstChance;
I _lastEventEnd;
i _nearMissLogPreDelayTimer;
B _nearMissLogPending;
B _firstChanceDetected;
d _firstChanceDetectionTime;
B _isSecondChanceEffective;
d _lastUptime;
d _lastDowntime;
d _lastScore;
B _earlyDetected;
d _earlyDetectTime;
@"NSObject<OS_dispatch_queue>" _loggingQueue;
@"NSObject<OS_dispatch_queue>" _ndetectQueue;
i _heartbeatCounter;
i _languageCodeChangedNotificationToken;
@"NSObject<OS_dispatch_queue>" _assetChangedQueue;
B _registeredForPhraseSpotterNotification;
B _phraseSpotterEnabled;
B _registeredforVoiceTriggerEnabledNotification;
B _voiceTriggerEnabled;
B _phraseSpotterBypassed;
B _isSecondPass;
i _secondPassResetTimer;
B _secondPassAccepted;
d _secondPassBestScore;
B _didWakeAP;
B _secondPassTriggered;
B _secondPassStopSent;
@? _assetChangedCallback;
@"NSObject<OS_dispatch_queue>" _desQueue;
B _useRecognizer;
B _isRunningRecognizer;
B _isRecognitionResultPending;
B _firstRecognitionResultReceived;
B _useFallbackThresholdUponTimeout;
B _useKeywordSpotting;
@"NSString" _recognizerConfigName;
d _recognizerThresholdOffset;
d _recognizerWaitTime;
d _recognizerScore;
d _recognizerScoreScaleFactor;
@"NSString" _triggerTokens;
@"VTTranscriber" _transcriber;
@"VTTextDependentSpeakerRecognizer" _satDetectionTdSr;
@"NSObject<OS_dispatch_semaphore>" _satDetectionTdSrSemaphore;
d _tdSpeakerRecognizerSATThreshold;
d _lastCombinedTdSpeakerRecognizerSATScore;
d _tdSpeakerRecognizerCombinationWeight;
@"NSMutableArray" _nonceTriggerEvents;
C _lastTriggerType;
@"VTCorruptDetector" _corruptDetector;
q _triggerCount;
Q _earlyDetecFiredMachTime;
Q _triggerStartMachTime;
Q _triggerFireMachTime;
B _deviceHandheld;
d _handHeldDetectedTime;
@"NSData" _firstChanceAudioBuffer;
@"NSDictionary" _firstChanceVTEventInfo;
@"NSDate" _firstChanceTriggeredDate;
d _firstPassScore;
@"VTPhraseSpotterEnabledPolicy" _policy;
^{OpaqueAudioConverter=} _deinterleaver;
Q _numChannels;
^{AudioBufferList=I[1{AudioBuffer=II^v}]} _deinterleavedABL;
@"VTAudioFileReader" _audioFileReader;
Q _audioInjectionIndex;
@"NSString" _injectedAudioFilePath;
B _externalPhraseSpotterRunning;
@"NSDictionary" _lastVoiceTriggerEventInfo;
@"VTBiometricMatchMonitor" _biometricMonitor;
d _lastPHSRejectedTime;
d _consecutivePHSRejects;
d _lastSupervecScore;
Q _samplerate;
```

## Properties

```
@property (TQ,R,V_samplerate) samplerate;
@property (TQ,R) sampleCount;
@property (TQ,R) sampleCountAtStartOfTrigger;
@property (TQ,R) sampleCountAtEndOfTrigger;
@property (Td,R,V_lastScore) lastScore;
@property (Td,R,V_lastSupervecScore) lastSupervecScore;
@property (TC,R,V_lastTriggerType) lastTriggerType;
@property (Tq,R,V_triggerCount) triggerCount;
@property (T@"NSData",R,V_firstChanceAudioBuffer) firstChanceAudioBuffer;
@property (T@"NSDictionary",R,V_firstChanceVTEventInfo) firstChanceVTEventInfo;
@property (T@"NSDate",R,V_firstChanceTriggeredDate) firstChanceTriggeredDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTPhraseSpotter initialize];
+[VTPhraseSpotter currentSpotter];
```

## Instance methods

```
-[VTPhraseSpotter _commonInit];
-[VTPhraseSpotter init];
-[VTPhraseSpotter dealloc];
-[VTPhraseSpotter sampleCount];
-[VTPhraseSpotter _resetCounters];
-[VTPhraseSpotter getLanguageCode];
-[VTPhraseSpotter setBypass:];
-[VTPhraseSpotter assetDictionary];
-[VTPhraseSpotter _phraseSpotterEnabledDidChange];
-[VTPhraseSpotter triggerCount];
-[VTPhraseSpotter _analyzeEvents:];
-[VTPhraseSpotter getSATDirectory];
-[VTPhraseSpotter lastTriggerType];
-[VTPhraseSpotter VTAssetMonitor:didReceiveNewAssetAvailable:];
-[VTPhraseSpotter VTAudioRouteChangeMonitorDidChangeAudioRoute:];
-[VTPhraseSpotter VTLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:];
-[VTPhraseSpotter _addExtraTime:to:];
-[VTPhraseSpotter _analyzeMakeResult:eventKind:satScore:];
-[VTPhraseSpotter _analyzeResetWithOption:];
-[VTPhraseSpotter _applyExtraTime:to:];
-[VTPhraseSpotter _cancelSecondChance];
-[VTPhraseSpotter _capturePathWithPrefix:eventKind:];
-[VTPhraseSpotter _clearDeviceHandHeld];
-[VTPhraseSpotter _computeSATScore:];
-[VTPhraseSpotter _configureWithConfig:resourcePath:];
-[VTPhraseSpotter _configureWithDefaults];
-[VTPhraseSpotter _createFirstChanceMeta:];
-[VTPhraseSpotter _createVTEventInfoString:];
-[VTPhraseSpotter _firstUnlockedAndSpringBoardStarted];
-[VTPhraseSpotter _getBiometricMatchResult];
-[VTPhraseSpotter _getNumberOfAudioFilesInDirectory:];
-[VTPhraseSpotter _getSecondChanceEffective];
-[VTPhraseSpotter _handleAssetChangeForLanguageCode:];
-[VTPhraseSpotter _handleTriggerEvent:num_new_samples:satScore:];
-[VTPhraseSpotter _initDetector];
-[VTPhraseSpotter _isDeviceHandheld];
-[VTPhraseSpotter _logCorruptAudio];
-[VTPhraseSpotter _logMetaData:];
-[VTPhraseSpotter _logPrepareProperty:];
-[VTPhraseSpotter _notifyAssetChangedCallback];
-[VTPhraseSpotter _performReadyCompletion];
-[VTPhraseSpotter _randomSubset:numSelected:];
-[VTPhraseSpotter _resetVoiceTriggerDueToRTSTrigger];
-[VTPhraseSpotter _safeConfigureWithAnalyzer:path:data:resourcePath:];
-[VTPhraseSpotter _safeReconfig];
-[VTPhraseSpotter _sampleFromSortedArray:numSelected:];
-[VTPhraseSpotter _sampleLengthFrom:To:];
-[VTPhraseSpotter _setDeviceHandHeld];
-[VTPhraseSpotter _setSecondChance];
-[VTPhraseSpotter _shouldCreateAudioBuffer];
-[VTPhraseSpotter _shouldPerformRetrainingWithAnalyzerNDAPI:resourcePath:];
-[VTPhraseSpotter _storeFirstChanceAudio];
-[VTPhraseSpotter _storeTrainingAudioAndMetaInfo];
-[VTPhraseSpotter _voiceTriggerEnabledDidChange];
-[VTPhraseSpotter analyze:];
-[VTPhraseSpotter analyzeBufferList:];
-[VTPhraseSpotter clearTriggerCount];
-[VTPhraseSpotter didReceiveSiriSessionCancellation:];
-[VTPhraseSpotter didReceiveSleepGesture];
-[VTPhraseSpotter didReceiveWakeGesture];
-[VTPhraseSpotter firstChanceAudioBuffer];
-[VTPhraseSpotter firstChanceTriggeredDate];
-[VTPhraseSpotter firstChanceVTEventInfo];
-[VTPhraseSpotter getAdjustedDeviceStartTime:];
-[VTPhraseSpotter getAudioBuffer];
-[VTPhraseSpotter getCorealisRTModel];
-[VTPhraseSpotter initWithConfig:assetDir:runMode:];
-[VTPhraseSpotter initWithConfig:resourcePath:];
-[VTPhraseSpotter initWithHardwareSampleRate:];
-[VTPhraseSpotter initWithHardwareSampleRate:readyCompletion:];
-[VTPhraseSpotter initWithLanguageCodeForSATEnrollment:];
-[VTPhraseSpotter isFollowedBySpeech];
-[VTPhraseSpotter lastScore];
-[VTPhraseSpotter lastSupervecScore];
-[VTPhraseSpotter lastVoiceTriggerEventInfo];
-[VTPhraseSpotter looseTriggerThreshold];
-[VTPhraseSpotter notifyAssetChangeWithCallback:];
-[VTPhraseSpotter prepareWithProperty:readyCompletion:];
-[VTPhraseSpotter requestFoceTrigger];
-[VTPhraseSpotter requestSecondChance];
-[VTPhraseSpotter sampleCountAtEndOfTrigger];
-[VTPhraseSpotter sampleCountAtStartOfTrigger];
-[VTPhraseSpotter samplerate];
-[VTPhraseSpotter setStartSampleHostTime:];
-[VTPhraseSpotter startAudioCapture];
-[VTPhraseSpotter stopAudioCapture];
-[VTPhraseSpotter textDependentSpeakerRecognizer:failedWithError:];
-[VTPhraseSpotter textDependentSpeakerRecognizer:hasSatScore:];
```
