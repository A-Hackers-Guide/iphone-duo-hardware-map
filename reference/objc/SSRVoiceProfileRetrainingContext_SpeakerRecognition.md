# `SSRVoiceProfileRetrainingContext`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _filterToVoiceTriggerUtterances;
B _forceRetrain;
f _combinationWeight;
@"NSString" _sessionId;
@"NSArray" _compareVoiceProfileArray;
@"SSRVoiceProfile" _voiceProfile;
Q _spIdType;
@"NSURL" _resourceFilePath;
@"NSString" _configVersion;
Q _maxAllowedSpeakerVectors;
@"NSDictionary" _modelsContext;
@"CSAsset" _asset;
@"SecureAsset" _secureAsset;
@"SSRLoggingAggregator" _logAggregator;
```

## Properties

```
@property (T@"NSArray",&,N,V_compareVoiceProfileArray) compareVoiceProfileArray;
@property (T@"SSRVoiceProfile",&,N,V_voiceProfile) voiceProfile;
@property (TQ,R,N,V_spIdType) spIdType;
@property (T@"NSURL",R,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSString",R,N,V_configVersion) configVersion;
@property (TB,R,N,V_filterToVoiceTriggerUtterances) filterToVoiceTriggerUtterances;
@property (TB,R,N,V_forceRetrain) forceRetrain;
@property (TQ,R,N,V_maxAllowedSpeakerVectors) maxAllowedSpeakerVectors;
@property (T@"NSDictionary",R,N,V_modelsContext) modelsContext;
@property (Tf,R,N,V_combinationWeight) combinationWeight;
@property (T@"CSAsset",&,N,V_asset) asset;
@property (T@"SecureAsset",&,N,V_secureAsset) secureAsset;
@property (T@"SSRLoggingAggregator",&,N,V_logAggregator) logAggregator;
@property (T@"NSString",R,N,V_sessionId) sessionId;
```

## Instance methods

```
-[SSRVoiceProfileRetrainingContext asset];
-[SSRVoiceProfileRetrainingContext setAsset:];
-[SSRVoiceProfileRetrainingContext sessionId];
-[SSRVoiceProfileRetrainingContext configVersion];
-[SSRVoiceProfileRetrainingContext description];
-[SSRVoiceProfileRetrainingContext initWithVoiceRetrainingContext:error:];
-[SSRVoiceProfileRetrainingContext setSecureAsset:];
-[SSRVoiceProfileRetrainingContext combinationWeight];
-[SSRVoiceProfileRetrainingContext compareVoiceProfileArray];
-[SSRVoiceProfileRetrainingContext filterToVoiceTriggerUtterances];
-[SSRVoiceProfileRetrainingContext forceRetrain];
-[SSRVoiceProfileRetrainingContext initWithVoiceRetrainingContext:skipClassTypeValidate:error:];
-[SSRVoiceProfileRetrainingContext logAggregator];
-[SSRVoiceProfileRetrainingContext maxAllowedSpeakerVectors];
-[SSRVoiceProfileRetrainingContext modelsContext];
-[SSRVoiceProfileRetrainingContext resourceFilePath];
-[SSRVoiceProfileRetrainingContext secureAsset];
-[SSRVoiceProfileRetrainingContext setCompareVoiceProfileArray:];
-[SSRVoiceProfileRetrainingContext setLogAggregator:];
-[SSRVoiceProfileRetrainingContext setVoiceProfile:];
-[SSRVoiceProfileRetrainingContext spIdType];
-[SSRVoiceProfileRetrainingContext voiceProfile];
```
