# `_UIViewerRelativeDevicePose`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`
- 3 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"_UIMotionEffectAcceleratedOutputRange" _acceleratedOutputRange;
d _planarRotationAngle;
{UIOffset="horizontal"d"vertical"d} _viewerOffset;
```

## Properties

```
@property (T{UIOffset=dd},N,V_viewerOffset) viewerOffset;
@property (Td,N,V_planarRotationAngle) planarRotationAngle;
```

## Instance methods

```
-[_UIViewerRelativeDevicePose _reset];
-[_UIViewerRelativeDevicePose encodeWithCoder:];
-[_UIViewerRelativeDevicePose hash];
-[_UIViewerRelativeDevicePose description];
-[_UIViewerRelativeDevicePose initWithCoder:];
-[_UIViewerRelativeDevicePose copyWithZone:];
-[_UIViewerRelativeDevicePose isEqual:];
-[_UIViewerRelativeDevicePose _acceleratedOutputForViewerOffset:accelerationBoostFactor:];
-[_UIViewerRelativeDevicePose _acceleratedOutputRange];
-[_UIViewerRelativeDevicePose _setAcceleration:fixingOutputForViewerOffset:];
-[_UIViewerRelativeDevicePose planarRotationAngle];
-[_UIViewerRelativeDevicePose setPlanarRotationAngle:];
-[_UIViewerRelativeDevicePose setViewerOffset:];
-[_UIViewerRelativeDevicePose viewerOffset];
```
