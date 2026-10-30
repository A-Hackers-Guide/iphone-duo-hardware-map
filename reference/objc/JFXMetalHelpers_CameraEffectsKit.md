# `JFXMetalHelpers`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"<MTLDevice>" m_device;
```

## Class methods

```
+[JFXMetalHelpers copyMetalLibraryWithDevice:error:];
+[JFXMetalHelpers createCVTextureFromImage:withTextureCache:];
+[JFXMetalHelpers metalPixelFormatForImage:];
```

## Instance methods

```
-[JFXMetalHelpers initWithDevice:];
-[JFXMetalHelpers device];
-[JFXMetalHelpers newPipelineStateForFunctionWithName:];
-[JFXMetalHelpers newTexture:];
-[JFXMetalHelpers newTextureWithSameSizeAs:pixelFormat:];
-[JFXMetalHelpers newTextureWithWidth:height:pixelFormat:usage:];
-[JFXMetalHelpers runComputeEncoder:pipelineState:referenceTexture:];
```
