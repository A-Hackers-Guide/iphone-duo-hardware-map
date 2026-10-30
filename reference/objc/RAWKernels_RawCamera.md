# `RAWKernels`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 5 instance methods, 6 class methods

## Instance variables

```
@"NSMutableDictionary" priv;
```

## Class methods

```
+[RAWKernels allocWithZone:];
+[RAWKernels kernelWithName:];
+[RAWKernels colorKernelWithName:group:];
+[RAWKernels kernelWithName:group:];
+[RAWKernels sharedKernels];
+[RAWKernels warpKernelWithName:group:];
```

## Instance methods

```
-[RAWKernels init];
-[RAWKernels copyWithZone:];
-[RAWKernels kernelSourceForGroup:];
-[RAWKernels kernelWithName:group:];
-[RAWKernels loadKernelsForGroup:];
```
