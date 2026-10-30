# `CAMBurstImageSet`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"CAMBurstImageSetInternal" _priv;
```

## Class methods

```
+[CAMBurstImageSet burstImageSet];
+[CAMBurstImageSet burstImageSetWithOptions:];
+[CAMBurstImageSet defaultVersionString];
```

## Instance methods

```
-[CAMBurstImageSet isPortrait];
-[CAMBurstImageSet init];
-[CAMBurstImageSet dealloc];
-[CAMBurstImageSet initWithOptions:];
-[CAMBurstImageSet burstId];
-[CAMBurstImageSet addImageFromIOSurface:properties:identifier:completionBlock:];
-[CAMBurstImageSet allImageIdentifiers];
-[CAMBurstImageSet bestImageIdentifiers];
-[CAMBurstImageSet coverImageIdentifier];
-[CAMBurstImageSet imageClusterCount];
-[CAMBurstImageSet imageClusterForIdentifier:];
-[CAMBurstImageSet imageClusterForIndex:];
-[CAMBurstImageSet isAction];
-[CAMBurstImageSet secondsSinceStart];
-[CAMBurstImageSet setLoggingListener:withUserInfo:];
-[CAMBurstImageSet statsForImageWithIdentifier:];
```
