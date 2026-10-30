# `ICDocCamDocumentInfoCollection`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 6 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"NSString" _title;
@"NSDate" _creationDate;
@"NSDate" _modificationDate;
@"NSString" _uniqueIdentifier;
@"NSMutableArray" _docInfos;
```

## Properties

```
@property (Tq,R,N) docCamPDFVersion;
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSDate",&,N,V_creationDate) creationDate;
@property (T@"NSDate",&,N,V_modificationDate) modificationDate;
@property (T@"NSString",&,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSMutableArray",&,N,V_docInfos) docInfos;
```

## Class methods

```
+[ICDocCamDocumentInfoCollection supportsSecureCoding];
+[ICDocCamDocumentInfoCollection infoCollectionFromSidecarItems:imageCache:completion:];
+[ICDocCamDocumentInfoCollection infoCollectionFromArchiveSidecarItems:imageCache:];
+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:];
+[ICDocCamDocumentInfoCollection infoCollectionWithArchivedDocumentCameraScanData:imageCache:error:];
```

## Instance methods

```
-[ICDocCamDocumentInfoCollection setModificationDate:];
-[ICDocCamDocumentInfoCollection modificationDate];
-[ICDocCamDocumentInfoCollection init];
-[ICDocCamDocumentInfoCollection setUniqueIdentifier:];
-[ICDocCamDocumentInfoCollection creationDate];
-[ICDocCamDocumentInfoCollection uniqueIdentifier];
-[ICDocCamDocumentInfoCollection title];
-[ICDocCamDocumentInfoCollection setCreationDate:];
-[ICDocCamDocumentInfoCollection encodeWithCoder:];
-[ICDocCamDocumentInfoCollection initWithCoder:];
-[ICDocCamDocumentInfoCollection setTitle:];
-[ICDocCamDocumentInfoCollection docInfos];
-[ICDocCamDocumentInfoCollection docCamPDFVersion];
-[ICDocCamDocumentInfoCollection setDocInfos:];
-[ICDocCamDocumentInfoCollection bumpModificationDate];
```
