# `BWCMPhotoEncoderManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPhotoEncoderManager`
- 5 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{CMPhotoCompressionSession=} _photoCompressionSession;
q _currentSettingsID;
Q _containerSize;
i _containerFormat;
B _asyncEncoding;
```

## Properties

```
@property (TQ,R,N) containerSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCMPhotoEncoderManager initialize];
```

## Instance methods

```
-[BWCMPhotoEncoderManager containerSize];
-[BWCMPhotoEncoderManager dealloc];
-[BWCMPhotoEncoderManager description];
-[BWCMPhotoEncoderManager isContainerOpen];
-[BWCMPhotoEncoderManager addAlternateImageWithDerivedImageHandles:options:parentImageHandle:alternateGroupHandleInOut:];
-[BWCMPhotoEncoderManager addAuxImage:type:auxImageMetadata:options:parentImageHandle:auxImageHandleOut:];
-[BWCMPhotoEncoderManager addAuxImageMetadata:type:auxImageHandle:options:parentImageHandle:];
-[BWCMPhotoEncoderManager addCompressedThumbnailImage:thumbnailImageSize:options:];
-[BWCMPhotoEncoderManager addCustomMetadataContents:URI:name:];
-[BWCMPhotoEncoderManager addMainImage:metadata:options:imageHandleOut:];
-[BWCMPhotoEncoderManager addMetadata:parentImageHandle:];
-[BWCMPhotoEncoderManager addThumbnailImage:options:parentImageHandle:];
-[BWCMPhotoEncoderManager closeContainer];
-[BWCMPhotoEncoderManager closeContainerAndCopySurfaceOut:];
-[BWCMPhotoEncoderManager initWithDeferredPhotoProcessorEnabled:];
-[BWCMPhotoEncoderManager openContainerWithOptions:settingsID:];
-[BWCMPhotoEncoderManager openExistingContainer:options:];
-[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:];
```
