# `AVAssetWriterInputTaggedPixelBufferGroupAdaptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"AVAssetWriterInput" _input;
```

## Properties

```
@property (T@"AVAssetWriterInput",R,N) assetWriterInput;
@property (T@"NSDictionary",R,N) sourcePixelBufferAttributes;
@property (T^{__CVPixelBufferPool=},R,N) pixelBufferPool;
```

## Class methods

```
+[AVAssetWriterInputTaggedPixelBufferGroupAdaptor assetWriterInputTaggedPixelBufferGroupAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:];
```

## Instance methods

```
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor pixelBufferPool];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor init];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor dealloc];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor description];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor initWithAssetWriterInput:sourcePixelBufferAttributes:];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor sourcePixelBufferAttributes];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputTaggedPixelBufferGroupAdaptor assetWriterInput];
```
