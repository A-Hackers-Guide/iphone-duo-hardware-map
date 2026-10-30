# `BWRenderListProcessorPixelBufferJuggler`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _cachedPixelBuffer;
^{__CVBuffer=} _bufferToDrop;
@"NSString" _name;
@"<BWPixelBufferProvider>" _backingProvider;
```

## Properties

```
@property (T@"<BWPixelBufferProvider>",R,N,V_backingProvider) backingProvider;
```

## Instance methods

```
-[BWRenderListProcessorPixelBufferJuggler flush];
-[BWRenderListProcessorPixelBufferJuggler dealloc];
-[BWRenderListProcessorPixelBufferJuggler newPixelBuffer];
-[BWRenderListProcessorPixelBufferJuggler backingProvider];
-[BWRenderListProcessorPixelBufferJuggler initWithBackingProvider:bufferToDrop:name:];
-[BWRenderListProcessorPixelBufferJuggler returnPixelBuffer:];
-[BWRenderListProcessorPixelBufferJuggler setBufferToDrop:];
```
