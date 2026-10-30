# `CAMDocumentScanFlowController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- Protocols: `QLPreviewControllerDataSource`, `QLPreviewControllerDelegate`, `VNDocumentCameraViewControllerDelegate`, `UIDocumentPickerDelegate`
- 2 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"<CAMDocumentScanFlowControllerDelegate>" _documentFlowDelegate;
@"NSURL" __url;
```

## Properties

```
@property (T@"NSURL",&,N,V__url) _url;
@property (T@"<CAMDocumentScanFlowControllerDelegate>",W,N,V_documentFlowDelegate) documentFlowDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMDocumentScanFlowController nameForDocumentWithDate:];
```

## Instance methods

```
-[CAMDocumentScanFlowController previewController:previewItemAtIndex:];
-[CAMDocumentScanFlowController init];
-[CAMDocumentScanFlowController _url];
-[CAMDocumentScanFlowController documentPicker:didPickDocumentsAtURLs:];
-[CAMDocumentScanFlowController numberOfPreviewItemsInPreviewController:];
-[CAMDocumentScanFlowController set_url:];
-[CAMDocumentScanFlowController previewController:editingModeForPreviewItem:];
-[CAMDocumentScanFlowController documentCameraViewController:didFailWithError:];
-[CAMDocumentScanFlowController documentCameraViewController:didFinishWithScan:];
-[CAMDocumentScanFlowController documentCameraViewControllerDidCancel:];
-[CAMDocumentScanFlowController _asyncConvertToPDFAndWrite:completionHandler:];
-[CAMDocumentScanFlowController _handlePDFResults:];
-[CAMDocumentScanFlowController _pdfConversionQueue];
-[CAMDocumentScanFlowController documentFlowDelegate];
-[CAMDocumentScanFlowController setDocumentFlowDelegate:];
```
