# `BWPhotoEncoderManager` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 15 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) containerSize;
```

## Instance methods

```
-[BWPhotoEncoderManager containerSize];
-[BWPhotoEncoderManager isContainerOpen];
-[BWPhotoEncoderManager addAlternateImageWithDerivedImageHandles:options:parentImageHandle:alternateGroupHandleInOut:];
-[BWPhotoEncoderManager addAuxImage:type:auxImageMetadata:options:parentImageHandle:auxImageHandleOut:];
-[BWPhotoEncoderManager addAuxImageMetadata:type:auxImageHandle:options:parentImageHandle:];
-[BWPhotoEncoderManager addCompressedThumbnailImage:thumbnailImageSize:options:];
-[BWPhotoEncoderManager addCustomMetadataContents:URI:name:];
-[BWPhotoEncoderManager addMainImage:metadata:options:imageHandleOut:];
-[BWPhotoEncoderManager addMetadata:parentImageHandle:];
-[BWPhotoEncoderManager addThumbnailImage:options:parentImageHandle:];
-[BWPhotoEncoderManager closeContainer];
-[BWPhotoEncoderManager closeContainerAndCopySurfaceOut:];
-[BWPhotoEncoderManager openContainerWithOptions:settingsID:];
-[BWPhotoEncoderManager openExistingContainer:options:];
-[BWPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:];
```
