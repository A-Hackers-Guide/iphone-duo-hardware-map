# `EspressoConvolutionWeightsForMPS`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPSCNNConvolutionDataSource`
- 9 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
{convolution_uniforms="W"i"H"i"Winput"i"Hinput"i"start_channel_low_priority_split"i"output_row_bytes"i"fused_relu"i"fused_tanh"i"has_biases"i"leaky_relu_alpha"f"C"i"K"i"Nx"i"Ny"i"backward_stride"i"fused_activation_mode"i"fused_activation_alpha"f"fused_activation_beta"f"pad"{padding_params_t="pad_mode"s"fill_mode"s"value"f"l"s"r"s"t"s"b"s"front"s"back"s}"stride_x"s"stride_y"s"dilation_x"s"dilation_y"s"mtl_pad_l"S"mtl_pad_t"S"has_8bit_weights"i"do_ncc"i"has_batch_norm"i"n_groups"i"n_parallel"i"start_channel_bottom"S"start_channel_top"S"total_channel_bottom"S"total_channel_top"S"split_K_channels_low_priority_split"S"n_batch"s"deconv_out_width"i"deconv_out_height"i"low_precision_accumulation"i"hint_use_winograd_win_size"i"Nt"i"stride_t"s"disable_bnns_client_ptr"i"use_sequential_cblas"B} params;
{shared_ptr<Espresso::blob<unsigned char, 4>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantized_weights_blob;
{shared_ptr<Espresso::blob<float, 4>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} weights_blob;
{shared_ptr<Espresso::blob<unsigned short, 4>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} weights_f16_blob;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} biases_blob;
{shared_ptr<Espresso::blob<float __attribute__((ext_vector_type(2))), 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantization_ranges;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} quantization_lut;
{shared_ptr<Espresso::blob<float, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} scale_factor_batch_norm;
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
-[EspressoConvolutionWeightsForMPS load];
-[EspressoConvolutionWeightsForMPS descriptor];
-[EspressoConvolutionWeightsForMPS label];
-[EspressoConvolutionWeightsForMPS initWithParams:];
-[EspressoConvolutionWeightsForMPS purge];
-[EspressoConvolutionWeightsForMPS dataType];
-[EspressoConvolutionWeightsForMPS ready];
-[EspressoConvolutionWeightsForMPS copyWithZone:];
-[EspressoConvolutionWeightsForMPS weights];
-[EspressoConvolutionWeightsForMPS biasTerms];
-[EspressoConvolutionWeightsForMPS lookupTableForUInt8Kernel];
-[EspressoConvolutionWeightsForMPS rangesForUInt8Kernel];
```
