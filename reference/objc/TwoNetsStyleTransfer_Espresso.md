# `TwoNetsStyleTransfer`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
^v ctx;
^v plan;
{?="plan"^v"network_index"i} net;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} output_layer_name;
[5Q] dim_data0;
[5Q] dim_data0__small;
[5Q] dim_data2;
[5Q] dim_data2__small;
^{__IOSurface=} result;
{postprocessing_settings_t="name"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"network"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"do_blend"i"blend_alpha"f"grayscale_i0"i"grayscale_i1"i"temporal_alpha"f"gamma"f"saturation"f"contrast"f"brightness"f"color_transfer_mode"i"width"i"height"i"width_fast"i"height_fast"i"width_capture"i"height_capture"i"width_miniature"i"height_miniature"i"width_fullscreen"i"height_fullscreen"i"width_hd"i"height_hd"i"old_frame_scale"f"noise_strength"f"dyn_noise"i"noise_speed"f"preprocessing_bias_b"f"preprocessing_bias_g"f"preprocessing_bias_r"f"preprocessing_scale"f"preprocessing_old_frame_bias_scale"f"high_quality_scaling"B} current_postprocessing_settings;
@"NSString" currentNetworkPath;
```

## Class methods

```
+[TwoNetsStyleTransfer supportsANE];
```

## Instance methods

```
-[TwoNetsStyleTransfer init];
-[TwoNetsStyleTransfer dealloc];
-[TwoNetsStyleTransfer executeSyncWithImage:smallImage:];
-[TwoNetsStyleTransfer heightBig];
-[TwoNetsStyleTransfer heightSmall];
-[TwoNetsStyleTransfer load:outputName:];
-[TwoNetsStyleTransfer widthBig];
-[TwoNetsStyleTransfer widthSmall];
```
