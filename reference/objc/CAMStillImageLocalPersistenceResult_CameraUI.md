# `CAMStillImageLocalPersistenceResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CAMStillImageCaptureResult" _captureResult;
@"NSURL" _localDestinationURL;
@"NSURL" _linkedDestinationURL;
@"NSURL" _localAdjustmentsURL;
@"NSString" _localDiagnosticsPath;
@"NSString" _localFilteredPreviewPath;
@"NSString" _localPersistenceUUID;
@"NSDate" _creationDate;
@"NSString" _uniformTypeIdentifier;
q _imageOrientation;
@"NSDictionary" _metadata;
@"NSData" _adjustmentsData;
@"NSURL" _localPrivateMetadataFileURL;
@"NSURL" _provenanceMetadataURL;
@"NSError" _error;
```

## Properties

```
@property (T@"CAMStillImageCaptureResult",R,N,V_captureResult) captureResult;
@property (T@"NSURL",R,C,N,V_localDestinationURL) localDestinationURL;
@property (T@"NSURL",R,C,N,V_linkedDestinationURL) linkedDestinationURL;
@property (T@"NSURL",R,C,N,V_localAdjustmentsURL) localAdjustmentsURL;
@property (T@"NSString",R,C,N,V_localDiagnosticsPath) localDiagnosticsPath;
@property (T@"NSString",R,C,N,V_localFilteredPreviewPath) localFilteredPreviewPath;
@property (T@"NSString",R,C,N,V_localPersistenceUUID) localPersistenceUUID;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSString",R,C,N,V_uniformTypeIdentifier) uniformTypeIdentifier;
@property (Tq,R,N,V_imageOrientation) imageOrientation;
@property (T@"NSDictionary",R,C,N,V_metadata) metadata;
@property (T@"NSData",R,N,V_adjustmentsData) adjustmentsData;
@property (T@"NSURL",R,C,N,V_localPrivateMetadataFileURL) localPrivateMetadataFileURL;
@property (T@"NSURL",R,C,N,V_provenanceMetadataURL) provenanceMetadataURL;
@property (T@"NSError",R,N,V_error) error;
```

## Instance methods

```
-[CAMStillImageLocalPersistenceResult uniformTypeIdentifier];
-[CAMStillImageLocalPersistenceResult imageOrientation];
-[CAMStillImageLocalPersistenceResult linkedDestinationURL];
-[CAMStillImageLocalPersistenceResult provenanceMetadataURL];
-[CAMStillImageLocalPersistenceResult creationDate];
-[CAMStillImageLocalPersistenceResult error];
-[CAMStillImageLocalPersistenceResult metadata];
-[CAMStillImageLocalPersistenceResult localPrivateMetadataFileURL];
-[CAMStillImageLocalPersistenceResult localAdjustmentsURL];
-[CAMStillImageLocalPersistenceResult localDiagnosticsPath];
-[CAMStillImageLocalPersistenceResult captureResult];
-[CAMStillImageLocalPersistenceResult localPersistenceUUID];
-[CAMStillImageLocalPersistenceResult adjustmentsData];
-[CAMStillImageLocalPersistenceResult localFilteredPreviewPath];
-[CAMStillImageLocalPersistenceResult initWithCaptureResult:atURL:linkedURL:localAdjustmentsURL:diagnosticsPath:filteredPreviewPath:withUUID:creationDate:uniformTypeIdentifier:orientation:metadata:adjustmentsData:localPrivateMetadataFileURL:provenanceMetadataURL:error:];
-[CAMStillImageLocalPersistenceResult localDestinationURL];
```
