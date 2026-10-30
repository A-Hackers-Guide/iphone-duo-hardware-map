# `_UIVisualEffectViewBackdropCaptureGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSPointerArray" _backdrops;
B _disableInPlaceFiltering;
@"NSString" _groupName;
@"NSString" _groupNamespace;
d _scale;
d _minimumScale;
```

## Properties

```
@property (T@"NSString",C,N,V_groupName) groupName;
@property (T@"NSString",C,N,V_groupNamespace) groupNamespace;
@property (Td,N,V_scale) scale;
@property (Td,N,V_minimumScale) minimumScale;
@property (TB,N,V_disableInPlaceFiltering) disableInPlaceFiltering;
```

## Instance methods

```
-[_UIVisualEffectViewBackdropCaptureGroup minimumScale];
-[_UIVisualEffectViewBackdropCaptureGroup allowInPlaceFiltering];
-[_UIVisualEffectViewBackdropCaptureGroup addBackdrop:update:];
-[_UIVisualEffectViewBackdropCaptureGroup init];
-[_UIVisualEffectViewBackdropCaptureGroup setGroupName:];
-[_UIVisualEffectViewBackdropCaptureGroup updateAllBackdropViews];
-[_UIVisualEffectViewBackdropCaptureGroup setScale:];
-[_UIVisualEffectViewBackdropCaptureGroup initWithBackdrop:];
-[_UIVisualEffectViewBackdropCaptureGroup applyScaleHint:];
-[_UIVisualEffectViewBackdropCaptureGroup setDisableInPlaceFiltering:];
-[_UIVisualEffectViewBackdropCaptureGroup scale];
-[_UIVisualEffectViewBackdropCaptureGroup groupName];
-[_UIVisualEffectViewBackdropCaptureGroup setMinimumScale:];
-[_UIVisualEffectViewBackdropCaptureGroup removeBackdrop:update:];
-[_UIVisualEffectViewBackdropCaptureGroup description];
-[_UIVisualEffectViewBackdropCaptureGroup indexOfBackdropView:];
-[_UIVisualEffectViewBackdropCaptureGroup disableInPlaceFiltering];
-[_UIVisualEffectViewBackdropCaptureGroup initWithName:scale:];
-[_UIVisualEffectViewBackdropCaptureGroup setGroupNamespace:];
-[_UIVisualEffectViewBackdropCaptureGroup groupNamespace];
```
