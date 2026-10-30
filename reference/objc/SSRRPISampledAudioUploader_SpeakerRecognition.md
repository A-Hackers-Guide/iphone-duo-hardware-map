# `SSRRPISampledAudioUploader`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 9 class methods

## Class methods

```
+[SSRRPISampledAudioUploader _uploadAudioFilePath:requestId:audioId:metadataDict:completion:];
+[SSRRPISampledAudioUploader _convertToMetadataWithRequestId:audioUUId:audioMetadata:];
+[SSRRPISampledAudioUploader _getAudioFileMetadata:];
+[SSRRPISampledAudioUploader audioFileExist:date:];
+[SSRRPISampledAudioUploader cleanUpAudioOnAndBeforeDate:error:];
+[SSRRPISampledAudioUploader purgeOldAudioData];
+[SSRRPISampledAudioUploader removeAllAudioDataWithError:];
+[SSRRPISampledAudioUploader uploadAudioFilePath:requestId:audioId:completion:];
+[SSRRPISampledAudioUploader uploadAudioFileWithRequestId:audioId:date:completion:];
```
