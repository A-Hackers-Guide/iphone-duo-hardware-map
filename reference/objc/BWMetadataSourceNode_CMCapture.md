# `BWMetadataSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSourceNode`
- 4 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _running;
^{opaqueCMFormatDescription=} _formatDescription;
^{OpaqueCMClock=} _clock;
@"NSObject<OS_dispatch_queue>" _emitSamplesDispatchQueue;
```

## Properties

```
@property (T^{opaqueCMFormatDescription=},R,N,V_formatDescription) formatDescription;
```

## Class methods

```
+[BWMetadataSourceNode initialize];
```

## Instance methods

```
-[BWMetadataSourceNode formatDescription];
-[BWMetadataSourceNode start:];
-[BWMetadataSourceNode clock];
-[BWMetadataSourceNode dealloc];
-[BWMetadataSourceNode stop:];
-[BWMetadataSourceNode nodeSubType];
-[BWMetadataSourceNode initWithFormatDescription:clock:];
-[BWMetadataSourceNode appendMetadataSampleBuffer:];
```
