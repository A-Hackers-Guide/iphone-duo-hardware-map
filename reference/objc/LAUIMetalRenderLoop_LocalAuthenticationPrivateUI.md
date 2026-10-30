# `LAUIMetalRenderLoop`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAUIRenderLoop`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CAMetalLayer" _layer;
B _drawable_size_dirty;
@"<CAMetalDrawable>" _current_drawable;
Q _pixel_format;
^{CGColorSpace=} _color_space;
@"<MTLDevice>" _device;
{CGSize="width"d"height"d} _drawable_size;
```

## Properties

```
@property (TQ,R,N,V_pixel_format) pixelFormat;
@property (T@"<MTLDevice>",R,N,V_device) device;
@property (T@"CALayer",R,D,N) layer;
@property (T^{CGColorSpace=},N,V_color_space) colorSpace;
@property (TB,D,N) framebufferOnly;
@property (T{CGSize=dd},N,V_drawable_size) drawableSize;
@property (T@"<LAUIMetalRenderLoopDelegate>",W,D,N) delegate;
```

## Instance methods

```
-[LAUIMetalRenderLoop isDrawableAvailable];
-[LAUIMetalRenderLoop setColorSpace:];
-[LAUIMetalRenderLoop layer];
-[LAUIMetalRenderLoop device];
-[LAUIMetalRenderLoop init];
-[LAUIMetalRenderLoop dealloc];
-[LAUIMetalRenderLoop colorSpace];
-[LAUIMetalRenderLoop pixelFormat];
-[LAUIMetalRenderLoop framebufferOnly];
-[LAUIMetalRenderLoop currentDrawable];
-[LAUIMetalRenderLoop setFramebufferOnly:];
-[LAUIMetalRenderLoop drawableSize];
-[LAUIMetalRenderLoop setDrawableSize:];
-[LAUIMetalRenderLoop _didInvalidate];
-[LAUIMetalRenderLoop _isForcingPause];
-[LAUIMetalRenderLoop _didDraw];
-[LAUIMetalRenderLoop _willDraw];
-[LAUIMetalRenderLoop initWithPixelFormat:forDevice:];
```
