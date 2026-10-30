# `IOKConnection`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 26 instance methods, 0 class methods

## Instance variables

```
I _connection;
```

## Properties

```
@property (TI,R,N,V_connection) connection;
@property (T@"IOKService",R,C,N) service;
```

## Instance methods

```
-[IOKConnection init];
-[IOKConnection dealloc];
-[IOKConnection service];
-[IOKConnection connection];
-[IOKConnection hash];
-[IOKConnection isEqual:];
-[IOKConnection initWithService:];
-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:];
-[IOKConnection initWithService:andType:];
-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:];
-[IOKConnection mapMemory64OfType:withOptions:atAddress:ofSize:error:];
-[IOKConnection setNotificationPort:ofType:withReference:error:];
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:];
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:];
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:structInput:structInputSize:structOutput:structOutputSize:error:];
-[IOKConnection callMethodWithSelector:structInput:structInputSize:structOutput:structOutputSize:error:];
-[IOKConnection setProperties:error:];
-[IOKConnection setProperty:withKey:error:];
-[IOKConnection trap:error:];
-[IOKConnection trap:p1:error:];
-[IOKConnection trap:p1:p2:error:];
-[IOKConnection trap:p1:p2:p3:error:];
-[IOKConnection trap:p1:p2:p3:p4:error:];
-[IOKConnection trap:p1:p2:p3:p4:p5:error:];
-[IOKConnection trap:p1:p2:p3:p4:p5:p6:error:];
-[IOKConnection unmapMemory64OfType:atAddress:error:];
```
