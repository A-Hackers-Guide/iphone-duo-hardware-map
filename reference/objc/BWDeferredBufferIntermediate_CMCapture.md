# `BWDeferredBufferIntermediate`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWDeferredIntermediate`
- 16 instance variables, 17 properties, 31 instance methods, 1 class methods

## Instance variables

```
^{__CVBuffer=} _buffer;
@"NSDictionary" _attributes;
@"NSString" _metadataTag;
Q _bufferType;
Q _captureFrameFlags;
@"NSString" _rawThumbnailsBufferTag;
@"NSString" _rawThumbnailsMetadataTag;
@"NSString" _mainRawThumbnailBufferTag;
@"NSString" _mainRawThumbnailMetadataTag;
@"NSString" _sifrRawThumbnailBufferTag;
@"NSString" _sifrRawThumbnailMetadataTag;
@"NSString" _hueMapBufferTag;
@"NSString" _hueMapMetadataTag;
@"NSString" _portType;
i _compressionProfile;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _compressionCropRect;
```

## Properties

```
@property (T^{__CVBuffer=},R,N,V_buffer) buffer;
@property (TQ,R,N,V_bufferType) bufferType;
@property (TQ,R,N,V_captureFrameFlags) captureFrameFlags;
@property (T@"NSDictionary",R,N,V_attributes) attributes;
@property (T@"NSString",R,N,V_metadataTag) metadataTag;
@property (T@"NSString",R,N,V_rawThumbnailsBufferTag) rawThumbnailsBufferTag;
@property (T@"NSString",R,N,V_rawThumbnailsMetadataTag) rawThumbnailsMetadataTag;
@property (T@"NSString",R,N,V_mainRawThumbnailBufferTag) mainRawThumbnailBufferTag;
@property (T@"NSString",R,N,V_mainRawThumbnailMetadataTag) mainRawThumbnailMetadataTag;
@property (T@"NSString",R,N,V_sifrRawThumbnailBufferTag) sifrRawThumbnailBufferTag;
@property (T@"NSString",R,N,V_sifrRawThumbnailMetadataTag) sifrRawThumbnailMetadataTag;
@property (T@"NSString",R,N,V_hueMapBufferTag) hueMapBufferTag;
@property (T@"NSString",R,N,V_hueMapMetadataTag) hueMapMetadataTag;
@property (T@"NSString",R,N,V_portType) portType;
@property (Ti,R,N,V_compressionProfile) compressionProfile;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_compressionCropRect) compressionCropRect;
@property (T@"NSString",R,N) attachedMediaKey;
```

## Class methods

```
+[BWDeferredBufferIntermediate supportsSecureCoding];
```

## Instance methods

```
-[BWDeferredBufferIntermediate buffer];
-[BWDeferredBufferIntermediate setBuffer:];
-[BWDeferredBufferIntermediate portType];
-[BWDeferredBufferIntermediate flush];
-[BWDeferredBufferIntermediate dealloc];
-[BWDeferredBufferIntermediate encodeWithCoder:];
-[BWDeferredBufferIntermediate description];
-[BWDeferredBufferIntermediate initWithCoder:];
-[BWDeferredBufferIntermediate pixelFormat];
-[BWDeferredBufferIntermediate attributes];
-[BWDeferredBufferIntermediate fetchAndRetain:];
-[BWDeferredBufferIntermediate hueMapBufferTag];
-[BWDeferredBufferIntermediate _shortString];
-[BWDeferredBufferIntermediate archive:];
-[BWDeferredBufferIntermediate attachedMediaKey];
-[BWDeferredBufferIntermediate bufferType];
-[BWDeferredBufferIntermediate captureFrameFlags];
-[BWDeferredBufferIntermediate compressionCropRect];
-[BWDeferredBufferIntermediate compressionProfile];
-[BWDeferredBufferIntermediate hueMapMetadataTag];
-[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:portType:compressionProfile:URL:];
-[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:compressionCropRect:URL:];
-[BWDeferredBufferIntermediate mainRawThumbnailBufferTag];
-[BWDeferredBufferIntermediate mainRawThumbnailMetadataTag];
-[BWDeferredBufferIntermediate metadataTag];
-[BWDeferredBufferIntermediate rawThumbnailsBufferTag];
-[BWDeferredBufferIntermediate rawThumbnailsMetadataTag];
-[BWDeferredBufferIntermediate releaseBuffer];
-[BWDeferredBufferIntermediate setURL:prefetchQueue:];
-[BWDeferredBufferIntermediate sifrRawThumbnailBufferTag];
-[BWDeferredBufferIntermediate sifrRawThumbnailMetadataTag];
```
