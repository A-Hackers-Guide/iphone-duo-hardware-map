# `DCDocumentEditorViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- Protocols: `ICDocCamExtractedDocumentControllerDelegate`, `ICDocCamViewControllerDelegate`, `ICRemoteDocCamViewControllerDelegate`, `UINavigationControllerDelegate`, `UIViewControllerTransitioningDelegate`
- 11 instance variables, 15 properties, 53 instance methods, 3 class methods

## Instance variables

```
B _useCustomRecropTransition;
@"ICDocCamExtractedDocumentViewController" _extractedDocumentController;
@"<DCDocumentEditorViewControllerDelegate>" _docCamDelegate;
@"VNDocumentCameraScan" _scannedDocument;
@"ICDocCamDocumentInfoCollection" _docInfoCollection;
@"ICDocCamImageCache" _imageCache;
q _orientationForRecrop;
@"NSIndexPath" _indexPathForRecrop;
@"UIImage" _filteredImageForRecrop;
@"UIImage" _unfilteredImageForRecrop;
@"UIView" _sourceViewForZoomTransition;
```

## Properties

```
@property (T@"ICDocCamExtractedDocumentViewController",&,N,V_extractedDocumentController) extractedDocumentController;
@property (T@"<DCDocumentEditorViewControllerDelegate>",W,N,V_docCamDelegate) docCamDelegate;
@property (T@"VNDocumentCameraScan",&,N,V_scannedDocument) scannedDocument;
@property (T@"ICDocCamDocumentInfoCollection",&,N,V_docInfoCollection) docInfoCollection;
@property (T@"ICDocCamImageCache",&,N,V_imageCache) imageCache;
@property (TB,N,V_useCustomRecropTransition) useCustomRecropTransition;
@property (Tq,N,V_orientationForRecrop) orientationForRecrop;
@property (T@"NSIndexPath",&,N,V_indexPathForRecrop) indexPathForRecrop;
@property (T@"UIImage",&,N,V_filteredImageForRecrop) filteredImageForRecrop;
@property (T@"UIImage",&,N,V_unfilteredImageForRecrop) unfilteredImageForRecrop;
@property (T@"UIView",&,N,V_sourceViewForZoomTransition) sourceViewForZoomTransition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DCDocumentEditorViewController activityTypeOrder];
+[DCDocumentEditorViewController isAvailable];
+[DCDocumentEditorViewController docInfoCollectionFromScannedDocument:imageCache:];
```

## Instance methods

```
-[DCDocumentEditorViewController setImageCache:];
-[DCDocumentEditorViewController initWithNavigationBarClass:toolbarClass:];
-[DCDocumentEditorViewController navigationController:animationControllerForOperation:fromViewController:toViewController:];
-[DCDocumentEditorViewController viewDidLoad];
-[DCDocumentEditorViewController initWithNibName:bundle:];
-[DCDocumentEditorViewController _canShowWhileLocked];
-[DCDocumentEditorViewController imageCache];
-[DCDocumentEditorViewController didReceiveMemoryWarning];
-[DCDocumentEditorViewController initWithCoder:];
-[DCDocumentEditorViewController initWithRootViewController:];
-[DCDocumentEditorViewController _autoDismiss];
-[DCDocumentEditorViewController scanDataDelegateWithIdentifier:];
-[DCDocumentEditorViewController documentCameraController:canAddImages:];
-[DCDocumentEditorViewController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:];
-[DCDocumentEditorViewController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:closeViewController:];
-[DCDocumentEditorViewController documentCameraControllerCreateDataCryptorIfNecessary];
-[DCDocumentEditorViewController documentCameraControllerDidCancel:];
-[DCDocumentEditorViewController remoteDocumentCameraController:didFailWithError:];
-[DCDocumentEditorViewController remoteDocumentCameraController:didFinishWithInfoCollection:];
-[DCDocumentEditorViewController remoteDocumentCameraControllerDidCancel:];
-[DCDocumentEditorViewController scannedDocument];
-[DCDocumentEditorViewController setExtractedDocumentController:];
-[DCDocumentEditorViewController setSourceViewForZoomTransition:];
-[DCDocumentEditorViewController docCamDelegate];
-[DCDocumentEditorViewController docInfoCollection];
-[DCDocumentEditorViewController extractedDocumentController];
-[DCDocumentEditorViewController extractedDocumentController:didTapRecrop:index:];
-[DCDocumentEditorViewController extractedDocumentController:shareDocument:sender:];
-[DCDocumentEditorViewController extractedDocumentControllerDidChangeTitle:];
-[DCDocumentEditorViewController extractedDocumentControllerDidSelectCopyFromMenuForDocument:];
-[DCDocumentEditorViewController extractedDocumentControllerDidSelectShareFromMenuForDocument:sourceRect:sourceView:];
-[DCDocumentEditorViewController extractedDocumentControllerDidTapAddImage];
-[DCDocumentEditorViewController extractedDocumentControllerDidTapDone:];
-[DCDocumentEditorViewController extractedDocumentControllerDidTapDone:scanDataDelegate:];
-[DCDocumentEditorViewController extractedDocumentControllerDidTapRetake:];
-[DCDocumentEditorViewController extractedDocumentControllerDiscardMarkupModelDataForDocument:];
-[DCDocumentEditorViewController extractedDocumentControllerMarkupModelDataForDocument:];
-[DCDocumentEditorViewController extractedDocumentControllerTitle];
-[DCDocumentEditorViewController filteredImageForRecrop];
-[DCDocumentEditorViewController indexPathForRecrop];
-[DCDocumentEditorViewController initWithDelegate:scannedDocument:];
-[DCDocumentEditorViewController orientationForRecrop];
-[DCDocumentEditorViewController setDocCamDelegate:];
-[DCDocumentEditorViewController setDocInfoCollection:];
-[DCDocumentEditorViewController setFilteredImageForRecrop:];
-[DCDocumentEditorViewController setIndexPathForRecrop:];
-[DCDocumentEditorViewController setOrientationForRecrop:];
-[DCDocumentEditorViewController setScannedDocument:];
-[DCDocumentEditorViewController setUnfilteredImageForRecrop:];
-[DCDocumentEditorViewController setUseCustomRecropTransition:];
-[DCDocumentEditorViewController sourceViewForZoomTransition];
-[DCDocumentEditorViewController unfilteredImageForRecrop];
-[DCDocumentEditorViewController useCustomRecropTransition];
```
