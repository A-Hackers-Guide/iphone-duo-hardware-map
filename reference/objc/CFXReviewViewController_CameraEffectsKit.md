# `CFXReviewViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXPreviewViewControllerDelegate`, `CFXEffectBrowserContentPresenterViewControllerDelegate`, `CFXEffectBrowserViewControllerDelegate`
- 11 instance variables, 21 properties, 65 instance methods, 1 class methods

## Instance variables

```
B _mediaCapturedInFunCam_metadata;
@"<CFXReviewViewControllerDelegate>" _delegate;
@"CFXEffectBrowserViewController" _effectBrowserViewController;
@"CFXPreviewViewController" _internalPreviewViewController;
@"CFXReviewControlsViewController" _reviewControlsViewController;
@"NSString" _effectBrowserPresentedAppIdentifier;
@"CFXMediaItem" _mediaItem;
@"NSObject<OS_dispatch_group>" _metadataReaderGroup;
q _mediaInterfaceOrientationForDisplay_metadata;
@"NSData" _animojiMetadata_metadata;
q _cameraModeUsedForCapture;
```

## Properties

```
@property (T@"CFXEffectBrowserViewController",&,N,V_effectBrowserViewController) effectBrowserViewController;
@property (T@"CFXPreviewViewController",&,N,V_internalPreviewViewController) internalPreviewViewController;
@property (T@"CFXReviewControlsViewController",&,N,V_reviewControlsViewController) reviewControlsViewController;
@property (T@"NSString",&,N,V_effectBrowserPresentedAppIdentifier) effectBrowserPresentedAppIdentifier;
@property (T@"CFXMediaItem",&,N,V_mediaItem) mediaItem;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_metadataReaderGroup) metadataReaderGroup;
@property (TB,R,N) mediaCapturedInFunCam;
@property (TB,N,V_mediaCapturedInFunCam_metadata) mediaCapturedInFunCam_metadata;
@property (Tq,R,N) mediaCaptureDevicePosition;
@property (Tq,N,V_mediaInterfaceOrientationForDisplay_metadata) mediaInterfaceOrientationForDisplay_metadata;
@property (T@"NSData",R,N) animojiMetadata;
@property (T@"NSData",&,N,V_animojiMetadata_metadata) animojiMetadata_metadata;
@property (Tq,N,V_cameraModeUsedForCapture) cameraModeUsedForCapture;
@property (T@"NSData",R,C,N) adjustmentsData;
@property (T@"<CFXReviewViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N) effectsPickerDrawer;
@property (TB,R,N) mediaItemRequiresExport;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXReviewViewController initialize];
```

## Instance methods

```
-[CFXReviewViewController mediaItem];
-[CFXReviewViewController viewDidLoad];
-[CFXReviewViewController viewDidLayoutSubviews];
-[CFXReviewViewController setDelegate:];
-[CFXReviewViewController viewDidAppear:];
-[CFXReviewViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[CFXReviewViewController loadView];
-[CFXReviewViewController delegate];
-[CFXReviewViewController adjustmentsData];
-[CFXReviewViewController initWithMediaItem:];
-[CFXReviewViewController setMediaItem:];
-[CFXReviewViewController effectBrowserViewController:didDismissPickerForEffectType:];
-[CFXReviewViewController effectBrowserViewController:didSelectAppWithIdentifier:];
-[CFXReviewViewController effectBrowserViewController:didSelectEffect:];
-[CFXReviewViewController effectBrowserViewController:willChangeDockHeight:];
-[CFXReviewViewController setEffectsPickerDrawer:];
-[CFXReviewViewController shouldAlwaysPresentExpandedAppsForEffectBrowserViewController:];
-[CFXReviewViewController showMemojiPicker:];
-[CFXReviewViewController CFX_resetAndLoadPreviewViewController];
-[CFXReviewViewController CFX_updateAnalyticsForSentMediaItem:];
-[CFXReviewViewController animojiMetadata];
-[CFXReviewViewController setEffectBrowserViewController:];
-[CFXReviewViewController allowLandscapeForEffectBrowserViewController:];
-[CFXReviewViewController animojiMetadata_metadata];
-[CFXReviewViewController calculateMediaInterfaceOrientationForDisplay];
-[CFXReviewViewController cameraModeUsedForCapture];
-[CFXReviewViewController effectBrowserPresentedAppIdentifier];
-[CFXReviewViewController effectBrowserViewController];
-[CFXReviewViewController effectBrowserViewController:didDropOverlayEffect:atScreenLocation:atScreenSize:rotationAngle:];
-[CFXReviewViewController effectBrowserViewController:didPresentPickerForEffectType:];
-[CFXReviewViewController effectBrowserViewController:didRemoveAllEffectsOfType:];
-[CFXReviewViewController effectBrowserViewController:filterPickerPreviewBackgroundImageAtSizeInPixels:completion:];
-[CFXReviewViewController effectBrowserViewController:screenTopBarHeightForWindowBounds:orientation:];
-[CFXReviewViewController effectsPickerDrawer];
-[CFXReviewViewController exportMediaItemToFileURL:];
-[CFXReviewViewController internalPreviewViewController];
-[CFXReviewViewController localizedPromptForHidingAnimojiForEffectBrowserViewController:];
-[CFXReviewViewController mediaCaptureDevicePosition];
-[CFXReviewViewController mediaCapturedInFunCam];
-[CFXReviewViewController mediaCapturedInFunCam_metadata];
-[CFXReviewViewController mediaInterfaceOrientationForDisplay_metadata];
-[CFXReviewViewController mediaItemForEffectBrowserViewController:];
-[CFXReviewViewController mediaItemRequiresExport];
-[CFXReviewViewController metadataReaderGroup];
-[CFXReviewViewController preferredDisplayColorSpace];
-[CFXReviewViewController preferredExportColorSpace];
-[CFXReviewViewController previewViewController:didFinishExportingMediaItem:withError:];
-[CFXReviewViewController previewViewController:didProgress:exportingMediaItem:];
-[CFXReviewViewController previewViewController:didStartExportingMediaItem:];
-[CFXReviewViewController previewViewControllerDidHideUserInterface:];
-[CFXReviewViewController previewViewControllerDidShowUserInterface:];
-[CFXReviewViewController previewViewControllerDidStartEditingText:];
-[CFXReviewViewController previewViewControllerDidStopEditingText:];
-[CFXReviewViewController reviewControlsViewController];
-[CFXReviewViewController selectedAnimojiIdentifierForEffectBrowserViewController:];
-[CFXReviewViewController selectedAppIdentifierForPreviewViewController:];
-[CFXReviewViewController selectedFilterIdentifierForEffectBrowserViewController:];
-[CFXReviewViewController setAnimojiMetadata_metadata:];
-[CFXReviewViewController setCameraModeUsedForCapture:];
-[CFXReviewViewController setEffectBrowserPresentedAppIdentifier:];
-[CFXReviewViewController setInternalPreviewViewController:];
-[CFXReviewViewController setMediaCapturedInFunCam_metadata:];
-[CFXReviewViewController setMediaInterfaceOrientationForDisplay_metadata:];
-[CFXReviewViewController setMetadataReaderGroup:];
-[CFXReviewViewController setReviewControlsViewController:];
```
