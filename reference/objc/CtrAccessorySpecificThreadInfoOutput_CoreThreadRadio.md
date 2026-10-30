# `CtrAccessorySpecificThreadInfoOutput`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _threadMeshError;
Q _threadMeshUnderlyingStatusBitmap;
q _threadTXError;
Q _threadTXUnderlyingStatusBitmap;
Q _threadRXUnderlyingStatusBitmap;
q _srpError;
Q _srpUnderlyingStatusBitmap;
```

## Properties

```
@property (Tq,R,V_threadMeshError) threadMeshError;
@property (TQ,R,V_threadMeshUnderlyingStatusBitmap) threadMeshUnderlyingStatusBitmap;
@property (Tq,R,V_threadTXError) threadTXError;
@property (TQ,R,V_threadTXUnderlyingStatusBitmap) threadTXUnderlyingStatusBitmap;
@property (TQ,R,V_threadRXUnderlyingStatusBitmap) threadRXUnderlyingStatusBitmap;
@property (Tq,R,V_srpError) srpError;
@property (TQ,R,V_srpUnderlyingStatusBitmap) srpUnderlyingStatusBitmap;
```

## Class methods

```
+[CtrAccessorySpecificThreadInfoOutput supportsSecureCoding];
```

## Instance methods

```
-[CtrAccessorySpecificThreadInfoOutput encodeWithCoder:];
-[CtrAccessorySpecificThreadInfoOutput initWithCoder:];
-[CtrAccessorySpecificThreadInfoOutput threadMeshError];
-[CtrAccessorySpecificThreadInfoOutput initWithAccessorySpecificThreadInfoOutput:threadMeshUnderlyingStatusBitmap:threadTXError:threadTXUnderlyingStatusBitmap:threadRXUnderlyingStatusBitmap:srpError:srpUnderlyingStatusBitmap:];
-[CtrAccessorySpecificThreadInfoOutput srpError];
-[CtrAccessorySpecificThreadInfoOutput srpUnderlyingStatusBitmap];
-[CtrAccessorySpecificThreadInfoOutput threadMeshUnderlyingStatusBitmap];
-[CtrAccessorySpecificThreadInfoOutput threadRXUnderlyingStatusBitmap];
-[CtrAccessorySpecificThreadInfoOutput threadTXError];
-[CtrAccessorySpecificThreadInfoOutput threadTXUnderlyingStatusBitmap];
```
