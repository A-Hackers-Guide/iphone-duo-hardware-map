# `UIWebFileUploadPanel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIDocumentPickerDelegate`, `UIDocumentMenuDelegate`, `UINavigationControllerDelegate`, `UIImagePickerControllerDelegate`, `UIPopoverControllerDelegate`
- 13 instance variables, 11 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"UIDocumentMenuViewController" _documentMenuController;
@"UIImagePickerController" _imagePicker;
@"UIViewController" _presentationViewController;
@"UIPopoverController" _presentationPopover;
{CGPoint="x"d"y"d} _interactionPoint;
@"DOMNode" _interactionElement;
B _allowMultipleFiles;
B _isUsingCamera;
@"NSArray" _mimeTypes;
@"UIWebDocumentView" _documentView;
@"NSObject<WebOpenPanelResultListener>" _resultListener;
@"<UIWebFileUploadPanelDelegate>" _delegate;
q _mediaCaptureType;
```

## Properties

```
@property (T@"NSArray",C,N,V_mimeTypes) mimeTypes;
@property (T@"UIWebDocumentView",N,V_documentView) documentView;
@property (T@"NSObject<WebOpenPanelResultListener>",&,N,V_resultListener) resultListener;
@property (TB,N,V_allowMultipleFiles) allowMultipleFiles;
@property (TB,N,V_isUsingCamera) isUsingCamera;
@property (Tq,N,V_mediaCaptureType) mediaCaptureType;
@property (T@"<UIWebFileUploadPanelDelegate>",N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebFileUploadPanel present];
-[UIWebFileUploadPanel dismiss];
-[UIWebFileUploadPanel dealloc];
-[UIWebFileUploadPanel _cancel];
-[UIWebFileUploadPanel setDelegate:];
-[UIWebFileUploadPanel delegate];
-[UIWebFileUploadPanel documentPickerWasCancelled:];
-[UIWebFileUploadPanel isUsingCamera];
-[UIWebFileUploadPanel setIsUsingCamera:];
-[UIWebFileUploadPanel _displayStringForPhotos:videos:];
-[UIWebFileUploadPanel _mediaTypesForPickerSourceType:];
-[UIWebFileUploadPanel _showPhotoPickerWithSourceType:];
-[UIWebFileUploadPanel imagePickerControllerDidCancel:];
-[UIWebFileUploadPanel _UTIsForMIMETypes];
-[UIWebFileUploadPanel _adjustMediaCaptureType];
-[UIWebFileUploadPanel _cameraButtonLabel];
-[UIWebFileUploadPanel _chooseFilename:displayString:iconImage:];
-[UIWebFileUploadPanel _chooseFilenames:displayString:iconImage:];
-[UIWebFileUploadPanel _dismissDisplayAnimated:];
-[UIWebFileUploadPanel _dispatchDidDismiss];
-[UIWebFileUploadPanel _documentPickerMenuMediaTypes];
-[UIWebFileUploadPanel _photoPickerWithSourceType:];
-[UIWebFileUploadPanel _presentForCurrentInterfaceIdiom:];
-[UIWebFileUploadPanel _presentFullscreenViewController:animated:];
-[UIWebFileUploadPanel _presentPopoverWithContentViewController:animated:];
-[UIWebFileUploadPanel _processMediaInfoDictionaries:atIndex:processedResults:processedImageCount:processedVideoCount:successBlock:failureBlock:];
-[UIWebFileUploadPanel _processMediaInfoDictionaries:successBlock:failureBlock:];
-[UIWebFileUploadPanel _shouldMediaCaptureOpenMediaDevice];
-[UIWebFileUploadPanel _showDocumentPickerMenu];
-[UIWebFileUploadPanel _string:hasPrefixCaseInsensitive:];
-[UIWebFileUploadPanel _uploadItemForImageData:imageName:successBlock:failureBlock:];
-[UIWebFileUploadPanel _uploadItemForJPEGRepresentationOfImage:successBlock:failureBlock:];
-[UIWebFileUploadPanel _uploadItemFromMediaInfo:successBlock:failureBlock:];
-[UIWebFileUploadPanel _willMultipleSelectionDelegateBeCalled];
-[UIWebFileUploadPanel allowMultipleFiles];
-[UIWebFileUploadPanel documentMenu:didPickDocumentPicker:];
-[UIWebFileUploadPanel documentMenuWasCancelled:];
-[UIWebFileUploadPanel documentPicker:didPickDocumentAtURL:];
-[UIWebFileUploadPanel documentView];
-[UIWebFileUploadPanel imagePickerController:didFinishPickingMediaWithInfo:];
-[UIWebFileUploadPanel imagePickerController:didFinishPickingMultipleMediaWithInfo:];
-[UIWebFileUploadPanel initWithResultListener:configuration:documentView:];
-[UIWebFileUploadPanel mediaCaptureType];
-[UIWebFileUploadPanel mimeTypes];
-[UIWebFileUploadPanel popoverControllerDidDismissPopover:];
-[UIWebFileUploadPanel resultListener];
-[UIWebFileUploadPanel setAllowMultipleFiles:];
-[UIWebFileUploadPanel setDocumentView:];
-[UIWebFileUploadPanel setMediaCaptureType:];
-[UIWebFileUploadPanel setMimeTypes:];
-[UIWebFileUploadPanel setResultListener:];
```
