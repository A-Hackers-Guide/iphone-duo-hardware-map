# `CAMDisabledPreviewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<CAMDisabledPreviewControllerDelegate>" _delegate;
@"NSMutableSet" __reasonsForDisablingPreview;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__reasonsForDisablingPreview) _reasonsForDisablingPreview;
@property (T@"<CAMDisabledPreviewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisPreviewDisabled) previewDisabled;
```

## Instance methods

```
-[CAMDisabledPreviewController init];
-[CAMDisabledPreviewController _descriptionForReasons:];
-[CAMDisabledPreviewController isPreviewDisabled];
-[CAMDisabledPreviewController setDelegate:];
-[CAMDisabledPreviewController delegate];
-[CAMDisabledPreviewController _descriptionStringForReason:];
-[CAMDisabledPreviewController _reasonsForDisablingPreview];
-[CAMDisabledPreviewController addDisabledPreviewReason:];
-[CAMDisabledPreviewController removeDisabledPreviewReason:];
```
