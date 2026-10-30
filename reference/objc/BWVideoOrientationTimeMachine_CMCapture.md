# `BWVideoOrientationTimeMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _cache;
Q _capacity;
^{opaqueCMFormatDescription=} _formatDescription;
I _metadataLocalID;
^{OpaqueFigSimpleMutex=} _propertyMutex;
```

## Class methods

```
+[BWVideoOrientationTimeMachine initialize];
```

## Instance methods

```
-[BWVideoOrientationTimeMachine debugDescription];
-[BWVideoOrientationTimeMachine dealloc];
-[BWVideoOrientationTimeMachine _cachedItemsFromPTSSeconds:toPTSSeconds:];
-[BWVideoOrientationTimeMachine addItemToCacheWithPTS:exifOrientation:];
-[BWVideoOrientationTimeMachine copyVideoOrientationSbufFromPTS:toPTS:referencePTS:];
-[BWVideoOrientationTimeMachine initWithCapacity:formatDescription:metadataLocalID:];
```
