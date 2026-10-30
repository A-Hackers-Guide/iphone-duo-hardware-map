# `CLEEDMediaItem`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 20 instance variables, 20 properties, 45 instance methods, 2 class methods

## Instance variables

```
B _metricProcessed;
B _didApplyDelayMitigation;
q _type;
q _uploadStatus;
@"NSURL" _URL;
@"NSString" _assetIdentifier;
@"NSString" _sandboxExtension;
@"NSURL" _stagingURL;
@"NSURL" _encryptedFileURL;
@"NSData" _authTag;
@"NSUUID" _mediaItemID;
@"NSString" _mediaItemFormat;
Q _mediaItemSizeBytes;
Q _originalSizeBytes;
q _serverUploadStatus;
Q _uploadAttempts;
q _durationCopyMs;
q _durationTranscodeMs;
q _durationEncryptionMs;
q _durationUploadMs;
```

## Properties

```
@property (Tq,N,V_uploadStatus) uploadStatus;
@property (T@"NSURL",&,N,V_stagingURL) stagingURL;
@property (T@"NSURL",&,N,V_encryptedFileURL) encryptedFileURL;
@property (T@"NSData",&,N,V_authTag) authTag;
@property (T@"NSUUID",&,N,V_mediaItemID) mediaItemID;
@property (T@"NSString",&,N,V_mediaItemFormat) mediaItemFormat;
@property (TQ,N,V_mediaItemSizeBytes) mediaItemSizeBytes;
@property (TQ,N,V_originalSizeBytes) originalSizeBytes;
@property (Tq,N,V_serverUploadStatus) serverUploadStatus;
@property (TQ,N,V_uploadAttempts) uploadAttempts;
@property (Tq,N,V_durationCopyMs) durationCopyMs;
@property (Tq,N,V_durationTranscodeMs) durationTranscodeMs;
@property (Tq,N,V_durationEncryptionMs) durationEncryptionMs;
@property (Tq,N,V_durationUploadMs) durationUploadMs;
@property (TB,N,V_metricProcessed) metricProcessed;
@property (TB,N,V_didApplyDelayMitigation) didApplyDelayMitigation;
@property (Tq,R,N,V_type) type;
@property (T@"NSURL",R,&,N,V_URL) URL;
@property (T@"NSString",R,&,N,V_assetIdentifier) assetIdentifier;
@property (T@"NSString",R,&,N,V_sandboxExtension) sandboxExtension;
```

## Class methods

```
+[CLEEDMediaItem supportsSecureCoding];
+[CLEEDMediaItem createMediaItemFromDict:];
```

## Instance methods

```
-[CLEEDMediaItem assetIdentifier];
-[CLEEDMediaItem stagingURL];
-[CLEEDMediaItem sandboxExtension];
-[CLEEDMediaItem dealloc];
-[CLEEDMediaItem type];
-[CLEEDMediaItem encodeWithCoder:];
-[CLEEDMediaItem hash];
-[CLEEDMediaItem description];
-[CLEEDMediaItem initWithCoder:];
-[CLEEDMediaItem isEqual:];
-[CLEEDMediaItem URL];
-[CLEEDMediaItem authTag];
-[CLEEDMediaItem setAuthTag:];
-[CLEEDMediaItem setUploadAttempts:];
-[CLEEDMediaItem uploadAttempts];
-[CLEEDMediaItem mediaItemFormat];
-[CLEEDMediaItem metricProcessed];
-[CLEEDMediaItem setMediaItemID:];
-[CLEEDMediaItem createMediaItemDict];
-[CLEEDMediaItem didApplyDelayMitigation];
-[CLEEDMediaItem durationCopyMs];
-[CLEEDMediaItem durationEncryptionMs];
-[CLEEDMediaItem durationTranscodeMs];
-[CLEEDMediaItem durationUploadMs];
-[CLEEDMediaItem encryptedFileURL];
-[CLEEDMediaItem initWithURL:assetIdentifier:sandboxExtension:mediaType:];
-[CLEEDMediaItem initWithURL:sandboxExtension:mediaType:];
-[CLEEDMediaItem mediaItemID];
-[CLEEDMediaItem mediaItemSizeBytes];
-[CLEEDMediaItem originalSizeBytes];
-[CLEEDMediaItem serverUploadStatus];
-[CLEEDMediaItem setDidApplyDelayMitigation:];
-[CLEEDMediaItem setDurationCopyMs:];
-[CLEEDMediaItem setDurationEncryptionMs:];
-[CLEEDMediaItem setDurationTranscodeMs:];
-[CLEEDMediaItem setDurationUploadMs:];
-[CLEEDMediaItem setEncryptedFileURL:];
-[CLEEDMediaItem setMediaItemFormat:];
-[CLEEDMediaItem setMediaItemSizeBytes:];
-[CLEEDMediaItem setMetricProcessed:];
-[CLEEDMediaItem setOriginalSizeBytes:];
-[CLEEDMediaItem setServerUploadStatus:];
-[CLEEDMediaItem setStagingURL:];
-[CLEEDMediaItem setUploadStatus:];
-[CLEEDMediaItem uploadStatus];
```
