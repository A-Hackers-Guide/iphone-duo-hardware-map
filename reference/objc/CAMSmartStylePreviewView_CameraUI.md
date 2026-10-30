# `CAMSmartStylePreviewView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NUMediaViewDelegatePrivate`
- 12 instance variables, 19 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _didFinishRendering;
B __hasUpdatedZoomForComposition;
@"<CAMSmartStylePreviewViewDelegate>" _delegate;
@"CAMSmartStyleSettingsResourceLoadResult" _resourceLoadResult;
@"CEKSmartStyle" _style;
@"CEKTextureStyle" _textureStyle;
@"NSString" _logIdentifier;
@"NUMediaView" __mediaView;
@"NUComposition" __composition;
d __baseZoomScale;
d __zoomScale;
@"PICompositionController" __compositionController;
```

## Properties

```
@property (T@"NUMediaView",R,N,V__mediaView) _mediaView;
@property (T@"NUComposition",R,N,V__composition) _composition;
@property (TB,R,N,V__hasUpdatedZoomForComposition) _hasUpdatedZoomForComposition;
@property (Td,N,V__baseZoomScale) _baseZoomScale;
@property (Td,N,V__zoomScale) _zoomScale;
@property (T@"PICompositionController",R,N,V__compositionController) _compositionController;
@property (T@"<PEAsset>",R,N) _asset;
@property (T@"NSURL",R,N) _fileURL;
@property (T@"NSDictionary",R,N) _fileURLImageProperties;
@property (TB,N,S_setDidFinishRendering:,V_didFinishRendering) didFinishRendering;
@property (T@"<CAMSmartStylePreviewViewDelegate>",W,N,V_delegate) delegate;
@property (T@"CAMSmartStyleSettingsResourceLoadResult",&,N,V_resourceLoadResult) resourceLoadResult;
@property (T@"CEKSmartStyle",&,N,V_style) style;
@property (T@"CEKTextureStyle",&,N,V_textureStyle) textureStyle;
@property (T@"NSString",C,N,V_logIdentifier) logIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSmartStylePreviewView speedUpFadeInAnimations];
-[CAMSmartStylePreviewView _zoomScale];
-[CAMSmartStylePreviewView set_zoomScale:];
-[CAMSmartStylePreviewView set_baseZoomScale:];
-[CAMSmartStylePreviewView _hasUpdatedZoomForComposition];
-[CAMSmartStylePreviewView textureStyle];
-[CAMSmartStylePreviewView _fileURLImageProperties];
-[CAMSmartStylePreviewView _updatePreviewAdjustments];
-[CAMSmartStylePreviewView _setDidFinishRendering:];
-[CAMSmartStylePreviewView setZoomScale:animated:];
-[CAMSmartStylePreviewView setLogIdentifier:];
-[CAMSmartStylePreviewView _compositionController];
-[CAMSmartStylePreviewView style];
-[CAMSmartStylePreviewView setTextureStyle:];
-[CAMSmartStylePreviewView _composition];
-[CAMSmartStylePreviewView setStyle:];
-[CAMSmartStylePreviewView setResourceLoadResult:];
-[CAMSmartStylePreviewView logIdentifier];
-[CAMSmartStylePreviewView setDelegate:];
-[CAMSmartStylePreviewView _mediaView];
-[CAMSmartStylePreviewView _updateMediaViewZoomIfNecessary];
-[CAMSmartStylePreviewView resourceLoadResult];
-[CAMSmartStylePreviewView _addConstraints];
-[CAMSmartStylePreviewView delegate];
-[CAMSmartStylePreviewView didFinishRendering];
-[CAMSmartStylePreviewView _fileURL];
-[CAMSmartStylePreviewView _asset];
-[CAMSmartStylePreviewView setSmartStyle:textureStyle:];
-[CAMSmartStylePreviewView _baseZoomScale];
-[CAMSmartStylePreviewView mediaViewDidFinishRendering:withStatistics:];
-[CAMSmartStylePreviewView initWithFrame:];
-[CAMSmartStylePreviewView _setComposition:];
```
