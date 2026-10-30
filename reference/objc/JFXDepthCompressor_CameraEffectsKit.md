# `JFXDepthCompressor`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 19 instance methods, 6 class methods

## Instance variables

```
@"JFXVideoEncoderInterface" _videoEncoderInterface;
^{opaqueCMFormatDescription=} _previousFormatDescription;
i _depthCodecType;
```

## Properties

```
@property (Ti,R,N,V_depthCodecType) depthCodecType;
```

## Class methods

```
+[JFXDepthCompressor NSDataFromFloatDepth32:];
+[JFXDepthCompressor NSDataFromDepthMapInsideAVDepthData:];
+[JFXDepthCompressor decapsulatePayload:];
+[JFXDepthCompressor encapsulatePayload:];
+[JFXDepthCompressor fakeAuxDepthInfoDictionaryForCVPixelBuffer:];
+[JFXDepthCompressor fakeXMPDataIfNotFound];
```

## Instance methods

```
-[JFXDepthCompressor dealloc];
-[JFXDepthCompressor hevcSEIPayload:];
-[JFXDepthCompressor compressAVDepthData:timingInfo:error:];
-[JFXDepthCompressor compressAVDepthData_BGRA:timingInfo:error:];
-[JFXDepthCompressor compressAVDepthData_HEVC10:timingInfo:error:];
-[JFXDepthCompressor compressAVDepthData_LZ:timingInfo:error:];
-[JFXDepthCompressor compressAVDepthData_Photo:timingInfo:error:];
-[JFXDepthCompressor compressDepthMapCVPixelBuffer:timingInfo:error:];
-[JFXDepthCompressor copyDepthBufferAsBGRA:];
-[JFXDepthCompressor depthCodecType];
-[JFXDepthCompressor depthFormatDescriptionForDepthDimensions:];
-[JFXDepthCompressor depthOutputSettingsForDepthDimensions:];
-[JFXDepthCompressor depthSampleBufferAppendingDepthMetadata:depthSampleBufferFromCodec:];
-[JFXDepthCompressor depthSampleBufferWithNewHVCCWithDepthMetadata:depthSampleBufferFromCodec:];
-[JFXDepthCompressor getPayloadTypeOrSize:offsetPointer:];
-[JFXDepthCompressor hevcSEIMessageDataWithDepthXMPMetadata:isPrefixSEI:nuh_layer_id:nuh_temporal_id_plus1:];
-[JFXDepthCompressor hevcSEIPayloadHeaderForPayloadType:payloadSize:];
-[JFXDepthCompressor initWithDepthCodecType:];
-[JFXDepthCompressor mutableCopyExtensionsDictionaryCopyFromAVDepthData:];
```
