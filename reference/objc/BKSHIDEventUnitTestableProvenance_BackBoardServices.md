# `BKSHIDEventUnitTestableProvenance`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventProvenance`
- 4 instance variables, 7 properties, 8 instance methods, 4 class methods

## Instance variables

```
B _authentic;
I _eventType;
Q _timestamp;
q _versionedPID;
```

## Properties

```
@property (Tq,R,N,V_versionedPID) versionedPID;
@property (TI,R,N,V_eventType) eventType;
@property (TQ,R,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventUnitTestableProvenance valid];
+[BKSHIDEventUnitTestableProvenance supportsBSXPCSecureCoding];
+[BKSHIDEventUnitTestableProvenance invalid];
+[BKSHIDEventUnitTestableProvenance validWithTimestamp:];
```

## Instance methods

```
-[BKSHIDEventUnitTestableProvenance eventType];
-[BKSHIDEventUnitTestableProvenance initWithXPCDictionary:];
-[BKSHIDEventUnitTestableProvenance timestamp];
-[BKSHIDEventUnitTestableProvenance versionedPID];
-[BKSHIDEventUnitTestableProvenance encodeWithXPCDictionary:];
-[BKSHIDEventUnitTestableProvenance encodeWithBSXPCCoder:];
-[BKSHIDEventUnitTestableProvenance initWithBSXPCCoder:];
-[BKSHIDEventUnitTestableProvenance isAuthentic];
```
