# `BKSHIDEventDeferringConstraintAssertion`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 9 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"<BKSHIDEventDeferringSelectionPathSymbol>" _pathIdentifier;
@"BKSHIDEventDeferringSelectionTarget" _selectionTarget;
@"BKSHIDEventDeferringConstraint" _constraint;
@"NSString" _reason;
d _timestamp;
```

## Properties

```
@property (T@"<BKSHIDEventDeferringSelectionPathSymbol>",R,N) pathIdentifier;
@property (T@"BKSHIDEventDeferringSelectionTarget",R,N) selectionTarget;
@property (T@"BKSHIDEventDeferringConstraint",R,N) constraint;
@property (T@"NSString",R,C,N) reason;
@property (Td,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringConstraintAssertion build:];
+[BKSHIDEventDeferringConstraintAssertion supportsSecureCoding];
+[BKSHIDEventDeferringConstraintAssertion new];
+[BKSHIDEventDeferringConstraintAssertion _withTimestamp:build:];
```

## Instance methods

```
-[BKSHIDEventDeferringConstraintAssertion constraint];
-[BKSHIDEventDeferringConstraintAssertion pathIdentifier];
-[BKSHIDEventDeferringConstraintAssertion mutableCopyWithZone:];
-[BKSHIDEventDeferringConstraintAssertion init];
-[BKSHIDEventDeferringConstraintAssertion timestamp];
-[BKSHIDEventDeferringConstraintAssertion encodeWithCoder:];
-[BKSHIDEventDeferringConstraintAssertion hash];
-[BKSHIDEventDeferringConstraintAssertion description];
-[BKSHIDEventDeferringConstraintAssertion initWithCoder:];
-[BKSHIDEventDeferringConstraintAssertion appendDescriptionToStream:];
-[BKSHIDEventDeferringConstraintAssertion reason];
-[BKSHIDEventDeferringConstraintAssertion copyWithZone:];
-[BKSHIDEventDeferringConstraintAssertion isEqual:];
-[BKSHIDEventDeferringConstraintAssertion selectionTarget];
```
