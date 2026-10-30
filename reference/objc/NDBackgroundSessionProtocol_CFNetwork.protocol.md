# `NDBackgroundSessionProtocol` (protocol)

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 25 instance methods, 0 class methods

## Instance methods

```
-[NDBackgroundSessionProtocol invalidateWithReply:];
-[NDBackgroundSessionProtocol applyOverrides:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol avAggregateAssetDownloadTaskWithDownloadToken:serializedMediaSelections:assetTitle:assetArtworkData:options:assetOptions:childDownloadSessionIdentifier:identifier:uniqueIdentifier:reply:];
-[NDBackgroundSessionProtocol avAssetDownloadTaskWithDownloadToken:URL:destinationURL:temporaryDestinationURL:assetTitle:assetArtworkData:options:assetOptions:identifier:uniqueIdentifier:taskKind:enableSPIDelegateCallbacks:reply:];
-[NDBackgroundSessionProtocol cancelTaskWithIdentifier:];
-[NDBackgroundSessionProtocol cancelTaskWithIdentifier:byProducingResumeData:];
-[NDBackgroundSessionProtocol dataTaskWithRequest:originalRequest:identifier:uniqueIdentifier:reply:];
-[NDBackgroundSessionProtocol downloadTaskWithRequest:originalRequest:downloadFilePath:identifier:uniqueIdentifier:reply:];
-[NDBackgroundSessionProtocol downloadTaskWithResumeData:extractor:identifier:uniqueIdentifier:reply:];
-[NDBackgroundSessionProtocol pingForXPCObjectValidityWithReply:];
-[NDBackgroundSessionProtocol resetStorageWithReply:];
-[NDBackgroundSessionProtocol resumeTaskWithIdentifier:withProperties:];
-[NDBackgroundSessionProtocol setBytesPerSecondLimit:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setDescription:forTask:];
-[NDBackgroundSessionProtocol setDiscretionaryOverride:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setExpectedProgressTarget:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setLoadingPoolPriority:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setPriority:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setPropertyOnStreamWithIdentifier:propDict:propKey:withReply:];
-[NDBackgroundSessionProtocol setTLSMaximumSupportedProtocolVersion:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setTLSMinimumSupportedProtocolVersion:forTaskWithIdentifier:];
-[NDBackgroundSessionProtocol setTLSSessionCachePrefix:];
-[NDBackgroundSessionProtocol suspendTaskWithIdentifier:];
-[NDBackgroundSessionProtocol uploadTaskWithRequest:originalRequest:fromFile:sandboxExtensionData:identifier:uniqueIdentifier:potentialCredentials:reply:];
-[NDBackgroundSessionProtocol uploadTaskWithResumableUploadState:request:originalRequest:fromFile:sandboxExtensionData:identifier:uniqueIdentifier:potentialCredentials:reply:];
```
