# `CMISoftwareFlashRenderingProcessor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MetalImageBufferProcessor`
- 0 instance variables, 5 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"<CMISoftwareFlashRenderingProcessorDelegate>",W,N) delegate;
@property (T^{__CVBuffer=},&,N) outputImagePixelBuffer;
@property (T@"NSMutableDictionary",&,N) outputImageMetadata;
@property (T^{__CVBuffer=},&,N) linearOutputImagePixelBuffer;
@property (T@"NSMutableDictionary",&,N) linearOutputImageMetadata;
```

## Instance methods

```
-[CMISoftwareFlashRenderingProcessor setDelegate:];
-[CMISoftwareFlashRenderingProcessor delegate];
-[CMISoftwareFlashRenderingProcessor addFrame:metadata:frameType:frameParams:];
-[CMISoftwareFlashRenderingProcessor linearOutputImageMetadata];
-[CMISoftwareFlashRenderingProcessor linearOutputImagePixelBuffer];
-[CMISoftwareFlashRenderingProcessor outputImageMetadata];
-[CMISoftwareFlashRenderingProcessor outputImagePixelBuffer];
-[CMISoftwareFlashRenderingProcessor setLinearOutputImageMetadata:];
-[CMISoftwareFlashRenderingProcessor setLinearOutputImagePixelBuffer:];
-[CMISoftwareFlashRenderingProcessor setOutputImageMetadata:];
-[CMISoftwareFlashRenderingProcessor setOutputImagePixelBuffer:];
```
