# `ETDataTensor`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
^v _dataPointer;
@"NSArray" _dataArray;
Q _type;
@"NSArray" _shape;
@"NSArray" _strides;
@"NSNumber" _maxNumberOfElements;
{shared_ptr<Espresso::blob<float, 4>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _blob;
{vector<std::shared_ptr<unsigned char>, std::allocator<std::shared_ptr<unsigned char>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _allocatedImageData;
{float_buffer_t="ptr"^f"size"Q"free_when_done"B} _float_buffer;
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} _imageBuffer;
```

## Properties

```
@property (T{vImage_Buffer=^vQQQ},V_imageBuffer) imageBuffer;
@property (T{vector<std::shared_ptr<unsigned char>, std::allocator<std::shared_ptr<unsigned char>>>=^v^v{?=^v}},V_allocatedImageData) allocatedImageData;
@property (T{float_buffer_t=^fQB},V_float_buffer) float_buffer;
@property (T{shared_ptr<Espresso::blob<float, 4>>=^v^{__shared_weak_count}},V_blob) blob;
@property (T^v,N,V_dataPointer) dataPointer;
@property (T@"NSArray",&,N,V_dataArray) dataArray;
@property (TQ,N,V_type) type;
@property (T@"NSArray",&,N,V_shape) shape;
@property (T@"NSArray",&,N,V_strides) strides;
@property (T@"NSNumber",&,N,V_maxNumberOfElements) maxNumberOfElements;
```

## Instance methods

```
-[ETDataTensor setShape:];
-[ETDataTensor imageBuffer];
-[ETDataTensor shape];
-[ETDataTensor strides];
-[ETDataTensor setType:];
-[ETDataTensor type];
-[ETDataTensor dataPointer];
-[ETDataTensor description];
-[ETDataTensor blob];
-[ETDataTensor setBlob:];
-[ETDataTensor dataArray];
-[ETDataTensor setDataArray:];
-[ETDataTensor setImageBuffer:];
-[ETDataTensor setDataPointer:];
-[ETDataTensor allocatedImageData];
-[ETDataTensor float_buffer];
-[ETDataTensor initWithBlobContainer:];
-[ETDataTensor initWithBlobContainer:directBind:];
-[ETDataTensor initWithCVPixelBuffer:imageParameters:error:];
-[ETDataTensor initWithData:type:shape:strides:];
-[ETDataTensor maxNumberOfElements];
-[ETDataTensor setAllocatedImageData:];
-[ETDataTensor setFloat_buffer:];
-[ETDataTensor setMaxNumberOfElements:];
-[ETDataTensor setStrides:];
```
