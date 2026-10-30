# `EspressoDataFrameStorageExecutorMatchingBufferSet`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _index;
@"NSString" _name;
^{__CVBuffer=} _computed_pb;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _reference_buffer;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _computed_buffer;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _groundtruth_buffer;
```

## Properties

```
@property (TQ,V_index) index;
@property (T@"NSString",&,V_name) name;
@property (T{?=^v^v[4Q][4Q]QQQQQQQQQQi},V_reference_buffer) reference_buffer;
@property (T{?=^v^v[4Q][4Q]QQQQQQQQQQi},V_computed_buffer) computed_buffer;
@property (T^{__CVBuffer=},V_computed_pb) computed_pb;
@property (T{?=^v^v[4Q][4Q]QQQQQQQQQQi},V_groundtruth_buffer) groundtruth_buffer;
```

## Instance methods

```
-[EspressoDataFrameStorageExecutorMatchingBufferSet index];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setIndex:];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setName:];
-[EspressoDataFrameStorageExecutorMatchingBufferSet name];
-[EspressoDataFrameStorageExecutorMatchingBufferSet computed_buffer];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setComputed_pb:];
-[EspressoDataFrameStorageExecutorMatchingBufferSet computed_pb];
-[EspressoDataFrameStorageExecutorMatchingBufferSet groundtruth_buffer];
-[EspressoDataFrameStorageExecutorMatchingBufferSet reference_buffer];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setComputed_buffer:];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setGroundtruth_buffer:];
-[EspressoDataFrameStorageExecutorMatchingBufferSet setReference_buffer:];
```
