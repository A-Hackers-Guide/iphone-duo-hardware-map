# `_UIDragPreviewBlockProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDragPreviewProvider`
- 3 instance variables, 6 properties, 5 instance methods, 1 class methods

## Instance variables

```
@? _previewProviderBlock;
@"_UIDraggingImageComponent" _imageComponent;
@"UIDragPreview" _preview;
```

## Properties

```
@property (T@"<_UIDragPreviewProvider>",R,N) _dragPreviewProvider;
@property (T@"UIDragPreview",R,N,V_preview) preview;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDragPreviewBlockProvider previewProviderWithBlock:];
```

## Instance methods

```
-[_UIDragPreviewBlockProvider preview];
-[_UIDragPreviewBlockProvider imageComponent];
-[_UIDragPreviewBlockProvider _duiPreview];
-[_UIDragPreviewBlockProvider _dragPreviewProvider];
-[_UIDragPreviewBlockProvider _createImageComponent];
```
