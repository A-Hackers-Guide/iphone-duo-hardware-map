# `BWPhotoManifest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _photoDescriptors;
@"NSString" _captureRequestIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferPtrValueToPhotoDescriptorLock;
@"NSMutableDictionary" _bufferPtrValueToPhotoDescriptor;
```

## Properties

```
@property (T@"NSArray",R,N,V_photoDescriptors) photoDescriptors;
@property (T@"NSString",R,N,V_captureRequestIdentifier) captureRequestIdentifier;
```

## Class methods

```
+[BWPhotoManifest supportsSecureCoding];
```

## Instance methods

```
-[BWPhotoManifest dealloc];
-[BWPhotoManifest captureRequestIdentifier];
-[BWPhotoManifest encodeWithCoder:];
-[BWPhotoManifest hash];
-[BWPhotoManifest description];
-[BWPhotoManifest initWithCoder:];
-[BWPhotoManifest cannotProcessDepthPhotos];
-[BWPhotoManifest isEqual:];
-[BWPhotoManifest descriptorForIdentifier:];
-[BWPhotoManifest descriptorForSampleBuffer:];
-[BWPhotoManifest initWithDescriptors:captureRequestIdentifier:];
-[BWPhotoManifest photoDescriptors];
```
