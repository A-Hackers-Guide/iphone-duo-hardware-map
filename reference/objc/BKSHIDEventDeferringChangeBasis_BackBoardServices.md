# `BKSHIDEventDeferringChangeBasis`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 1 properties, 5 instance methods, 4 class methods

## Instance variables

```
@"NSString" _identifier;
@"<BKSHIDEventProvenance>" _eventProvenance;
```

## Properties

```
@property (T@"<BKSHIDEventProvenance>",R,N,V_eventProvenance) eventProvenance;
```

## Class methods

```
+[BKSHIDEventDeferringChangeBasis supportsSecureCoding];
+[BKSHIDEventDeferringChangeBasis new];
+[BKSHIDEventDeferringChangeBasis constraintBasis];
+[BKSHIDEventDeferringChangeBasis ruleOriginatorBasis];
```

## Instance methods

```
-[BKSHIDEventDeferringChangeBasis init];
-[BKSHIDEventDeferringChangeBasis encodeWithCoder:];
-[BKSHIDEventDeferringChangeBasis eventProvenance];
-[BKSHIDEventDeferringChangeBasis initWithCoder:];
-[BKSHIDEventDeferringChangeBasis initWithEventProvenance:];
```
