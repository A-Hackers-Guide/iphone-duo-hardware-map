# `DYMTLCommandQueueInfo`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DYCapturableObject`, `NSSecureCoding`, `NSCopying`
- 10 instance variables, 15 properties, 21 instance methods, 3 class methods

## Instance variables

```
B _canBeCaptured;
B _isOpenGLQueue;
B _isInternalQueue;
@"NSString" _displayName;
Q _streamRef;
Q _deviceAddress;
Q _deviceStreamRef;
Q _queueAddress;
Q _toolsQueueAddress;
@"NSString" _label;
```

## Properties

```
@property (TQ,N,V_streamRef) streamRef;
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_deviceStreamRef) deviceStreamRef;
@property (TQ,R,N,V_queueAddress) queueAddress;
@property (TQ,R,N,V_toolsQueueAddress) toolsQueueAddress;
@property (T@"NSString",R,N,V_label) label;
@property (TB,N,V_canBeCaptured) canBeCaptured;
@property (TB,N,V_isOpenGLQueue) isOpenGLQueue;
@property (TB,N,V_isInternalQueue) isInternalQueue;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DYMTLCommandQueueInfo supportsSecureCoding];
+[DYMTLCommandQueueInfo capturableObjectType];
+[DYMTLCommandQueueInfo isLabelAppleInternal:];
```

## Instance methods

```
-[DYMTLCommandQueueInfo isOpenGLQueue];
-[DYMTLCommandQueueInfo label];
-[DYMTLCommandQueueInfo displayName];
-[DYMTLCommandQueueInfo initWithCommandQueue:];
-[DYMTLCommandQueueInfo encodeWithCoder:];
-[DYMTLCommandQueueInfo description];
-[DYMTLCommandQueueInfo initWithCoder:];
-[DYMTLCommandQueueInfo setIsOpenGLQueue:];
-[DYMTLCommandQueueInfo copyWithZone:];
-[DYMTLCommandQueueInfo isEqual:];
-[DYMTLCommandQueueInfo deviceAddress];
-[DYMTLCommandQueueInfo setStreamRef:];
-[DYMTLCommandQueueInfo streamRef];
-[DYMTLCommandQueueInfo isInternalQueue];
-[DYMTLCommandQueueInfo deviceStreamRef];
-[DYMTLCommandQueueInfo canBeCaptured];
-[DYMTLCommandQueueInfo queueAddress];
-[DYMTLCommandQueueInfo setCanBeCaptured:];
-[DYMTLCommandQueueInfo setIsInternalQueue:];
-[DYMTLCommandQueueInfo toolsQueueAddress];
-[DYMTLCommandQueueInfo capturableObjectType];
```
