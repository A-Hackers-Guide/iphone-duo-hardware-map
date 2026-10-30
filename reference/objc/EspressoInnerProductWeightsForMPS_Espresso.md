# `EspressoInnerProductWeightsForMPS`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPSCNNConvolutionDataSource`
- 8 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
{inner_product_uniforms="nC"I"nB"I"has_biases"i"has_relu"i"has_tanh"i"tanh_alpha"f"tanh_beta"f"has_prelu"i"is_lookup"i"quantization_mode"i"nd_mode"B"add_to_output"i"use_raw_buffers"i"fused_activation_mode"i"fused_activation_alpha"f"fused_activation_beta"f"m"I"k"I"n"I"Abytes"I"Bbytes"I"k4"I"n4"I"n8"I"n8_splitk"I"argmax_tree_n_clusters"i"argmax_tree_n_clusters_keep"i"sparse_block_size_x"i"sparse_block_size_y"i"low_precision_accumulation"i"compute_every"i"is_lookup_rounds_to_nearest"i"disable_bnns_client_ptr"i} params;
{shared_ptr<Espresso::blob<float, 2>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} weights_blob;
{shared_ptr<Espresso::blob<unsigned short, 2>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} weights_f16_blob;
{shared_ptr<Espresso::blob<unsigned char, 2>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantized_weights_blob;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} biases_blob;
{shared_ptr<Espresso::blob<float __attribute__((ext_vector_type(2))), 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantization_ranges;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantization_lut;
I data_type;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[EspressoInnerProductWeightsForMPS load];
-[EspressoInnerProductWeightsForMPS descriptor];
-[EspressoInnerProductWeightsForMPS label];
-[EspressoInnerProductWeightsForMPS initWithParams:];
-[EspressoInnerProductWeightsForMPS purge];
-[EspressoInnerProductWeightsForMPS dataType];
-[EspressoInnerProductWeightsForMPS ready];
-[EspressoInnerProductWeightsForMPS copyWithZone:];
-[EspressoInnerProductWeightsForMPS weights];
-[EspressoInnerProductWeightsForMPS biasTerms];
-[EspressoInnerProductWeightsForMPS lookupTableForUInt8Kernel];
-[EspressoInnerProductWeightsForMPS rangesForUInt8Kernel];
```
