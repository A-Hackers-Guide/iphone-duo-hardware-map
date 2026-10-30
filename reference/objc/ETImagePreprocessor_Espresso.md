# `ETImagePreprocessor`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
{vimage2espresso_param="scale"f"center_mean"i"is_image_bgr"i"is_network_bgr"i"bias_r"f"bias_g"f"bias_b"f"bias_a"f"metal_output_plane"i"width"I"height"I"rowbytes"I"scaleXY""translateXY""rotate_deg"i"use_direct_cvpixelbuffer"i"no_alpha_premultiply"i} param;
{shared_ptr<Espresso::blob_cpu>="__ptr_"^{blob_cpu}"__cntrl_"^{__shared_weak_count}} imageBlob;
{shared_ptr<Espresso::abstract_context>="__ptr_"^{abstract_context}"__cntrl_"^{__shared_weak_count}} ctx;
Q nChannels;
@"NSArray" imageShape;
Q bytesPerPixel;
Q bitsPerComponent;
^{CGColorSpace=} colorSpace;
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} targetBuffer;
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} srcBuffer;
Q currentSrcBufferSize;
```

## Instance methods

```
-[ETImagePreprocessor preprocess];
-[ETImagePreprocessor dealloc];
-[ETImagePreprocessor tensorWithPath:];
-[ETImagePreprocessor initWithImagePreprocessParams:];
-[ETImagePreprocessor loadSrcBufferWithCGImage:];
-[ETImagePreprocessor tensorWithCGImage:];
```
