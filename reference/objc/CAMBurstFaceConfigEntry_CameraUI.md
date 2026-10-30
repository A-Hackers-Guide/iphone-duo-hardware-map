# `CAMBurstFaceConfigEntry`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
i faceId;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} faceRect;
i framesSinceLast;
```

## Properties

```
@property (Ti,VfaceId) faceId;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VfaceRect) faceRect;
@property (Ti,VframesSinceLast) framesSinceLast;
```

## Instance methods

```
-[CAMBurstFaceConfigEntry faceRect];
-[CAMBurstFaceConfigEntry setFaceRect:];
-[CAMBurstFaceConfigEntry faceId];
-[CAMBurstFaceConfigEntry setFaceId:];
-[CAMBurstFaceConfigEntry framesSinceLast];
-[CAMBurstFaceConfigEntry initWithRect:withFaceId:];
-[CAMBurstFaceConfigEntry setFramesSinceLast:];
```
