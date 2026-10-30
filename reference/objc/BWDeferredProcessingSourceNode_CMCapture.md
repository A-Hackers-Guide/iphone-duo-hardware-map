# `BWDeferredProcessingSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSourceNode`
- 3 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _outputsByPortType;
@"NSObject<OS_dispatch_queue>" _emitSamplesDispatchQueue;
B _running;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_outputsByPortType) outputsByPortType;
```

## Class methods

```
+[BWDeferredProcessingSourceNode initialize];
```

## Instance methods

```
-[BWDeferredProcessingSourceNode start:];
-[BWDeferredProcessingSourceNode dealloc];
-[BWDeferredProcessingSourceNode outputForPortType:];
-[BWDeferredProcessingSourceNode stop:];
-[BWDeferredProcessingSourceNode nodeSubType];
-[BWDeferredProcessingSourceNode initWithPortTypes:attributes:colorSpaceProperties:];
-[BWDeferredProcessingSourceNode outputsByPortType];
-[BWDeferredProcessingSourceNode portTypeForOutput:];
-[BWDeferredProcessingSourceNode processBuffer:];
```
