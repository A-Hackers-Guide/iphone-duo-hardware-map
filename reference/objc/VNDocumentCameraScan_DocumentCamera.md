# `VNDocumentCameraScan`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 30 instance methods, 2 class methods

## Instance variables

```
@"NSString" _title;
@"NSMutableArray" _docInfos;
@"NSURL" _scannedDocumentImageDirectoryURL;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSMutableArray",&,N,V_docInfos) docInfos;
@property (T@"NSURL",R,N,V_scannedDocumentImageDirectoryURL) scannedDocumentImageDirectoryURL;
@property (TQ,R,N) pageCount;
```

## Class methods

```
+[VNDocumentCameraScan initialize];
+[VNDocumentCameraScan scannedDocumentsFolderURL];
```

## Instance methods

```
-[VNDocumentCameraScan pageCount];
-[VNDocumentCameraScan dealloc];
-[VNDocumentCameraScan archivedDataWithError:];
-[VNDocumentCameraScan numberOfScans];
-[VNDocumentCameraScan saveToURL:error:];
-[VNDocumentCameraScan title];
-[VNDocumentCameraScan initWithURL:error:];
-[VNDocumentCameraScan applicationWillTerminate:];
-[VNDocumentCameraScan setTitle:];
-[VNDocumentCameraScan imageOfPageAtIndex:];
-[VNDocumentCameraScan docInfos];
-[VNDocumentCameraScan getImageURL:];
-[VNDocumentCameraScan setDocInfos:];
-[VNDocumentCameraScan copyImageAtURL:];
-[VNDocumentCameraScan copyImageForSaving:toFolderURL:];
-[VNDocumentCameraScan deleteAllImages];
-[VNDocumentCameraScan URLForImageInFolder:withUUID:];
-[VNDocumentCameraScan URLForImageWithUUID:];
-[VNDocumentCameraScan copyImageForLoading:fromFolderURL:];
-[VNDocumentCameraScan copyImagesFromDocInfoCollection:imageCache:];
-[VNDocumentCameraScan deleteImage:];
-[VNDocumentCameraScan getImage:];
-[VNDocumentCameraScan imageForScanAtIndex:error:];
-[VNDocumentCameraScan infoCollectionWithImageCache:error:];
-[VNDocumentCameraScan initWithArchivedData:error:];
-[VNDocumentCameraScan initWithDocInfoCollection:imageCache:];
-[VNDocumentCameraScan makeSureScanDirectoryExists:];
-[VNDocumentCameraScan pListURL:];
-[VNDocumentCameraScan replaceContentsWithDocInfoCollection:imageCache:];
-[VNDocumentCameraScan scannedDocumentImageDirectoryURL];
```
