# `BKSHIDEventDeferringModalityAssertion`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 9 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"<BKSHIDEventDeferringSelectionPathSymbol>" _pathIdentifier;
@"BKSHIDEventDeferringSelectionTarget" _selectionTarget;
@"BKSHIDEventDeferringModality" _modality;
@"BKSHIDEventDeferringChangeBasis" _basis;
d _timestamp;
```

## Properties

```
@property (T@"<BKSHIDEventDeferringSelectionPathSymbol>",R,N) pathIdentifier;
@property (T@"BKSHIDEventDeferringSelectionTarget",R,N) selectionTarget;
@property (T@"BKSHIDEventDeferringModality",R,N) modality;
@property (T@"BKSHIDEventDeferringChangeBasis",R,N) basis;
@property (Td,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringModalityAssertion build:];
+[BKSHIDEventDeferringModalityAssertion supportsSecureCoding];
+[BKSHIDEventDeferringModalityAssertion new];
```

## Instance methods

```
-[BKSHIDEventDeferringModalityAssertion pathIdentifier];
-[BKSHIDEventDeferringModalityAssertion mutableCopyWithZone:];
-[BKSHIDEventDeferringModalityAssertion basis];
-[BKSHIDEventDeferringModalityAssertion modality];
-[BKSHIDEventDeferringModalityAssertion init];
-[BKSHIDEventDeferringModalityAssertion timestamp];
-[BKSHIDEventDeferringModalityAssertion encodeWithCoder:];
-[BKSHIDEventDeferringModalityAssertion hash];
-[BKSHIDEventDeferringModalityAssertion description];
-[BKSHIDEventDeferringModalityAssertion initWithCoder:];
-[BKSHIDEventDeferringModalityAssertion appendDescriptionToStream:];
-[BKSHIDEventDeferringModalityAssertion copyWithZone:];
-[BKSHIDEventDeferringModalityAssertion isEqual:];
-[BKSHIDEventDeferringModalityAssertion selectionTarget];
```
