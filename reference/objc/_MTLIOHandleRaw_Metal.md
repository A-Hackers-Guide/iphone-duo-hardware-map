# `_MTLIOHandleRaw`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLIOHandleSPI`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
i _fd;
Q _labelTraceID;
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
-[_MTLIOHandleRaw globalTraceObjectID];
-[_MTLIOHandleRaw dealloc];
-[_MTLIOHandleRaw length];
-[_MTLIOHandleRaw decompress:size:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleRaw getHandleOffset:offset:];
-[_MTLIOHandleRaw initWithDevice:path:error:uncached:];
-[_MTLIOHandleRaw read:size:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleRaw read:size:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[_MTLIOHandleRaw readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:];
-[_MTLIOHandleRaw readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[_MTLIOHandleRaw stagingBufferSize:offset:];
```
