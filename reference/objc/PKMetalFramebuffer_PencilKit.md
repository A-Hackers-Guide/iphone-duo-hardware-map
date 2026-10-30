# `PKMetalFramebuffer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
q _nonVolatileLockCount;
B _isVolatile;
B _canBeMadeVolatile;
B _memoryless;
B _backedByIOSurface;
@"<MTLTexture>" _colorTexture;
@"<MTLDevice>" _device;
Q _pixelFormat;
Q _sampleCount;
^{__IOSurface=} _ioSurface;
q _blendMode;
{CGSize="width"d"height"d} _size;
{?="red"d"green"d"blue"d"alpha"d} _clearColor;
```

## Instance methods

```
-[PKMetalFramebuffer init];
-[PKMetalFramebuffer dealloc];
```
