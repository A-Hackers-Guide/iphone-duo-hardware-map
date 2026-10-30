# `RAWFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CIFilter`
- 0 instance variables, 0 properties, 10 instance methods, 3 class methods

## Class methods

```
+[RAWFilter filterWithName:];
+[RAWFilter filterWithDefaultsForClass:];
+[RAWFilter filterWithDefaultsForName:];
```

## Instance methods

```
-[RAWFilter encodeWithCoder:];
-[RAWFilter initWithCoder:];
-[RAWFilter apply:image:extent:roiCallback:arguments:inoutSpace:isAlphaOne:];
-[RAWFilter apply:image:arguments:inoutSpace:isPremultiplied:];
-[RAWFilter apply:image:arguments:inoutSpace:isPremultiplied:isAlphaOne:];
-[RAWFilter apply:image:extent:roiCallback:arguments:inoutSpace:];
-[RAWFilter applyMatrixToImage:vectorR:vectorG:vectorB:vectorBias:inSpace:outSpace:];
-[RAWFilter setPrimitiveNumberValue:inVariable:forKey:];
-[RAWFilter takeAttributesFromDictionary:];
-[RAWFilter takeAttributesFromDictionary:forKeys:];
```
