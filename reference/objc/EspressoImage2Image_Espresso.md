# `EspressoImage2Image`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 2 properties, 38 instance methods, 8 class methods

## Instance variables

```
^v ctx;
^v plan;
{?="plan"^v"network_index"i} net;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} output_layer_name;
@"<MTLCommandQueue>" queue;
@"<MTLDevice>" device;
@"NSObject<OS_dispatch_queue>" dispatch_queue;
B is_temporal_model;
[5Q] dim;
[5Q] dim_small;
i defaultWidth;
i defaultHeight;
f t0;
i scale_ratio;
@"<MTLTexture>" smallOldResultTexture;
{map<std::string, float, std::less<std::string>, std::allocator<std::pair<const std::string, float>>>="__tree_"{__tree<std::__value_type<std::string, float>, std::__map_value_compare<std::string, std::pair<const std::string, float>, std::less<std::string>>, std::allocator<std::pair<const std::string, float>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} tweaks;
{postprocessing_settings_t="name"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"network"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"do_blend"i"blend_alpha"f"grayscale_i0"i"grayscale_i1"i"temporal_alpha"f"gamma"f"saturation"f"contrast"f"brightness"f"color_transfer_mode"i"width"i"height"i"width_fast"i"height_fast"i"width_capture"i"height_capture"i"width_miniature"i"height_miniature"i"width_fullscreen"i"height_fullscreen"i"width_hd"i"height_hd"i"old_frame_scale"f"noise_strength"f"dyn_noise"i"noise_speed"f"preprocessing_bias_b"f"preprocessing_bias_g"f"preprocessing_bias_r"f"preprocessing_scale"f"preprocessing_old_frame_bias_scale"f"high_quality_scaling"B} current_postprocessing_settings;
{shared_ptr<Espresso::V9Engine::v9_noise_kernel>="__ptr_"^{v9_noise_kernel}"__cntrl_"^{__shared_weak_count}} noise_k;
{shared_ptr<Espresso::generic_load_constant_kernel>="__ptr_"^{generic_load_constant_kernel}"__cntrl_"^{__shared_weak_count}} noise_load_constant_kernel;
@"NSString" currentNetworkPath;
q currentResolutionPreset;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} precomputed_noise;
@"<MTLTexture>" tmpDestinationTexture;
i _rotation_degrees;
i _flip_y;
```

## Properties

```
@property (Ti,N,V_rotation_degrees) rotation_degrees;
@property (Ti,N,V_flip_y) flip_y;
```

## Class methods

```
+[EspressoImage2Image featureVersion];
+[EspressoImage2Image getStylesKeys];
+[EspressoImage2Image gpuSync:tex:];
+[EspressoImage2Image loadStylesConfigAtDefaultsKey:];
+[EspressoImage2Image loadStylesConfigAtPath:];
+[EspressoImage2Image setDefaultOption:toValue:];
+[EspressoImage2Image tuneNetworks:];
+[EspressoImage2Image tuneNetworksWGWindowSize:];
```

## Instance methods

```
-[EspressoImage2Image initWithQueue:];
-[EspressoImage2Image init];
-[EspressoImage2Image dealloc];
-[EspressoImage2Image reload];
-[EspressoImage2Image load:];
-[EspressoImage2Image width];
-[EspressoImage2Image height];
-[EspressoImage2Image styleName];
-[EspressoImage2Image setupWithQueue:];
-[EspressoImage2Image _resetTemporalState];
-[EspressoImage2Image _reshapeToResolutionPreset:];
-[EspressoImage2Image _reshapeToWidth:andHeight:];
-[EspressoImage2Image _tune];
-[EspressoImage2Image addNoiseLayer];
-[EspressoImage2Image aggregateWisdom:];
-[EspressoImage2Image benchmark];
-[EspressoImage2Image encodeToCommandBuffer:sourceTexture:destinationTexture:cropRect:];
-[EspressoImage2Image encodeToCommandBuffer:sourceTexture:destinationTexture:cropRect:destinationRect:];
-[EspressoImage2Image flip_y];
-[EspressoImage2Image getEspressoNetwork];
-[EspressoImage2Image getInternalDataForKey:];
-[EspressoImage2Image load:resolutionPreset:];
-[EspressoImage2Image newOutputTexture];
-[EspressoImage2Image postProcess:cameraSourceTexture:inputTexture:destinationTexture:];
-[EspressoImage2Image resetTemporalState];
-[EspressoImage2Image reshapeToResolutionPreset:];
-[EspressoImage2Image reshapeToResolutionPreset:aspectRatio:];
-[EspressoImage2Image reshapeToWidth:andHeight:];
-[EspressoImage2Image resolutionForPreset:];
-[EspressoImage2Image rotation_degrees];
-[EspressoImage2Image setFlip_y:];
-[EspressoImage2Image setRotation_degrees:];
-[EspressoImage2Image simpleLinearResize:sourceTexture:destinationTexture:];
-[EspressoImage2Image submitToQueueWithSourceTexture:destinationTexture:];
-[EspressoImage2Image submitToQueueWithSourceTexture:destinationTexture:cropRect:];
-[EspressoImage2Image tune];
-[EspressoImage2Image tweak:value:];
-[EspressoImage2Image wasReshaped];
```
