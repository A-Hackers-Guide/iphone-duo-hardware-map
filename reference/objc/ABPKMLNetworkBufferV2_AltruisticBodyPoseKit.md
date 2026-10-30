# `ABPKMLNetworkBufferV2`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 15 properties, 20 instance methods, 0 class methods

## Instance variables

```
^{e5rt_io_port=} _port;
^{e5rt_buffer_object=} _memory;
^{e5rt_surface_object=} _surfaceObject;
^{e5rt_tensor_desc=} _tensorDesc;
^{e5rt_surface_desc=} _surfaceDesc;
i _dataType;
Q _bytesPerElement;
B _useSurface;
i _surfaceFormat;
@"NSString" _name;
Q _width;
Q _height;
Q _channels;
Q _batchNumber;
Q _sequenceLength;
Q _size;
Q _strideWidth;
Q _strideHeight;
Q _strideChannels;
Q _strideBatchNumber;
Q _strideSequenceLength;
^{__CVBuffer=} _pixelBuffer;
^v _bytes;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (TQ,R,N,V_width) width;
@property (TQ,R,N,V_height) height;
@property (TQ,R,N,V_channels) channels;
@property (TQ,R,N,V_batchNumber) batchNumber;
@property (TQ,R,N,V_sequenceLength) sequenceLength;
@property (TQ,R,N,V_size) size;
@property (TQ,R,N,V_strideWidth) strideWidth;
@property (TQ,R,N,V_strideHeight) strideHeight;
@property (TQ,R,N,V_strideChannels) strideChannels;
@property (TQ,R,N,V_strideBatchNumber) strideBatchNumber;
@property (TQ,R,N,V_strideSequenceLength) strideSequenceLength;
@property (T^{__CVBuffer=},R,N,V_pixelBuffer) pixelBuffer;
@property (Ti,R,N,V_surfaceFormat) surfaceFormat;
@property (T^v,R,N,V_bytes) bytes;
```

## Instance methods

```
-[ABPKMLNetworkBufferV2 channels];
-[ABPKMLNetworkBufferV2 pixelBuffer];
-[ABPKMLNetworkBufferV2 dealloc];
-[ABPKMLNetworkBufferV2 batchNumber];
-[ABPKMLNetworkBufferV2 size];
-[ABPKMLNetworkBufferV2 width];
-[ABPKMLNetworkBufferV2 bytes];
-[ABPKMLNetworkBufferV2 name];
-[ABPKMLNetworkBufferV2 height];
-[ABPKMLNetworkBufferV2 sequenceLength];
-[ABPKMLNetworkBufferV2 strideHeight];
-[ABPKMLNetworkBufferV2 strideWidth];
-[ABPKMLNetworkBufferV2 _readSurfaceDescriptor];
-[ABPKMLNetworkBufferV2 _readTensorDescriptor];
-[ABPKMLNetworkBufferV2 initWithName:operation:bindMode:useSurface:];
-[ABPKMLNetworkBufferV2 setInput:FromIOSurface:];
-[ABPKMLNetworkBufferV2 strideBatchNumber];
-[ABPKMLNetworkBufferV2 strideChannels];
-[ABPKMLNetworkBufferV2 strideSequenceLength];
-[ABPKMLNetworkBufferV2 surfaceFormat];
```
