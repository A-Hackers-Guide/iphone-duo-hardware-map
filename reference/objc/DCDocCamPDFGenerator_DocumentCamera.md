# `DCDocCamPDFGenerator`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 20 class methods

## Class methods

```
+[DCDocCamPDFGenerator fileManager];
+[DCDocCamPDFGenerator initialize];
+[DCDocCamPDFGenerator applicationWillTerminate:];
+[DCDocCamPDFGenerator fileQueue];
+[DCDocCamPDFGenerator deleteAllDocCamPDFs];
+[DCDocCamPDFGenerator rootPDFFolderPath];
+[DCDocCamPDFGenerator syncGeneratorQueue];
+[DCDocCamPDFGenerator blockingGeneratepdfURLForDocumentInfoCollection:imageURLs:dataCryptor:withProgress:error:];
+[DCDocCamPDFGenerator createEmptyPDFFileAtURLIFNecessaryForDocumentInfoCollection:];
+[DCDocCamPDFGenerator createTmpDirectory:];
+[DCDocCamPDFGenerator deletePDFFolderIfExistsForDocumentInfoCollection:];
+[DCDocCamPDFGenerator deletePDFForDocumentInfoCollectionIfExists:];
+[DCDocCamPDFGenerator folderPathForDocumentInfoCollection:];
+[DCDocCamPDFGenerator folderPathForDocumentInfoCollectionIdentifier:];
+[DCDocCamPDFGenerator generatePDFsIfNecessaryForDocumentInfoCollection:imageCache:displayWindow:presentingViewController:completionHandler:];
+[DCDocCamPDFGenerator imageAtURL:uuid:dataCryptor:];
+[DCDocCamPDFGenerator pdfURLForDocumentInfoCollection:];
+[DCDocCamPDFGenerator performPDFGenerationWithGenerator:docInfoCollection:imageURLs:dataCryptor:progress:];
+[DCDocCamPDFGenerator versionPDFPathForDocumentInfoCollection:];
+[DCDocCamPDFGenerator versionfolderPathForDocumentInfoCollection:];
```
