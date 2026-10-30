# `CSVoiceTriggerUserSelectedPhrase`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _mphSelected;
@"<CSVoiceTriggerUserSelectedPhraseDelegate>" _delegate;
@"VTPreferences" _vtPrefrences;
@"NSUUID" _endpointDeviceId;
Q _uSelectedPhraseType;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"VTPreferences",&,N,V_vtPrefrences) vtPrefrences;
@property (T@"NSUUID",&,N,V_endpointDeviceId) endpointDeviceId;
@property (TB,N,V_mphSelected) mphSelected;
@property (TQ,N,V_uSelectedPhraseType) uSelectedPhraseType;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<CSVoiceTriggerUserSelectedPhraseDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CSVoiceTriggerUserSelectedPhrase initWithEndpointId:];
-[CSVoiceTriggerUserSelectedPhrase dealloc];
-[CSVoiceTriggerUserSelectedPhrase queue];
-[CSVoiceTriggerUserSelectedPhrase setDelegate:];
-[CSVoiceTriggerUserSelectedPhrase delegate];
-[CSVoiceTriggerUserSelectedPhrase setQueue:];
-[CSVoiceTriggerUserSelectedPhrase _isMultiPhrase:];
-[CSVoiceTriggerUserSelectedPhrase setMphSelected:];
-[CSVoiceTriggerUserSelectedPhrase _fetchUserSelectedPhraseType];
-[CSVoiceTriggerUserSelectedPhrase _localeSupportsMultiPhrase];
-[CSVoiceTriggerUserSelectedPhrase _registerForNotification];
-[CSVoiceTriggerUserSelectedPhrase endpointDeviceId];
-[CSVoiceTriggerUserSelectedPhrase initWithEndpointId:vtPreferences:];
-[CSVoiceTriggerUserSelectedPhrase mphSelected];
-[CSVoiceTriggerUserSelectedPhrase multiPhraseSelected];
-[CSVoiceTriggerUserSelectedPhrase setEndpointDeviceId:];
-[CSVoiceTriggerUserSelectedPhrase setUSelectedPhraseType:];
-[CSVoiceTriggerUserSelectedPhrase setVtPrefrences:];
-[CSVoiceTriggerUserSelectedPhrase uSelectedPhraseType];
-[CSVoiceTriggerUserSelectedPhrase userSelectedPhraseType];
-[CSVoiceTriggerUserSelectedPhrase vtPhraseTypeDidChangeNotificationReceived];
-[CSVoiceTriggerUserSelectedPhrase vtPrefrences];
```
