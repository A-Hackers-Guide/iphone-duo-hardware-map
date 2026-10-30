# `ICDocCamDocumentInfo`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 14 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _constantColor;
s _currentFilter;
@"NSDictionary" _metaData;
@"ICDocCamImageQuad" _imageQuad;
@"NSString" _croppedAndFilteredImageUUID;
@"NSString" _croppedButNotFilteredImageUUID;
@"NSString" _fullImageUUID;
@"NSString" _meshAnimImageUUID;
q _currentOrientation;
@"NSString" _scanDataDelegateIdentifier;
@"NSData" _markupModelData;
@"<ICDocCamViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<ICDocCamViewControllerDelegate>",W,V_delegate) delegate;
@property (TB,N,V_constantColor) constantColor;
@property (T@"<DCScanDataDelegate>",R,N) scanDataDelegate;
@property (T@"NSDictionary",&,N,V_metaData) metaData;
@property (T@"ICDocCamImageQuad",&,N,V_imageQuad) imageQuad;
@property (T@"NSString",&,N,V_croppedAndFilteredImageUUID) croppedAndFilteredImageUUID;
@property (T@"NSString",&,N,V_croppedButNotFilteredImageUUID) croppedButNotFilteredImageUUID;
@property (T@"NSString",&,N,V_fullImageUUID) fullImageUUID;
@property (T@"NSString",&,N,V_meshAnimImageUUID) meshAnimImageUUID;
@property (Ts,N,V_currentFilter) currentFilter;
@property (Tq,N,V_currentOrientation) currentOrientation;
@property (T@"NSString",&,N,V_scanDataDelegateIdentifier) scanDataDelegateIdentifier;
@property (TB,R,N) hasFilter;
@property (T@"NSData",&,N,V_markupModelData) markupModelData;
```

## Class methods

```
+[ICDocCamDocumentInfo supportsSecureCoding];
```

## Instance methods

```
-[ICDocCamDocumentInfo currentOrientation];
-[ICDocCamDocumentInfo setMetaData:];
-[ICDocCamDocumentInfo initWithDelegate:];
-[ICDocCamDocumentInfo metaData];
-[ICDocCamDocumentInfo init];
-[ICDocCamDocumentInfo setDelegate:];
-[ICDocCamDocumentInfo encodeWithCoder:];
-[ICDocCamDocumentInfo delegate];
-[ICDocCamDocumentInfo description];
-[ICDocCamDocumentInfo initWithCoder:];
-[ICDocCamDocumentInfo hasFilter];
-[ICDocCamDocumentInfo setCurrentOrientation:];
-[ICDocCamDocumentInfo allUUIDs];
-[ICDocCamDocumentInfo markupModelData];
-[ICDocCamDocumentInfo setMarkupModelData:];
-[ICDocCamDocumentInfo currentFilter];
-[ICDocCamDocumentInfo fullImageUUID];
-[ICDocCamDocumentInfo imageQuad];
-[ICDocCamDocumentInfo setScanDataDelegateIdentifier:];
-[ICDocCamDocumentInfo croppedAndFilteredImageUUID];
-[ICDocCamDocumentInfo setCurrentFilter:];
-[ICDocCamDocumentInfo constantColor];
-[ICDocCamDocumentInfo setConstantColor:];
-[ICDocCamDocumentInfo setImageQuad:];
-[ICDocCamDocumentInfo setCroppedAndFilteredImageUUID:];
-[ICDocCamDocumentInfo croppedButNotFilteredImageUUID];
-[ICDocCamDocumentInfo meshAnimImageUUID];
-[ICDocCamDocumentInfo scanDataDelegate];
-[ICDocCamDocumentInfo scanDataDelegateIdentifier];
-[ICDocCamDocumentInfo setCroppedButNotFilteredImageUUID:];
-[ICDocCamDocumentInfo setFullImageUUID:];
-[ICDocCamDocumentInfo setMeshAnimImageUUID:];
```
