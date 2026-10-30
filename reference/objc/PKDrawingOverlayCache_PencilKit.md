# `PKDrawingOverlayCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSCache" _memoryCache;
@"NSObject<OS_dispatch_queue>" _accessQueue;
```

## Class methods

```
+[PKDrawingOverlayCache sharedCache];
```

## Instance methods

```
-[PKDrawingOverlayCache init];
-[PKDrawingOverlayCache clearMemoryCache];
-[PKDrawingOverlayCache overlayDrawingForDrawingUUID:tintColor:completion:];
```
