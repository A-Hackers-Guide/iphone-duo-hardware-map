# `DCScannedDocument`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 27 instance methods, 2 class methods

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
+[DCScannedDocument initialize];
+[DCScannedDocument scannedDocumentsFolderURL];
```

## Instance methods

```
-[DCScannedDocument pageCount];
-[DCScannedDocument dealloc];
-[DCScannedDocument numberOfScans];
-[DCScannedDocument saveToURL:error:];
-[DCScannedDocument title];
-[DCScannedDocument initWithURL:error:];
-[DCScannedDocument applicationWillTerminate:];
-[DCScannedDocument setTitle:];
-[DCScannedDocument imageOfPageAtIndex:];
-[DCScannedDocument docInfos];
-[DCScannedDocument getImageURL:];
-[DCScannedDocument setDocInfos:];
-[DCScannedDocument copyImageAtURL:];
-[DCScannedDocument copyImageForSaving:toFolderURL:];
-[DCScannedDocument deleteAllImages];
-[DCScannedDocument URLForImageInFolder:withUUID:];
-[DCScannedDocument URLForImageWithUUID:];
-[DCScannedDocument copyImageForLoading:fromFolderURL:];
-[DCScannedDocument copyImagesFromDocInfoCollection:imageCache:];
-[DCScannedDocument deleteImage:];
-[DCScannedDocument getImage:];
-[DCScannedDocument imageForScanAtIndex:error:];
-[DCScannedDocument initWithDocInfoCollection:imageCache:];
-[DCScannedDocument makeSureScanDirectoryExists:];
-[DCScannedDocument pListURL:];
-[DCScannedDocument replaceContentsWithDocInfoCollection:imageCache:];
-[DCScannedDocument scannedDocumentImageDirectoryURL];
```
