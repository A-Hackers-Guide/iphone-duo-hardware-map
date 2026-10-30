# `BWCoreMotionMetadataSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSourceNode`
- 10 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"CMMotionManager" _motionManager;
i _bufferGenerationRate;
i _samplesPerBuffer;
B _running;
^{BWCoreMotionMetadataSampleData=IIdddddfff} _sampleDataForBuffer;
i _numSamplesInBuffer;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
I _localIDOfCoreMotionMetadata_BE;
@"NSObject<OS_dispatch_queue>" _emitSamplesDispatchQueue;
^{opaqueCMFormatDescription=} _formatDescription;
```

## Properties

```
@property (T^{opaqueCMFormatDescription=},R,N,V_formatDescription) formatDescription;
```

## Class methods

```
+[BWCoreMotionMetadataSourceNode initialize];
+[BWCoreMotionMetadataSourceNode extractBWCoreMotionMetadataFromBlockBuffer:intoNativeEndianSampleData:];
+[BWCoreMotionMetadataSourceNode extractBWCoreMotionMetadataFromSampleBuffer:intoNativeEndianSampleData:];
```

## Instance methods

```
-[BWCoreMotionMetadataSourceNode formatDescription];
-[BWCoreMotionMetadataSourceNode start:];
-[BWCoreMotionMetadataSourceNode clock];
-[BWCoreMotionMetadataSourceNode dealloc];
-[BWCoreMotionMetadataSourceNode stop:];
-[BWCoreMotionMetadataSourceNode nodeSubType];
-[BWCoreMotionMetadataSourceNode initWithBufferGenerationRate:samplesPerBuffer:];
```
