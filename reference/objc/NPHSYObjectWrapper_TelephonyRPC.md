# `NPHSYObjectWrapper`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SYChange`
- 2 instance variables, 8 properties, 5 instance methods, 0 class methods

## Instance variables

```
q _type;
@"<SYObject>" _wrappedObject;
```

## Properties

```
@property (T@"<SYObject>",R,N,V_wrappedObject) wrappedObject;
@property (T@"NSString",R,N) objectIdentifier;
@property (T@"NSString",R,N) sequencer;
@property (Tq,R,N) changeType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NPHSYObjectWrapper wrappedObject];
-[NPHSYObjectWrapper changeType];
-[NPHSYObjectWrapper objectIdentifier];
-[NPHSYObjectWrapper sequencer];
-[NPHSYObjectWrapper initWithSYObject:type:];
```
