# `SSRRPISampler`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSREnrollmentHealthXPCProtocol`, `SSRRPISamplingXPCProtocol`
- 1 instance variables, 0 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
```

## Class methods

```
+[SSRRPISampler sharedInstance];
+[SSRRPISampler deleteAllRPISampledData];
```

## Instance methods

```
-[SSRRPISampler init];
-[SSRRPISampler _handleVoiceProfileRPICleanupEvent];
-[SSRRPISampler checkAndPromptRepairIfNeededWithLocale:completion:];
-[SSRRPISampler getActiveRequestIdsForLocale:date:completion:];
-[SSRRPISampler getAudioIdWithRequestId:languageCode:date:completion:];
-[SSRRPISampler getEnrollmentSelectionStatusWithLocale:completion:];
-[SSRRPISampler removeAllSamplingMetaDataWithCompletion:];
-[SSRRPISampler removeMappingOnAndBefore:completion:];
-[SSRRPISampler removeMappingWithLocale:date:completion:];
-[SSRRPISampler removeRequestIdToAudioIdMappingWithCompletion:];
-[SSRRPISampler updateEnrollmentHealthWithLocale:completion:];
-[SSRRPISampler updateStatus:languageCode:completion:];
-[SSRRPISampler writeIntoMappingWithRequestId:audioId:date:locale:completion:];
```
