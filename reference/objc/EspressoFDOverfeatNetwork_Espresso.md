# `EspressoFDOverfeatNetwork`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 31 instance variables, 11 properties, 54 instance methods, 0 class methods

## Instance variables

```
{vector<std::shared_ptr<Espresso::net>, std::allocator<std::shared_ptr<Espresso::net>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} gpu_nets;
{vector<std::shared_ptr<Espresso::net>, std::allocator<std::shared_ptr<Espresso::net>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} ecpu_nets;
{vector<std::pair<unsigned long long, unsigned long long>, std::allocator<std::pair<unsigned long long, unsigned long long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} net_scales;
{vector<std::pair<unsigned long long, unsigned long long>, std::allocator<std::pair<unsigned long long, unsigned long long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} full_scales;
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} scalesc;
{vector<std::shared_ptr<Espresso::fast_pyramid_resizer>, std::allocator<std::shared_ptr<Espresso::fast_pyramid_resizer>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} resizers_for_batching;
i n_resizers_for_batching;
{vector<std::shared_ptr<Espresso::blob<float, 3>>, std::allocator<std::shared_ptr<Espresso::blob<float, 3>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} probBlobs;
{vector<std::shared_ptr<Espresso::blob<float, 3>>, std::allocator<std::shared_ptr<Espresso::blob<float, 3>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} boxBlobs;
@"NSMutableDictionary" _errorForLayers;
{pair<unsigned long long, unsigned long long>="first"Q"second"Q} cropDims;
^{CGColorSpace=} colorSpace;
{net_strides_configuration="num_layer"i"kernel_size"{vector<int, std::allocator<int>>="__begin_"^i"__end_"^i""{?="__cap_"^i}}"stride"{vector<int, std::allocator<int>>="__begin_"^i"__end_"^i""{?="__cap_"^i}}"pad"{vector<int, std::allocator<int>>="__begin_"^i"__end_"^i""{?="__cap_"^i}}} strideConf;
i retile_stride;
i retile_tile_sz;
{vector<int, std::allocator<int>>="__begin_"^i"__end_"^i""{?="__cap_"^i}} retile_n_outputs_v;
i tile_w_1;
i tile_h_1;
@"NSObject<OS_dispatch_queue>" cpu_queue_0;
@"NSObject<OS_dispatch_semaphore>" cpu_semaphore;
B _useGPUScaler;
i _scalingMode;
f _maxScale;
i _forceMaxNScales;
i _scaleConfig;
i _mode;
i _cpin;
@"NSString" _basename;
@"NSString" _weights;
{shared_ptr<Espresso::abstract_context>="__ptr_"^{abstract_context}"__cntrl_"^{__shared_weak_count}} _context_metal;
{shared_ptr<Espresso::abstract_context>="__ptr_"^{abstract_context}"__cntrl_"^{__shared_weak_count}} _context_cpu;
```

## Properties

```
@property (T@"NSString",&,N,V_basename) basename;
@property (T@"NSString",&,N,V_weights) weights;
@property (Ti,N,V_scaleConfig) scaleConfig;
@property (Ti,N,V_mode) mode;
@property (Ti,N,V_cpin) cpin;
@property (T{shared_ptr<Espresso::abstract_context>=^{abstract_context}^{__shared_weak_count}},N,V_context_metal) context_metal;
@property (T{shared_ptr<Espresso::abstract_context>=^{abstract_context}^{__shared_weak_count}},N,V_context_cpu) context_cpu;
@property (TB,N,V_useGPUScaler) useGPUScaler;
@property (Ti,N,V_scalingMode) scalingMode;
@property (Tf,N,V_maxScale) maxScale;
@property (Ti,N,V_forceMaxNScales) forceMaxNScales;
```

## Instance methods

```
-[EspressoFDOverfeatNetwork setScalingMode:];
-[EspressoFDOverfeatNetwork scalingMode];
-[EspressoFDOverfeatNetwork init];
-[EspressoFDOverfeatNetwork dealloc];
-[EspressoFDOverfeatNetwork reset];
-[EspressoFDOverfeatNetwork setMaxScale:];
-[EspressoFDOverfeatNetwork setMode:];
-[EspressoFDOverfeatNetwork mode];
-[EspressoFDOverfeatNetwork maxScale];
-[EspressoFDOverfeatNetwork processPyramid:];
-[EspressoFDOverfeatNetwork setContext_cpu:];
-[EspressoFDOverfeatNetwork weights];
-[EspressoFDOverfeatNetwork forceMaxNScales];
-[EspressoFDOverfeatNetwork resizerAtIndex:];
-[EspressoFDOverfeatNetwork setScaleConfig:];
-[EspressoFDOverfeatNetwork autoResizeForAspectRatio:useLowPriorityMode:gpuPriority:];
-[EspressoFDOverfeatNetwork autoSetupNetBaseName:weights:scaleConfig:setupMode:computePath:autoAspectRatio:forceReset:useLowPriorityMode:gpuPriority:];
-[EspressoFDOverfeatNetwork basename];
-[EspressoFDOverfeatNetwork boxBlobForScale:];
-[EspressoFDOverfeatNetwork context_cpu];
-[EspressoFDOverfeatNetwork context_metal];
-[EspressoFDOverfeatNetwork cpin];
-[EspressoFDOverfeatNetwork cpu_net:];
-[EspressoFDOverfeatNetwork default_retile_outputs];
-[EspressoFDOverfeatNetwork errorForLayers];
-[EspressoFDOverfeatNetwork forward_cpu_network_at_index:pyr:];
-[EspressoFDOverfeatNetwork generatePyramid:tex:];
-[EspressoFDOverfeatNetwork getNumScales];
-[EspressoFDOverfeatNetwork getScale:];
-[EspressoFDOverfeatNetwork gpu_net:];
-[EspressoFDOverfeatNetwork needRetiling:];
-[EspressoFDOverfeatNetwork probBlobForScale:];
-[EspressoFDOverfeatNetwork processBlob:tex:];
-[EspressoFDOverfeatNetwork processBlobNoRotation:tex:doBGRA2RGBA:];
-[EspressoFDOverfeatNetwork processPyramid:gpu_resizer:];
-[EspressoFDOverfeatNetwork processVimageNoRotation:tex:doBGRA2RGBA:];
-[EspressoFDOverfeatNetwork resizerCount];
-[EspressoFDOverfeatNetwork retile_and_forward_espresso_gpu_network_at_index:net:pyr:];
-[EspressoFDOverfeatNetwork retile_and_forward_espresso_network_at_index:net:pyr:];
-[EspressoFDOverfeatNetwork retryLoadingCaffeNet:name:weights:context:cp:];
-[EspressoFDOverfeatNetwork scaleConfig];
-[EspressoFDOverfeatNetwork setBasename:];
-[EspressoFDOverfeatNetwork setContextCpu:];
-[EspressoFDOverfeatNetwork setContextMetal:];
-[EspressoFDOverfeatNetwork setContext_metal:];
-[EspressoFDOverfeatNetwork setCpin:];
-[EspressoFDOverfeatNetwork setForceMaxNScales:];
-[EspressoFDOverfeatNetwork setUseGPUScaler:];
-[EspressoFDOverfeatNetwork setWeights:];
-[EspressoFDOverfeatNetwork setup_retile];
-[EspressoFDOverfeatNetwork storeDataForPruning:prob:];
-[EspressoFDOverfeatNetwork strideConfiguration];
-[EspressoFDOverfeatNetwork useGPUScaler];
-[EspressoFDOverfeatNetwork wipeLayersMemory];
```
