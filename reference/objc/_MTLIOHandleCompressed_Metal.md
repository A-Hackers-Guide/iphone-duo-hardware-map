# `_MTLIOHandleCompressed`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLIOHandleSPI`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
i _fd;
Q _labelTraceID;
^v _handle;
```

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (TI,?,R) vnioID;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIOHandleCompressed globalTraceObjectID];
-[_MTLIOHandleCompressed dealloc];
-[_MTLIOHandleCompressed length];
-[_MTLIOHandleCompressed decompress:size:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleCompressed getHandleOffset:offset:];
-[_MTLIOHandleCompressed initWithDevice:path:compressionType:error:uncached:];
-[_MTLIOHandleCompressed read:size:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleCompressed read:size:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[_MTLIOHandleCompressed readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleCompressed readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[_MTLIOHandleCompressed stagingBufferSize:offset:];
```
