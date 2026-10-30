# `BKSHIDEventHitTestClientContext`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `BSXPCSecureCoding`
- 2 instance variables, 6 properties, 9 instance methods, 2 class methods

## Instance variables

```
i _pid;
I _contextID;
```

## Properties

```
@property (Ti,N,V_pid) pid;
@property (TI,N,V_contextID) contextID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventHitTestClientContext supportsBSXPCSecureCoding];
+[BKSHIDEventHitTestClientContext protobufSchema];
```

## Instance methods

```
-[BKSHIDEventHitTestClientContext setPid:];
-[BKSHIDEventHitTestClientContext setContextID:];
-[BKSHIDEventHitTestClientContext pid];
-[BKSHIDEventHitTestClientContext description];
-[BKSHIDEventHitTestClientContext encodeWithBSXPCCoder:];
-[BKSHIDEventHitTestClientContext contextID];
-[BKSHIDEventHitTestClientContext initWithBSXPCCoder:];
-[BKSHIDEventHitTestClientContext copyWithZone:];
-[BKSHIDEventHitTestClientContext isEqual:];
```
