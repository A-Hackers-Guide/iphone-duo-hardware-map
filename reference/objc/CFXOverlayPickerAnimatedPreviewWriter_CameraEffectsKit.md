# `CFXOverlayPickerAnimatedPreviewWriter`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 14 properties, 32 instance methods, 0 class methods

## Instance variables

```
^{CGImageDestination=} _imageDestination;
B _isFirstAnimatedFrame;
@"JFXOverlayEffect" _overlay;
@"NSString" _destinationPath;
@"NSDictionary" _frameProperties;
Q _currentFrameCount;
Q _previewFrameRate;
d _previewDuration;
Q _previewStartFrameIndex;
Q _targetFrameCount;
@"JFXEffectsPreviewGenerator" _previewGenerator;
@"NSObject<OS_dispatch_queue>" _writerQueue;
@? _completionBlock;
{CGSize="width"d"height"d} _previewSizeInPixels;
{?="value"q"timescale"i"flags"I"epoch"q} _currentRenderTime;
```

## Properties

```
@property (T@"JFXOverlayEffect",&,N,V_overlay) overlay;
@property (T{CGSize=dd},R,N,V_previewSizeInPixels) previewSizeInPixels;
@property (T@"NSString",&,N,V_destinationPath) destinationPath;
@property (T@"NSDictionary",&,N,V_frameProperties) frameProperties;
@property (TQ,N,V_currentFrameCount) currentFrameCount;
@property (TQ,N,V_previewFrameRate) previewFrameRate;
@property (Td,N,V_previewDuration) previewDuration;
@property (TQ,N,V_previewStartFrameIndex) previewStartFrameIndex;
@property (TQ,N,V_targetFrameCount) targetFrameCount;
@property (T{?=qiIq},N,V_currentRenderTime) currentRenderTime;
@property (T@"JFXEffectsPreviewGenerator",&,N,V_previewGenerator) previewGenerator;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_writerQueue) writerQueue;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TB,N,V_isFirstAnimatedFrame) isFirstAnimatedFrame;
```

## Instance methods

```
-[CFXOverlayPickerAnimatedPreviewWriter setCompletionBlock:];
-[CFXOverlayPickerAnimatedPreviewWriter completionBlock];
-[CFXOverlayPickerAnimatedPreviewWriter setOverlay:];
-[CFXOverlayPickerAnimatedPreviewWriter overlay];
-[CFXOverlayPickerAnimatedPreviewWriter previewDuration];
-[CFXOverlayPickerAnimatedPreviewWriter currentFrameCount];
-[CFXOverlayPickerAnimatedPreviewWriter setCurrentFrameCount:];
-[CFXOverlayPickerAnimatedPreviewWriter destinationPath];
-[CFXOverlayPickerAnimatedPreviewWriter setDestinationPath:];
-[CFXOverlayPickerAnimatedPreviewWriter previewGenerator];
-[CFXOverlayPickerAnimatedPreviewWriter frameProperties];
-[CFXOverlayPickerAnimatedPreviewWriter setFrameProperties:];
-[CFXOverlayPickerAnimatedPreviewWriter CFX_initializeEffectForPreviewing];
-[CFXOverlayPickerAnimatedPreviewWriter CFX_writeNextEffectFrame];
-[CFXOverlayPickerAnimatedPreviewWriter CFX_beginWriting];
-[CFXOverlayPickerAnimatedPreviewWriter CFX_finishWriting];
-[CFXOverlayPickerAnimatedPreviewWriter currentRenderTime];
-[CFXOverlayPickerAnimatedPreviewWriter initWithOverlayEffectId:previewSizeInPixels:previewDuration:previewFrameRate:previewStartFrameIndex:];
-[CFXOverlayPickerAnimatedPreviewWriter isFirstAnimatedFrame];
-[CFXOverlayPickerAnimatedPreviewWriter previewFrameRate];
-[CFXOverlayPickerAnimatedPreviewWriter previewSizeInPixels];
-[CFXOverlayPickerAnimatedPreviewWriter previewStartFrameIndex];
-[CFXOverlayPickerAnimatedPreviewWriter setCurrentRenderTime:];
-[CFXOverlayPickerAnimatedPreviewWriter setIsFirstAnimatedFrame:];
-[CFXOverlayPickerAnimatedPreviewWriter setPreviewDuration:];
-[CFXOverlayPickerAnimatedPreviewWriter setPreviewFrameRate:];
-[CFXOverlayPickerAnimatedPreviewWriter setPreviewGenerator:];
-[CFXOverlayPickerAnimatedPreviewWriter setPreviewStartFrameIndex:];
-[CFXOverlayPickerAnimatedPreviewWriter setTargetFrameCount:];
-[CFXOverlayPickerAnimatedPreviewWriter targetFrameCount];
-[CFXOverlayPickerAnimatedPreviewWriter writeAnimatedPreviewToPath:completion:];
-[CFXOverlayPickerAnimatedPreviewWriter writerQueue];
```
