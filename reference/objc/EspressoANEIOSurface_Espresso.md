# `EspressoANEIOSurface`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 2 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" params_dict;
{vector<Espresso::ANERuntimeEngine::surface_and_buffer, std::allocator<Espresso::ANERuntimeEngine::surface_and_buffer>>="__begin_"^{surface_and_buffer}"__end_"^{surface_and_buffer}""{?="__cap_"^{surface_and_buffer}}} multiple_buffer_io_surfaces;
B created_with_lazy_iosurface;
B ane_surface_use_cvpixelbuffer;
Q width;
Q height;
Q rowBytes;
@"NSSet" valid_pixel_formats;
I _pixelFormat;
{shared_ptr<Espresso::blob<unsigned char, 1>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _external_storage_blob_for_aliasing_mem;
```

## Properties

```
@property (T{shared_ptr<Espresso::blob<unsigned char, 1>>=^v^{__shared_weak_count}},N,V_external_storage_blob_for_aliasing_mem) external_storage_blob_for_aliasing_mem;
@property (TI,R,N,V_pixelFormat) pixelFormat;
```

## Instance methods

```
-[EspressoANEIOSurface cleanup];
-[EspressoANEIOSurface doNonLazyAllocation:];
-[EspressoANEIOSurface nFrames];
-[EspressoANEIOSurface ane_io_surfaceForMultiBufferFrame:];
-[EspressoANEIOSurface initWithIOSurfaceProperties:andPixelFormats:];
-[EspressoANEIOSurface ioSurfaceForMultiBufferFrameNoLazyForTesting:];
-[EspressoANEIOSurface restoreInternalStorageForAllMultiBufferFrames];
-[EspressoANEIOSurface setExternalStorage:ioSurface:];
-[EspressoANEIOSurface setExternal_storage_blob_for_aliasing_mem:];
-[EspressoANEIOSurface checkIfMatches:];
-[EspressoANEIOSurface metalBufferWithDevice:multiBufferFrame:];
-[EspressoANEIOSurface external_storage_blob_for_aliasing_mem];
-[EspressoANEIOSurface pixelFormat];
-[EspressoANEIOSurface lazilyAutoCreateSurfaceForFrame:];
-[EspressoANEIOSurface restoreInternalStorage:];
-[EspressoANEIOSurface checkIfMatchesIOSurface:];
-[EspressoANEIOSurface ioSurfaceForMultiBufferFrame:];
-[EspressoANEIOSurface createIOSurfaceWithExtraProperties:];
-[EspressoANEIOSurface resizeForMultipleAsyncBuffers:];
```
