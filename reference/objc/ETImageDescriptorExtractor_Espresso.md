# `ETImageDescriptorExtractor`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 10 properties, 25 instance methods, 4 class methods

## Instance variables

```
^v _plan;
{?="plan"^v"network_index"i} _net;
^v _ctx;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _inputBlob;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _outputBlob;
Q _targetWidth;
Q _targetHeight;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} _inputName;
^Q _inputShape;
f _rotation_range;
f _horizontal_flip;
f _zoom_range;
f _shear_range;
f _contrast_range;
f _brightness_range;
i _nAugmentations;
i _doBatchnormTuning;
Q _descriptors_mem_cache_size;
Q _descriptors_file_cache_size;
```

## Properties

```
@property (Tf,V_rotation_range) rotation_range;
@property (Tf,V_horizontal_flip) horizontal_flip;
@property (Tf,V_zoom_range) zoom_range;
@property (Tf,V_shear_range) shear_range;
@property (Tf,V_contrast_range) contrast_range;
@property (Tf,V_brightness_range) brightness_range;
@property (Ti,V_nAugmentations) nAugmentations;
@property (Ti,V_doBatchnormTuning) doBatchnormTuning;
@property (TQ,V_descriptors_mem_cache_size) descriptors_mem_cache_size;
@property (TQ,V_descriptors_file_cache_size) descriptors_file_cache_size;
```

## Class methods

```
+[ETImageDescriptorExtractor VisionSceneNet_iOS10_Extractor];
+[ETImageDescriptorExtractor VisionSmartCamNet_iOS11_Extractor];
+[ETImageDescriptorExtractor inception_v3_Extractor];
+[ETImageDescriptorExtractor passthroughExtractor];
```

## Instance methods

```
-[ETImageDescriptorExtractor initWithNetwork:];
-[ETImageDescriptorExtractor numberOfChannels];
-[ETImageDescriptorExtractor horizontal_flip];
-[ETImageDescriptorExtractor setDescriptors_file_cache_size:];
-[ETImageDescriptorExtractor setShear_range:];
-[ETImageDescriptorExtractor brightness_range];
-[ETImageDescriptorExtractor contrast_range];
-[ETImageDescriptorExtractor cropResizeInputImage:];
-[ETImageDescriptorExtractor descriptors_file_cache_size];
-[ETImageDescriptorExtractor descriptors_mem_cache_size];
-[ETImageDescriptorExtractor doBatchnormTuning];
-[ETImageDescriptorExtractor extractDescriptorForDataPoint:freeWhenDone:];
-[ETImageDescriptorExtractor extractForDataPoint:];
-[ETImageDescriptorExtractor nAugmentations];
-[ETImageDescriptorExtractor rotation_range];
-[ETImageDescriptorExtractor setBrightness_range:];
-[ETImageDescriptorExtractor setContrast_range:];
-[ETImageDescriptorExtractor setDescriptors_mem_cache_size:];
-[ETImageDescriptorExtractor setDoBatchnormTuning:];
-[ETImageDescriptorExtractor setHorizontal_flip:];
-[ETImageDescriptorExtractor setNAugmentations:];
-[ETImageDescriptorExtractor setRotation_range:];
-[ETImageDescriptorExtractor setZoom_range:];
-[ETImageDescriptorExtractor shear_range];
-[ETImageDescriptorExtractor zoom_range];
```
