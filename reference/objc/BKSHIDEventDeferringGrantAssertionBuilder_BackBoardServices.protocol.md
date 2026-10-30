# `BKSHIDEventDeferringGrantAssertionBuilder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"<BKSHIDEventDeferringSelectionPathSymbol>",&,N) pathIdentifier;
@property (T@"BKSHIDEventDeferringTarget",&,N) grantorTarget;
@property (T@"BKSHIDEventDeferringTarget",&,N) granteeTarget;
@property (T@"NSString",C,N) reason;
```

## Instance methods

```
-[BKSHIDEventDeferringGrantAssertionBuilder pathIdentifier];
-[BKSHIDEventDeferringGrantAssertionBuilder setGrantorTarget:];
-[BKSHIDEventDeferringGrantAssertionBuilder setReason:];
-[BKSHIDEventDeferringGrantAssertionBuilder granteeTarget];
-[BKSHIDEventDeferringGrantAssertionBuilder setGranteeTarget:];
-[BKSHIDEventDeferringGrantAssertionBuilder reason];
-[BKSHIDEventDeferringGrantAssertionBuilder grantorTarget];
-[BKSHIDEventDeferringGrantAssertionBuilder setPathIdentifier:];
```
