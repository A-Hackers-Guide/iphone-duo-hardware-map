# `RawCameraCIImageProxy`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxy`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"CIImage" ciImage;
{shared_ptr<CRawImage>="__ptr_"^{CRawImage}"__cntrl_"^{__shared_weak_count}} rawImage;
```

## Properties

```
@property (T{shared_ptr<CRawImage>=^{CRawImage}^{__shared_weak_count}},VrawImage) rawImage;
@property (T@"CIImage",&,VciImage) ciImage;
```

## Class methods

```
+[RawCameraCIImageProxy respondsToSelector:];
```

## Instance methods

```
-[RawCameraCIImageProxy forwardingTargetForSelector:];
-[RawCameraCIImageProxy ciImage];
-[RawCameraCIImageProxy methodSignatureForSelector:];
-[RawCameraCIImageProxy setCiImage:];
-[RawCameraCIImageProxy forwardInvocation:];
-[RawCameraCIImageProxy rawImage];
-[RawCameraCIImageProxy initWithRawImage:];
-[RawCameraCIImageProxy proxyedObject];
-[RawCameraCIImageProxy setRawImage:];
```
