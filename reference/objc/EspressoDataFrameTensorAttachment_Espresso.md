# `EspressoDataFrameTensorAttachment`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EspressoDataFrameAttachment`
- 1 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} buffer;
```

## Class methods

```
+[EspressoDataFrameTensorAttachment copyFromCVPixelBuffer:];
```

## Instance methods

```
-[EspressoDataFrameTensorAttachment copyAsEspressoBuffer];
-[EspressoDataFrameTensorAttachment loadFromDict:frameStorage:];
```
