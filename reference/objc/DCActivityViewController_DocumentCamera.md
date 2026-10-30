# `DCActivityViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIActivityViewController`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _ignoreAttachmentsForCopyToPasteboard;
@"ICDocCamDocumentInfoCollection" _documentInfoCollection;
@"ICDocCamImageCache" _imageCache;
```

## Properties

```
@property (T@"ICDocCamDocumentInfoCollection",&,N,V_documentInfoCollection) documentInfoCollection;
@property (T@"ICDocCamImageCache",&,N,V_imageCache) imageCache;
@property (TB,N,V_ignoreAttachmentsForCopyToPasteboard) ignoreAttachmentsForCopyToPasteboard;
```

## Instance methods

```
-[DCActivityViewController setImageCache:];
-[DCActivityViewController _canShowWhileLocked];
-[DCActivityViewController imageCache];
-[DCActivityViewController _performActivity:];
-[DCActivityViewController activityTypesThatInhibitPDFGeneration];
-[DCActivityViewController ignoreAttachmentsForCopyToPasteboard];
-[DCActivityViewController inhibitPDFGenerationForActivityType:];
-[DCActivityViewController setIgnoreAttachmentsForCopyToPasteboard:];
-[DCActivityViewController documentInfoCollection];
-[DCActivityViewController setDocumentInfoCollection:];
-[DCActivityViewController writeGalleryPDFDataToPasteboardIfNecessaryForActivity:documentInfoCollection:];
```
