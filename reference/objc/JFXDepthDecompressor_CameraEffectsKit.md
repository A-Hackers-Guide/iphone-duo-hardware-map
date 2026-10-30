# `JFXDepthDecompressor`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 9 instance methods, 4 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _previousFormatDescription;
@"JFXVideoDecoderInterface" _videoDecoderInterface;
i _depthCodecType;
```

## Properties

```
@property (Ti,R,N,V_depthCodecType) depthCodecType;
```

## Class methods

```
+[JFXDepthDecompressor NSDataWithCMBlockBuffer:range:];
+[JFXDepthDecompressor bitDepthOf:];
+[JFXDepthDecompressor dataWithCMSampleBuffer:];
+[JFXDepthDecompressor trackOptionsForDepthCodecType:error:];
```

## Instance methods

```
-[JFXDepthDecompressor init];
-[JFXDepthDecompressor dealloc];
-[JFXDepthDecompressor decompressAVDepthData_LZ:error:];
-[JFXDepthDecompressor decompressAVDepthData:error:];
-[JFXDepthDecompressor decompressAVDepthData_BGRA:error:];
-[JFXDepthDecompressor decompressAVDepthData_HEVC10:error:];
-[JFXDepthDecompressor decompressAVDepthData_Photo:error:];
-[JFXDepthDecompressor depthCodecType];
-[JFXDepthDecompressor incompleteImageSourceAuxDataInfoDict:error:];
```
