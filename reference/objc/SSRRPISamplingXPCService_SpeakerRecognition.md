# `SSRRPISamplingXPCService`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 14 class methods

## Class methods

```
+[SSRRPISamplingXPCService _createConnection];
+[SSRRPISamplingXPCService _invalidateConnection:];
+[SSRRPISamplingXPCService checkAndPromptRepairIfNeededWithLocale:completion:];
+[SSRRPISamplingXPCService getActiveRequestIdsForLocale:date:error:];
+[SSRRPISamplingXPCService getAudioIdWithRequestId:languageCode:date:error:];
+[SSRRPISamplingXPCService getEnrollmentSelectionStatusWithLocale:error:];
+[SSRRPISamplingXPCService getRemoteObjectProxyWithConnection:errorHandler:];
+[SSRRPISamplingXPCService removeAllSamplingMetaDataWithCompletion:];
+[SSRRPISamplingXPCService removeMappingOnAndBefore:completion:];
+[SSRRPISamplingXPCService removeMappingWithLocale:date:completion:];
+[SSRRPISamplingXPCService removeRequestIdToAudioIdMappingWithCompletion:];
+[SSRRPISamplingXPCService updateEnrollmentHealthWithLocale:completion:];
+[SSRRPISamplingXPCService updateStatus:languageCode:completion:];
+[SSRRPISamplingXPCService writeIntoMappingWithRequestId:audioId:date:locale:completion:];
```
