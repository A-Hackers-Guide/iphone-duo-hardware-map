# `EGInputGroup`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGNodeInput`, `EGInputHandler`
- 5 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"<EGInputGroupHandler>" _inputGroupHandler;
@"NSMutableDictionary" _inputs;
@"NSMutableDictionary" _inputDataGroup;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _receiveLock;
```

## Properties

```
@property (T@"NSDictionary",R,N) egInputsByName;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGInputGroup initialize];
```

## Instance methods

```
-[EGInputGroup dealloc];
-[EGInputGroup parent];
-[EGInputGroup description];
-[EGInputGroup name];
-[EGInputGroup initWithName:];
-[EGInputGroup addInputsIntoArray:];
-[EGInputGroup egInputsByName];
-[EGInputGroup installInput:];
-[EGInputGroup receiveData:fromInput:];
-[EGInputGroup setInputGroupHandler:];
```
