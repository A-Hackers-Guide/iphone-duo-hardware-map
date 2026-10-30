# `BKMousePointerRegionArrangement`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _coalitionIdentifier;
{CGPoint="x"d"y"d} _baseTranslation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _globalBounds;
@"NSDictionary" _regionToComputedFrame;
@"NSMutableDictionary" _regionToLayoutDescriptor;
```

## Properties

```
@property (T@"NSString",R,C,N,V_coalitionIdentifier) coalitionIdentifier;
@property (T@"NSArray",R,C,N) regions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKMousePointerRegionArrangement regions];
-[BKMousePointerRegionArrangement mutableCopyWithZone:];
-[BKMousePointerRegionArrangement description];
-[BKMousePointerRegionArrangement appendDescriptionToStream:];
-[BKMousePointerRegionArrangement copyWithZone:];
-[BKMousePointerRegionArrangement _initWithCopyOf:];
-[BKMousePointerRegionArrangement _frameForRegion:];
-[BKMousePointerRegionArrangement _layoutDescriptorForRegion:];
-[BKMousePointerRegionArrangement closestRegionForGlobalPoint:returningClosestContainingPoint:returningEdgeMask:];
-[BKMousePointerRegionArrangement coalitionIdentifier];
-[BKMousePointerRegionArrangement convertFromGlobalPoint:toRegion:];
-[BKMousePointerRegionArrangement convertToGlobalPoint:fromRegion:];
-[BKMousePointerRegionArrangement denormalizedAbsoluteGlobalPosition:];
-[BKMousePointerRegionArrangement initWithCoalitionIdentifier:];
-[BKMousePointerRegionArrangement normalizedGlobalPosition:];
-[BKMousePointerRegionArrangement regionForDisplayUUID:];
```
