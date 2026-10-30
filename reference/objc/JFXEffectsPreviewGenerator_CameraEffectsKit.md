# `JFXEffectsPreviewGenerator`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"PVRenderer" _renderer;
@"NSString" _name;
@"NSObject<OS_dispatch_queue>" _renderCompleteQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_renderCompleteQueue) renderCompleteQueue;
@property (T@"NSString",&,N,V_name) name;
```

## Instance methods

```
-[JFXEffectsPreviewGenerator clearCaches];
-[JFXEffectsPreviewGenerator init];
-[JFXEffectsPreviewGenerator dealloc];
-[JFXEffectsPreviewGenerator colorSpace];
-[JFXEffectsPreviewGenerator setName:];
-[JFXEffectsPreviewGenerator name];
-[JFXEffectsPreviewGenerator perfLog];
-[JFXEffectsPreviewGenerator _renderJob:completionHandler:];
-[JFXEffectsPreviewGenerator generatePreviewRequest:completionHandler:];
-[JFXEffectsPreviewGenerator initWithRendererOptions:];
-[JFXEffectsPreviewGenerator renderCompleteQueue];
-[JFXEffectsPreviewGenerator setRenderCompleteQueue:];
-[JFXEffectsPreviewGenerator trackStats:];
```
