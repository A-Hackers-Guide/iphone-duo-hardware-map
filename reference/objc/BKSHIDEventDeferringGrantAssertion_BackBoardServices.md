# `BKSHIDEventDeferringGrantAssertion`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventDeferringGrantAssertionBuilder`, `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`
- 6 instance variables, 9 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"<BKSHIDEventDeferringSelectionPathSymbol>" _pathIdentifier;
@"BKSHIDEventDeferringTarget" _grantorTarget;
@"BKSHIDEventDeferringTarget" _granteeTarget;
@"NSString" _reason;
d _timestamp;
B _immutable;
```

## Properties

```
@property (T@"<BKSHIDEventDeferringSelectionPathSymbol>",R,N) pathIdentifier;
@property (T@"BKSHIDEventDeferringTarget",R,N) grantorTarget;
@property (T@"BKSHIDEventDeferringTarget",R,N) granteeTarget;
@property (T@"NSString",R,C,N) reason;
@property (Td,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringGrantAssertion build:];
+[BKSHIDEventDeferringGrantAssertion supportsSecureCoding];
+[BKSHIDEventDeferringGrantAssertion new];
```

## Instance methods

```
-[BKSHIDEventDeferringGrantAssertion pathIdentifier];
-[BKSHIDEventDeferringGrantAssertion init];
-[BKSHIDEventDeferringGrantAssertion setGrantorTarget:];
-[BKSHIDEventDeferringGrantAssertion timestamp];
-[BKSHIDEventDeferringGrantAssertion setReason:];
-[BKSHIDEventDeferringGrantAssertion granteeTarget];
-[BKSHIDEventDeferringGrantAssertion encodeWithCoder:];
-[BKSHIDEventDeferringGrantAssertion setGranteeTarget:];
-[BKSHIDEventDeferringGrantAssertion hash];
-[BKSHIDEventDeferringGrantAssertion description];
-[BKSHIDEventDeferringGrantAssertion initWithCoder:];
-[BKSHIDEventDeferringGrantAssertion appendDescriptionToStream:];
-[BKSHIDEventDeferringGrantAssertion reason];
-[BKSHIDEventDeferringGrantAssertion copyWithZone:];
-[BKSHIDEventDeferringGrantAssertion grantorTarget];
-[BKSHIDEventDeferringGrantAssertion isEqual:];
-[BKSHIDEventDeferringGrantAssertion setPathIdentifier:];
```
