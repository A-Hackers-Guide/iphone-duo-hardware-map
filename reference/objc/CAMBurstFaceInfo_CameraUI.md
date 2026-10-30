# `CAMBurstFaceInfo`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
i swFaceId;
i swLastFrameSeen;
i hwFaceId;
i hwLastFrameSeen;
{CGPoint="x"d"y"d} swCenter;
{CGSize="width"d"height"d} swSize;
{CGPoint="x"d"y"d} hwCenter;
{CGSize="width"d"height"d} hwSize;
```

## Properties

```
@property (Ti,VswFaceId) swFaceId;
@property (T{CGPoint=dd},VswCenter) swCenter;
@property (T{CGSize=dd},VswSize) swSize;
@property (Ti,VswLastFrameSeen) swLastFrameSeen;
@property (Ti,VhwFaceId) hwFaceId;
@property (T{CGPoint=dd},VhwCenter) hwCenter;
@property (T{CGSize=dd},VhwSize) hwSize;
@property (Ti,VhwLastFrameSeen) hwLastFrameSeen;
```

## Instance methods

```
-[CAMBurstFaceInfo init];
-[CAMBurstFaceInfo hwLastFrameSeen];
-[CAMBurstFaceInfo swLastFrameSeen];
-[CAMBurstFaceInfo hwCenter];
-[CAMBurstFaceInfo hwFaceId];
-[CAMBurstFaceInfo hwFaceRect];
-[CAMBurstFaceInfo hwSize];
-[CAMBurstFaceInfo overlapWithHwRect:];
-[CAMBurstFaceInfo overlapWithSwRect:];
-[CAMBurstFaceInfo setHwCenter:];
-[CAMBurstFaceInfo setHwFaceId:];
-[CAMBurstFaceInfo setHwLastFrameSeen:];
-[CAMBurstFaceInfo setHwSize:];
-[CAMBurstFaceInfo setSwCenter:];
-[CAMBurstFaceInfo setSwFaceId:];
-[CAMBurstFaceInfo setSwLastFrameSeen:];
-[CAMBurstFaceInfo setSwSize:];
-[CAMBurstFaceInfo swCenter];
-[CAMBurstFaceInfo swFaceId];
-[CAMBurstFaceInfo swFaceRect];
-[CAMBurstFaceInfo swSize];
```
