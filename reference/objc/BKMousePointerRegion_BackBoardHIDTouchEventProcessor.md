# `BKMousePointerRegion`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 4 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _cornerRadius;
d _scale;
@"NSString" _displayUUID;
{CGSize="width"d"height"d} _pointSize;
```

## Properties

```
@property (Td,R,N,V_cornerRadius) cornerRadius;
@property (Td,R,N,V_scale) scale;
@property (T{CGSize=dd},R,N,V_pointSize) pointSize;
@property (T@"NSString",R,C,N,V_displayUUID) displayUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKMousePointerRegion displayUUID];
-[BKMousePointerRegion scale];
-[BKMousePointerRegion pointSize];
-[BKMousePointerRegion cornerRadius];
-[BKMousePointerRegion hash];
-[BKMousePointerRegion description];
-[BKMousePointerRegion appendDescriptionToStream:];
-[BKMousePointerRegion copyWithZone:];
-[BKMousePointerRegion isEqual:];
-[BKMousePointerRegion initWithPointSize:cornerRadius:scale:displayUUID:];
```
