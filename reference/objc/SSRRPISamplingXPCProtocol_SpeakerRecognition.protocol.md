# `SSRRPISamplingXPCProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SSREnrollmentHealthXPCProtocol`
- 0 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance methods

```
-[SSRRPISamplingXPCProtocol getActiveRequestIdsForLocale:date:completion:];
-[SSRRPISamplingXPCProtocol getAudioIdWithRequestId:languageCode:date:completion:];
-[SSRRPISamplingXPCProtocol getEnrollmentSelectionStatusWithLocale:completion:];
-[SSRRPISamplingXPCProtocol removeAllSamplingMetaDataWithCompletion:];
-[SSRRPISamplingXPCProtocol removeMappingOnAndBefore:completion:];
-[SSRRPISamplingXPCProtocol removeMappingWithLocale:date:completion:];
-[SSRRPISamplingXPCProtocol removeRequestIdToAudioIdMappingWithCompletion:];
-[SSRRPISamplingXPCProtocol updateStatus:languageCode:completion:];
-[SSRRPISamplingXPCProtocol writeIntoMappingWithRequestId:audioId:date:locale:completion:];
```
