# `AVAssetWriterInputPixelBufferAdaptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVWeakObservable`, `AVKeyPathDependencyHost`
- 1 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVAssetWriterInputPixelBufferAdaptorInternal" _internal;
```

## Properties

```
@property (T@"AVAssetWriterInput",R,N) assetWriterInput;
@property (T@"NSDictionary",R,N) sourcePixelBufferAttributes;
@property (T^{__CVPixelBufferPool=},R,N) pixelBufferPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAssetWriterInputPixelBufferAdaptor assetWriterInputPixelBufferAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:];
```

## Instance methods

```
-[AVAssetWriterInputPixelBufferAdaptor pixelBufferPool];
-[AVAssetWriterInputPixelBufferAdaptor init];
-[AVAssetWriterInputPixelBufferAdaptor dealloc];
-[AVAssetWriterInputPixelBufferAdaptor description];
-[AVAssetWriterInputPixelBufferAdaptor appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputPixelBufferAdaptor initWithAssetWriterInput:sourcePixelBufferAttributes:];
-[AVAssetWriterInputPixelBufferAdaptor sourcePixelBufferAttributes];
-[AVAssetWriterInputPixelBufferAdaptor addCallbackToCancelDuringDeallocation:];
-[AVAssetWriterInputPixelBufferAdaptor assetWriterInput];
-[AVAssetWriterInputPixelBufferAdaptor declareKeyPathDependenciesWithRegistry:];
```
