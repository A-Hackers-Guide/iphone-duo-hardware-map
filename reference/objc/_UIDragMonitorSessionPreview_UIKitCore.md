# `_UIDragMonitorSessionPreview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_DUIImageComponent" _imageComponent;
@"_DUIPreview" _preview;
@"UIDragPreviewParameters" _parameters;
```

## Properties

```
@property (T@"_DUIImageComponent",&,N,V_imageComponent) imageComponent;
@property (T@"_DUIPreview",&,N,V_preview) preview;
@property (T@"UIDragPreviewParameters",R,N,V_parameters) parameters;
@property (T{CGSize=dd},R) previewScaledSize;
@property (T{CGSize=dd},R) previewContentSize;
@property (T{CGPoint=dd},R) previewContentOffset;
@property (T{CGPoint=dd},R) center;
@property (T@"UIImage",R,N) previewImage;
@property (T@"UIBezierPath",R,N) outline;
```

## Instance methods

```
-[_UIDragMonitorSessionPreview preview];
-[_UIDragMonitorSessionPreview parameters];
-[_UIDragMonitorSessionPreview setPreview:];
-[_UIDragMonitorSessionPreview previewImage];
-[_UIDragMonitorSessionPreview imageComponent];
-[_UIDragMonitorSessionPreview center];
-[_UIDragMonitorSessionPreview outline];
-[_UIDragMonitorSessionPreview initWithImageComponent:preview:];
-[_UIDragMonitorSessionPreview previewContentOffset];
-[_UIDragMonitorSessionPreview previewContentSize];
-[_UIDragMonitorSessionPreview previewImageWithSnapshotSettings:];
-[_UIDragMonitorSessionPreview previewScaledSize];
-[_UIDragMonitorSessionPreview setImageComponent:];
```
