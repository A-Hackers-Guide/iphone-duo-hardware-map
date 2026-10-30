# `BWDNGEncoderManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPhotoEncoderManager`
- 5 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
^{CMPhotoDNGCompressor=} _dngCompressor;
q _currentSettingsID;
Q _previewImageSize;
Q _auxiliaryImagesSize;
Q _containerSize;
```

## Properties

```
@property (TQ,R,N) auxiliaryImagesSize;
@property (TQ,R,N) thumbnailImageSize;
@property (TQ,R,N) containerSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWDNGEncoderManager initialize];
```

## Instance methods

```
-[BWDNGEncoderManager containerSize];
-[BWDNGEncoderManager dealloc];
-[BWDNGEncoderManager description];
-[BWDNGEncoderManager auxiliaryImagesSize];
-[BWDNGEncoderManager thumbnailImageSize];
-[BWDNGEncoderManager isContainerOpen];
-[BWDNGEncoderManager addAlternateImageWithDerivedImageHandles:options:parentImageHandle:alternateGroupHandleInOut:];
-[BWDNGEncoderManager addAuxImage:type:auxImageMetadata:options:parentImageHandle:auxImageHandleOut:];
-[BWDNGEncoderManager addAuxImageMetadata:type:auxImageHandle:options:parentImageHandle:];
-[BWDNGEncoderManager addCompressedThumbnailImage:thumbnailImageSize:options:];
-[BWDNGEncoderManager addCustomMetadataContents:URI:name:];
-[BWDNGEncoderManager addMainImage:metadata:options:imageHandleOut:];
-[BWDNGEncoderManager addMetadata:parentImageHandle:];
-[BWDNGEncoderManager addThumbnailImage:options:parentImageHandle:];
-[BWDNGEncoderManager closeContainer];
-[BWDNGEncoderManager closeContainerAndCopySurfaceOut:];
-[BWDNGEncoderManager openContainerWithOptions:settingsID:];
-[BWDNGEncoderManager openExistingContainer:options:];
-[BWDNGEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:];
```
