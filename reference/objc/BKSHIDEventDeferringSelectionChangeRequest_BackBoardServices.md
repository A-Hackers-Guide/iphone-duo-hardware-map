# `BKSHIDEventDeferringSelectionChangeRequest`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 9 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"<BKSHIDEventDeferringSelectionPathSymbol>" _pathIdentifier;
@"BKSHIDEventDeferringSelectionTarget" _selectionTarget;
@"BKSHIDEventDeferringChangeBasis" _basis;
d _timestamp;
B _ignoreModalities;
```

## Properties

```
@property (T@"<BKSHIDEventDeferringSelectionPathSymbol>",R,N) pathIdentifier;
@property (T@"BKSHIDEventDeferringSelectionTarget",R,N) selectionTarget;
@property (T@"BKSHIDEventDeferringChangeBasis",R,N) basis;
@property (Td,R,N) timestamp;
@property (TB,R,N) ignoreModalities;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringSelectionChangeRequest build:];
+[BKSHIDEventDeferringSelectionChangeRequest supportsSecureCoding];
+[BKSHIDEventDeferringSelectionChangeRequest new];
```

## Instance methods

```
-[BKSHIDEventDeferringSelectionChangeRequest ignoreModalities];
-[BKSHIDEventDeferringSelectionChangeRequest pathIdentifier];
-[BKSHIDEventDeferringSelectionChangeRequest mutableCopyWithZone:];
-[BKSHIDEventDeferringSelectionChangeRequest basis];
-[BKSHIDEventDeferringSelectionChangeRequest init];
-[BKSHIDEventDeferringSelectionChangeRequest timestamp];
-[BKSHIDEventDeferringSelectionChangeRequest encodeWithCoder:];
-[BKSHIDEventDeferringSelectionChangeRequest hash];
-[BKSHIDEventDeferringSelectionChangeRequest description];
-[BKSHIDEventDeferringSelectionChangeRequest initWithCoder:];
-[BKSHIDEventDeferringSelectionChangeRequest appendDescriptionToStream:];
-[BKSHIDEventDeferringSelectionChangeRequest copyWithZone:];
-[BKSHIDEventDeferringSelectionChangeRequest isEqual:];
-[BKSHIDEventDeferringSelectionChangeRequest selectionTarget];
```
