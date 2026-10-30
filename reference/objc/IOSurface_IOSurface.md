# `IOSurface`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 15 properties, 60 instance methods, 2 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Tq,R) allocationSize;
@property (Tq,R) width;
@property (Tq,R) height;
@property (T^v,R) baseAddress;
@property (TI,R) pixelFormat;
@property (Tq,R) bytesPerRow;
@property (Tq,R) bytesPerElement;
@property (Tq,R) elementWidth;
@property (Tq,R) elementHeight;
@property (TI,R) surfaceID;
@property (TI,R) seed;
@property (TQ,R) planeCount;
@property (TB,R,GisInUse) inUse;
@property (Ti,R) localUseCount;
@property (TB,R) allowsPixelSizeCasting;
```

## Class methods

```
+[IOSurface supportsSecureCoding];
+[IOSurface numberOfUseCountCategories];
```

## Instance methods

```
-[IOSurface seed];
-[IOSurface initWithProperties:];
-[IOSurface surfaceID];
-[IOSurface allocationSize];
-[IOSurface formattedDescription:];
-[IOSurface protectionOptions];
-[IOSurface bytesPerRow];
-[IOSurface dealloc];
-[IOSurface _cfTypeID];
-[IOSurface incrementUseCount];
-[IOSurface encodeWithCoder:];
-[IOSurface hash];
-[IOSurface isInUse];
-[IOSurface description];
-[IOSurface baseAddress];
-[IOSurface initWithCoder:];
-[IOSurface pixelFormat];
-[IOSurface planeCount];
-[IOSurface width];
-[IOSurface registryID];
-[IOSurface decrementUseCount];
-[IOSurface isEqual:];
-[IOSurface traceID];
-[IOSurface height];
-[IOSurface initWithMachPort:];
-[IOSurface lockWithOptions:seed:];
-[IOSurface unlockWithOptions:seed:];
-[IOSurface timestampAtIndex:];
-[IOSurface attachmentForKey:];
-[IOSurface setAttachment:forKey:];
-[IOSurface removeAllAttachments];
-[IOSurface localUseCount];
-[IOSurface bytesPerElement];
-[IOSurface allAttachments];
-[IOSurface allowsPixelSizeCasting];
-[IOSurface baseAddressOfPlaneAtIndex:];
-[IOSurface bytesPerElementOfPlaneAtIndex:];
-[IOSurface bytesPerRowOfPlaneAtIndex:];
-[IOSurface decrementUseCountForCategory:];
-[IOSurface elementHeight];
-[IOSurface elementHeightOfPlaneAtIndex:];
-[IOSurface elementWidth];
-[IOSurface elementWidthOfPlaneAtIndex:];
-[IOSurface heightOfPlaneAtIndex:];
-[IOSurface incrementUseCountForCategory:];
-[IOSurface initWithClientBuffer:];
-[IOSurface initWithSurfaceID:];
-[IOSurface isDisplayable];
-[IOSurface isInUseForAnyOtherCategory:];
-[IOSurface isInUseForCategory:];
-[IOSurface isMemoryRegionUsed];
-[IOSurface isSysMemOnly];
-[IOSurface newChildSurfaceWithProperties:];
-[IOSurface newWiringAssertion];
-[IOSurface removeAttachmentForKey:];
-[IOSurface setAllAttachments:];
-[IOSurface setPurgeable:oldState:];
-[IOSurface setTimestamp:atIndex:];
-[IOSurface supportsProtectionOptions:];
-[IOSurface widthOfPlaneAtIndex:];
```
