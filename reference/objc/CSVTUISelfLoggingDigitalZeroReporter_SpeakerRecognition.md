# `CSVTUISelfLoggingDigitalZeroReporter`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSDigitalZeroReporting`
- 12 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _siriSetupID;
i _pageNumber;
@"NSString" _phId;
i _maxNumContinuousZeros;
i _maxNumAllowedContinuousZeros;
B _isMaxNumContinuousZerosOverThreshold;
@"NSString" _locale;
@"NSString" _vtAssetConfigVersion;
i _sessionStatus;
B _didDetectSpeechStart;
B _didUseTwoPassDetector;
B _didFirstPassTrigger;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CSVTUISelfLoggingDigitalZeroReporter reportDigitalZerosWithAudioZeroRun:];
-[CSVTUISelfLoggingDigitalZeroReporter logDigitalZeroDetectionComplete];
-[CSVTUISelfLoggingDigitalZeroReporter _getStageStatusFromTrainingManagerSessionStatus:];
-[CSVTUISelfLoggingDigitalZeroReporter digitalZeroDetected];
-[CSVTUISelfLoggingDigitalZeroReporter initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:];
```
