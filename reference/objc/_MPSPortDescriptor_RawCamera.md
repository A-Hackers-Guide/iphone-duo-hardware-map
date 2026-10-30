# `_MPSPortDescriptor`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isInput;
I _dataType;
@"NSString" _name;
@"IOSurface" _surface;
@"<MTLBuffer>" _buffer;
@"NSArray" _shape;
Q _byteSize;
@? _surfaceReleaseBlock;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (TB,N,V_isInput) isInput;
@property (T@"IOSurface",&,N,V_surface) surface;
@property (T@"<MTLBuffer>",&,N,V_buffer) buffer;
@property (T@"NSArray",C,N,V_shape) shape;
@property (TI,N,V_dataType) dataType;
@property (TQ,N,V_byteSize) byteSize;
@property (T@?,C,N,V_surfaceReleaseBlock) surfaceReleaseBlock;
```

## Instance methods

```
-[_MPSPortDescriptor buffer];
-[_MPSPortDescriptor setBuffer:];
-[_MPSPortDescriptor setShape:];
-[_MPSPortDescriptor setSurface:];
-[_MPSPortDescriptor isInput];
-[_MPSPortDescriptor surface];
-[_MPSPortDescriptor setDataType:];
-[_MPSPortDescriptor shape];
-[_MPSPortDescriptor dataType];
-[_MPSPortDescriptor setName:];
-[_MPSPortDescriptor name];
-[_MPSPortDescriptor byteSize];
-[_MPSPortDescriptor setIsInput:];
-[_MPSPortDescriptor setByteSize:];
-[_MPSPortDescriptor setSurfaceReleaseBlock:];
-[_MPSPortDescriptor surfaceReleaseBlock];
```
