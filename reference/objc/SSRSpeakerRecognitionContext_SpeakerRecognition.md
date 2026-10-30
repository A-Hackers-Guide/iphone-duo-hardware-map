# `SSRSpeakerRecognitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 23 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _osTransactionReqd;
f _combinationWeight;
@"NSString" _sessionId;
Q _spIdType;
@"SecureAsset" _secureAsset;
@"NSUUID" _endpointUUID;
Q _activeChannel;
Q _scoreType;
Q _recognitionStyle;
@"NSArray" _voiceProfileArray;
@"NSString" _locale;
@"CSAsset" _asset;
@"NSDictionary" _vtEventInfo;
@"NSString" _configVersion;
@"NSURL" _resourceFilePath;
@"NSURL" _vadResourcePath;
@"NSDictionary" _modelsContext;
@"NSDictionary" _expModelsContext;
Q _maxAllowedAudioSamples;
@"NSString" _debugUtteranceAudioFile;
@"NSString" _debugUtteranceMetaFile;
@"SSRLoggingAggregator" _logAggregator;
```

## Properties

```
@property (TQ,N,V_spIdType) spIdType;
@property (T@"SecureAsset",&,N,V_secureAsset) secureAsset;
@property (T@"NSUUID",&,N,V_endpointUUID) endpointUUID;
@property (TQ,R,N,V_activeChannel) activeChannel;
@property (TQ,R,N,V_scoreType) scoreType;
@property (TQ,R,N,V_recognitionStyle) recognitionStyle;
@property (T@"NSArray",R,N,V_voiceProfileArray) voiceProfileArray;
@property (T@"NSString",R,N,V_locale) locale;
@property (Tf,R,N,V_combinationWeight) combinationWeight;
@property (T@"CSAsset",R,N,V_asset) asset;
@property (T@"NSDictionary",R,N,V_vtEventInfo) vtEventInfo;
@property (T@"NSString",R,N,V_configVersion) configVersion;
@property (T@"NSURL",R,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSURL",R,N,V_vadResourcePath) vadResourcePath;
@property (T@"NSDictionary",R,N,V_modelsContext) modelsContext;
@property (T@"NSDictionary",R,N,V_expModelsContext) expModelsContext;
@property (T@"NSDictionary",R,N) numEnrollmentUtterances;
@property (TQ,R,N,V_maxAllowedAudioSamples) maxAllowedAudioSamples;
@property (TB,R,N,V_osTransactionReqd) osTransactionReqd;
@property (T@"NSString",R,N,V_debugUtteranceAudioFile) debugUtteranceAudioFile;
@property (T@"NSString",R,N,V_debugUtteranceMetaFile) debugUtteranceMetaFile;
@property (T@"SSRLoggingAggregator",&,N,V_logAggregator) logAggregator;
@property (T@"NSString",R,N,V_sessionId) sessionId;
```

## Instance methods

```
-[SSRSpeakerRecognitionContext asset];
-[SSRSpeakerRecognitionContext sessionId];
-[SSRSpeakerRecognitionContext dealloc];
-[SSRSpeakerRecognitionContext locale];
-[SSRSpeakerRecognitionContext setEndpointUUID:];
-[SSRSpeakerRecognitionContext endpointUUID];
-[SSRSpeakerRecognitionContext configVersion];
-[SSRSpeakerRecognitionContext description];
-[SSRSpeakerRecognitionContext activeChannel];
-[SSRSpeakerRecognitionContext scoreType];
-[SSRSpeakerRecognitionContext initWithVoiceRecognitionContext:error:];
-[SSRSpeakerRecognitionContext setSecureAsset:];
-[SSRSpeakerRecognitionContext vadResourcePath];
-[SSRSpeakerRecognitionContext _checkIfModelsPresentForProfiles:forSpIdType:forAsset:];
-[SSRSpeakerRecognitionContext combinationWeight];
-[SSRSpeakerRecognitionContext composeModelContextsForProfiles:forSpIdType:forAsset:completion:];
-[SSRSpeakerRecognitionContext debugUtteranceAudioFile];
-[SSRSpeakerRecognitionContext debugUtteranceMetaFile];
-[SSRSpeakerRecognitionContext expModelsContext];
-[SSRSpeakerRecognitionContext logAggregator];
-[SSRSpeakerRecognitionContext maxAllowedAudioSamples];
-[SSRSpeakerRecognitionContext modelsContext];
-[SSRSpeakerRecognitionContext numEnrollmentUtterances];
-[SSRSpeakerRecognitionContext osTransactionReqd];
-[SSRSpeakerRecognitionContext pickAssetForProfiles:forSpIdType:];
-[SSRSpeakerRecognitionContext pickAssetForProfiles:forSpIdType:withAssetArray:];
-[SSRSpeakerRecognitionContext recognitionStyle];
-[SSRSpeakerRecognitionContext resourceFilePath];
-[SSRSpeakerRecognitionContext secureAsset];
-[SSRSpeakerRecognitionContext setLogAggregator:];
-[SSRSpeakerRecognitionContext setSpIdType:];
-[SSRSpeakerRecognitionContext spIdType];
-[SSRSpeakerRecognitionContext voiceProfileArray];
-[SSRSpeakerRecognitionContext vtEventInfo];
```
