# `SSRVoiceProfileStoreData`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _vpArray;
@"NSDictionary" _enrollmentMetaDataDict;
@"NSNumber" _version;
@"NSNumber" _rpiDataRemovalStatus;
@"NSDictionary" _requestIdToAudioIdMap;
```

## Properties

```
@property (T@"NSArray",R,N,V_vpArray) vpArray;
@property (T@"NSDictionary",R,N,V_enrollmentMetaDataDict) enrollmentMetaDataDict;
@property (T@"NSNumber",R,N,V_version) version;
@property (T@"NSNumber",R,N,V_rpiDataRemovalStatus) rpiDataRemovalStatus;
@property (T@"NSDictionary",R,N,V_requestIdToAudioIdMap) requestIdToAudioIdMap;
```

## Class methods

```
+[SSRVoiceProfileStoreData supportsSecureCoding];
```

## Instance methods

```
-[SSRVoiceProfileStoreData version];
-[SSRVoiceProfileStoreData encodeWithCoder:];
-[SSRVoiceProfileStoreData description];
-[SSRVoiceProfileStoreData initWithCoder:];
-[SSRVoiceProfileStoreData vpArray];
-[SSRVoiceProfileStoreData enrollmentMetaDataDict];
-[SSRVoiceProfileStoreData initWithVoiceProfileArray:withVersion:];
-[SSRVoiceProfileStoreData initWithVoiceProfileArray:withVersion:enrollmentSamplingMetaDataDict:requestIdAudioIdsMap:];
-[SSRVoiceProfileStoreData requestIdToAudioIdMap];
-[SSRVoiceProfileStoreData rpiDataRemovalStatus];
```
