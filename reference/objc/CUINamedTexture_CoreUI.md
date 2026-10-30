# `CUINamedTexture`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
d _scale;
{_cuintproperties="exifOrientation"b4"isAlphaCropped"b1"isOpaque"b1"_reserved"b26} _textureProperties;
```

## Properties

```
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N,V_scale) scale;
@property (Ti,R,N) exifOrientation;
@property (TB,R,N) isOpaque;
@property (TB,R,N) isAlphaCropped;
```

## Instance methods

```
-[CUINamedTexture exifOrientation];
-[CUINamedTexture isOpaque];
-[CUINamedTexture size];
-[CUINamedTexture scale];
-[CUINamedTexture alphaCroppedRect];
-[CUINamedTexture description];
-[CUINamedTexture _cacheRenditionProperties];
-[CUINamedTexture isAlphaCropped];
-[CUINamedTexture textureWithBufferAllocator:];
```
