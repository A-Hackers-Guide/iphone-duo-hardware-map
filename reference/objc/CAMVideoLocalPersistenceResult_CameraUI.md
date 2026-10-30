# `CAMVideoLocalPersistenceResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 16 instance variables, 16 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _localDestinationURL;
@"NSURL" _filteredLocalDestinationURL;
@"NSURL" _linkedDestinationURL;
@"NSURL" _filteredLinkedDestinationURL;
@"NSString" _filteredVideoPreviewPath;
@"NSString" _localPersistenceUUID;
{?="width"i"height"i} _dimensions;
@"NSString" _stillPersistenceUUID;
@"NSArray" _metadataItems;
@"NSDate" _creationDate;
@"NSData" _adjustmentsData;
@"CAMCaptureCoordinationInfo" _coordinationInfo;
@"NSURL" _localPrivateMetadataFileURL;
@"NSError" _error;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{?="value"q"timescale"i"flags"I"epoch"q} _stillDisplayTime;
```

## Properties

```
@property (T@"NSURL",R,C,N,V_localDestinationURL) localDestinationURL;
@property (T@"NSURL",R,C,N,V_filteredLocalDestinationURL) filteredLocalDestinationURL;
@property (T@"NSURL",R,C,N,V_linkedDestinationURL) linkedDestinationURL;
@property (T@"NSURL",R,C,N,V_filteredLinkedDestinationURL) filteredLinkedDestinationURL;
@property (T@"NSString",R,C,N,V_filteredVideoPreviewPath) filteredVideoPreviewPath;
@property (T@"NSString",R,C,N,V_localPersistenceUUID) localPersistenceUUID;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T{?=ii},R,N,V_dimensions) dimensions;
@property (T@"NSString",R,C,N,V_stillPersistenceUUID) stillPersistenceUUID;
@property (T{?=qiIq},R,N,V_stillDisplayTime) stillDisplayTime;
@property (T@"NSArray",R,N,V_metadataItems) metadataItems;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSData",R,N,V_adjustmentsData) adjustmentsData;
@property (T@"CAMCaptureCoordinationInfo",R,N,V_coordinationInfo) coordinationInfo;
@property (T@"NSURL",R,C,N,V_localPrivateMetadataFileURL) localPrivateMetadataFileURL;
@property (T@"NSError",R,N,V_error) error;
```

## Class methods

```
+[CAMVideoLocalPersistenceResult supportsSecureCoding];
```

## Instance methods

```
-[CAMVideoLocalPersistenceResult dimensions];
-[CAMVideoLocalPersistenceResult filteredLocalDestinationURL];
-[CAMVideoLocalPersistenceResult metadataItems];
-[CAMVideoLocalPersistenceResult linkedDestinationURL];
-[CAMVideoLocalPersistenceResult stillPersistenceUUID];
-[CAMVideoLocalPersistenceResult creationDate];
-[CAMVideoLocalPersistenceResult error];
-[CAMVideoLocalPersistenceResult duration];
-[CAMVideoLocalPersistenceResult initWithURL:filteredLocalDestinationURL:linkedURL:filteredLinkedURL:videoThumbnailPath:UUID:duration:dimensions:stillPersistenceUUID:stillDisplayTime:metadataItems:creationDate:adjustmentsData:coordinationInfo:localPrivateMetadataFileURL:error:];
-[CAMVideoLocalPersistenceResult localPrivateMetadataFileURL];
-[CAMVideoLocalPersistenceResult stillDisplayTime];
-[CAMVideoLocalPersistenceResult encodeWithCoder:];
-[CAMVideoLocalPersistenceResult filteredVideoPreviewPath];
-[CAMVideoLocalPersistenceResult initWithCoder:];
-[CAMVideoLocalPersistenceResult localPersistenceUUID];
-[CAMVideoLocalPersistenceResult filteredLinkedDestinationURL];
-[CAMVideoLocalPersistenceResult adjustmentsData];
-[CAMVideoLocalPersistenceResult coordinationInfo];
-[CAMVideoLocalPersistenceResult localDestinationURL];
```
